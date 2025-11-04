# AIM-short (Affect Intensity Measure - Version courte)

## Vue d'ensemble

Le **AIM-short (Affect Intensity Measure - Version courte)** est un questionnaire d'auto-évaluation de 20 items mesurant l'intensité de la réactivité émotionnelle, c'est-à-dire la force avec laquelle une personne vit ses émotions.

### Informations générales

- **ID**: AIM-short.fr
- **Nom complet**: Affect Intensity Measure (AIM) – Version courte (FR)
- **Abréviation**: AIM-20
- **Langue**: Français (fr-FR)
- **Version**: 1.0
- **Nombre d'items**: 20
- **Période de référence**: "Mode de fonctionnement habituel (hors périodes d'humeur anormalement basse ou élevée)"
- **Échelle de réponse**: 6 points (1=Jamais … 6=Toujours)
- **Plage de scores**: 1.0–6.0 (moyenne)
- **Temps d'administration**: 5-10 minutes

## Concept de l'intensité affective

L'intensité affective (affect intensity) se réfère à la **force typique** avec laquelle une personne vit ses émotions. Ce n'est pas une mesure de la fréquence des émotions ni de leur valence (positive/négative), mais de leur **intensité**.

### Caractéristiques mesurées

- **Intensité des émotions positives** : exubérance, joie intense, énergie débordante
- **Intensité des émotions négatives** : anxiété forte, culpabilité intense, peur marquée
- **Stabilité émotionnelle** : tendance à osciller entre états émotionnels
- **Réactivité émotionnelle** : force des réactions émotionnelles aux événements

## Structure du questionnaire

### Items

Le questionnaire comprend 20 items évaluant différents aspects de l'intensité émotionnelle :

**Items directs (forte intensité)** - Items 1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 14, 16, 17, 19 :
- Reflètent des expériences émotionnelles intenses
- Exemples : "forte exubérance", "impression d'être au paradis", "éclater de joie"
- Score direct : réponse élevée = haute intensité émotionnelle

**Items inversés (faible intensité)** - Items 5, 10, 13, 15, 18, 20 :
- Reflètent des expériences émotionnelles calmes et modérées
- Exemples : "sans inquiétude et content plutôt qu'excité", "satisfaction calme"
- Score inversé : réponse élevée = faible intensité émotionnelle (inversé dans le calcul)

### Options de réponse

Chaque item est évalué sur une échelle de 6 points :

| Code | Label | Score |
|------|-------|-------|
| 1 | Jamais | 1 |
| 2 | Presque jamais | 2 |
| 3 | Occasionnellement | 3 |
| 4 | Habituellement | 4 |
| 5 | Presque toujours | 5 |
| 6 | Toujours | 6 |

## Cotation

### Calcul du score

1. **Items directs** (1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 14, 16, 17, 19) :
   - Score = valeur brute (1-6)

2. **Items inversés** (5, 10, 13, 15, 18, 20) :
   - Score = 7 - valeur brute
   - Exemple : "Jamais" (1) devient 6, "Toujours" (6) devient 1

3. **Score moyen** :
   - Somme des 20 items après recodage ÷ 20
   - Plage : 1.0–6.0

### Interprétation (échelle continue)

| Score moyen | Catégorie | Interprétation |
|-------------|-----------|----------------|
| < 2.0 | Très faible | Émotions vécues avec très peu d'intensité |
| 2.0-2.9 | Presque jamais intense | Intensité émotionnelle faible |
| 3.0-3.9 | Occasionnellement intense | Intensité émotionnelle modérée |
| 4.0-4.9 | Habituellement intense | Intensité émotionnelle élevée |
| 5.0-5.9 | Presque toujours intense | Intensité émotionnelle très élevée |
| ≥ 6.0 | Toujours intense | Intensité émotionnelle maximale |

**Note** : L'interprétation est continue plutôt que catégorielle. Un score plus proche de 6 indique des émotions vécues plus intensément.

## Utilisation

### Exemple de base

```python
from questionnaires.auto.aim_short import AIMShort

# Initialiser le questionnaire
aim = AIMShort()

# Préparer les réponses (1=Jamais ... 6=Toujours)
answers = {
    "q1": 4,   # Exubérance - habituellement
    "q2": 3,   # Impression paradis - occasionnellement
    "q3": 4,   # Extase - habituellement
    # ... (tous les 20 items)
    "q20": 3   # Sentiments calmes - occasionnellement (inversé)
}

# Calculer le score
result = aim.calculate_score(answers)

print(f"Score moyen: {result['mean_score']}/6.00")
print(f"Catégorie: {result['category']}")
print(f"Sévérité: {result['severity']}")
print(f"Interprétation: {result['interpretation']}")
```

