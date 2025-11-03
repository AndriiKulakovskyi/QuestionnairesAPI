# MARS - Medication Adherence Rating Scale

## Description

La **MARS (Medication Adherence Rating Scale)** est une échelle d'auto-évaluation en 10 items évaluant l'adhérence médicamenteuse chez les patients psychiatriques. Chaque item utilise un format de réponse binaire (OUI/NON).

## Caractéristiques

- **Nombre d'items**: 10
- **Format de réponse**: Binaire (OUI=1 / NON=0)
- **Période de référence**: Semaine écoulée
- **Durée d'administration**: ~2-3 minutes
- **Score total**: 0–10 (score élevé = meilleure adhérence)

## Cotation

### Barème de recodage

Le scoring MARS utilise un système de recodage différencié :

**Items négatifs (1, 2, 3, 4, 5, 6, 9, 10)** : NON = 1 point, OUI = 0 point
- Q1: Oublier de prendre les médicaments
- Q2: Négliger l'heure de prise
- Q3: Interrompre le traitement en se sentant mieux
- Q4: Arrêter le traitement en se sentant moins bien
- Q5: Ne prendre les médicaments que lors de maladie
- Q6: Sentiment que les médicaments ne sont pas naturels
- Q9: Sensation de "zombie" avec les médicaments
- Q10: Médicaments rendent lourd(e) et fatigué(e)

**Items positifs (7, 8)** : OUI = 1 point, NON = 0 point
- Q7: Idées plus claires avec les médicaments
- Q8: Continuer les médicaments pour éviter une rechute

### Score total

Le score total est la somme des 10 items recodés (0–10).

### Interprétation

- **Distribution typique**: Médiane ≈6 ; IQR ≈4–8
- **Interprétation**: Continuum d'adhérence (pas de cut-off diagnostic universel)
  - ≥8 : Adhérence excellente
  - 6-7 : Adhérence bonne
  - 4-5 : Adhérence modérée
  - ≤3 : Adhérence faible (intervention recommandée)

## Utilisation

```python
from questionnaires.mars import MARS

# Initialiser le questionnaire
mars = MARS()

# Obtenir les métadonnées
metadata = mars.get_metadata()

# Obtenir les questions
questions = mars.get_questions()

# Exemple de réponses (1=OUI, 0=NON)
answers = {
    "q1": 0,  # Non, je n'oublie pas
    "q2": 0,  # Non, je ne néglige pas l'heure
    "q3": 0,  # Non, je n'interromps pas
    "q4": 0,  # Non, je n'arrête pas
    "q5": 0,  # Non, je ne prends pas seulement en cas de maladie
    "q6": 0,  # Non, je ne pense pas que c'est non-naturel
    "q7": 1,  # Oui, mes idées sont plus claires
    "q8": 1,  # Oui, je continue pour éviter une rechute
    "q9": 0,  # Non, je ne me sens pas comme un zombie
    "q10": 0  # Non, les médicaments ne me rendent pas lourd
}

# Valider les réponses
validation = mars.validate_answers(answers)
if validation.valid:
    # Calculer le score
    result = mars.calculate_score(answers)
    print(f"Score total: {result.total_score}/10")
    print(f"Interprétation: {result.interpretation}")
    print(f"Scores recodés: {result.recoded_scores}")
else:
    print(f"Erreurs: {validation.errors}")
```

## Références

- **Thompson K, Kulkarni J, Sergejew AA.** Reliability and validity of a new Medication Adherence Rating Scale (MARS) for the psychoses. *Schizophrenia Research*, 2000;42(3):241–247.
- **MARS.pdf** (version française fournie)
- **MARS_CotationScore.docx** (règles de cotation)

## Notes cliniques

- L'échelle MARS est conçue pour évaluer l'adhérence médicamenteuse de manière dimensionnelle plutôt que catégorielle.
- Les items 7 et 8 capturent les attitudes positives envers les médicaments.
- Les items négatifs explorent les comportements de non-adhérence et les attitudes négatives.
- Un score faible (≤5) justifie une exploration clinique des barrières à l'adhérence médicamenteuse.
- L'échelle peut être utilisée pour le suivi longitudinal de l'adhérence médicamenteuse.

## Propriétés psychométriques

- **Fiabilité**: Bonnes propriétés psychométriques rapportées dans les psychoses
- **Validité**: Corrélations avec d'autres mesures d'adhérence
- **Sensibilité**: Détecte les changements d'adhérence dans le temps

