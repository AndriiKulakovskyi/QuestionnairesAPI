"""
Scoring Strategies for Questionnaires
======================================

This module implements various scoring strategies used across different questionnaires.
Each strategy encapsulates a specific scoring algorithm (simple sum, weighted, conditional, etc.)

Strategies are designed to be:
- Reusable across multiple questionnaires
- Composable (can be combined)
- Testable in isolation
- Easy to extend with new scoring logic

Author: Fondation FondaMental
Version: 2.0.0 (Refactored)
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Union, Callable, Optional, Any
from dataclasses import dataclass
from .models import Question, QuestionnaireResponse, ScoreResult, AnswerOption


# ============================================================================
# Abstract Scoring Strategy
# ============================================================================

class ScoringStrategy(ABC):
    """
    Abstract base class for scoring strategies.
    
    Each concrete strategy implements a specific scoring algorithm.
    """
    
    @abstractmethod
    def calculate(
        self,
        responses: QuestionnaireResponse,
        questions: List[Question]
    ) -> ScoreResult:
        """
        Calculate scores based on responses and questions.
        
        Args:
            responses: Complete questionnaire responses
            questions: List of questions being scored
        
        Returns:
            ScoreResult with computed scores
        """
        pass


# ============================================================================
# Simple Scoring Strategies
# ============================================================================

class SimpleSumStrategy(ScoringStrategy):
    """
    Simple summation of all question scores.
    
    This is the most common scoring method - just add up all the scores.
    
    Example:
        Q1: answer with score 2
        Q2: answer with score 3
        Total: 2 + 3 = 5
    """
    
    def __init__(self, missing_value_handling: str = "error"):
        """
        Args:
            missing_value_handling: How to handle missing responses
                - "error": Raise an error
                - "zero": Treat as score of 0
                - "skip": Skip the question in sum
        """
        self.missing_value_handling = missing_value_handling
    
    def calculate(
        self,
        responses: QuestionnaireResponse,
        questions: List[Question]
    ) -> ScoreResult:
        """Calculate simple sum of all scores."""
        total = 0
        warnings = []
        
        for question in questions:
            response_value = responses.get_response(question.id)
            
            if response_value is None:
                if self.missing_value_handling == "error":
                    raise ValueError(f"Missing response for question {question.id}")
                elif self.missing_value_handling == "zero":
                    warnings.append(f"Missing response for {question.id}, using 0")
                    continue
                elif self.missing_value_handling == "skip":
                    warnings.append(f"Skipping missing response for {question.id}")
                    continue
            
            # Get the score for this response
            option = question.get_option_by_value(response_value)
            if option and option.score is not None:
                score = option.score
                
                # Handle reverse scoring
                if question.reverse_scored:
                    max_score = max(opt.score for opt in question.options if opt.score is not None)
                    score = max_score - score
                
                total += score
        
        return ScoreResult(
            total_score=total,
            warnings=warnings
        )


class NotImplementedStrategy(ScoringStrategy):
    """Placeholder strategy used when validated scoring is unavailable."""

    def __init__(self, reason: str = "Scoring not implemented"):
        self.reason = reason

    def calculate(
        self,
        responses: QuestionnaireResponse,
        questions: List[Question]
    ) -> ScoreResult:
        raise NotImplementedError(self.reason)


class WeightedSumStrategy(ScoringStrategy):
    """
    Weighted summation where specific questions have multipliers.
    
    Example (YMRS):
        Q1-Q4: normal scoring (×1)
        Q5-Q6: double weight (×2)
        
    This is used in YMRS where items 5, 6, 8, 9 are weighted double.
    """
    
    def __init__(self, weights: Dict[str, float]):
        """
        Args:
            weights: Mapping of question IDs to their weights
                     Questions not in this dict have weight of 1.0
        """
        self.weights = weights
    
    def calculate(
        self,
        responses: QuestionnaireResponse,
        questions: List[Question]
    ) -> ScoreResult:
        """Calculate weighted sum of scores."""
        total = 0
        raw_scores = {}
        
        for question in questions:
            response_value = responses.get_response(question.id)
            if response_value is None:
                raise ValueError(f"Missing response for question {question.id}")
            
            option = question.get_option_by_value(response_value)
            if option and option.score is not None:
                score = option.score
                weight = self.weights.get(question.id, 1.0)
                weighted_score = score * weight
                
                raw_scores[question.id] = score
                total += weighted_score
        
        return ScoreResult(
            total_score=total,
            raw_values={'raw_scores': raw_scores, 'weights': self.weights}
        )


# ============================================================================
# Subscale Scoring Strategies
# ============================================================================

class SubscaleStrategy(ScoringStrategy):
    """
    Calculates scores for multiple subscales and a total score.
    
    Used for questionnaires like PANSS, FAST, etc. that have
    distinct subscales/domains.
    
    Example (PANSS):
        - Positive symptoms (P1-P7)
        - Negative symptoms (N1-N7)
        - General psychopathology (G1-G16)
        - Total = sum of all
    """
    
    def __init__(
        self,
        subscale_definitions: Dict[str, List[str]],
        calculate_total: bool = True
    ):
        """
        Args:
            subscale_definitions: Mapping of subscale names to question IDs
                Example: {'positive': ['p1', 'p2'], 'negative': ['n1', 'n2']}
            calculate_total: Whether to also calculate an overall total
        """
        self.subscale_definitions = subscale_definitions
        self.calculate_total = calculate_total
    
    def calculate(
        self,
        responses: QuestionnaireResponse,
        questions: List[Question]
    ) -> ScoreResult:
        """Calculate subscale and total scores."""
        subscale_scores = {}
        total_score = 0
        
        for subscale_name, question_ids in self.subscale_definitions.items():
            subscale_total = 0
            
            for qid in question_ids:
                # Find the question
                question = next((q for q in questions if q.id == qid), None)
                if not question:
                    continue
                
                response_value = responses.get_response(qid)
                if response_value is None:
                    raise ValueError(f"Missing response for question {qid}")
                
                option = question.get_option_by_value(response_value)
                if option and option.score is not None:
                    subscale_total += option.score
            
            subscale_scores[subscale_name] = subscale_total
            total_score += subscale_total
        
        result = ScoreResult(
            total_score=total_score if self.calculate_total else 0,
            subscale_scores=subscale_scores
        )
        
        return result


# ============================================================================
# Complex Scoring Strategies
# ============================================================================

class ConditionalScoringStrategy(ScoringStrategy):
    """
    Scoring with conditional logic - some questions only count if conditions are met.
    
    Example (MDQ):
        - Need at least 7 "yes" answers
        - AND they occurred together
        - AND severity level >= 2
        
    Only then is it a positive screen.
    """
    
    def __init__(
        self,
        scoring_function: Callable[[QuestionnaireResponse, List[Question]], ScoreResult]
    ):
        """
        Args:
            scoring_function: Custom function that implements the conditional logic
        """
        self.scoring_function = scoring_function
    
    def calculate(
        self,
        responses: QuestionnaireResponse,
        questions: List[Question]
    ) -> ScoreResult:
        """Delegate to the custom scoring function."""
        return self.scoring_function(responses, questions)


class GroupedMaxStrategy(ScoringStrategy):
    """
    Take the maximum score from groups of questions.
    
    Used in questionnaires like QIDS where you have multiple questions
    about sleep, but only count the highest scoring one.
    
    Example (QIDS):
        Sleep questions: early insomnia, middle insomnia, late insomnia
        → Take the maximum score from these three
    """
    
    def __init__(self, groups: Dict[str, List[str]]):
        """
        Args:
            groups: Mapping of group names to question IDs
                Example: {'sleep': ['q1', 'q2', 'q3'], 'appetite': ['q4', 'q5']}
        """
        self.groups = groups
    
    def calculate(
        self,
        responses: QuestionnaireResponse,
        questions: List[Question]
    ) -> ScoreResult:
        """Calculate score using maximum from each group."""
        total_score = 0
        group_scores = {}
        
        for group_name, question_ids in self.groups.items():
            max_score = 0
            
            for qid in question_ids:
                question = next((q for q in questions if q.id == qid), None)
                if not question:
                    continue
                
                response_value = responses.get_response(qid)
                if response_value is not None:
                    option = question.get_option_by_value(response_value)
                    if option and option.score is not None:
                        max_score = max(max_score, option.score)
            
            group_scores[group_name] = max_score
            total_score += max_score
        
        return ScoreResult(
            total_score=total_score,
            subscale_scores=group_scores
        )


class PercentageStrategy(ScoringStrategy):
    """
    Calculate scores as percentages.
    
    Used in questionnaires like S-QoL where scores are converted to
    a 0-100 scale for each domain.
    
    Formula: (actual_score / max_possible_score) * 100
    """
    
    def __init__(
        self,
        subscales: Optional[Dict[str, List[str]]] = None,
        allow_not_applicable: bool = False
    ):
        """
        Args:
            subscales: Optional subscale definitions
            allow_not_applicable: Whether to handle "N/A" responses
        """
        self.subscales = subscales
        self.allow_not_applicable = allow_not_applicable
    
    def calculate(
        self,
        responses: QuestionnaireResponse,
        questions: List[Question]
    ) -> ScoreResult:
        """Calculate percentage scores."""
        if self.subscales:
            return self._calculate_subscale_percentages(responses, questions)
        else:
            return self._calculate_overall_percentage(responses, questions)
    
    def _calculate_overall_percentage(
        self,
        responses: QuestionnaireResponse,
        questions: List[Question]
    ) -> ScoreResult:
        """Calculate overall percentage score."""
        actual_score = 0
        max_possible = 0
        
        for question in questions:
            response_value = responses.get_response(question.id)
            if response_value is not None:
                option = question.get_option_by_value(response_value)
                if option and option.score is not None:
                    actual_score += option.score
            
            # Max possible for this question
            max_score = max(opt.score for opt in question.options if opt.score is not None)
            max_possible += max_score
        
        percentage = (actual_score / max_possible * 100) if max_possible > 0 else 0
        
        return ScoreResult(
            total_score=round(percentage, 2),
            raw_values={'actual_score': actual_score, 'max_possible': max_possible}
        )
    
    def _calculate_subscale_percentages(
        self,
        responses: QuestionnaireResponse,
        questions: List[Question]
    ) -> ScoreResult:
        """Calculate percentage for each subscale."""
        subscale_percentages = {}
        
        for subscale_name, question_ids in self.subscales.items():
            actual_score = 0
            max_possible = 0
            
            for qid in question_ids:
                question = next((q for q in questions if q.id == qid), None)
                if not question:
                    continue
                
                response_value = responses.get_response(qid)
                if response_value is not None:
                    option = question.get_option_by_value(response_value)
                    if option and option.score is not None:
                        actual_score += option.score
                
                max_score = max(opt.score for opt in question.options if opt.score is not None)
                max_possible += max_score
            
            percentage = (actual_score / max_possible * 100) if max_possible > 0 else 0
            subscale_percentages[subscale_name] = round(percentage, 2)
        
        # Overall is average of subscales
        avg_percentage = sum(subscale_percentages.values()) / len(subscale_percentages)
        
        return ScoreResult(
            total_score=round(avg_percentage, 2),
            subscale_scores=subscale_percentages
        )


# ============================================================================
# Interpretation Helpers
# ============================================================================

@dataclass
class InterpretationThreshold:
    """
    Defines a threshold for score interpretation.
    
    Example:
        InterpretationThreshold(
            lower_bound=0,
            upper_bound=12,
            label="Rémission",
            severity="normal"
        )
    """
    lower_bound: Union[int, float]
    upper_bound: Optional[Union[int, float]]
    label: str
    severity: str


class ThresholdInterpreter:
    """
    Interprets scores based on threshold ranges.
    
    Example (YMRS):
        0-12: Remission
        13-19: Minimal symptoms
        20-25: Moderate mania
        26+: Severe mania
    """
    
    def __init__(self, thresholds: List[InterpretationThreshold]):
        """
        Args:
            thresholds: List of interpretation thresholds
        """
        self.thresholds = sorted(thresholds, key=lambda t: t.lower_bound)
    
    def interpret(self, score: Union[int, float]) -> InterpretationThreshold:
        """
        Find the interpretation for a given score.
        
        Args:
            score: The score to interpret
        
        Returns:
            Matching InterpretationThreshold
        """
        for threshold in self.thresholds:
            if threshold.upper_bound is None:
                # Last threshold (e.g., "26+")
                if score >= threshold.lower_bound:
                    return threshold
            else:
                if threshold.lower_bound <= score <= threshold.upper_bound:
                    return threshold
        
        # Default to first threshold if nothing matches
        return self.thresholds[0]
