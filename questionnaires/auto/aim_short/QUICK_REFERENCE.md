# AIM-short - Guide de référence rapide

## En bref

- **20 items** mesurant l'intensité de la réactivité émotionnelle
- **Échelle 6 points** : 1 (Jamais) … 6 (Toujours)
- **Score** : Moyenne des 20 items recodés (1.0-6.0)
- **6 items inversés** : 5, 10, 13, 15, 18, 20 (recodage 7 - valeur)
- **14 items directs** : 1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 14, 16, 17, 19

## Utilisation rapide

```python
from questionnaires.auto.aim_short import AIMShort

aim = AIMShort()
answers = {f"q{i}": 3 for i in range(1, 21)}
result = aim.calculate_score(answers)

print(result['mean_score'])  # 3.3
print(result['category'])    # "Occasionnellement intense"
```

## Cotation

### Items inversés (calmes, modérés) - Recodage : 7 - valeur

| Item | Contenu clé | Recodage |
|------|-------------|----------|
| 5 | sans inquiétude et content plutôt qu'excité | 7 - valeur |
| 10 | satisfaction calme | 7 - valeur |
| 13 | détendu et content plutôt qu'excité | 7 - valeur |
| 15 | sentiment de bonheur calme | 7 - valeur |
| 18 | satisfaction plutôt que joie | 7 - valeur |
| 20 | satisfaction et calme plutôt qu'excitation | 7 - valeur |

### Items directs (intenses, forts) - Score = valeur

| Item | Contenu clé |
|------|-------------|
| 1 | forte exubérance |
| 2 | impression d'être au paradis |
| 3 | extase |
| 4 | films tristes touchent profondément |
| 6 | voix tremblante, cœur bat vite |
| 7 | osciller entre bonne humeur et très joyeux |
| 8 | éclater de joie |
| 9 | plein d'énergie |
| 11 | sentiment très fort de culpabilité |
| 12 | au sommet du monde |
| 14 | anxiété très forte |
| 16 | déborder d'énergie |
| 17 | émotion de culpabilité forte |
| 19 | trembler quand heureux |

## Interprétation

| Score moyen | Catégorie | Signification clinique |
|-------------|-----------|------------------------|
| < 2.0 | Très faible | Émoussement affectif possible |
| 2.0-2.9 | Presque jamais intense | Intensité faible |
| 3.0-3.9 | Occasionnellement intense | Intensité modérée (normal) |
| 4.0-4.9 | Habituellement intense | Intensité élevée |
| ≥ 5.0 | Presque toujours/Toujours intense | ⚠️ Risque bipolaire, évaluation nécessaire |

## Formules de calcul

### Pour chaque item

```
Si item inversé (5, 10, 13, 15, 18, 20):
    score_item = 7 - réponse
Sinon:
    score_item = réponse
```

### Score moyen

```
somme_totale = Σ(score_item pour tous les 20 items)
score_moyen = somme_totale / 20
```

**Plages** :
- Somme : 20-120
- Moyenne : 1.0-6.0

## Exemples de scores

### Patient faible intensité (Score moyen = 2.0)

```python
# D'accord avec items calmes, en désaccord avec items intenses
answers = {}
for i in range(1, 21):
    if i in {5,10,13,15,18,20}:  # Items calmes
        answers[f"q{i}"] = 5  # Presque toujours calme → 7-5=2
    else:  # Items intenses
        answers[f"q{i}"] = 2  # Presque jamais intense → 2
# Moyenne: (6*2 + 14*2) / 20 = 2.0
```

### Patient intensité modérée (Score moyen = 3.5)

```python
# Réponses mixtes, équilibrées
answers = {f"q{i}": 3 for i in range(1, 21)}
# Items inversés: 7-3=4, items directs: 3
# Moyenne: (6*4 + 14*3) / 20 = 3.3
```

### Patient haute intensité (Score moyen = 5.0)

```python
# En désaccord avec items calmes, d'accord avec items intenses
answers = {}
for i in range(1, 21):
    if i in {5,10,13,15,18,20}:  # Items calmes
        answers[f"q{i}"] = 2  # Presque jamais calme → 7-2=5
    else:  # Items intenses
        answers[f"q{i}"] = 5  # Presque toujours intense → 5
# Moyenne: (6*5 + 14*5) / 20 = 5.0
```

## Contextes cliniques

### 🔵 Dépistage bipolaire

**Score ≥ 5.0** suggère :
- Hypersensibilité émotionnelle
- Tempérament cyclothymique
- Vulnérabilité bipolaire
- → Évaluation avec MDQ, HCL-32

### 🟡 Dépression

**Score < 2.5** peut indiquer :
- Émoussement affectif
- Anhédonie
- Détachement émotionnel
- → Évaluation avec MADRS, BDI

### 🔴 Troubles anxieux

