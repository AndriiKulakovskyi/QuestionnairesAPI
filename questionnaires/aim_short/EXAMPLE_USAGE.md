# AIM-short - Exemples d'utilisation

Ce document présente des exemples complets d'utilisation du questionnaire AIM-short dans différents contextes cliniques.

## Table des matières

1. [Utilisation de base](#utilisation-de-base)
2. [Scénarios cliniques](#scénarios-cliniques)
3. [Validation et gestion des erreurs](#validation-et-gestion-des-erreurs)
4. [Dépistage et évaluation](#dépistage-et-évaluation)
5. [Intégration système](#intégration-système)

---

## Utilisation de base

### Exemple simple

```python
from questionnaires.aim_short import AIMShort

# Initialiser le questionnaire
aim = AIMShort()

# Définir les réponses du patient
# 1=Jamais, 2=Presque jamais, 3=Occasionnellement
# 4=Habituellement, 5=Presque toujours, 6=Toujours
answers = {
    "q1": 4,   # Exubérance forte - habituellement
    "q2": 3,   # Paradis - occasionnellement
    "q3": 4,   # Extase - habituellement
    "q4": 3,   # Films tristes touchent - occasionnellement
    "q5": 3,   # Content plutôt qu'excité - occasionnellement (INVERSÉ)
    "q6": 3,   # Voix tremblante - occasionnellement
    "q7": 3,   # Osciller humeurs - occasionnellement
    "q8": 4,   # Éclater de joie - habituellement
    "q9": 4,   # Plein d'énergie - habituellement
    "q10": 3,  # Satisfaction calme - occasionnellement (INVERSÉ)
    "q11": 3,  # Culpabilité forte - occasionnellement
    "q12": 4,  # Sommet du monde - habituellement
    "q13": 3,  # Détendu plutôt qu'excité - occasionnellement (INVERSÉ)
    "q14": 3,  # Anxiété forte - occasionnellement
    "q15": 3,  # Bonheur calme - occasionnellement (INVERSÉ)
    "q16": 4,  # Déborder d'énergie - habituellement
    "q17": 3,  # Culpabilité forte - occasionnellement
    "q18": 3,  # Satisfaction plutôt que joie - occasionnellement (INVERSÉ)
    "q19": 2,  # Trembler - presque jamais
    "q20": 3   # Calme plutôt qu'excitation - occasionnellement (INVERSÉ)
}

# Calculer le score
result = aim.calculate_score(answers)

# Afficher les résultats
print("=== Résultats AIM-short ===")
print(f"Score moyen: {result['mean_score']}/6.00")
print(f"Score somme: {result['sum_score']}/120")
print(f"Catégorie: {result['category']}")
print(f"Sévérité: {result['severity']}")
print(f"\nInterprétation:")
print(result['interpretation'])
```

**Sortie attendue:**
```
=== Résultats AIM-short ===
Score moyen: 3.55/6.00
Score somme: 71/120
Catégorie: Occasionnellement intense
Sévérité: moderate

Interprétation:
Score moyen de 3.55/6.00 indique une intensité émotionnelle 
« Occasionnellement intense ». Le patient rapporte une intensité 
émotionnelle dans la moyenne. Les émotions sont vécues de manière 
habituelle, avec une réactivité émotionnelle typique.
```

### Accès aux métadonnées

```python
from questionnaires.aim_short import AIMShort

aim = AIMShort()

# Informations générales
metadata = aim.get_metadata()
print(f"Questionnaire: {metadata['name']}")
print(f"Abréviation: {metadata['abbreviation']}")
print(f"Nombre d'items: {metadata['num_items']}")
print(f"Type de score: {metadata['score_type']}")
print(f"Plage de scores: {metadata['score_range']}")
print(f"Items inversés: {metadata['reverse_items']}")

# Liste des questions
questions = aim.get_questions()
print("\n=== Questions (5 premières) ===")
for q in questions[:5]:
    reverse_indicator = "🔄" if q['reverse_scored'] else "➡️"
    print(f"{reverse_indicator} {q['id']}: {q['text'][:60]}...")

# Sections
sections = aim.get_sections()
print(f"\n=== Sections ===")
for section in sections:
    print(f"{section['label']}")
    print(f"Description: {section['description']}")
    print(f"Nombre d'items: {len(section['question_ids'])}")
```

---

## Scénarios cliniques

### Scénario 1 : Patient avec faible intensité émotionnelle

```python
from questionnaires.aim_short import AIMShort

aim = AIMShort()

# Patient rapportant des émotions peu intenses
# (possible émoussement affectif ou tempérament stable)
low_intensity_answers = {}
for i in range(1, 21):
    if i in AIMShort.REVERSE_ITEMS:  # Items calmes (5,10,13,15,18,20)
        # Fort accord avec calme/satisfaction
        low_intensity_answers[f"q{i}"] = 5  # Presque toujours calme
    else:  # Items intenses
        # Faible accord avec intensité
        low_intensity_answers[f"q{i}"] = 2  # Presque jamais intense

result = aim.calculate_score(low_intensity_answers)

print("=== Patient à faible intensité émotionnelle ===")
print(f"Score moyen: {result['mean_score']:.2f}/6.00")
print(f"Catégorie: {result['category']}")
print(f"\nInterprétation clinique:")
print(result['interpretation'])

if result['mean_score'] < 2.5:
    print("\n⚠️ ALERTE CLINIQUE")
    print("- Considérer émoussement affectif")
    print("- Évaluer pour dépression (MADRS, BDI)")
    print("- Vérifier alexithymie (TAS-20)")
    print("- Exclure détachement émotionnel")
```

### Scénario 2 : Patient avec très haute intensité émotionnelle

```python
from questionnaires.aim_short import AIMShort

aim = AIMShort()

# Patient rapportant des émotions très intenses
# (possible vulnérabilité bipolaire)
high_intensity_answers = {}
for i in range(1, 21):
    if i in AIMShort.REVERSE_ITEMS:  # Items calmes
        # Faible accord avec calme
        high_intensity_answers[f"q{i}"] = 2  # Presque jamais calme
    else:  # Items intenses
        # Fort accord avec intensité
        high_intensity_answers[f"q{i}"] = 5  # Presque toujours intense

result = aim.calculate_score(high_intensity_answers)

print("=== Patient à très haute intensité émotionnelle ===")
print(f"Score moyen: {result['mean_score']:.2f}/6.00")
print(f"Catégorie: {result['category']}")
print(f"Sévérité: {result['severity']}")

if result['mean_score'] >= 5.0:
    print("\n🚨 ALERTE CLINIQUE MAJEURE")
    print("Score suggérant une vulnérabilité aux troubles bipolaires")
    print("\nÉvaluations recommandées:")
    print("□ MDQ (Mood Disorder Questionnaire)")
    print("□ HCL-32 (Hypomania Checklist)")
    print("□ Entretien diagnostique structuré")
    print("□ Antécédents familiaux de troubles bipolaires")
    print("□ Épisodes d'élévation thymique passés")
    
    print("\nPoints de vigilance:")
    print("- Tempérament cyclothymique ou hyperthymique")
    print("- Risque de virage maniaque sous antidépresseurs")
    print("- Surveillance étroite si traitement initié")
```

### Scénario 3 : Dépistage bipolaire en consultation

```python
from questionnaires.aim_short import AIMShort

aim = AIMShort()

# Patient consultant pour dépression
# Évaluation de l'intensité émotionnelle pour dépistage bipolaire
consultation_answers = {
    "q1": 5,   # Exubérance forte - presque toujours
    "q2": 4,   # Paradis - habituellement
    "q3": 5,   # Extase - presque toujours
    "q4": 4,   # Films touchent - habituellement
    "q5": 2,   # Content vs excité - presque jamais (inversé → 5)
    "q6": 4,   # Voix tremblante - habituellement
    "q7": 5,   # Osciller - presque toujours
    "q8": 5,   # Éclater de joie - presque toujours
    "q9": 5,   # Plein énergie - presque toujours
    "q10": 2,  # Satisfaction calme - presque jamais (inversé → 5)
    "q11": 4,  # Culpabilité forte - habituellement
    "q12": 5,  # Sommet monde - presque toujours
    "q13": 2,  # Détendu vs excité - presque jamais (inversé → 5)
    "q14": 4,  # Anxiété forte - habituellement
    "q15": 2,  # Bonheur calme - presque jamais (inversé → 5)
    "q16": 5,  # Déborder énergie - presque toujours
    "q17": 4,  # Culpabilité - habituellement
    "q18": 2,  # Satisfaction vs joie - presque jamais (inversé → 5)
    "q19": 4,  # Trembler - habituellement
    "q20": 2   # Calme vs excitation - presque jamais (inversé → 5)
}

result = aim.calculate_score(consultation_answers)

print("=== DÉPISTAGE BIPOLAIRE ===")
print(f"Patient: Martin, Jean (35 ans)")
print(f"Motif: Épisode dépressif caractérisé")
print(f"\nScore AIM-short: {result['mean_score']:.2f}/6.00")
print(f"Catégorie: {result['category']}")

# Analyse des items spécifiques
print("\n=== ANALYSE DÉTAILLÉE ===")
high_items = []
for item_id, scores in result['item_scores'].items():
    if scores['scored'] >= 5:
        item_num = int(item_id[1:])
        question = aim.get_questions()[item_num - 1]
        high_items.append({
            'id': item_id,
            'text': question['text'],
            'score': scores['scored']
        })

if high_items:
    print(f"Items avec scores très élevés ({len(high_items)} items):")
    for item in high_items[:5]:  # Top 5
        print(f"  • {item['id']}: Score {item['score']}/6")
        print(f"    {item['text'][:70]}...")

# Décision clinique
print("\n=== DÉCISION CLINIQUE ===")
if result['mean_score'] >= 5.0:
    print("✓ Score très élevé suggérant vulnérabilité bipolaire")
    print("\nDIAGNOSTIC DIFFÉRENTIEL:")
    print("  • Trouble bipolaire de type II (à explorer)")
    print("  • vs. Dépression unipolaire")
    print("\nCONDUITE À TENIR:")
    print("  1. Évaluation MDQ et HCL-32")
    print("  2. Recherche d'hypomanies passées")
    print("  3. Antécédents familiaux")
    print("  4. PRUDENCE avec antidépresseurs seuls")
    print("  5. Envisager thymorégulateur si bipolaire confirmé")
elif result['mean_score'] >= 4.0:
    print("⚠️ Score modérément élevé - surveillance recommandée")
    print("  → Évaluer MDQ")
    print("  → Surveiller virage thymique si antidépresseur")
else:
    print("Score dans la norme - moins évocateur de bipolarité")
```

### Scénario 4 : Évaluation du tempérament affectif

```python
from questionnaires.aim_short import AIMShort

aim = AIMShort()

def classify_temperament(mean_score):
    """Classifier le tempérament basé sur AIM score."""
    if mean_score < 2.5:
        return {
            'type': 'Dysthymique',
            'caractéristiques': [
                'Émotions peu intenses',
                'Tendance à la stabilité émotionnelle',
                'Faible réactivité aux événements'
            ]
        }
    elif mean_score < 3.5:
        return {
            'type': 'Euthymique stable',
            'caractéristiques': [
                'Intensité émotionnelle modérée',
                'Bonne régulation émotionnelle',
                'Réactivité dans la norme'
            ]
        }
    elif mean_score < 4.5:
        return {
            'type': 'Hyperthymique léger',
            'caractéristiques': [
                'Émotions assez intenses',
                'Bonne énergie habituelle',
                'Réactivité émotionnelle accrue'
            ]
        }
    else:
        return {
            'type': 'Cyclothymique',
            'caractéristiques': [
                'Émotions très intenses',
                'Grande réactivité émotionnelle',
                'Oscillations thymiques fréquentes',
                'Vulnérabilité bipolaire'
            ]
        }

# Exemple d'évaluation
patient_answers = {f"q{i}": 4 for i in range(1, 21)}
result = aim.calculate_score(patient_answers)

temperament = classify_temperament(result['mean_score'])

print("=== ÉVALUATION DU TEMPÉRAMENT ===")
print(f"Score AIM: {result['mean_score']:.2f}/6.00")
print(f"\nTempérament: {temperament['type']}")
print("\nCaractéristiques:")
for carac in temperament['caractéristiques']:
    print(f"  • {carac}")

# Implications cliniques
print("\n=== IMPLICATIONS CLINIQUES ===")
if result['mean_score'] >= 4.5:
    print("• Risque élevé de trouble bipolaire")
    print("• Attention aux antidépresseurs (risque virage)")
    print("• Envisager thymorégulateurs si traitement nécessaire")
    print("• Psychoéducation sur régulation émotionnelle")
elif result['mean_score'] < 2.5:
    print("• Possible émoussement affectif")
    print("• Évaluer dépression chronique")
    print("• Considérer interventions activantes")
else:
    print("• Tempérament dans la norme")
    print("• Pas de précautions particulières")
```

---

## Validation et gestion des erreurs

### Validation complète avant calcul

```python
from questionnaires.aim_short import AIMShort, AIMShortError

aim = AIMShort()

# Réponses avec possibles problèmes
answers = {
    "q1": 3,
    "q2": 4,
    # ... autres items
}

# Validation explicite
validation = aim.validate_answers(answers)

print("=== VALIDATION ===")
print(f"Valide: {validation['valid']}")

if not validation['valid']:
    print("\n❌ ERREURS DÉTECTÉES:")
    for i, error in enumerate(validation['errors'], 1):
        print(f"  {i}. {error}")

if validation['warnings']:
    print("\n⚠️ AVERTISSEMENTS:")
    for i, warning in enumerate(validation['warnings'], 1):
        print(f"  {i}. {warning}")

# Calcul seulement si valide
if validation['valid']:
    try:
        result = aim.calculate_score(answers)
        print(f"\n✓ Score calculé: {result['mean_score']:.2f}/6.00")
    except AIMShortError as e:
        print(f"\n❌ Erreur lors du calcul: {e}")
else:
    print("\n❌ Impossible de calculer le score - corriger les erreurs")
```

### Gestion robuste des erreurs

```python
from questionnaires.aim_short import AIMShort, AIMShortError

def process_aim_safely(answers_dict, patient_id=None):
    """
    Traite un questionnaire AIM-short avec gestion d'erreurs complète.
    
    Args:
        answers_dict: Dictionnaire des réponses
        patient_id: Identifiant patient (optionnel)
    
    Returns:
        Dictionnaire avec success, result/errors, warnings
    """
    aim = AIMShort()
    
    try:
        # Validation d'abord
        validation = aim.validate_answers(answers_dict)
        
        if not validation['valid']:
            return {
                'success': False,
                'patient_id': patient_id,
                'errors': validation['errors'],
                'warnings': validation['warnings']
            }
        
        # Calcul du score
        result = aim.calculate_score(answers_dict)
        
        # Ajout de flags cliniques
        clinical_flags = []
        if result['mean_score'] >= 5.0:
            clinical_flags.append('RISQUE_BIPOLAIRE')
        if result['mean_score'] < 2.5:
            clinical_flags.append('EMOUSSEMENT_AFFECTIF')
        
        return {
            'success': True,
            'patient_id': patient_id,
            'result': result,
            'warnings': validation['warnings'],
            'clinical_flags': clinical_flags
        }
        
    except AIMShortError as e:
        return {
            'success': False,
            'patient_id': patient_id,
            'errors': [f"Erreur AIM-short: {str(e)}"],
            'warnings': []
        }
    except Exception as e:
        return {
            'success': False,
            'patient_id': patient_id,
            'errors': [f"Erreur inattendue: {str(e)}"],
            'warnings': []
        }

# Utilisation
test_answers = {f"q{i}": 5 for i in range(1, 21)}
outcome = process_aim_safely(test_answers, patient_id="P12345")

if outcome['success']:
    print(f"✓ Score calculé: {outcome['result']['mean_score']:.2f}")
    if outcome['clinical_flags']:
        print(f"🚨 Flags cliniques: {', '.join(outcome['clinical_flags'])}")
else:
    print("✗ Échec du traitement:")
    for error in outcome['errors']:
        print(f"  • {error}")
```

### Validation de types de données

```python
from questionnaires.aim_short import AIMShort

aim = AIMShort()

# Test avec différents types de données incorrects
test_cases = [
    ({"q1": "3"}, "String au lieu d'int"),
    ({"q1": 3.5}, "Float au lieu d'int"),
    ({"q1": 0}, "Valeur hors limites (trop bas)"),
    ({"q1": 7}, "Valeur hors limites (trop haut)"),
    ({"q1": None}, "Valeur None"),
]

print("=== TESTS DE VALIDATION ===\n")

for test_data, description in test_cases:
    # Compléter avec valeurs valides
    full_data = {f"q{i}": 3 for i in range(1, 21)}
    full_data.update(test_data)
    
    validation = aim.validate_answers(full_data)
    
    print(f"Test: {description}")
    print(f"  Valide: {validation['valid']}")
    if not validation['valid']:
        print(f"  Erreur: {validation['errors'][0]}")
    print()
```

---

## Dépistage et évaluation

### Protocole de dépistage bipolaire

```python
from questionnaires.aim_short import AIMShort

def bipolar_screening_protocol(aim_answers, mdq_positive=None, history=None):
    """
    Protocole complet de dépistage bipolaire avec AIM-short.
    
    Args:
        aim_answers: Réponses AIM
        mdq_positive: Résultat MDQ (optionnel)
        history: Antécédents cliniques (optionnel)
    
    Returns:
        Rapport de dépistage avec recommandations
    """
    aim = AIMShort()
    result = aim.calculate_score(aim_answers)
    
    report = {
        'aim_score': result['mean_score'],
        'aim_category': result['category'],
        'risk_level': 'low',
        'recommendations': []
    }
    
    # Évaluation du risque basée sur AIM
    if result['mean_score'] >= 5.0:
        report['risk_level'] = 'high'
        report['recommendations'].extend([
            'Évaluation psychiatrique spécialisée URGENTE',
            'Passation MDQ et HCL-32',
            'Recherche systématique d\'hypomanies passées',
            'Antécédents familiaux de troubles bipolaires'
        ])
    elif result['mean_score'] >= 4.5:
        report['risk_level'] = 'moderate'
        report['recommendations'].extend([
            'Évaluation psychiatrique recommandée',
            'Passation MDQ',
            'Surveillance si traitement antidépresseur'
        ])
    elif result['mean_score'] >= 4.0:
        report['risk_level'] = 'mild'
        report['recommendations'].extend([
            'Surveillance clinique',
            'Attention aux antécédents personnels/familiaux'
        ])
    
    # Intégration avec MDQ si disponible
    if mdq_positive is not None:
        report['mdq_positive'] = mdq_positive
        if mdq_positive and result['mean_score'] >= 4.5:
            report['risk_level'] = 'very_high'
            report['recommendations'].insert(0,
                '🚨 FORT RISQUE BIPOLAIRE - Consultation psychiatrique IMMÉDIATE'
            )
    
    # Intégration avec histoire clinique
    if history:
        if history.get('family_bipolar') and result['mean_score'] >= 4.0:
            report['risk_level'] = 'high' if report['risk_level'] == 'moderate' else report['risk_level']
            report['recommendations'].append(
                'Antécédents familiaux + AIM élevé = risque accru'
            )
    
    return report

# Exemple d'utilisation
patient_answers = {f"q{i}": 5 for i in range(1, 21)}
history = {'family_bipolar': True, 'hypomanic_episodes': 'uncertain'}

screening = bipolar_screening_protocol(
    aim_answers=patient_answers,
    mdq_positive=True,
    history=history
)

print("=== RAPPORT DE DÉPISTAGE BIPOLAIRE ===")
print(f"Score AIM: {screening['aim_score']:.2f}/6.00")
print(f"Catégorie: {screening['aim_category']}")
print(f"Niveau de risque: {screening['risk_level'].upper()}")
if 'mdq_positive' in screening:
    print(f"MDQ positif: {'Oui' if screening['mdq_positive'] else 'Non'}")

print("\n=== RECOMMANDATIONS ===")
for i, rec in enumerate(screening['recommendations'], 1):
    print(f"{i}. {rec}")
```

### Suivi longitudinal

```python
from questionnaires.aim_short import AIMShort
from datetime import datetime, timedelta

aim = AIMShort()

# Simulation d'un suivi sur 12 mois
timeline = [
    {
        'month': 0,
        'date': datetime(2025, 1, 1),
        'answers': {f"q{i}": 5 for i in range(1, 21)},
        'clinical_note': 'Baseline - consultation initiale'
    },
    {
        'month': 3,
        'date': datetime(2025, 4, 1),
        'answers': {f"q{i}": 4 for i in range(1, 21)},
        'clinical_note': 'Après 3 mois de thérapie'
    },
    {
        'month': 6,
        'date': datetime(2025, 7, 1),
        'answers': {f"q{i}": 4 for i in range(1, 21)},
        'clinical_note': '6 mois - stabilisation'
    },
    {
        'month': 12,
        'date': datetime(2026, 1, 1),
        'answers': {f"q{i}": 3 for i in range(1, 21)},
        'clinical_note': '12 mois - amélioration maintenue'
    }
]

# Calcul et analyse
print("=== SUIVI LONGITUDINAL AIM-SHORT ===")
print("Patient: Durand, Marie (28 ans)")
print("Diagnostic: Tempérament cyclothymique\n")

results_history = []
for assessment in timeline:
    result = aim.calculate_score(assessment['answers'])
    results_history.append({
        'month': assessment['month'],
        'date': assessment['date'],
        'score': result['mean_score'],
        'category': result['category'],
        'note': assessment['clinical_note']
    })

# Affichage du tableau
print("Mois | Date       | Score | Catégorie              | Évolution")
print("-----|------------|-------|------------------------|----------")
for i, res in enumerate(results_history):
    evolution = ""
    if i > 0:
        diff = res['score'] - results_history[i-1]['score']
        if diff < -0.3:
            evolution = f"↓ {abs(diff):.2f}"
        elif diff > 0.3:
            evolution = f"↑ {diff:.2f}"
        else:
            evolution = "→ stable"
    
    print(f"{res['month']:^5}| {res['date'].strftime('%d/%m/%Y')} | "
          f"{res['score']:^5.2f} | {res['category']:<22} | {evolution}")
    print(f"     | Note: {res['note']}")
    print("-----|------------|-------|------------------------|----------")

# Analyse de stabilité
scores = [r['score'] for r in results_history]
mean_score = sum(scores) / len(scores)
variance = sum((s - mean_score)**2 for s in scores) / len(scores)
std_dev = variance ** 0.5

print(f"\n=== ANALYSE DE STABILITÉ ===")
print(f"Score moyen sur 12 mois: {mean_score:.2f}")
print(f"Écart-type: {std_dev:.2f}")

if std_dev < 0.5:
    print("✓ Trait stable (écart-type < 0.5)")
    print("  → Conforme à un trait de personnalité")
elif std_dev < 1.0:
    print("⚠️ Variabilité modérée")
    print("  → Possibles variations d'état vs. trait")
else:
    print("❌ Forte variabilité")
    print("  → Possibles influences d'états thymiques")
    print("  → Vérifier consigne (exclure épisodes anormaux)")
```

---

## Intégration système

### API REST complète

```python
from flask import Flask, request, jsonify
from questionnaires.aim_short import AIMShort, AIMShortError
from datetime import datetime

app = Flask(__name__)
aim = AIMShort()

@app.route('/api/aim-short/metadata', methods=['GET'])
def get_metadata():
    """Endpoint pour obtenir les métadonnées."""
    metadata = aim.get_metadata()
    return jsonify(metadata), 200

@app.route('/api/aim-short/questions', methods=['GET'])
def get_questions():
    """Endpoint pour obtenir les questions."""
    questions = aim.get_questions()
    return jsonify({'questions': questions}), 200

@app.route('/api/aim-short/validate', methods=['POST'])
def validate_answers():
    """Endpoint pour valider les réponses."""
    try:
        data = request.get_json()
        answers = data.get('answers', {})
        
        validation = aim.validate_answers(answers)
        
        return jsonify({
            'valid': validation['valid'],
            'errors': validation['errors'],
            'warnings': validation['warnings']
        }), 200
        
    except Exception as e:
        return jsonify({
            'error': 'Erreur serveur',
            'details': str(e)
        }), 500

@app.route('/api/aim-short/calculate', methods=['POST'])
def calculate_score():
    """Endpoint pour calculer le score."""
    try:
        data = request.get_json()
        answers = data.get('answers', {})
        patient_id = data.get('patient_id')
        
        # Validation
        validation = aim.validate_answers(answers)
        if not validation['valid']:
            return jsonify({
                'success': False,
                'errors': validation['errors']
            }), 400
        
        # Calcul
        result = aim.calculate_score(answers)
        
        # Ajout de flags cliniques
        clinical_alerts = []
        if result['mean_score'] >= 5.0:
            clinical_alerts.append({
                'level': 'critical',
                'message': 'Score très élevé - Risque bipolaire - Évaluation urgente'
            })
        elif result['mean_score'] < 2.5:
            clinical_alerts.append({
                'level': 'warning',
                'message': 'Score très faible - Émoussement affectif possible'
            })
        
        return jsonify({
            'success': True,
            'patient_id': patient_id,
            'data': {
                'mean_score': result['mean_score'],
                'sum_score': result['sum_score'],
                'category': result['category'],
                'severity': result['severity'],
                'interpretation': result['interpretation'],
                'warnings': result['warnings'],
                'clinical_alerts': clinical_alerts
            },
            'timestamp': datetime.utcnow().isoformat() + 'Z'
        }), 200
        
    except AIMShortError as e:
        return jsonify({
            'success': False,
            'errors': [str(e)]
        }), 400
    except Exception as e:
        return jsonify({
            'success': False,
            'errors': ['Erreur serveur']
        }), 500

@app.route('/api/aim-short/schema', methods=['GET'])
def get_schema():
    """Endpoint pour obtenir le schéma complet."""
    schema = aim.get_schema()
    return jsonify(schema), 200

if __name__ == '__main__':
    app.run(debug=True)
```

### Export pour analyse statistique

```python
from questionnaires.aim_short import AIMShort
import pandas as pd
import numpy as np

def export_to_dataframe(assessments_list):
    """
    Convertit des évaluations AIM-short en DataFrame pandas.
    
    Args:
        assessments_list: Liste de dictionnaires d'évaluations
    
    Returns:
        DataFrame avec colonnes structurées
    """
    aim = AIMShort()
    
    records = []
    for assessment in assessments_list:
        # Calculer si nécessaire
        if 'result' not in assessment:
            result = aim.calculate_score(assessment['answers'])
        else:
            result = assessment['result']
        
        # Créer enregistrement plat
        record = {
            'patient_id': assessment.get('patient_id'),
            'assessment_date': assessment.get('date'),
            'mean_score': result['mean_score'],
            'sum_score': result['sum_score'],
            'category': result['category'],
            'severity': result['severity']
        }
        
        # Ajouter scores par item (brut et recodé)
        for item_id, scores in result['item_scores'].items():
            record[f'{item_id}_raw'] = scores['raw']
            record[f'{item_id}_scored'] = scores['scored']
            record[f'{item_id}_reversed'] = scores['reversed']
        
        records.append(record)
    
    return pd.DataFrame(records)

# Exemple d'utilisation
assessments = [
    {
        'patient_id': 'P001',
        'date': '2025-01-01',
        'answers': {f"q{i}": np.random.randint(1, 7) for i in range(1, 21)}
    },
    {
        'patient_id': 'P002',
        'date': '2025-01-02',
        'answers': {f"q{i}": np.random.randint(1, 7) for i in range(1, 21)}
    }
]

df = export_to_dataframe(assessments)
print(df[['patient_id', 'mean_score', 'category', 'severity']])

# Export vers fichiers
df.to_csv('aim_short_data.csv', index=False)
df.to_excel('aim_short_data.xlsx', index=False, sheet_name='AIM-Short')

# Statistiques descriptives
print("\n=== STATISTIQUES ===")
print(f"Nombre d'évaluations: {len(df)}")
print(f"Score moyen: {df['mean_score'].mean():.2f} (ET={df['mean_score'].std():.2f})")
print(f"Min: {df['mean_score'].min():.2f}, Max: {df['mean_score'].max():.2f}")
```

---

## Résumé

Ces exemples couvrent les principaux cas d'usage du questionnaire AIM-short :
- ✓ Utilisation de base et accès aux métadonnées
- ✓ Scénarios cliniques (faible/haute intensité, dépistage bipolaire)
- ✓ Validation et gestion robuste des erreurs
- ✓ Protocoles de dépistage et suivi longitudinal
- ✓ Intégration système (API, export données)

Pour plus d'informations, consultez :
- `README.md` - Documentation complète
- `QUICK_REFERENCE.md` - Guide de référence rapide
- `tests/test_aim_short.py` - Tests unitaires

