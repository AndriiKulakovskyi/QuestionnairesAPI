# PRISE-M - Profil des effets indésirables médicamenteux

## Description

Le **PRISE-M (Profil des effets indésirables médicamenteux)** est un questionnaire d'auto-évaluation en 32 items évaluant les effets secondaires perçus des traitements psychotropes. Chaque item est coté sur une échelle à 3 niveaux selon l'intensité de la gêne ressentie.

## Caractéristiques

- **Nombre d'items**: 32
- **Format de réponse**: 0 (Absent), 1 (Tolérable), 2 (Pénible)
- **Période de référence**: Semaine écoulée
- **Durée d'administration**: ~5-10 minutes
- **Score total**: 0–62 (somme de 31 items)
- **Sections**: 9 catégories d'effets indésirables

## Structure par sections

### 1. Troubles gastro-intestinaux (4 items)
- Diarrhée
- Constipation
- Bouche sèche
- Nausée, vomissement

### 2. Troubles cardiaques (3 items)
- Palpitations
- Vertiges
- Douleurs dans la poitrine

### 3. Problèmes cutanés (3 items)
- Augmentation de la transpiration
- Démangeaisons
- Sécheresse de la peau

### 4. Troubles neurologiques (4 items)
- Mal à la tête
- Tremblements
- Mauvais contrôle moteur
- Étourdissements

### 5. Vision/Audition (2 items)
- Vision floue
- Acouphènes (bourdonnements dans les oreilles)

### 6. Troubles uro-génital (4 items)
- Difficultés pour uriner
- Mictions douloureuses
- Mictions fréquentes
- **Règles irrégulières (pour les femmes)** - Q20 ♀

### 7. Problèmes de sommeil (2 items)
- Difficultés d'endormissement
- Augmentation du temps de sommeil

### 8. Fonctions sexuelles (3 items)
- Perte du désir sexuel
- Difficultés à atteindre un orgasme
- **Troubles de l'érection (pour les hommes)** - Q25 ♂

### 9. Autres troubles (7 items)
- Anxiété
- Difficultés de concentration
- Malaise général
- Agitation
- Fatigue
- Diminution de l'énergie
- Prise de poids

## Cotation

### Échelle de réponse

Chaque item est coté selon trois niveaux d'intensité :

- **0 = Absent** : L'effet indésirable n'est pas présent
- **1 = Tolérable** : L'effet indésirable est présent mais supportable
- **2 = Pénible** : L'effet indésirable est présent et difficile à supporter

### Items spécifiques au sexe

Le PRISE-M inclut deux items alternatifs selon le sexe du patient :

- **Q20** : "Règles irrégulières" → **Pour les femmes uniquement** ♀
- **Q25** : "Troubles de l'érection" → **Pour les hommes uniquement** ♂

**Règle de cotation** :
- Le score total somme **31 items** (32 moins 1 item selon le sexe)
- **Femmes** : Exclure Q25, score = somme des Q1-Q32 sauf Q25 (range: 0-62)
- **Hommes** : Exclure Q20, score = somme des Q1-Q32 sauf Q20 (range: 0-62)

### Logique d'exclusion automatique

Si le sexe n'est pas fourni, le système infère lequel exclure :

1. **Si Q20 ≠ 0 et Q25 = 0** → Assume femme, exclut Q25
2. **Si Q25 ≠ 0 et Q20 = 0** → Assume homme, exclut Q20
3. **Si les deux = 0** → Exclut Q25 par défaut (avec avertissement)
4. **Si les deux ≠ 0** → Génère un avertissement de cohérence

### Interprétation des scores

| Score | Niveau | Interprétation |
|-------|--------|----------------|
| **0-14** | Bas | Peu d'effets indésirables |
| **15-24** | Modéré | Effets indésirables présents mais modérés |
| **25-39** | Élevé | Effets indésirables significatifs |
| **≥40** | Très élevé | Charge importante d'effets indésirables |

**Seuils cliniques** :
- **Score ≥25** : Révision du traitement recommandée
- **≥10 items à "2" (Pénible)** : Charge élevée, intervention nécessaire

## Utilisation

