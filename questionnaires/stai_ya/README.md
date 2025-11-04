# STAI-YA (Inventaire d'Anxiété État - STAI Forme Y-A)

## Vue d'ensemble

Le **STAI-YA (State-Trait Anxiety Inventory - Form Y-A)** est un questionnaire d'auto-évaluation de 20 items mesurant l'anxiété-état, c'est-à-dire comment la personne se sent "à l'instant, juste en ce moment".

### Informations générales

- **ID**: STAI-YA.fr
- **Nom complet**: Inventaire d'Anxiété État (STAI – Forme Y-A)
- **Langue**: Français (fr-FR)
- **Version**: 1.0
- **Nombre d'items**: 20
- **Période de référence**: "À l'instant, juste en ce moment"
- **Échelle de réponse**: 4 points (non / plutôt non / plutôt oui / oui)
- **Plage de scores**: 20–80
- **Temps d'administration**: 5-10 minutes

## Structure du questionnaire

### Items

Le questionnaire comprend 20 items évaluant l'anxiété-état actuelle :

**Items inversés (positifs)** - Items 1, 2, 5, 8, 10, 11, 15, 16, 19, 20 :
- Reflètent des états de calme, sécurité, confort
- Exemples : "Je me sens calme", "Je me sens en sécurité", "Je me sens tranquille"
- Score inversé : une réponse "non" indique une anxiété élevée

**Items directs (négatifs)** - Items 3, 4, 6, 7, 9, 12, 13, 14, 17, 18 :
- Reflètent des états de tension, inquiétude, détresse
- Exemples : "Je suis tendu(e)", "Je me sens surmené(e)", "Je me sens ému(e)"
- Score direct : une réponse "oui" indique une anxiété élevée

### Options de réponse

Chaque item est évalué sur une échelle de 4 points :

| Code | Label | Score brut |
|------|-------|-----------|
| 1 | non | 1 |
| 2 | plutôt non | 2 |
| 3 | plutôt oui | 3 |
| 4 | oui | 4 |

## Cotation

### Calcul du score

1. **Items directs** (3, 4, 6, 7, 9, 12, 13, 14, 17, 18) :
   - Score = valeur brute (1-4)

2. **Items inversés** (1, 2, 5, 8, 10, 11, 15, 16, 19, 20) :
   - Score = 5 - valeur brute
   - Exemple : "non" (1) devient 4, "oui" (4) devient 1

3. **Score total** :
   - Somme des 20 items après recodage
   - Plage : 20–80

### Interprétation (normes françaises)

| Score | Catégorie | Interprétation clinique |
|-------|-----------|------------------------|
| ≤35 | Anxiété état très faible | Niveau d'anxiété très bas, patient très calme |
| 36-45 | Anxiété état faible | Niveau d'anxiété légèrement en dessous de la moyenne |
| 46-55 | Anxiété état moyenne | Niveau d'anxiété dans la norme |
| 56-65 | Anxiété état élevée | Niveau cliniquement significatif nécessitant attention |
| ≥66 | Anxiété état très élevée | Détresse aiguë nécessitant intervention immédiate |

## Utilisation

### Exemple de base

```python
from questionnaires.stai_ya import STAIYA

# Initialiser le questionnaire
stai = STAIYA()

# Préparer les réponses (1=non, 2=plutôt non, 3=plutôt oui, 4=oui)
answers = {
    "q1": 2,   # Je me sens calme - plutôt non
    "q2": 3,   # Je me sens en sécurité - plutôt oui
    "q3": 3,   # Je suis tendu(e) - plutôt oui
    # ... (tous les 20 items)
    "q20": 3   # Je me sens de bonne humeur - plutôt oui
}

# Calculer le score
result = stai.calculate_score(answers)

print(f"Score total: {result['total_score']}/80")
print(f"Catégorie: {result['category']}")
print(f"Sévérité: {result['severity']}")
print(f"Interprétation: {result['interpretation']}")
```

### Validation des réponses

```python
# Valider avant le calcul du score
validation = stai.validate_answers(answers)

if validation["valid"]:
    result = stai.calculate_score(answers)
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
metadata = stai.get_metadata()
print(f"Nombre d'items: {metadata['num_items']}")
print(f"Items inversés: {metadata['reverse_items']}")

# Obtenir toutes les questions
questions = stai.get_questions()
for q in questions:
    print(f"{q['id']}: {q['text']}")
    print(f"  Inversé: {q['reverse_scored']}")

# Obtenir le schéma complet
schema = stai.get_schema()
```

## Scénarios cliniques

### Patient calme (anxiété faible)

```python
# Patient se sent calme et détendu
answers = {}
for i in range(1, 21):
    if i in STAIYA.REVERSE_ITEMS:  # Items positifs
        answers[f"q{i}"] = 4  # "oui" - se sent calme/content
    else:  # Items négatifs
        answers[f"q{i}"] = 1  # "non" - pas tendu/inquiet

result = stai.calculate_score(answers)
# Score: 20, Catégorie: "Anxiété état très faible"
```

