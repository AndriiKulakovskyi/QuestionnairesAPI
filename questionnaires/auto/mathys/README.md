# MAThyS - Évaluation Multidimensionnelle des états thymiques

## Description

Le **MAThyS (Évaluation Multidimensionnelle des états thymiques)** est une échelle d'auto-évaluation en 20 items évaluant l'intensité et la variabilité des états thymiques sur 5 dimensions cliniques. Chaque item utilise une échelle visuelle analogique de 0 à 10 avec des ancrages bipolaires.

## Caractéristiques

- **Nombre d'items**: 20
- **Format de réponse**: Échelle 0-10 (continue ou par paliers de 1)
- **Période de référence**: La dernière semaine
- **Durée d'administration**: ~5-7 minutes
- **Score total**: 0–200
- **Dimensions**: 5 subscales

## Dimensions évaluées

### 1. Émotion (4 items: 3, 7, 10, 18)
- **Range**: 0-40
- Évalue l'intensité et la variabilité émotionnelle
- Items couvrant l'anesthésie émotionnelle vs. perte de contrôle émotionnel
- Réactivité émotionnelle et intensité des ressentis

### 2. Motivation (7 items: 2, 11, 12, 15, 16, 17, 19)
- **Range**: 0-70
- Évalue le tonus, l'énergie et la motivation
- Ralentissement vs. agitation psychomotrice
- Initiative et projets

### 3. Perception sensorielle (5 items: 1, 6, 8, 13, 20)
- **Range**: 0-50
- Évalue la sensibilité aux stimuli sensoriels
- Couleurs, toucher, musique, goût, odeurs
- Hypo- vs. hypersensibilité

### 4. Interaction personnelle (2 items: 4, 14)
- **Range**: 0-20
- Évalue le retrait social vs. désinhibition
- Désir de communication

### 5. Cognition (2 items: 5, 9)
- **Range**: 0-20
- Évalue la distractibilité et le rythme de pensée
- Ralentissement vs. accélération cognitive

## Cotation

### Items inversés

Les items suivants nécessitent un **recodage inversé** (score = 10 - valeur brute) :

**Items inversés (8 au total)**: 5, 6, 7, 8, 9, 10, 17, 18

### Calcul des scores

Après recodage des items inversés :

1. **Émotion** = q3 + q7(inversé) + q10(inversé) + q18(inversé)
2. **Motivation** = q2 + q11 + q12 + q15 + q16 + q17(inversé) + q19
3. **Perception** = q1 + q6(inversé) + q8(inversé) + q13 + q20
4. **Interaction** = q4 + q14
5. **Cognition** = q5(inversé) + q9(inversé)

**Score total** = Somme des 5 sous-scores (0-200)

### Interprétation

Le MAThyS est un outil **dimensionnel** qui évalue l'intensité des états thymiques :
- Les scores ne sont pas catégoriels (pas de seuils diagnostiques stricts)
- Utile pour caractériser le profil thymique
- Permet le suivi longitudinal des variations
- Chaque dimension peut être analysée indépendamment

**Points de repère** :
- Score à 100/200 (50%) = état habituel moyen sur l'ensemble des dimensions
- Scores extrêmes (très bas ou très élevés) sur une dimension = déviation significative

## Utilisation

```python
from questionnaires.auto.mathys import MAThyS

# Initialiser le questionnaire
mathys = MAThyS()

# Obtenir les métadonnées
metadata = mathys.get_metadata()

# Obtenir les questions
questions = mathys.get_questions()

# Exemple de réponses (0-10 pour chaque item)
answers = {
    "q1": 5.0, "q2": 6.0, "q3": 4.0, "q4": 5.0, "q5": 5.0,
    "q6": 5.0, "q7": 5.0, "q8": 5.0, "q9": 5.0, "q10": 5.0,
    "q11": 6.0, "q12": 5.0, "q13": 5.0, "q14": 5.0, "q15": 4.0,
    "q16": 5.0, "q17": 5.0, "q18": 5.0, "q19": 5.0, "q20": 5.0
}

# Valider les réponses
validation = mathys.validate_answers(answers)
if validation.valid:
    # Calculer les scores
    result = mathys.calculate_score(answers)
    print(f"Score total: {result.total_score}/200")
    print(f"Émotion: {result.subscales['emotion'].score}/40")
    print(f"Motivation: {result.subscales['motivation'].score}/70")
    print(f"Perception: {result.subscales['perception'].score}/50")
    print(f"Interaction: {result.subscales['interaction'].score}/20")
    print(f"Cognition: {result.subscales['cognition'].score}/20")
else:
    print(f"Erreurs: {validation.errors}")
```

## Ancrages bipolaires des items

Chaque item présente deux pôles opposés (0 = pôle gauche, 10 = pôle droit, ~5 = état habituel) :