```python
from questionnaires.prise_m import PRISEM

# Initialiser le questionnaire
prisem = PRISEM()

# Obtenir les métadonnées
metadata = prisem.get_metadata()

# Obtenir les questions (toutes)
questions = prisem.get_questions()

# Obtenir les questions filtrées par sexe
questions_femme = prisem.get_questions(gender="F")  # Exclut Q25
questions_homme = prisem.get_questions(gender="M")  # Exclut Q20

# Exemple de réponses (0=Absent, 1=Tolérable, 2=Pénible)
answers = {
    "q1": 0, "q2": 1, "q3": 2, "q4": 0, "q5": 1,
    "q6": 0, "q7": 0, "q8": 1, "q9": 0, "q10": 0,
    "q11": 1, "q12": 0, "q13": 0, "q14": 1, "q15": 0,
    "q16": 0, "q17": 0, "q18": 0, "q19": 1, "q20": 2,  # Règles irrégulières pénible
    "q21": 1, "q22": 0, "q23": 1, "q24": 0, "q25": 0,  # Pas de troubles érection
    "q26": 1, "q27": 1, "q28": 0, "q29": 1, "q30": 2,
    "q31": 1, "q32": 1
}

# Valider les réponses (avec sexe)
validation = prisem.validate_answers(answers, gender="F")
if validation.valid:
    # Calculer le score
    result = prisem.calculate_score(answers, gender="F")
    print(f"Score total: {result.total_score}/62")
    print(f"Sexe utilisé: {result.gender_used}")
    print(f"Item exclu: {result.excluded_item}")
    print(f"Interprétation: {result.interpretation}")
else:
    print(f"Erreurs: {validation.errors}")
```

## Exemple de scoring

### Exemple 1 : Patiente avec effets modérés

```python
answers_femme = {
    f"q{i}": 0 for i in range(1, 33)  # Tous absents par défaut
}
# Quelques effets présents
answers_femme.update({
    "q3": 1,   # Bouche sèche tolérable
    "q8": 1,   # Transpiration tolérable
    "q11": 1,  # Mal de tête tolérable
    "q20": 2,  # Règles irrégulières pénibles
    "q21": 1,  # Difficultés d'endormissement tolérables
    "q23": 1,  # Perte désir sexuel tolérable
    "q26": 1,  # Anxiété tolérable
    "q30": 2,  # Fatigue pénible
})

result = prisem.calculate_score(answers_femme, gender="F")
# Score total: 10/62 (bas à modéré)
# Items exclus: q25 (troubles érection - homme)
```

### Exemple 2 : Patient avec charge élevée

```python
answers_homme = {
    f"q{i}": 1 for i in range(1, 33)  # Tous tolérables
}
# Certains effets pénibles
answers_homme.update({
    "q3": 2,   # Bouche sèche pénible
    "q5": 2,   # Palpitations pénibles
    "q8": 2,   # Transpiration pénible
    "q11": 2,  # Mal de tête pénible
    "q20": 0,  # Règles (non applicable)
    "q21": 2,  # Insomnie pénible
    "q23": 2,  # Perte désir pénible
    "q25": 2,  # Troubles érection pénibles
    "q30": 2,  # Fatigue pénible
    "q32": 2,  # Prise de poids pénible
})

result = prisem.calculate_score(answers_homme, gender="M")
# Score total: ≈39/62 (élevé)
# Items exclus: q20 (règles - femme)
# Interprétation: Révision du traitement recommandée
```

### Exemple 3 : Sexe non fourni, inférence automatique

```python
answers_inference = {f"q{i}": 0 for i in range(1, 33)}
answers_inference["q20"] = 2  # Règles irrégulières pénibles
answers_inference["q25"] = 0  # Pas de troubles érection

result = prisem.calculate_score(answers_inference)  # Pas de gender fourni
# gender_used: "F" (inféré car q20 renseigné)
# excluded_item: "q25"
# warning: "Sexe non fourni: exclusion de q25 (homme) car q20 (femme) est renseigné."
```

## Scores par section

Le PRISE-M permet également d'identifier les catégories d'effets indésirables les plus problématiques :

```python
result = prisem.calculate_score(answers, gender="F")

# Afficher les scores par section
for sec_id, score in result.section_scores.items():
    section = next(s for s in prisem.get_sections() if s['id'] == sec_id)
    print(f"{section['label']}: {score}")

# Exemple de sortie:
# 1. Troubles gastro-intestinaux: 3
# 2. Troubles cardiaques: 1
# 3. Problèmes cutanés: 1
# 4. Troubles neurologiques: 2
# 5. Vision/Audition: 0
# 6. Troubles uro-génital: 3  # Inclut règles irrégulières
# 7. Problèmes de sommeil: 1
# 8. Fonctions sexuelles: 2
# 9. Autres troubles: 5
```