### Validation des réponses

```python
# Valider avant le calcul du score
validation = aim.validate_answers(answers)

if validation["valid"]:
    result = aim.calculate_score(answers)
else:
    print("Erreurs de validation:")
    for error in validation["errors"]:
        print(f"  - {error}")
    
    if validation["warnings"]:
        print("Avertissements:")
        for warning in validation["warnings"]:
            print(f"  - {warning}")
```

### Accéder aux métadonnées

```python
# Obtenir les métadonnées du questionnaire
metadata = aim.get_metadata()
print(f"Nombre d'items: {metadata['num_items']}")
print(f"Items inversés: {metadata['reverse_items']}")
print(f"Type de score: {metadata['score_type']}")

# Obtenir toutes les questions
questions = aim.get_questions()
for q in questions:
    print(f"{q['id']}: {q['text']}")
    print(f"  Inversé: {q['reverse_scored']}")

# Obtenir le schéma complet
schema = aim.get_schema()
```

## Scénarios cliniques

### Patient avec faible intensité émotionnelle

```python
# Patient rapportant des émotions peu intenses
answers = {}
for i in range(1, 21):
    if i in AIMShort.REVERSE_ITEMS:  # Items calmes
        answers[f"q{i}"] = 5  # D'accord avec calme (inversé = 2)
    else:  # Items intenses
        answers[f"q{i}"] = 2  # Presque jamais intense

result = aim.calculate_score(answers)
# Score moyen bas (< 3.0) - faible intensité émotionnelle
```

### Patient avec haute intensité émotionnelle

```python
# Patient rapportant des émotions très intenses
answers = {}
for i in range(1, 21):
    if i in AIMShort.REVERSE_ITEMS:  # Items calmes
        answers[f"q{i}"] = 2  # Peu d'accord avec calme (inversé = 5)
    else:  # Items intenses
        answers[f"q{i}"] = 5  # Presque toujours intense

result = aim.calculate_score(answers)
# Score moyen élevé (> 4.5) - haute intensité émotionnelle
```

## Contextes cliniques

### 1. Dépistage des troubles bipolaires

Une intensité émotionnelle très élevée peut être un marqueur de vulnérabilité aux troubles bipolaires :

- **Score moyen > 5.0** : Risque accru de cyclothymie ou trouble bipolaire
- Scores particulièrement élevés sur items de joie intense et énergie
- Utile en combinaison avec d'autres outils de dépistage (MDQ, HCL-32)

### 2. Évaluation de la dépression

Une intensité émotionnelle très faible peut suggérer :

- **Score moyen < 2.5** : Possible émoussement affectif
- Symptôme dépressif (perte de réactivité émotionnelle)
- Anhédonie ou détachement émotionnel

### 3. Troubles anxieux

Une haute intensité sur items négatifs (anxiété, peur) :

- Peut indiquer une vulnérabilité aux troubles anxieux
- Hyperréactivité émotionnelle aux stresseurs
- Difficulté de régulation émotionnelle

### 4. Personnalité et tempérament

L'AIM mesure un trait de personnalité stable :

- **Score élevé** : Tempérament cyclothymique, hyperthymique
- **Score faible** : Tempérament dysthymique, détachement émotionnel
- Utile pour comprendre le fonctionnement émotionnel habituel

## Caractéristiques psychométriques

### Fidélité

- **Cohérence interne** : α de Cronbach = 0.90 (version originale anglaise)
- **Test-retest** : Corrélations > 0.80 (stabilité sur 3 mois)
- **Fidélité des sous-échelles** : Émotions positives (α = 0.83), Émotions négatives (α = 0.75)

### Validité

- **Validité de construit** : 
  - Corrélations positives avec extraversion (r = 0.45)
  - Corrélations positives avec névrosisme (r = 0.35)
  - Corrélations négatives avec stabilité émotionnelle (r = -0.40)

- **Validité discriminante** :
  - Distingue les patients bipolaires des contrôles
  - Distingue les tempéraments cyclothymiques des autres

- **Validité prédictive** :
  - Prédit la réactivité émotionnelle aux événements de vie
  - Prédit le risque de trouble bipolaire chez les sujets à risque

### Normes

**Population générale française** (données indicatives) :
- Moyenne : 3.5 (ET = 0.8)
- Hommes : M = 3.3, Femmes : M = 3.7
- Variation selon l'âge : plus élevé chez les jeunes adultes

**Populations cliniques** :
- Trouble bipolaire : M = 4.5-5.2
- Dépression majeure : M = 2.8-3.2
- Trouble anxieux : M = 3.8-4.3

## Applications cliniques

### Indications

1. **Dépistage des troubles de l'humeur**
   - Identification de la vulnérabilité bipolaire
   - Évaluation du tempérament affectif
   - Distinction unipôlaire vs. bipolaire

