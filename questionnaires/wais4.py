"""
WAIS-IV - Wechsler Adult Intelligence Scale, Fourth Edition
A comprehensive neuropsychological test battery for assessing cognitive abilities.
"""

from typing import Dict, Any, Optional


class WAIS4Test:
    """WAIS-IV (Wechsler Adult Intelligence Scale - Fourth Edition)
    
    Similar to WAIS-III but with updated norms and revised index structure:
    - Verbal Comprehension Index (VCI)
    - Perceptual Reasoning Index (PRI) - replaces POI
    - Working Memory Index (WMI)
    - Processing Speed Index (PSI)
    - Full Scale IQ (FSIQ)
    
    Note: This is based on the same WAIS structure. In the Asperger database,
    forms 260.php appears to collect WAIS-IV summary scores.
    """
    
    def __init__(self):
        """Initialize WAIS-IV test battery."""
        self.name = "WAIS-IV"
        self.full_name = "Wechsler Adult Intelligence Scale - Fourth Edition (WAIS-IV)"
        self.description = "Batterie d'évaluation cognitive de l'adulte - 4ème édition"
        
        # WAIS-IV has 15 subtests (10 core + 5 supplemental)
        self.core_subtests = [
            "block_design", "similarities", "digit_span", "matrix_reasoning",
            "vocabulary", "arithmetic", "symbol_search", "visual_puzzles",
            "information", "coding"
        ]
        
        self.supplemental_subtests = [
            "letter_number", "figure_weights", "comprehension",
            "cancellation", "picture_completion"
        ]
        
        self.indices = {
            "VCI": ["similarities", "vocabulary", "information"],
            "PRI": ["block_design", "matrix_reasoning", "visual_puzzles"],
            "WMI": ["digit_span", "arithmetic"],
            "PSI": ["symbol_search", "coding"]
        }
    
    def calculate_index_score(self, scaled_scores: Dict[str, int], index_name: str) -> Optional[int]:
        """Calculate composite index from scaled scores."""
        if index_name not in self.indices and index_name != "FSIQ":
            return None
        
        if index_name == "FSIQ":
            required = self.core_subtests
        else:
            required = self.indices[index_name]
        
        if not all(s in scaled_scores and scaled_scores[s] is not None for s in required):
            return None
        
        # Placeholder - requires conversion tables
        return None
    
    def calculate_scores(self, scaled_scores: Dict[str, int], age: int) -> Dict[str, Any]:
        """
        Calculate WAIS-IV composite scores from subtest scaled scores.
        
        Args:
            scaled_scores: Dictionary of subtest scaled scores (M=10, SD=3)
            age: Age of examinee
        
        Returns:
            Dictionary with index scores and interpretation
        """
        index_scores = {}
        for index_name in list(self.indices.keys()) + ["FSIQ"]:
            index_scores[index_name] = self.calculate_index_score(scaled_scores, index_name)
        
        return {
            "index_scores": index_scores,
            "age": age,
            "note": "Index score conversion requires WAIS-IV technical manual tables"
        }


if __name__ == '__main__':
    wais4 = WAIS4Test()
    print(f"Test: {wais4.full_name}")
    print(f"Core subtests: {len(wais4.core_subtests)}")
    print(f"Supplemental subtests: {len(wais4.supplemental_subtests)}")
    print("\nIndices:")
    for idx, subtests in wais4.indices.items():
        print(f"  {idx}: {', '.join(subtests)}")

