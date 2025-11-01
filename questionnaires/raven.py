"""
Raven's Progressive Matrices - PM38
A non-verbal test of abstract reasoning and fluid intelligence.
"""

from typing import Dict, Any


class RavenProgressiveMatricesTest:
    """Raven's Progressive Matrices (Standard Progressive Matrices - PM38)
    
    A 60-item non-verbal intelligence test measuring abstract reasoning.
    
    Structure:
    - 5 series (A, B, C, D, E), each with 12 items
    - Each item scored 0 (incorrect) or 1 (correct)
    - Total score: 0-60
    - Percentile scores based on age/education norms
    """
    
    def __init__(self):
        """Initialize Raven's Progressive Matrices test."""
        self.name = "Raven-PM38"
        self.full_name = "Raven's Progressive Matrices - Standard (PM38)"
        self.description = "Test non-verbal de raisonnement abstrait et d'intelligence fluide"
        
        # 5 series, 12 items each
        self.series = ["A", "B", "C", "D", "E"]
        self.items_per_series = 12
        self.total_items = 60
    
    def calculate_score(self, responses: Dict[str, int]) -> Dict[str, Any]:
        """
        Calculate Raven's Progressive Matrices scores.
        
        Args:
            responses: Dictionary mapping item IDs to responses (0=incorrect, 1=correct)
                      Format: "SPMA1", "SPMA2", ..., "SPME12"
        
        Returns:
            Dictionary containing raw scores, series scores, and interpretation
        """
        series_scores = {}
        total_score = 0
        
        # Calculate score for each series
        for series_name in self.series:
            series_score = 0
            for item_num in range(1, self.items_per_series + 1):
                item_id = f"SPM{series_name}{item_num}"
                series_score += responses.get(item_id, 0)
            series_scores[f"Series_{series_name}"] = series_score
            total_score += series_score
        
        # Interpret score (simplified - actual interpretation requires age/education norms)
        if total_score >= 50:
            interpretation = "Supérieur - Capacités de raisonnement exceptionnelles"
        elif total_score >= 40:
            interpretation = "Bon - Capacités de raisonnement au-dessus de la moyenne"
        elif total_score >= 25:
            interpretation = "Moyen - Capacités de raisonnement moyennes"
        elif total_score >= 15:
            interpretation = "Faible - Capacités de raisonnement en dessous de la moyenne"
        else:
            interpretation = "Très faible - Difficultés marquées de raisonnement abstrait"
        
        return {
            "total_score": total_score,
            "total_possible": self.total_items,
            "percentage": round((total_score / self.total_items) * 100, 1),
            "series_scores": series_scores,
            "interpretation": interpretation,
            "note": "Percentile scores require age- and education-specific norms"
        }


if __name__ == '__main__':
    raven = RavenProgressiveMatricesTest()
    
    print(f"Test: {raven.full_name}")
    print(f"Total items: {raven.total_items}")
    print(f"Series: {', '.join(raven.series)}\n")
    
    # Example: High scorer
    print("Example 1: High performance")
    responses1 = {}
    for series in raven.series:
        for i in range(1, 13):
            # Simulate decreasing accuracy through series (A easier, E harder)
            if series == "A":
                responses1[f"SPM{series}{i}"] = 1
            elif series == "B":
                responses1[f"SPM{series}{i}"] = 1 if i <= 10 else 0
            elif series == "C":
                responses1[f"SPM{series}{i}"] = 1 if i <= 9 else 0
            elif series == "D":
                responses1[f"SPM{series}{i}"] = 1 if i <= 8 else 0
            else:  # E
                responses1[f"SPM{series}{i}"] = 1 if i <= 7 else 0
    
    result1 = raven.calculate_score(responses1)
    print(f"Total score: {result1['total_score']}/{result1['total_possible']} ({result1['percentage']}%)")
    print("\nSeries scores:")
    for series, score in result1['series_scores'].items():
        print(f"  {series}: {score}/12")
    print(f"\nInterprétation: {result1['interpretation']}\n")

