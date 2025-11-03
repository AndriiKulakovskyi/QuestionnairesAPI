# STAI-YA - Guide de référence rapide

## En bref

- **20 items** mesurant l'anxiété-état actuelle
- **Échelle 4 points** : non (1) / plutôt non (2) / plutôt oui (3) / oui (4)
- **Score total** : 20–80
- **10 items inversés** : 1, 2, 5, 8, 10, 11, 15, 16, 19, 20
- **10 items directs** : 3, 4, 6, 7, 9, 12, 13, 14, 17, 18

## Utilisation rapide

```python
from questionnaires.stai_ya import STAIYA

stai = STAIYA()
answers = {f"q{i}": 2 for i in range(1, 21)}
result = stai.calculate_score(answers)

print(result['total_score'])  # 50
print(result['category'])     # "Anxiété état moyenne"
```

## Cotation

### Items inversés (positifs) - Recodage : 5 - valeur

| Item | Contenu | Type |
|------|---------|------|
| 1 | Je me sens calme | Inversé |
| 2 | Je me sens en sécurité | Inversé |
| 5 | Je me sens tranquille | Inversé |
| 8 | Je me sens content(e) | Inversé |
| 10 | Je me sens à mon aise | Inversé |
| 11 | Je sens que j'ai confiance en moi | Inversé |
| 15 | Je suis décontracté(e) | Inversé |
| 16 | Je suis satisfait(e) | Inversé |
| 19 | Je me sens solide, posé(e) | Inversé |
| 20 | Je me sens de bonne humeur | Inversé |

### Items directs (négatifs) - Score = valeur

| Item | Contenu | Type |
|------|---------|------|
| 3 | Je suis tendu(e), crispé(e) | Direct |
| 4 | Je me sens surmené(e) | Direct |
| 6 | Je me sens ému(e), bouleversé(e) | Direct |
| 7 | L'idée de malheurs éventuels me tracasse | Direct |
| 9 | Je me sens effrayé(e) | Direct |
| 12 | Je me sens nerveux(se), irritable | Direct |
| 13 | J'ai la frousse, la trouille | Direct |
| 14 | Je me sens indécis(e) | Direct |
| 17 | Je suis inquiet, soucieux | Direct |
| 18 | Je me sens déconcerté(e), dérouté(e) | Direct |

## Interprétation

| Score | Niveau | Action clinique |
|-------|--------|----------------|
| ≤35 | Très faible | Aucune intervention nécessaire |
| 36-45 | Faible | Surveillance recommandée |
| 46-55 | Moyen | Dans la norme |
| 56-65 | Élevé | ⚠️ Attention clinique nécessaire |
| ≥66 | Très élevé | 🚨 Intervention immédiate recommandée |

## Exemples de scores

### Patient très calme (Score = 20)

```python
# Positif sur items inversés, négatif sur items directs
answers = {}
for i in range(1, 21):
    if i in {1,2,5,8,10,11,15,16,19,20}:
        answers[f"q{i}"] = 4  # "oui" à calme = score 1
    else:
        answers[f"q{i}"] = 1  # "non" à tendu = score 1
# Total: 20 × 1 = 20
```

### Patient très anxieux (Score = 80)

```python
# Négatif sur items inversés, positif sur items directs
answers = {}
for i in range(1, 21):
    if i in {1,2,5,8,10,11,15,16,19,20}:
        answers[f"q{i}"] = 1  # "non" à calme = score 4
    else:
        answers[f"q{i}"] = 4  # "oui" à tendu = score 4
# Total: 20 × 4 = 80
```

### Patient anxiété moyenne (Score = 50)

```python
# Réponses mixtes
answers = {f"q{i}": 2 for i in range(1, 21)}
# Inversés: 5-2=3, Directs: 2
# Total: (10×3) + (10×2) = 50
```

## Formules de calcul

### Pour chaque item

```
Si item inversé (1,2,5,8,10,11,15,16,19,20):
    score_item = 5 - réponse
Sinon:
    score_item = réponse
```

### Score total

```
score_total = Σ(score_item pour tous les 20 items)
```

## Points de vigilance

✓ **Tous les 20 items sont obligatoires**  
✓ **Valeurs valides : 1, 2, 3, 4 uniquement**  
✓ **Vérifier l'application du recodage inversé**  
⚠️ **Avertissement si toutes les réponses identiques**  
⚠️ **Score ≥66 nécessite attention immédiate**

## Validation rapide

```python
# Validation avant calcul
validation = stai.validate_answers(answers)

if not validation["valid"]:
    print("Erreurs:", validation["errors"])
if validation["warnings"]:
    print("Avertissements:", validation["warnings"])
```

## Structure du résultat

```python
{
    "total_score": 50,
    "score_range": [20, 80],
    "category": "Anxiété état moyenne",
    "severity": "average",
    "item_scores": {
        "q1": {"raw": 2, "scored": 3, "reversed": True},
        # ...
    },
    "interpretation": "Score de 50/80 indique...",
    "warnings": [],
    "calculation_date": "2025-11-03T..."
}
```

## Comparaison avec STAI-Trait

| Caractéristique | STAI-YA (État) | STAI-YB (Trait) |
|----------------|----------------|-----------------|
| Mesure | Anxiété actuelle | Tendance générale |
| Période | "en ce moment" | "en général" |
| Stabilité | Variable | Stable |
| Sensibilité | Situations | Personnalité |
| Usage clinique | Suivi symptômes | Dépistage vulnérabilité |

## API minimale

```python
stai = STAIYA()

# Métadonnées
stai.get_metadata()
stai.get_questions()
stai.get_sections()
stai.get_schema()

# Validation & Scoring
stai.validate_answers(answers)
stai.calculate_score(answers)
```

## Cas d'usage typiques

### 1. Évaluation pré-opératoire

```python
pre_op = stai.calculate_score(pre_op_answers)
if pre_op['total_score'] >= 56:
    print("Anxiété pré-opératoire élevée détectée")
```

### 2. Suivi thérapeutique

```python
baseline = stai.calculate_score(week0_answers)
followup = stai.calculate_score(week4_answers)
improvement = baseline['total_score'] - followup['total_score']
print(f"Réduction de {improvement} points")
```

### 3. Monitoring en temps réel

```python
current_anxiety = stai.calculate_score(current_answers)
if current_anxiety['severity'] in ['high', 'very_high']:
    alert_clinician()
```

## Dépannage

**Erreur : Items manquants**
- Vérifier que tous les q1 à q20 sont présents

**Erreur : Valeur hors limites**
- S'assurer que toutes les valeurs sont 1, 2, 3, ou 4

**Score inattendu**
- Vérifier que les items inversés sont correctement codés
- Consulter `result['item_scores']` pour détails

**Avertissement : Réponses identiques**
- Vérifier la compréhension du patient
- Peut indiquer réponse automatique

