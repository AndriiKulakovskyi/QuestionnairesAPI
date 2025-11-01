"""
WAIS-III - Wechsler Adult Intelligence Scale, Third Edition
A comprehensive neuropsychological test battery for assessing cognitive abilities in adults.
"""

from typing import Any, Dict, List, Optional


class WAIS3Test:
    """WAIS-III (Wechsler Adult Intelligence Scale - Third Edition)
    
    A comprehensive cognitive assessment battery with 14 subtests measuring:
    - Verbal Comprehension Index (VCI)
    - Perceptual Organization Index (POI)  
    - Working Memory Index (WMI)
    - Processing Speed Index (PSI)
    - Full Scale IQ (FSIQ)
    
    Structure:
    - 14 subtests (11 standard + 3 optional)
    - Each subtest yields a raw score converted to scaled score (M=10, SD=3)
    - Index scores and IQ scores (M=100, SD=15)
    """
    
    def __init__(self):
        """Initialize WAIS-III test battery."""
        self.name = "WAIS-III"
        self.full_name = "Wechsler Adult Intelligence Scale - Third Edition (WAIS-III)"
        self.description = "Batterie complète d'évaluation cognitive de l'adulte (14 subtests)"
        
        # Define subtests
        self.subtests = {
            # Verbal Comprehension Index (VCI) subtests
            "vocabulary": {"name": "Vocabulaire", "num_items": 33, "max_points_per_item": 2, "index": "VCI"},
            "similarities": {"name": "Similitudes", "num_items": 19, "max_points_per_item": 2, "index": "VCI"},
            "information": {"name": "Information", "num_items": 28, "max_points_per_item": 1, "index": "VCI"},
            "comprehension": {"name": "Compréhension", "num_items": 18, "max_points_per_item": 2, "index": "VCI", "optional": True},
            
            # Perceptual Organization Index (POI) subtests  
            "picture_completion": {"name": "Complètement d'images", "num_items": 25, "max_points_per_item": 1, "index": "POI"},
            "block_design": {"name": "Cubes", "num_items": 14, "max_points_per_item": 7, "index": "POI"},
            "matrix_reasoning": {"name": "Matrices", "num_items": 26, "max_points_per_item": 1, "index": "POI"},
            "picture_arrangement": {"name": "Arrangement d'images", "num_items": 11, "max_points_per_item": 6, "index": "POI", "optional": True},
            
            # Working Memory Index (WMI) subtests
            "arithmetic": {"name": "Arithmétique", "num_items": 20, "max_points_per_item": 1, "index": "WMI"},
            "digit_span": {"name": "Mémoire des chiffres", "num_items": 30, "max_points_per_item": 1, "index": "WMI"},
            "letter_number": {"name": "Séquences Lettres-chiffres", "num_items": 21, "max_points_per_item": 1, "index": "WMI"},
            
            # Processing Speed Index (PSI) subtests
            "digit_symbol": {"name": "Code", "type": "timed", "max_score": 133, "index": "PSI"},
            "symbol_search": {"name": "Symboles", "type": "timed", "max_score": 60, "index": "PSI"},
            
            # Optional subtest
            "object_assembly": {"name": "Assemblage d'objets", "num_items": 5, "max_points_per_item": 13, "optional": True}
        }
        
        # Index composition
        self.indices = {
            "VCI": ["vocabulary", "similarities", "information"],
            "POI": ["picture_completion", "block_design", "matrix_reasoning"],
            "WMI": ["arithmetic", "digit_span", "letter_number"],
            "PSI": ["digit_symbol", "symbol_search"]
        }
    
    def calculate_subtest_raw_score(self, subtest_name: str, responses: Dict[str, int]) -> int:
        """
        Calculate raw score for a specific subtest.
        
        Args:
            subtest_name: Name of the subtest
            responses: Dictionary mapping item IDs to scores
        
        Returns:
            Raw score for the subtest
        """
        if subtest_name not in self.subtests:
            raise ValueError(f"Invalid subtest: {subtest_name}")
        
        subtest = self.subtests[subtest_name]
        
        # Handle timed tests differently
        if subtest.get("type") == "timed":
            return responses.get(f"{subtest_name}_total", 0)
        
        # Calculate sum of item scores
        raw_score = 0
        num_items = subtest.get("num_items", 0)
        
        for i in range(1, num_items + 1):
            item_key = f"{subtest_name}_{i}"
            raw_score += responses.get(item_key, 0)
        
        return raw_score
    
    def raw_to_scaled_score(self, subtest_name: str, raw_score: int, age: int) -> Optional[int]:
        """
        Convert raw score to scaled score (M=10, SD=3).
        
        Note: This requires age-based normative tables from the WAIS-III manual.
        This is a placeholder that returns None - implement with actual norms.
        
        Args:
            subtest_name: Name of the subtest
            raw_score: Raw score from the subtest
            age: Age of the examinee in years
        
        Returns:
            Scaled score (1-19 scale) or None if norms not implemented
        """
        # Placeholder: In production, this would look up normative tables
        # based on age group and return scaled score
        # For now, return None to indicate norms are needed
        return None
    
    def calculate_index_score(self, scaled_scores: Dict[str, int], index_name: str) -> Optional[int]:
        """
        Calculate composite index score from scaled scores.
        
        Args:
            scaled_scores: Dictionary mapping subtest names to scaled scores
            index_name: Name of the index (VCI, POI, WMI, PSI, or FSIQ)
        
        Returns:
            Index score (M=100, SD=15) or None if insufficient data
        """
        if index_name not in self.indices and index_name != "FSIQ":
            raise ValueError(f"Invalid index: {index_name}")
        
        # For FSIQ, use all standard subtests
        if index_name == "FSIQ":
            required_subtests = []
            for idx_subtests in self.indices.values():
                required_subtests.extend(idx_subtests)
        else:
            required_subtests = self.indices[index_name]
        
        # Check if all required subtests have scaled scores (and are not None)
        if not all(subtest in scaled_scores and scaled_scores[subtest] is not None 
                   for subtest in required_subtests):
            return None
        
        # Sum scaled scores
        sum_scaled = sum(scaled_scores[subtest] for subtest in required_subtests)
        
        # Placeholder: In production, this would use sum of scaled scores
        # conversion tables to get index score
        # For now, return None to indicate conversion tables are needed
        return None
    
    def calculate_scores(self, responses: Dict[str, int], age: int) -> Dict[str, Any]:
        """
        Calculate all WAIS-III scores from raw responses.
        
        Args:
            responses: Dictionary containing all subtest responses
            age: Age of the examinee in years
        
        Returns:
            Dictionary containing raw scores, scaled scores, and index scores
        """
        # Calculate raw scores for all subtests
        raw_scores = {}
        for subtest_name in self.subtests.keys():
            try:
                raw_score = self.calculate_subtest_raw_score(subtest_name, responses)
                raw_scores[subtest_name] = raw_score
            except:
                raw_scores[subtest_name] = None
        
        # Calculate scaled scores (requires normative tables)
        scaled_scores = {}
        for subtest_name, raw_score in raw_scores.items():
            if raw_score is not None:
                scaled_score = self.raw_to_scaled_score(subtest_name, raw_score, age)
                scaled_scores[subtest_name] = scaled_score
        
        # Calculate index scores
        index_scores = {}
        for index_name in list(self.indices.keys()) + ["FSIQ"]:
            index_score = self.calculate_index_score(scaled_scores, index_name)
            index_scores[index_name] = index_score
        
        return {
            "raw_scores": raw_scores,
            "scaled_scores": scaled_scores,
            "index_scores": index_scores,
            "age": age,
            "note": "Scaled scores and index scores require age-based normative tables from WAIS-III manual"
        }
    
    def get_subtest_info(self) -> List[Dict[str, Any]]:
        """Get information about all subtests."""
        info = []
        for name, details in self.subtests.items():
            info.append({
                "name": name,
                "french_name": details["name"],
                "index": details.get("index", "None"),
                "num_items": details.get("num_items", "Variable"),
                "optional": details.get("optional", False)
            })
        return info