## Considérations cliniques

### Usage approprié

Le PRISE-M évalue les **effets indésirables perçus comme liés au traitement médicamenteux en cours**. Il est important de :

1. **Instruction au patient** : Ne coter que les symptômes perçus comme effets secondaires
2. **Contexte temporel** : Semaine écoulée (peut refléter des variations récentes)
3. **Subjectivité** : L'échelle est auto-rapportée et subjective

### Interprétation

- **Score total** : Indicateur global de la charge d'effets indésirables
- **Scores par section** : Identification des domaines problématiques
- **Items à "2" (Pénible)** : Cibles prioritaires pour intervention

### Actions cliniques selon le score

**Score 0-14 (Bas)** :
- Surveillance continue
- Rappel de l'importance de l'observance

**Score 15-24 (Modéré)** :
- Évaluation des items "Pénibles"
- Mesures symptomatiques ciblées
- Suivi rapproché

**Score 25-39 (Élevé)** :
- Révision du traitement nécessaire
- Considérer :
  - Ajustement posologique
  - Changement de molécule
  - Traitements adjuvants pour effets spécifiques

**Score ≥40 (Très élevé)** :
- **Intervention urgente**
- Réévaluation complète du plan thérapeutique
- Balance bénéfice/risque à reconsidérer

### Effets spécifiques préoccupants

Certains effets indésirables justifient une attention particulière même avec un score total modéré :

- **Troubles cardiaques** (palpitations, douleurs thoraciques) → Évaluation cardiologique
- **Troubles sexuels sévères** → Impact sur qualité de vie et observance
- **Prise de poids importante** → Risque métabolique
- **Insomnie sévère** → Impact sur état thymique

## Références

- **PRISE-M.pdf** - Formulaire français original
- **PRISE-M_CotationScore.docx** - Consignes et cotation

## Notes cliniques

### Avantages du PRISE-M

1. **Rapide** : 5-10 minutes d'administration
2. **Complet** : 9 domaines d'effets indésirables couverts
3. **Sensible** : Échelle à 3 niveaux capture l'intensité
4. **Spécifique** : Items adaptés selon le sexe
5. **Actionnable** : Identifie les cibles d'intervention

### Limites

- **Auto-rapporté** : Subjectivité individuelle
- **Attribution causale** : Patient doit percevoir le lien avec le traitement
- **Snapshot** : Ne capture qu'une semaine
- **Pas de validation extensive** publiée

### Utilisation recommandée

- **Baseline** : Avant initiation d'un traitement
- **Suivi régulier** : Mensuel ou trimestriel
- **Post-changement** : Après modification thérapeutique
- **Plainte du patient** : Investigation ciblée

### Compléments utiles

Le PRISE-M peut être utilisé conjointement avec :
- **Échelles d'observance** (ex: MARS) pour évaluer l'impact sur l'adhérence
- **Échelles de qualité de vie** pour contexte global
- **Bilans biologiques** pour objectiver certains effets (poids, métabolisme)

## Propriétés psychométriques

- **Validité de contenu** : Items couvrent les effets indésirables courants des psychotropes
- **Sensibilité** : Détecte les changements suite à modifications thérapeutiques
- **Utilité clinique** : Guide les décisions thérapeutiques

## Exemple d'intégration dans le suivi

```python
def monitor_side_effects(patient_id, sessions):
    """Suivi longitudinal des effets indésirables"""
    
    results = []
    for date, answers, gender in sessions:
        result = prisem.calculate_score(answers, gender=gender)
        results.append({
            "date": date,
            "total": result.total_score,
            "severe_items": sum(1 for a in answers.values() if a == 2),
            "problematic_sections": [
                sec_id for sec_id, score in result.section_scores.items()
                if score >= 4  # Seuil arbitraire
            ]
        })
    
    return results

# Exemple d'utilisation
tracking = monitor_side_effects("patient_001", [
    ("2024-01-01", baseline_answers, "F"),
    ("2024-02-01", followup_1_answers, "F"),
    ("2024-03-01", followup_2_answers, "F"),
])

for entry in tracking:
    print(f"{entry['date']}: Score={entry['total']}, Items sévères={entry['severe_items']}")
```