2. **Évaluation de la personnalité**
   - Profil émotionnel habituel
   - Style de régulation émotionnelle
   - Réactivité émotionnelle

3. **Recherche**
   - Études sur la régulation émotionnelle
   - Prédiction de la réponse thérapeutique
   - Études de vulnérabilité aux troubles affectifs

### Interprétation clinique

- **Score < 2.5** : 
  - Possible émoussement affectif ou alexithymie
  - Envisager dépression, détachement émotionnel
  - Peut indiquer style émotionnel très contrôlé

- **Score 2.5-4.0** :
  - Intensité émotionnelle dans la norme
  - Réactivité émotionnelle typique
  - Pas de préoccupation particulière

- **Score 4.0-5.0** :
  - Intensité émotionnelle élevée
  - Sensibilité émotionnelle accrue
  - Surveiller pour troubles de l'humeur

- **Score > 5.0** :
  - Intensité émotionnelle très élevée
  - Fort risque de trouble bipolaire ou cyclothymie
  - Évaluation psychiatrique recommandée

### Limites

1. Mesure trait (stable) plutôt qu'état (momentané)
2. Sensibilité aux biais de rappel et de désirabilité sociale
3. Ne distingue pas intensité positive vs. négative (score global)
4. Peut être influencé par l'état thymique actuel malgré la consigne

## Instructions de passation

### Consigne importante

**"Répondez en pensant à votre mode de fonctionnement habituel, en excluant les périodes où votre humeur était anormalement basse (dépression) ou élevée (hypomanie/manie)."**

Cette consigne est cruciale car :
- L'AIM mesure un **trait** (tempérament) et non un **état** (humeur actuelle)
- Les épisodes thymiques peuvent biaiser les réponses
- On cherche à évaluer la réactivité émotionnelle typique

### Points de vigilance

✓ **Vérifier la compréhension de la consigne** (exclure épisodes thymiques)  
✓ **Toutes les réponses doivent être entre 1 et 6**  
✓ **Les 20 items sont obligatoires**  
✓ **Attention aux réponses toutes identiques** (avertissement automatique)  
⚠️ **Score > 5.0 nécessite évaluation psychiatrique approfondie**

## Validation des données

Le module effectue automatiquement :

- ✓ Vérification de la présence des 20 items
- ✓ Validation des valeurs (1-6)
- ✓ Détection des types de données incorrects
- ✓ Avertissement si toutes les réponses sont identiques
- ✓ Avertissement si toutes les réponses sont minimales (1) ou maximales (6)
- ✓ Application correcte du recodage inversé

## Résultat du calcul

La méthode `calculate_score()` retourne un dictionnaire contenant :

```python
{
    "mean_score": 3.65,              # Score moyen (1.0-6.0)
    "sum_score": 73,                 # Somme (20-120)
    "score_range": [1.0, 6.0],       # Plage moyenne
    "sum_range": [20, 120],          # Plage somme
    "category": "Occasionnellement intense",  # Catégorie
    "severity": "moderate",          # Niveau
    "item_scores": {                 # Détails par item
        "q1": {
            "raw": 4,                # Réponse brute
            "scored": 4,             # Score après recodage
            "reversed": False        # Item inversé?
        },
        "q5": {
            "raw": 3,
            "scored": 4,             # 7-3 pour item inversé
            "reversed": True
        },
        # ... autres items
    },
    "interpretation": "...",         # Interprétation clinique
    "warnings": [],                  # Avertissements éventuels
    "calculation_date": "2025-11-03T..."  # Date de calcul
}
```

## Références

1. Larsen, R. J., & Diener, E. (1987). 
   *Affect intensity as an individual difference characteristic: A review*. 
   Journal of Research in Personality, 21(1), 1-39.

2. Larsen, R. J., Diener, E., & Emmons, R. A. (1986). 
   *Affect intensity and reactions to daily life events*. 
   Journal of Personality and Social Psychology, 51(4), 803-814.

3. Weinfurt, K. P., Bryant, F. B., & Yarnold, P. R. (1994). 
   *The factor structure of the Affect Intensity Measure: In search of a measurement model*. 
   Journal of Research in Personality, 28(3), 314-331.

4. Geuens, M., & De Pelsmacker, P. (2002). 
   *Developing a short affect intensity scale*. 
   Psychological Reports, 91(2), 657-670.

## Support

Pour des questions ou problèmes concernant ce module :
- Consultez les tests unitaires dans `tests/test_aim_short.py`
- Vérifiez les exemples d'utilisation dans `EXAMPLE_USAGE.md`
- Référez-vous au guide rapide dans `QUICK_REFERENCE.md`