1. **Sensibilité aux couleurs**: Moins sensible ↔ Plus sensible
2. **Tonus**: Manque de tonus ↔ Tension interne importante
3. **Émotions**: Anesthésié(e) émotionnellement ↔ Perte de contrôle émotionnel
4. **Interaction sociale**: Replié(e) sur soi ↔ Désinhibé(e)
5. **Attention**: Facilement distrait(e) ↔ Pas attentif(ve) à l'environnement (inversé)
6. **Sensibilité au toucher**: Plus sensible ↔ Moins sensible (inversé)
7. **Variabilité de l'humeur**: Humeur variable ↔ Humeur monotone (inversé)
8. **Sensibilité à la musique**: Particulièrement sensible ↔ Plus indifférent(e) (inversé)
9. **Rythme de pensée**: Cerveau qui ne s'arrête jamais ↔ Cerveau au ralenti (inversé)
10. **Réactivité**: Plus réactif(ve) ↔ Moins réactif(ve) (inversé)
11. **Énergie**: Sans énergie ↔ Grande énergie
12. **Pensées**: Pensées ralenties ↔ Idées qui défilent
13. **Goût**: Nourriture sans goût ↔ Plaisirs gastronomiques
14. **Communication**: Moins envie de communiquer ↔ Plus envie de communiquer
15. **Motivation**: Manque de motivation ↔ Multiplie les projets
16. **Intérêt**: Perte d'intérêt ↔ Envie de faire plus de choses
17. **Décisions**: Décisions plus rapides ↔ Difficultés à décider (inversé)
18. **Intensité émotionnelle**: Émotions très intenses ↔ Émotions atténuées (inversé)
19. **Psychomotricité**: Ralenti(e) dans les mouvements ↔ Physiquement agité(e)
20. **Sensibilité aux odeurs**: Moins sensible ↔ Plus sensible

## Références

- **Henry C., M'Bailara K., Poinsot R., et al.** Evidence for two types of bipolar depression using a dimensional approach. *Psychotherapy and Psychosomatics*, 2007;76(6):325-331.
- **Henry C., M'Bailara K., Mathieu F., et al.** Construction and validation of a dimensional scale exploring mood disorders: MAThyS (Multidimensional Assessment of Thymic States). *BMC Psychiatry*, 2008;8:82.
- **MATHYS.pdf** - French version questionnaire
- **Mathys_CotationScore.docx** - Scoring rules documentation

## Notes cliniques

### Utilité clinique

1. **Diagnostic différentiel** : Aide à distinguer les différents profils thymiques
2. **Suivi longitudinal** : Évalue l'évolution des dimensions au fil du temps
3. **Personnalisation du traitement** : Identifie les dimensions les plus affectées
4. **Recherche** : Outil dimensionnel pour études sur les troubles de l'humeur

### Points d'attention

- **Items inversés** : 8 items (5,6,7,8,9,10,17,18) nécessitent un recodage
- **Pas de seuils diagnostiques** : L'échelle est dimensionnelle, pas catégorielle
- **Contexte clinique** : Les scores doivent être interprétés dans le contexte clinique global
- **État habituel** : Le centre de l'échelle (~5) représente l'état habituel du patient

### Profils typiques

**Profil dépressif** :
- Motivation basse
- Émotion basse (anesthésie émotionnelle)
- Cognition ralentie
- Interaction sociale réduite

**Profil maniaque/hypomaniaque** :
- Motivation élevée
- Émotion intense
- Cognition accélérée
- Perception sensorielle accrue

**Profil mixte** :
- Scores élevés sur plusieurs dimensions
- Variabilité importante
- Combinaison d'éléments dépressifs et maniaques

## Propriétés psychométriques

- **Validité** : Validée dans les troubles bipolaires et unipolaires
- **Fiabilité** : Bonnes propriétés psychométriques
- **Sensibilité** : Détecte les variations d'états thymiques
- **Structure factorielle** : 5 dimensions distinctes et cohérentes

## Exemples d'interprétation

### Exemple 1 : État habituel équilibré
```
Total: 100/200 (50%)
Émotion: 20/40, Motivation: 35/70, Perception: 25/50, 
Interaction: 10/20, Cognition: 10/20
```
→ Profil centré, correspondant à un état habituel équilibré

### Exemple 2 : Profil dépressif
```
Total: 60/200 (30%)
Émotion: 10/40, Motivation: 15/70, Perception: 15/50, 
Interaction: 8/20, Cognition: 12/20
```
→ Scores bas sur la plupart des dimensions, suggérant un ralentissement global

### Exemple 3 : Profil hypomaniaque
```
Total: 150/200 (75%)
Émotion: 32/40, Motivation: 60/70, Perception: 38/50, 
Interaction: 16/20, Cognition: 4/20
```
→ Scores élevés sauf en cognition (accélération = score bas après recodage)