if __name__ == '__main__':
    # Example usage
    wais3 = WAIS3Test()
    
    print(f"Test: {wais3.full_name}")
    print(f"Number of subtests: {len(wais3.subtests)}\n")
    
    print("Subtests by Index:")
    for index_name, subtests in wais3.indices.items():
        print(f"\n{index_name}:")
        for subtest in subtests:
            print(f"  - {wais3.subtests[subtest]['name']}")
    
    # Example: Calculate raw scores for Picture Completion subtest
    print("\n" + "="*80)
    print("EXAMPLE: Picture Completion Subtest")
    print("="*80)
    
    # Simulate responses (25 items, each scored 0 or 1)
    pic_comp_responses = {f"picture_completion_{i}": 1 if i <= 20 else 0 for i in range(1, 26)}
    
    raw_score = wais3.calculate_subtest_raw_score("picture_completion", pic_comp_responses)
    print(f"Raw score: {raw_score}/25")
    print(f"Scaled score: {wais3.raw_to_scaled_score('picture_completion', raw_score, 30)}")
    print("Note: Scaled score requires normative tables from WAIS-III manual")
    
    # Example: Calculate all scores
    print("\n" + "="*80)
    print("EXAMPLE: Full Battery Scoring Structure")
    print("="*80)
    
    # Simulate complete battery responses  
    all_responses = {}
    # Picture Completion (25 items)
    for i in range(1, 26):
        all_responses[f"picture_completion_{i}"] = 1 if i <= 18 else 0
    # Vocabulary (33 items, 0-2 points each)
    for i in range(1, 34):
        all_responses[f"vocabulary_{i}"] = 2 if i <= 10 else (1 if i <= 25 else 0)
    # Add more subtests as needed...
    
    results = wais3.calculate_scores(all_responses, age=30)
    
    print("\nRaw Scores:")
    for subtest, score in results["raw_scores"].items():
        if score is not None:
            print(f"  {wais3.subtests[subtest]['name']}: {score}")
    
    print("\nIndex Scores:")
    for index, score in results["index_scores"].items():
        print(f"  {index}: {score if score else 'Requires normative tables'}")
    
    print(f"\nNote: {results['note']}")