### Patient anxieux (anxiété élevée)

```python
# Patient rapporte une anxiété élevée
answers = {}
for i in range(1, 21):
    if i in STAIYA.REVERSE_ITEMS:  # Items positifs
        answers[f"q{i}"] = 1  # "non" - ne se sent pas calme
    else:  # Items négatifs
        answers[f"q{i}"] = 4  # "oui" - très tendu/inquiet

result = stai.calculate_score(answers)
# Score: 80, Catégorie: "Anxiété état très élevée"
```

### Comparaison pré-post intervention

```python
# Évaluation avant intervention
pre_answers = {f"q{i}": 3 for i in range(1, 21)}
pre_result = stai.calculate_score(pre_answers)

# Évaluation après intervention (amélioration)
post_answers = {f"q{i}": 2 for i in range(1, 21)}
post_result = stai.calculate_score(post_answers)

reduction = pre_result['total_score'] - post_result['total_score']
print(f"Réduction de l'anxiété: {reduction} points")
```

## Caractéristiques psychométriques

### Fidélité

- **Cohérence interne** : α de Cronbach généralement > 0.90
- **Test-retest** : Corrélations faibles à modérées (attendu pour une mesure d'état)

### Validité

- **Validité de contenu** : Items reflètent les symptômes anxieux selon DSM
- **Validité de critère** : Corrélations avec autres mesures d'anxiété
- **Sensibilité au changement** : Bonne sensibilité aux fluctuations situationnelles

### Normes

Les seuils d'interprétation sont basés sur des normes françaises établies pour :
- Population générale adulte
- Populations cliniques (troubles anxieux, dépression)
- Contextes situationnels (examens, interventions médicales)

## Applications cliniques

### Indications

1. **Évaluation de l'anxiété situationnelle**
   - Anxiété pré-opératoire
   - Anxiété lors d'examens
   - Réactions de stress aigu

2. **Suivi thérapeutique**
   - Évaluation de l'efficacité des interventions
   - Monitoring des symptômes anxieux
   - Ajustement des traitements

3. **Recherche**
   - Études sur l'anxiété-état
   - Essais cliniques
   - Validation d'interventions

### Interprétation clinique

- **Score ≤35** : Pas d'anxiété cliniquement significative
- **Score 36-55** : Anxiété légère à moyenne, surveillance recommandée
- **Score 56-65** : Anxiété cliniquement significative, intervention suggérée
- **Score ≥66** : Anxiété sévère, intervention urgente recommandée

### Limites

1. Mesure uniquement l'anxiété-état (pas l'anxiété-trait)
2. Sensible au contexte de passation
3. Possibilité de biais de désirabilité sociale
4. Nécessite compréhension de lecture adéquate

## Validation des données

Le module effectue automatiquement :

- ✓ Vérification de la présence des 20 items
- ✓ Validation des valeurs (1-4)
- ✓ Détection des types de données incorrects
- ✓ Avertissement si toutes les réponses sont identiques
- ✓ Application correcte du recodage inversé

## Résultat du calcul

La méthode `calculate_score()` retourne un dictionnaire contenant :

```python
{
    "total_score": 50,           # Score total (20-80)
    "score_range": [20, 80],     # Plage possible
    "category": "Anxiété état moyenne",  # Catégorie
    "severity": "average",       # Niveau de sévérité
    "item_scores": {             # Détails par item
        "q1": {
            "raw": 2,            # Réponse brute
            "scored": 3,         # Score après recodage
            "reversed": True     # Item inversé?
        },
        # ... autres items
    },
    "interpretation": "...",     # Interprétation clinique
    "warnings": [],              # Avertissements éventuels
    "calculation_date": "2025-11-03T..."  # Date de calcul
}
```

## Références

1. Spielberger, C. D., Gorsuch, R. L., Lushene, R., Vagg, P. R., & Jacobs, G. A. (1983). 
   *Manual for the State-Trait Anxiety Inventory*. Palo Alto, CA: Consulting Psychologists Press.

2. Bruchon-Schweitzer, M., & Paulhan, I. (1993). 
   *Adaptation française de l'inventaire d'anxiété Trait-État (Forme Y) de Spielberger*. 
   Paris: Les Éditions du Centre de Psychologie Appliquée.

3. Gauthier, J., & Bouchard, S. (1993). 
   Adaptation canadienne-française de la forme révisée du State-Trait Anxiety Inventory de Spielberger. 
   *Canadian Journal of Behavioural Science*, 25(4), 559-578.

## Support

Pour des questions ou problèmes concernant ce module :
- Consultez les tests unitaires dans `tests/test_stai_ya.py`
- Vérifiez les exemples d'utilisation dans ce README
- Référez-vous à la documentation de l'API dans le code source

