"""
FAST - Functioning Assessment Short Test

This module implements the FAST scale (Échelle Brève d'Évaluation du Fonctionnement),
a 24-item clinician-rated assessment of functional impairment in six domains:
autonomy, work, cognition, finances, interpersonal relations, and leisure.

Developed specifically for bipolar disorder but applicable to other psychiatric conditions.
Higher scores indicate greater functional impairment.
"""

from typing import Dict, List, Optional, Any
from datetime import datetime


class FASTError(Exception):
    """Custom exception for FAST scale errors."""
    pass


class FAST:
    """
    FAST - Functioning Assessment Short Test
    
    A brief 24-item assessment of functional impairment across six life domains.
    Originally developed for bipolar disorder but widely used in various psychiatric conditions.
    
    Domains (24 items total):
    - Autonomy (4 items): Self-care, independent living
    - Work/Occupation (5 items): Employment and professional functioning
    - Cognitive functioning (5 items): Concentration, memory, problem-solving
    - Financial issues (2 items): Money management
    - Interpersonal relations (6 items): Social relationships, family
    - Leisure time (2 items): Hobbies, exercise
    
    Response scale: 0 (No difficulty) to 3 (Severe difficulty)
    Total score: 0-72 (higher = more impaired)
    
    Attributes:
        id: Unique identifier for the scale
        name: Full name in French
        abbreviation: Short form (FAST)
        language: Language code
        version: Version number
        reference_period: Time frame for assessment
        description: Brief description of the scale
    """
    
    # Domain definitions with item ranges
    DOMAINS = {
        "autonomie": {
            "name": "Autonomie",
            "name_en": "Autonomy",
            "items": list(range(1, 5)),  # q1-q4
            "max_score": 12
        },
        "profession": {
            "name": "Activité professionnelle",
            "name_en": "Work/Occupation",
            "items": list(range(5, 10)),  # q5-q9
            "max_score": 15
        },
        "cognition": {
            "name": "Fonctionnement cognitif",
            "name_en": "Cognitive functioning",
            "items": list(range(10, 15)),  # q10-q14
            "max_score": 15
        },
        "finances": {
            "name": "Finances",
            "name_en": "Financial issues",
            "items": list(range(15, 17)),  # q15-q16
            "max_score": 6
        },
        "relations": {
            "name": "Relations interpersonnelles",
            "name_en": "Interpersonal relations",
            "items": list(range(17, 23)),  # q17-q22
            "max_score": 18
        },
        "loisirs": {
            "name": "Loisirs",
            "name_en": "Leisure time",
            "items": list(range(23, 25)),  # q23-q24
            "max_score": 6
        }
    }
    
    # Clinical cutoffs (from literature)
    CUTOFF_MODERATE_IMPAIRMENT = 20
    CUTOFF_SEVERE_IMPAIRMENT = 50
    
    def __init__(self):
        """Initialize the FAST scale."""
        self.id = "FAST.fr"
        self.name = "Échelle Brève d'Évaluation du Fonctionnement – FAST (FR)"
        self.abbreviation = "FAST"
        self.language = "fr-FR"
        self.version = "1.0"
        self.reference_period = "Fonctionnement actuel (semaine écoulée / au moment de l'évaluation)"
        self.description = (
            "24 items, 0=Aucune difficulté … 3=Difficulté sévère. "
            "Score total 0–72 (plus élevé = plus altéré)."
        )
    
    def get_metadata(self) -> Dict[str, Any]:
        """
        Get scale metadata.
        
        Returns:
            Dictionary containing scale metadata
        """
        return {
            "id": self.id,
            "name": self.name,
            "abbreviation": self.abbreviation,
            "language": self.language,
            "version": self.version,
            "reference_period": self.reference_period,
            "description": self.description,
            "num_items": 24,
            "num_domains": 6,
            "response_scale": "0-3 ordinal scale (0=No difficulty, 3=Severe difficulty)",
            "score_range": [0, 72],
            "interpretation": "Higher scores = Greater functional impairment",
            "domains": {
                domain_id: {
                    "name": info["name"],
                    "name_en": info["name_en"],
                    "num_items": len(info["items"]),
                    "range": [0, info["max_score"]]
                }
                for domain_id, info in self.DOMAINS.items()
            },
            "cutoffs": {
                "moderate_impairment": self.CUTOFF_MODERATE_IMPAIRMENT,
                "severe_impairment": self.CUTOFF_SEVERE_IMPAIRMENT
            },
            "target_populations": [
                "Bipolar disorder (primary)",
                "Schizophrenia",
                "Major depression",
                "Other psychiatric conditions"
            ]
        }
    
    def get_questions(self) -> List[Dict[str, Any]]:
        """
        Get all scale items.
        
        Returns:
            List of 24 question dictionaries
        """
        # Item texts exactly as in the French FAST form
        item_texts = [
            "Prendre des responsabilités au sein de la maison",
            "Vivre seul(e)",
            "Faire les courses",
            "Prendre soin de soi (aspect physique, hygiène…)",
            "Avoir un emploi rémunéré",
            "Terminer les tâches le plus rapidement possible",
            "Travailler dans le champ correspondant à votre formation",
            "Recevoir le salaire que vous méritez",
            "Gérer correctement la somme de travail",
            "Capacité à se concentrer devant un film, un livre…",
            "Capacité au calcul mental",
            "Capacité à résoudre des problèmes correctement",
            "Capacité à se souvenir des noms récemment appris",
            "Capacité à apprendre de nouvelles informations",
            "Gérer votre propre argent",
            "Dépenser de façon équilibrée",
            "Conserver des amitiés",
            "Participer à des activités sociales",
            "Avoir de bonnes relations avec vos proches",
            "Habiter avec votre famille",
            "Avoir des relations sexuelles satisfaisantes",
            "Être capable de défendre vos intérêts",
            "Faire de l'exercice ou pratiquer un sport",
            "Avoir des loisirs"
        ]
        
        questions = []
        
        for i, text in enumerate(item_texts, start=1):
            # Determine section
            if 1 <= i <= 4:
                section_id = "autonomie"
            elif 5 <= i <= 9:
                section_id = "profession"
            elif 10 <= i <= 14:
                section_id = "cognition"
            elif 15 <= i <= 16:
                section_id = "finances"
            elif 17 <= i <= 22:
                section_id = "relations"
            else:  # 23-24
                section_id = "loisirs"
            
            questions.append({
                "id": f"q{i}",
                "section_id": section_id,
                "text": f"{i}. {text}",
                "type": "single_choice",
                "required": True,
                "options": [
                    {"code": 0, "label": "0 – Aucune difficulté", "score": 0},
                    {"code": 1, "label": "1 – Difficulté légère", "score": 1},
                    {"code": 2, "label": "2 – Difficulté modérée", "score": 2},
                    {"code": 3, "label": "3 – Difficulté sévère", "score": 3}
                ],
                "constraints": {
                    "value_type": "integer",
                    "allowed_values": [0, 1, 2, 3]
                }
            })
        
        return questions
    
    def get_sections(self) -> List[Dict[str, Any]]:
        """
        Get scale sections.
        
        Returns:
            List of 6 section dictionaries
        """
        sections = []
        
        for domain_id, domain_info in self.DOMAINS.items():
            item_ids = [f"q{i}" for i in domain_info["items"]]
            
            sections.append({
                "id": domain_id,
                "label": domain_info["name"],
                "description": f"Items {min(domain_info['items'])}–{max(domain_info['items'])}",
                "question_ids": item_ids,
                "max_score": domain_info["max_score"]
            })
        
        return sections
    
    def validate_answers(self, answers: Dict[str, int]) -> Dict[str, Any]:
        """
        Validate scale responses.
        
        Args:
            answers: Dictionary mapping item IDs to response values
        
        Returns:
            Dictionary containing validation results with 'valid', 'errors', and 'warnings' keys
        """
        errors = []
        warnings = []
        
        # Check all 24 items are present
        expected_items = [f"q{i}" for i in range(1, 25)]
        missing = [item for item in expected_items if item not in answers]
        
        if missing:
            errors.append(f"Items manquants: {', '.join(missing)}")
        
        # Validate response values
        for item_id, value in answers.items():
            if item_id in expected_items:
                if not isinstance(value, int):
                    errors.append(f"{item_id}: la valeur doit être un entier (reçu: {type(value).__name__})")
                elif value < 0 or value > 3:
                    errors.append(f"{item_id}: la valeur doit être entre 0 et 3 (reçu: {value})")
        
        # Clinical warnings (only if validation passes)
        if not errors:
            # Calculate total for warning thresholds
            total = sum(answers.get(f"q{i}", 0) for i in range(1, 25))
            
            if total >= self.CUTOFF_SEVERE_IMPAIRMENT:
                warnings.append(
                    f"Altération fonctionnelle sévère (score total ≥ {self.CUTOFF_SEVERE_IMPAIRMENT}). "
                    "Déficits marqués dans plusieurs domaines de vie. Intervention intensive recommandée."
                )
            elif total >= self.CUTOFF_MODERATE_IMPAIRMENT:
                warnings.append(
                    f"Altération fonctionnelle modérée (score total ≥ {self.CUTOFF_MODERATE_IMPAIRMENT}). "
                    "Difficultés significatives nécessitant intervention et soutien."
                )
            
            # Check for severe impairment in individual domains
            for domain_id, domain_info in self.DOMAINS.items():
                domain_score = sum(answers.get(f"q{i}", 0) for i in domain_info["items"])
                max_score = domain_info["max_score"]
                
                # Severe if > 75% of maximum
                if domain_score > (max_score * 0.75):
                    warnings.append(
                        f"Altération sévère dans le domaine '{domain_info['name']}' "
                        f"({domain_score}/{max_score}). Attention particulière requise."
                    )
                # Moderate if > 50% of maximum
                elif domain_score > (max_score * 0.5):
                    warnings.append(
                        f"Altération modérée dans le domaine '{domain_info['name']}' "
                        f"({domain_score}/{max_score})."
                    )
            
            # Check for severe difficulties (score 3) in specific critical items
            critical_items = {
                "q2": "Vivre seul(e)",
                "q4": "Prendre soin de soi",
                "q5": "Avoir un emploi rémunéré"
            }
            for item_id, description in critical_items.items():
                if answers.get(item_id) == 3:
                    warnings.append(
                        f"Difficulté sévère identifiée: {description}. "
                        "Évaluation approfondie et support intensif recommandés."
                    )
        
        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings
        }
    
    def calculate_score(self, answers: Dict[str, int]) -> Dict[str, Any]:
        """
        Calculate FAST scores.
        
        Args:
            answers: Dictionary mapping item IDs to response values
        
        Returns:
            Dictionary containing:
                - total_score: Total FAST score (0-72)
                - domain_scores: Dictionary of scores for each domain
                - impairment_level: Overall impairment category
                - domain_impairments: Impairment level for each domain
                - interpretation: Clinical interpretation
                - warnings: Clinical warnings
        
        Raises:
            FASTError: If validation fails
        """
        # Validate answers
        validation = self.validate_answers(answers)
        if not validation["valid"]:
            raise FASTError(
                f"Validation échouée: {'; '.join(validation['errors'])}"
            )
        
        # Calculate domain scores
        domain_scores = {}
        for domain_id, domain_info in self.DOMAINS.items():
            score = sum(answers.get(f"q{i}", 0) for i in domain_info["items"])
            domain_scores[domain_id] = {
                "score": score,
                "max_score": domain_info["max_score"],
                "name": domain_info["name"],
                "percentage": round((score / domain_info["max_score"]) * 100, 1)
            }
        
        # Calculate total score
        total_score = sum(ds["score"] for ds in domain_scores.values())
        
        # Determine overall impairment level
        impairment_level = self._get_impairment_level(total_score)
        
        # Determine impairment level for each domain
        domain_impairments = {}
        for domain_id, ds in domain_scores.items():
            domain_impairments[domain_id] = self._get_domain_impairment(
                ds["score"], ds["max_score"]
            )
        
        # Generate interpretation
        interpretation = self._generate_interpretation(
            total_score,
            domain_scores,
            impairment_level,
            domain_impairments,
            answers
        )
        
        return {
            "total_score": total_score,
            "domain_scores": domain_scores,
            "impairment_level": impairment_level,
            "domain_impairments": domain_impairments,
            "interpretation": interpretation,
            "warnings": validation["warnings"],
            "calculation_date": datetime.utcnow().isoformat() + "Z"
        }
    
    def _get_impairment_level(self, total_score: int) -> str:
        """Get overall impairment level based on total score."""
        if total_score == 0:
            return "Aucune altération"
        elif total_score < self.CUTOFF_MODERATE_IMPAIRMENT:
            return "Altération légère"
        elif total_score < self.CUTOFF_SEVERE_IMPAIRMENT:
            return "Altération modérée"
        else:
            return "Altération sévère"
    
    def _get_domain_impairment(self, score: int, max_score: int) -> str:
        """Get impairment level for a specific domain."""
        percentage = (score / max_score) * 100
        
        if score == 0:
            return "Aucune"
        elif percentage <= 25:
            return "Légère"
        elif percentage <= 50:
            return "Modérée"
        elif percentage <= 75:
            return "Importante"
        else:
            return "Sévère"
    
    def _generate_interpretation(
        self,
        total_score: int,
        domain_scores: Dict[str, Dict[str, Any]],
        impairment_level: str,
        domain_impairments: Dict[str, str],
        answers: Dict[str, int]
    ) -> str:
        """Generate clinical interpretation."""
        interpretation = "=== FAST – ÉCHELLE D'ÉVALUATION DU FONCTIONNEMENT ===\n\n"
        
        # Summary
        interpretation += "=== RÉSUMÉ ===\n"
        interpretation += f"Score total: {total_score}/72\n"
        interpretation += f"Niveau d'altération globale: {impairment_level.upper()}\n\n"
        
        # Overall interpretation
        if total_score == 0:
            interpretation += (
                "✅ AUCUNE ALTÉRATION FONCTIONNELLE\n"
                "Le patient ne rapporte aucune difficulté dans les domaines évalués. "
                "Fonctionnement optimal dans toutes les sphères de vie.\n"
            )
        elif total_score < self.CUTOFF_MODERATE_IMPAIRMENT:
            interpretation += (
                "🟢 ALTÉRATION FONCTIONNELLE LÉGÈRE\n"
                f"Score total: {total_score}/72\n\n"
                "Le patient présente des difficultés mineures qui n'entravent pas "
                "significativement le fonctionnement global. Les capacités adaptatives "
                "sont généralement préservées.\n\n"
                "Recommandations:\n"
                "• Surveillance de l'évolution\n"
                "• Interventions préventives ciblées si nécessaire\n"
                "• Renforcement des stratégies d'adaptation\n"
                "• Maintien des activités actuelles\n"
            )
        elif total_score < self.CUTOFF_SEVERE_IMPAIRMENT:
            interpretation += (
                "🟡 ALTÉRATION FONCTIONNELLE MODÉRÉE\n"
                f"Score total: {total_score}/72\n\n"
                "Le patient présente des difficultés significatives qui affectent "
                "le fonctionnement quotidien dans un ou plusieurs domaines. "
                "Intervention et soutien nécessaires.\n\n"
                "Recommandations:\n"
                "• Réhabilitation psychosociale ciblée\n"
                "• Interventions sur les domaines les plus altérés\n"
                "• Support social et familial\n"
                "• Adaptations au travail/études si nécessaire\n"
                "• Thérapie occupationnelle si indiqué\n"
                "• Suivi régulier de l'évolution\n"
            )
        else:
            interpretation += (
                "🔴 ALTÉRATION FONCTIONNELLE SÉVÈRE\n"
                f"Score total: {total_score}/72\n\n"
                "Le patient présente des déficits fonctionnels marqués dans plusieurs "
                "domaines de vie. Impact majeur sur l'autonomie et la qualité de vie. "
                "Intervention intensive requise.\n\n"
                "Recommandations URGENTES:\n"
                "• Programme de réhabilitation psychosociale intensive\n"
                "• Évaluation multidisciplinaire complète\n"
                "• Support social et familial structuré\n"
                "• Aménagements majeurs (logement, travail, vie quotidienne)\n"
                "• Thérapie occupationnelle\n"
                "• Considérer hôpital de jour ou programme de jour\n"
                "• Évaluation des besoins en aide sociale/tutelle\n"
                "• Suivi rapproché hebdomadaire minimum\n"
            )
        
        # Domain-by-domain analysis
        interpretation += "\n=== ANALYSE PAR DOMAINE ===\n\n"
        
        for domain_id, domain_info in self.DOMAINS.items():
            ds = domain_scores[domain_id]
            impairment = domain_impairments[domain_id]
            
            interpretation += f"**{ds['name'].upper()}**\n"
            interpretation += f"Score: {ds['score']}/{ds['max_score']} ({ds['percentage']}%)\n"
            interpretation += f"Niveau: {impairment}\n"
            
            # Add specific interpretation for each domain
            interpretation += self._interpret_domain(domain_id, ds, answers)
            interpretation += "\n"
        
        # Pattern analysis
        interpretation += "=== ANALYSE DES PROFILS ===\n"
        
        # Identify most impaired domains
        sorted_domains = sorted(
            domain_scores.items(),
            key=lambda x: x[1]["percentage"],
            reverse=True
        )
        
        most_impaired = [d for d in sorted_domains if d[1]["percentage"] > 50]
        
        if most_impaired:
            interpretation += "\nDomaines les plus altérés:\n"
            for domain_id, ds in most_impaired[:3]:
                interpretation += f"  • {ds['name']}: {ds['score']}/{ds['max_score']} ({ds['percentage']}%)\n"
        
        least_impaired = [d for d in sorted_domains if d[1]["percentage"] <= 25]
        if least_impaired:
            interpretation += "\nDomaines préservés (forces):\n"
            for domain_id, ds in least_impaired:
                interpretation += f"  • {ds['name']}: {ds['score']}/{ds['max_score']}\n"
        
        # Clinical patterns
        interpretation += "\n=== IMPLICATIONS CLINIQUES ===\n"
        
        # Check for specific clinical patterns
        cognition_severe = domain_scores["cognition"]["percentage"] > 60
        work_severe = domain_scores["profession"]["percentage"] > 60
        relations_severe = domain_scores["relations"]["percentage"] > 60
        autonomy_severe = domain_scores["autonomie"]["percentage"] > 60
        
        if cognition_severe:
            interpretation += (
                "\n⚠️ DÉFICITS COGNITIFS MARQUÉS\n"
                "Altération importante des fonctions cognitives (concentration, mémoire, "
                "résolution de problèmes). Considérer:\n"
                "• Évaluation neuropsychologique complète\n"
                "• Remédiation cognitive\n"
                "• Adaptations compensatoires\n"
                "• Vérifier facteurs contributifs (médication, sommeil, substances)\n"
            )
        
        if work_severe:
            interpretation += (
                "\n⚠️ ALTÉRATION PROFESSIONNELLE SÉVÈRE\n"
                "Impact majeur sur la capacité de travail. Considérer:\n"
                "• Évaluation des capacités de travail\n"
                "• Aménagement de poste ou temps partiel thérapeutique\n"
                "• Orientation professionnelle\n"
                "• Programmes de réinsertion professionnelle\n"
                "• Évaluation pour arrêt de travail/invalidité si nécessaire\n"
            )
        
        if relations_severe:
            interpretation += (
                "\n⚠️ DIFFICULTÉS RELATIONNELLES IMPORTANTES\n"
                "Altération marquée des relations interpersonnelles. Considérer:\n"
                "• Thérapie interpersonnelle\n"
                "• Groupes de compétences sociales\n"
                "• Thérapie familiale\n"
                "• Support aux proches/aidants\n"
            )
        
        if autonomy_severe:
            interpretation += (
                "\n⚠️ AUTONOMIE COMPROMISE\n"
                "Difficultés dans les activités de vie quotidienne. Considérer:\n"
                "• Ergothérapie\n"
                "• Aide à domicile\n"
                "• Évaluation du logement et des besoins d'adaptation\n"
                "• Support pour les activités de vie quotidienne\n"
            )
        
        # Compare cognitive vs other domains
        cognitive_vs_others = domain_scores["cognition"]["percentage"] - (
            sum(ds["percentage"] for did, ds in domain_scores.items() if did != "cognition") / 5
        )
        
        if abs(cognitive_vs_others) > 30:
            if cognitive_vs_others > 30:
                interpretation += (
                    "\n📊 PROFIL: Déficits cognitifs disproportionnés par rapport aux autres domaines. "
                    "Suggère possible contribution neurocognitive primaire.\n"
                )
            else:
                interpretation += (
                    "\n📊 PROFIL: Cognition relativement préservée malgré altérations dans autres domaines. "
                    "Les difficultés fonctionnelles peuvent être plus liées à facteurs motivationnels, "
                    "sociaux ou symptomatiques qu'à déficits cognitifs.\n"
                )
        
        # General recommendations
        interpretation += "\n=== RECOMMANDATIONS GÉNÉRALES ===\n"
        interpretation += (
            "• Réévaluer régulièrement le fonctionnement (tous les 3-6 mois)\n"
            "• Corréler avec la symptomatologie clinique actuelle\n"
            "• Impliquer les proches dans l'évaluation fonctionnelle\n"
            "• Fixer des objectifs fonctionnels réalistes et mesurables\n"
            "• Approche multidisciplinaire (psychiatre, psychologue, ergothérapeute, AS)\n"
            "• Traiter les symptômes résiduels qui impactent le fonctionnement\n"
            "• Promouvoir l'adhésion thérapeutique\n"
            "• Favoriser le maintien/reprise des activités valorisantes\n"
        )
        
        # Note about FAST
        interpretation += (
            "\n=== NOTES SUR LE FAST ===\n"
            "• Le FAST évalue le fonctionnement ACTUEL (période récente)\n"
            "• Initialement développé pour trouble bipolaire mais applicable largement\n"
            "• Sensible aux changements dans le temps (utile pour suivi)\n"
            "• Complémentaire aux échelles de symptômes\n"
            "• Les scores peuvent être influencés par symptômes résiduels, cognition, support social\n"
            "• Un score élevé ne préjuge pas du potentiel de récupération fonctionnelle\n"
        )
        
        return interpretation
    
    def _interpret_domain(
        self,
        domain_id: str,
        domain_score: Dict[str, Any],
        answers: Dict[str, int]
    ) -> str:
        """Generate interpretation for a specific domain."""
        score = domain_score["score"]
        max_score = domain_score["max_score"]
        percentage = domain_score["percentage"]
        
        if score == 0:
            return "Aucune difficulté rapportée dans ce domaine. Fonctionnement optimal.\n"
        
        interpretation = ""
        
        # Specific interpretations by domain
        if domain_id == "autonomie":
            if percentage > 75:
                interpretation += (
                    "⚠️ Altération sévère de l'autonomie. Difficultés majeures dans les activités "
                    "de vie quotidienne. Support intensif et évaluation ergothérapique nécessaires.\n"
                )
            elif percentage > 50:
                interpretation += (
                    "Difficultés significatives dans l'autonomie quotidienne. "
                    "Support et adaptations recommandés.\n"
                )
            else:
                interpretation += "Difficultés mineures dans l'autonomie. Globalement préservée.\n"
        
        elif domain_id == "profession":
            if percentage > 75:
                interpretation += (
                    "⚠️ Impact professionnel majeur. Capacité de travail sévèrement compromise. "
                    "Évaluation des capacités et réorientation possiblement nécessaires.\n"
                )
            elif percentage > 50:
                interpretation += (
                    "Difficultés professionnelles importantes. Aménagements de poste "
                    "ou réduction d'activité à considérer.\n"
                )
            else:
                interpretation += "Impact professionnel modéré. Adaptations mineures possibles.\n"
        
        elif domain_id == "cognition":
            if percentage > 75:
                interpretation += (
                    "⚠️ Déficits cognitifs sévères. Évaluation neuropsychologique et "
                    "remédiation cognitive fortement recommandées.\n"
                )
            elif percentage > 50:
                interpretation += (
                    "Difficultés cognitives significatives. Considérer évaluation "
                    "neuropsychologique et stratégies compensatoires.\n"
                )
            else:
                interpretation += "Difficultés cognitives légères. Stratégies d'adaptation possibles.\n"
        
        elif domain_id == "finances":
            if score >= 5:
                interpretation += (
                    "⚠️ Gestion financière très problématique. Évaluation pour mesures "
                    "de protection (curatelle/tutelle) à considérer.\n"
                )
            elif score >= 3:
                interpretation += (
                    "Difficultés importantes dans la gestion financière. "
                    "Support et accompagnement recommandés.\n"
                )
            else:
                interpretation += "Difficultés mineures dans la gestion financière.\n"
        
        elif domain_id == "relations":
            if percentage > 75:
                interpretation += (
                    "⚠️ Isolement social majeur et/ou conflits relationnels sévères. "
                    "Interventions sociales et thérapie interpersonnelle prioritaires.\n"
                )
            elif percentage > 50:
                interpretation += (
                    "Difficultés relationnelles importantes. Thérapie de groupe ou "
                    "compétences sociales à considérer.\n"
                )
            else:
                interpretation += "Difficultés relationnelles modérées. Support social recommandé.\n"
        
        elif domain_id == "loisirs":
            if score >= 5:
                interpretation += (
                    "⚠️ Absence quasi-totale d'activités de loisirs. Risque de désinvestissement "
                    "et isolement. Activation comportementale recommandée.\n"
                )
            elif score >= 3:
                interpretation += (
                    "Réduction marquée des activités de loisirs. Encourager reprise progressive.\n"
                )
            else:
                interpretation += "Réduction modérée des activités de loisirs. Maintien encouragé.\n"
        
        return interpretation
    
    def get_schema(self) -> Dict[str, Any]:
        """
        Get complete scale schema in JSON format for frontend integration.
        
        Returns:
            Complete scale schema
        """
        return {
            "instrument": self.get_metadata(),
            "sections": self.get_sections(),
            "questions": self.get_questions(),
            "logic": {
                "validators": [
                    {
                        "id": "response_range",
                        "level": "error",
                        "message": "Les réponses doivent être entre 0 (aucune difficulté) et 3 (difficulté sévère)."
                    },
                    {
                        "id": "completeness",
                        "level": "error",
                        "message": "Tous les 24 items doivent être complétés."
                    }
                ]
            },
            "scoring": {
                "scales": [
                    {
                        "id": "fast_total",
                        "label": "FAST – Total (0–72)",
                        "items": [f"q{i}" for i in range(1, 25)],
                        "formula": {"+": [{"var": f"q{i}"} for i in range(1, 25)]},
                        "range": [0, 72]
                    },
                    {
                        "id": "fast_autonomie",
                        "label": "Autonomie (0–12)",
                        "items": [f"q{i}" for i in range(1, 5)],
                        "formula": {"+": [{"var": f"q{i}"} for i in range(1, 5)]},
                        "range": [0, 12]
                    },
                    {
                        "id": "fast_profession",
                        "label": "Activité professionnelle (0–15)",
                        "items": [f"q{i}" for i in range(5, 10)],
                        "formula": {"+": [{"var": f"q{i}"} for i in range(5, 10)]},
                        "range": [0, 15]
                    },
                    {
                        "id": "fast_cognition",
                        "label": "Cognition (0–15)",
                        "items": [f"q{i}" for i in range(10, 15)],
                        "formula": {"+": [{"var": f"q{i}"} for i in range(10, 15)]},
                        "range": [0, 15]
                    },
                    {
                        "id": "fast_finances",
                        "label": "Finances (0–6)",
                        "items": [f"q{i}" for i in range(15, 17)],
                        "formula": {"+": [{"var": f"q{i}"} for i in range(15, 17)]},
                        "range": [0, 6]
                    },
                    {
                        "id": "fast_relations",
                        "label": "Relations (0–18)",
                        "items": [f"q{i}" for i in range(17, 23)],
                        "formula": {"+": [{"var": f"q{i}"} for i in range(17, 23)]},
                        "range": [0, 18]
                    },
                    {
                        "id": "fast_loisirs",
                        "label": "Loisirs (0–6)",
                        "items": [f"q{i}" for i in range(23, 25)],
                        "formula": {"+": [{"var": f"q{i}"} for i in range(23, 25)]},
                        "range": [0, 6]
                    }
                ]
            },
            "provenance": {
                "created_at": datetime.utcnow().isoformat() + "Z",
                "updated_at": datetime.utcnow().isoformat() + "Z",
                "validated_by": "IngénieurQuestionnaire",
                "validation_date": datetime.utcnow().date().isoformat()
            }
        }
    
    def get_full_questionnaire(self) -> Dict[str, Any]:
        """
        Get complete questionnaire structure for frontend rendering.
        
        Returns:
            Dictionary with metadata, sections, and questions
        """
        return {
            "metadata": self.get_metadata(),
            "sections": self.get_sections(),
            "questions": self.get_questions()
        }