**Score 4.0-5.0** avec items anxieux élevés :
- Hyperréactivité aux stresseurs
- Difficulté de régulation
- → Évaluation avec STAI, HADS

### 🟢 Personnalité

**Toutes plages** :
- Trait de personnalité stable
- Style émotionnel habituel
- Tempérament affectif

## Points de vigilance

✓ **Consigne cruciale** : "Mode de fonctionnement habituel, hors épisodes thymiques anormaux"  
✓ **Tous les 20 items obligatoires**  
✓ **Valeurs valides : 1-6 uniquement**  
✓ **Vérifier le recodage des 6 items inversés**  
⚠️ **Score ≥ 5.0 nécessite évaluation psychiatrique**  
⚠️ **Avertissement si toutes réponses identiques**

## Validation rapide

```python
# Validation avant calcul
validation = aim.validate_answers(answers)

if not validation["valid"]:
    print("Erreurs:", validation["errors"])
if validation["warnings"]:
    print("Avertissements:", validation["warnings"])
```

## Structure du résultat

```python
{
    "mean_score": 3.65,           # Moyenne (1.0-6.0) 
    "sum_score": 73,              # Somme (20-120)
    "score_range": [1.0, 6.0],
    "sum_range": [20, 120],
    "category": "Occasionnellement intense",
    "severity": "moderate",
    "item_scores": {
        "q1": {"raw": 4, "scored": 4, "reversed": False},
        "q5": {"raw": 3, "scored": 4, "reversed": True},
        # ...
    },
    "interpretation": "Score moyen de 3.65/6.00...",
    "warnings": [],
    "calculation_date": "2025-11-03T..."
}
```

## Profils typiques

### Profil "Tempérament stable"
- Score moyen: 2.5-3.5
- Émotions mesurées et contrôlées
- Réactivité émotionnelle typique
- **Interprétation**: Normal

### Profil "Hypersensible"
- Score moyen: 4.5-5.5
- Émotions intenses et fortes
- Grande réactivité aux événements
- **Interprétation**: Risque troubles affectifs

### Profil "Émoussé"
- Score moyen: 1.5-2.5
- Émotions peu intenses
- Faible réactivité émotionnelle
- **Interprétation**: Possible alexithymie

### Profil "Cyclothymique"
- Score moyen: > 5.0
- Émotions extrêmement intenses
- Oscillations émotionnelles fortes
- **Interprétation**: Fort risque bipolaire

## Combinaisons avec autres échelles

### AIM + MDQ (Mood Disorder Questionnaire)
```python
if aim_result['mean_score'] >= 5.0 and mdq_positive:
    print("⚠️ Forte suspicion de trouble bipolaire")
```

### AIM + MADRS (dépression)
```python
if aim_result['mean_score'] < 2.5 and madrs_score > 20:
    print("Émoussement affectif dans contexte dépressif")
```

### AIM + STAI (anxiété)
```python
if aim_result['mean_score'] > 4.5 and stai_trait_high:
    print("Hyperréactivité émotionnelle + anxiété trait")
```

## API minimale

```python
aim = AIMShort()

# Métadonnées
aim.get_metadata()      # Info générale
aim.get_questions()     # Liste des 20 items
aim.get_sections()      # Sections (1 seule)
aim.get_schema()        # Schéma JSON complet

# Validation & Scoring
aim.validate_answers(answers)    # Validation seule
aim.calculate_score(answers)     # Calcul avec validation
```

## Cas d'usage typiques

### 1. Dépistage en consultation initiale

```python
result = aim.calculate_score(patient_answers)
if result['mean_score'] >= 5.0:
    flag_for_bipolar_screening()
```

### 2. Évaluation du tempérament

```python
result = aim.calculate_score(answers)
temperament = classify_temperament(result['mean_score'])
# Ex: cyclothymique, hyperthymique, dysthymique
```

### 3. Suivi longitudinal

```python
baseline = aim.calculate_score(t0_answers)
followup = aim.calculate_score(t6months_answers)
stability = abs(baseline['mean_score'] - followup['mean_score'])
# Trait stable devrait avoir stability < 0.5
```

## Dépannage

**Erreur : Items manquants**
- Vérifier que tous q1-q20 sont présents

**Erreur : Valeur hors limites**
- S'assurer que toutes les valeurs sont 1-6

**Score inattendu**
- Vérifier le recodage des items 5, 10, 13, 15, 18, 20
- Consulter `result['item_scores']` pour détails

**Score très élevé (> 5.5)**
- Vérifier la compréhension de la consigne
- Exclure influence d'épisode hypomaniaque actuel
- Considérer évaluation psychiatrique

**Score très faible (< 1.5)**
- Vérifier sincérité des réponses
- Exclure influence d'épisode dépressif actuel
- Considérer alexithymie, détachement

