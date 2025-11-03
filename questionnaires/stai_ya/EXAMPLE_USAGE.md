# STAI-YA - Exemples d'utilisation

Ce document présente des exemples complets d'utilisation du questionnaire STAI-YA dans différents contextes cliniques.

## Table des matières

1. [Utilisation de base](#utilisation-de-base)
2. [Scénarios cliniques](#scénarios-cliniques)
3. [Validation et gestion des erreurs](#validation-et-gestion-des-erreurs)
4. [Comparaisons et suivi](#comparaisons-et-suivi)
5. [Intégration système](#intégration-système)

---

## Utilisation de base

### Exemple simple

```python
from questionnaires.stai_ya import STAIYA

# Initialiser le questionnaire
stai = STAIYA()

# Définir les réponses du patient
# 1=non, 2=plutôt non, 3=plutôt oui, 4=oui
answers = {
    "q1": 2,   # Je me sens calme - plutôt non
    "q2": 3,   # Je me sens en sécurité - plutôt oui
    "q3": 3,   # Je suis tendu(e) - plutôt oui
    "q4": 2,   # Je me sens surmené(e) - plutôt non
    "q5": 2,   # Je me sens tranquille - plutôt non
    "q6": 3,   # Je me sens ému(e) - plutôt oui
    "q7": 2,   # L'idée de malheurs me tracasse - plutôt non
    "q8": 3,   # Je me sens content(e) - plutôt oui
    "q9": 2,   # Je me sens effrayé(e) - plutôt non
    "q10": 3,  # Je me sens à mon aise - plutôt oui
    "q11": 3,  # J'ai confiance en moi - plutôt oui
    "q12": 2,  # Je me sens nerveux - plutôt non
    "q13": 2,  # J'ai peur - plutôt non
    "q14": 2,  # Je me sens indécis(e) - plutôt non
    "q15": 2,  # Je suis décontracté(e) - plutôt non
    "q16": 3,  # Je suis satisfait(e) - plutôt oui
    "q17": 2,  # Je suis inquiet - plutôt non
    "q18": 2,  # Je me sens déconcerté(e) - plutôt non
    "q19": 3,  # Je me sens solide - plutôt oui
    "q20": 3   # Je me sens de bonne humeur - plutôt oui
}

# Calculer le score
result = stai.calculate_score(answers)

# Afficher les résultats
print("=== Résultats STAI-YA ===")
print(f"Score total: {result['total_score']}/80")
print(f"Catégorie: {result['category']}")
print(f"Sévérité: {result['severity']}")
print(f"\nInterprétation:")
print(result['interpretation'])
```

**Sortie attendue:**
```
=== Résultats STAI-YA ===
Score total: 50/80
Catégorie: Anxiété état moyenne
Sévérité: average

Interprétation:
Score de 50/80 indique un niveau d'anxiété état moyen. 
Le patient rapporte un niveau d'anxiété dans la norme.
```

### Accès aux métadonnées

```python
from questionnaires.stai_ya import STAIYA

stai = STAIYA()

# Informations générales
metadata = stai.get_metadata()
print(f"Questionnaire: {metadata['name']}")
print(f"Nombre d'items: {metadata['num_items']}")
print(f"Plage de scores: {metadata['score_range']}")
print(f"Items inversés: {metadata['reverse_items']}")

# Liste des questions
questions = stai.get_questions()
print("\n=== Questions ===")
for q in questions[:3]:  # Afficher les 3 premières
    reverse_indicator = "📊" if q['reverse_scored'] else "📈"
    print(f"{reverse_indicator} {q['text']}")

# Sections
sections = stai.get_sections()
print(f"\n=== Sections ===")
for section in sections:
    print(f"{section['label']}: {len(section['question_ids'])} items")
```

---

## Scénarios cliniques

### Scénario 1 : Patient avec anxiété très faible

```python
from questionnaires.stai_ya import STAIYA

stai = STAIYA()

# Patient se sentant très calme et détendu
# Répond positivement aux items de calme, négativement aux items d'anxiété
calm_patient = {}
for i in range(1, 21):
    if i in STAIYA.REVERSE_ITEMS:  # Items positifs (calme, content, etc.)
        calm_patient[f"q{i}"] = 4  # "oui" - je suis calme
    else:  # Items négatifs (tendu, inquiet, etc.)
        calm_patient[f"q{i}"] = 1  # "non" - pas tendu

result = stai.calculate_score(calm_patient)

print("=== Patient calme ===")
print(f"Score: {result['total_score']}/80")
print(f"Catégorie: {result['category']}")
print(f"Action: Aucune intervention nécessaire")
```

### Scénario 2 : Patient avec anxiété très élevée

```python
from questionnaires.stai_ya import STAIYA

stai = STAIYA()

# Patient en détresse aiguë
# Répond négativement aux items de calme, positivement aux items d'anxiété
anxious_patient = {}
for i in range(1, 21):
    if i in STAIYA.REVERSE_ITEMS:  # Items positifs
        anxious_patient[f"q{i}"] = 1  # "non" - pas calme du tout
    else:  # Items négatifs
        anxious_patient[f"q{i}"] = 4  # "oui" - très tendu/inquiet

result = stai.calculate_score(anxious_patient)

print("=== Patient en détresse aiguë ===")
print(f"Score: {result['total_score']}/80")
print(f"Catégorie: {result['category']}")
print(f"⚠️ ALERTE: Intervention immédiate recommandée")

if result['severity'] == 'very_high':
    print("\nActions recommandées:")
    print("- Évaluation psychiatrique urgente")
    print("- Vérifier risque suicidaire")
    print("- Envisager intervention de crise")
```

### Scénario 3 : Anxiété pré-opératoire

```python
from questionnaires.stai_ya import STAIYA
from datetime import datetime

stai = STAIYA()

# Évaluation avant chirurgie
pre_op_answers = {
    "q1": 2, "q2": 2, "q3": 3, "q4": 3, "q5": 2,
    "q6": 3, "q7": 3, "q8": 2, "q9": 3, "q10": 2,
    "q11": 3, "q12": 3, "q13": 2, "q14": 3, "q15": 2,
    "q16": 2, "q17": 3, "q18": 2, "q19": 3, "q20": 2
}

result = stai.calculate_score(pre_op_answers)

print("=== Évaluation pré-opératoire ===")
print(f"Patient: Jean Dupont")
print(f"Date: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
print(f"Intervention prévue: Chirurgie cardiaque")
print(f"\nScore STAI-YA: {result['total_score']}/80")
print(f"Niveau d'anxiété: {result['category']}")

# Décision clinique basée sur le score
if result['total_score'] >= 56:
    print("\n⚠️ Anxiété pré-opératoire élevée détectée")
    print("Recommandations:")
    print("- Consultation avec psychologue")
    print("- Envisager prémédication anxiolytique")
    print("- Renforcer information et support")
elif result['total_score'] >= 46:
    print("\nAnxiété pré-opératoire modérée")
    print("Recommandations:")
    print("- Renforcer information patient")
    print("- Techniques de relaxation")
else:
    print("\nAnxiété pré-opératoire dans les limites normales")
    print("Procédure standard applicable")
```

### Scénario 4 : Évaluation en urgence psychiatrique

```python
from questionnaires.stai_ya import STAIYA

stai = STAIYA()

# Patient présentant aux urgences
emergency_answers = {
    "q1": 1, "q2": 1, "q3": 4, "q4": 3, "q5": 1,
    "q6": 4, "q7": 4, "q8": 1, "q9": 4, "q10": 1,
    "q11": 2, "q12": 4, "q13": 3, "q14": 3, "q15": 1,
    "q16": 1, "q17": 4, "q18": 3, "q19": 2, "q20": 1
}

result = stai.calculate_score(emergency_answers)

print("=== ÉVALUATION URGENCE PSYCHIATRIQUE ===")
print(f"Score STAI-YA: {result['total_score']}/80")
print(f"Sévérité: {result['severity'].upper()}")

# Protocole d'urgence
if result['severity'] in ['high', 'very_high']:
    print("\n🚨 PROTOCOLE ANXIÉTÉ AIGUË ACTIVÉ")
    print("\nÉvaluations immédiates requises:")
    print("□ Risque suicidaire (échelle Columbia)")
    print("□ Risque auto/hétéro-agressif")
    print("□ Capacité de jugement")
    print("□ Symptômes psychotiques associés")
    print("□ Consommation substances")
    
    print("\nInterventions immédiates:")
    print("□ Sécurisation environnement")
    print("□ Présence continue si nécessaire")
    print("□ Consultation psychiatrique urgente")
    print("□ Envisager médication anxiolytique")
    print("□ Contacter personne de confiance")

# Détails par item pour analyse clinique
print("\n=== Analyse détaillée ===")
high_anxiety_items = []
for item_id, scores in result['item_scores'].items():
    if scores['scored'] >= 3:  # Score élevé après recodage
        question = next(q for q in stai.get_questions() if q['id'] == item_id)
        high_anxiety_items.append({
            'item': item_id,
            'text': question['text'],
            'score': scores['scored']
        })

if high_anxiety_items:
    print("Items avec scores élevés:")
    for item in high_anxiety_items:
        print(f"  {item['item']}: {item['text']} (score: {item['score']})")
```

---

## Validation et gestion des erreurs

### Validation avant calcul

```python
from questionnaires.stai_ya import STAIYA, STAIYAError

stai = STAIYA()

# Réponses avec erreurs potentielles
answers = {
    "q1": 2,
    "q2": 3,
    # ... (items q3-q19 manquants)
    "q20": 2
}

# Validation explicite
validation = stai.validate_answers(answers)

print("=== Validation ===")
print(f"Valide: {validation['valid']}")

if not validation['valid']:
    print("\nErreurs détectées:")
    for error in validation['errors']:
        print(f"  ❌ {error}")

if validation['warnings']:
    print("\nAvertissements:")
    for warning in validation['warnings']:
        print(f"  ⚠️  {warning}")

# Tentative de calcul sans validation préalable
try:
    result = stai.calculate_score(answers)
except STAIYAError as e:
    print(f"\n❌ Erreur lors du calcul: {e}")
```

### Gestion robuste des erreurs

```python
from questionnaires.stai_ya import STAIYA, STAIYAError

def process_stai_safely(answers_dict):
    """Traite un questionnaire STAI-YA avec gestion d'erreurs complète."""
    stai = STAIYA()
    
    try:
        # Validation d'abord
        validation = stai.validate_answers(answers_dict)
        
        if not validation['valid']:
            return {
                'success': False,
                'errors': validation['errors'],
                'warnings': validation['warnings']
            }
        
        # Calcul du score
        result = stai.calculate_score(answers_dict)
        
        return {
            'success': True,
            'result': result,
            'warnings': validation['warnings']
        }
        
    except STAIYAError as e:
        return {
            'success': False,
            'errors': [f"Erreur STAI-YA: {str(e)}"],
            'warnings': []
        }
    except Exception as e:
        return {
            'success': False,
            'errors': [f"Erreur inattendue: {str(e)}"],
            'warnings': []
        }

# Utilisation
test_answers = {f"q{i}": 2 for i in range(1, 21)}
outcome = process_stai_safely(test_answers)

if outcome['success']:
    print(f"✓ Score calculé: {outcome['result']['total_score']}")
else:
    print("✗ Échec du traitement:")
    for error in outcome['errors']:
        print(f"  {error}")
```

### Validation de types de données

```python
from questionnaires.stai_ya import STAIYA

stai = STAIYA()

# Test avec différents types de données incorrects
test_cases = [
    {"q1": "2", "q2": 3},           # String au lieu d'int
    {"q1": 2.5, "q2": 3},           # Float au lieu d'int
    {"q1": 0, "q2": 3},             # Valeur hors limites
    {"q1": 5, "q2": 3},             # Valeur hors limites
    {"q1": None, "q2": 3},          # Valeur None
]

for i, test_data in enumerate(test_cases, 1):
    # Compléter avec valeurs valides
    full_data = {f"q{j}": 2 for j in range(1, 21)}
    full_data.update(test_data)
    
    validation = stai.validate_answers(full_data)
    print(f"\nTest {i}: {list(test_data.items())[0]}")
    print(f"Valide: {validation['valid']}")
    if not validation['valid']:
        print(f"Erreur: {validation['errors'][0]}")
```

---

## Comparaisons et suivi

### Suivi longitudinal

```python
from questionnaires.stai_ya import STAIYA
from datetime import datetime, timedelta

stai = STAIYA()

# Simulation d'un suivi thérapeutique sur 8 semaines
timeline = [
    # Semaine 0 - Baseline
    {
        'week': 0,
        'date': datetime(2025, 1, 1),
        'answers': {f"q{i}": 3 if i in [3,4,6,7,9,12,13,14,17,18] else 2
                   for i in range(1, 21)}
    },
    # Semaine 4 - Mi-traitement
    {
        'week': 4,
        'date': datetime(2025, 1, 29),
        'answers': {f"q{i}": 2 for i in range(1, 21)}
    },
    # Semaine 8 - Fin de traitement
    {
        'week': 8,
        'date': datetime(2025, 2, 26),
        'answers': {f"q{i}": 2 if i in [3,4,6,7,9,12,13,14,17,18] else 3
                   for i in range(1, 21)}
    }
]

# Calcul et comparaison
print("=== SUIVI THÉRAPEUTIQUE - STAI-YA ===")
print("Patient: Marie Martin")
print("Intervention: Thérapie cognitive-comportementale\n")

results_history = []
for assessment in timeline:
    result = stai.calculate_score(assessment['answers'])
    results_history.append({
        'week': assessment['week'],
        'date': assessment['date'],
        'score': result['total_score'],
        'category': result['category'],
        'severity': result['severity']
    })

# Affichage du tableau de suivi
print("Semaine | Date       | Score | Catégorie              | Évolution")
print("--------|------------|-------|------------------------|----------")
for i, res in enumerate(results_history):
    evolution = ""
    if i > 0:
        diff = res['score'] - results_history[i-1]['score']
        if diff < 0:
            evolution = f"↓ {abs(diff)} points"
        elif diff > 0:
            evolution = f"↑ {diff} points"
        else:
            evolution = "→ stable"
    
    print(f"{res['week']:^7} | {res['date'].strftime('%d/%m/%Y')} | "
          f"{res['score']:^5} | {res['category']:<22} | {evolution}")

# Analyse de l'évolution
baseline = results_history[0]['score']
final = results_history[-1]['score']
improvement = baseline - final
percent_change = (improvement / baseline) * 100

print(f"\n=== ANALYSE ===")
print(f"Score initial: {baseline}")
print(f"Score final: {final}")
print(f"Réduction: {improvement} points ({percent_change:.1f}%)")

if improvement >= 10:
    print("✓ Amélioration cliniquement significative")
elif improvement >= 5:
    print("→ Amélioration modérée")
elif improvement > 0:
    print("→ Amélioration légère")
else:
    print("✗ Pas d'amélioration ou détérioration")
```

### Comparaison pré-post intervention

```python
from questionnaires.stai_ya import STAIYA

stai = STAIYA()

# Avant intervention anxiolytique
pre_intervention = {
    "q1": 2, "q2": 2, "q3": 4, "q4": 3, "q5": 2,
    "q6": 3, "q7": 3, "q8": 2, "q9": 3, "q10": 2,
    "q11": 2, "q12": 4, "q13": 3, "q14": 3, "q15": 2,
    "q16": 2, "q17": 4, "q18": 3, "q19": 2, "q20": 2
}

# Après intervention (1 heure plus tard)
post_intervention = {
    "q1": 3, "q2": 3, "q3": 2, "q4": 2, "q5": 3,
    "q6": 2, "q7": 2, "q8": 3, "q9": 2, "q10": 3,
    "q11": 3, "q12": 2, "q13": 2, "q14": 2, "q15": 3,
    "q16": 3, "q17": 2, "q18": 2, "q19": 3, "q20": 3
}

pre_result = stai.calculate_score(pre_intervention)
post_result = stai.calculate_score(post_intervention)

print("=== ÉVALUATION PRÉ-POST INTERVENTION ===")
print("\nPRÉ-INTERVENTION:")
print(f"  Score: {pre_result['total_score']}/80")
print(f"  Catégorie: {pre_result['category']}")

print("\nPOST-INTERVENTION:")
print(f"  Score: {post_result['total_score']}/80")
print(f"  Catégorie: {post_result['category']}")

reduction = pre_result['total_score'] - post_result['total_score']
print(f"\nRÉDUCTION: {reduction} points")

# Analyse item par item
print("\n=== CHANGEMENTS PAR ITEM ===")
significant_changes = []
for i in range(1, 21):
    qid = f"q{i}"
    pre_scored = pre_result['item_scores'][qid]['scored']
    post_scored = post_result['item_scores'][qid]['scored']
    change = pre_scored - post_scored
    
    if abs(change) >= 2:  # Changement significatif
        question = next(q for q in stai.get_questions() if q['id'] == qid)
        significant_changes.append({
            'item': qid,
            'text': question['text'],
            'change': change
        })

if significant_changes:
    for change in significant_changes:
        direction = "↓" if change['change'] > 0 else "↑"
        print(f"{direction} {change['item']}: {change['text']}")
        print(f"   Changement: {change['change']} points")
```

---

## Intégration système

### Intégration dans une API REST

```python
from flask import Flask, request, jsonify
from questionnaires.stai_ya import STAIYA, STAIYAError

app = Flask(__name__)
stai = STAIYA()

@app.route('/api/stai-ya/calculate', methods=['POST'])
def calculate_stai_ya():
    """Endpoint pour calculer le score STAI-YA."""
    try:
        # Récupérer les données
        data = request.get_json()
        answers = data.get('answers', {})
        
        # Valider
        validation = stai.validate_answers(answers)
        if not validation['valid']:
            return jsonify({
                'success': False,
                'errors': validation['errors']
            }), 400
        
        # Calculer
        result = stai.calculate_score(answers)
        
        return jsonify({
            'success': True,
            'data': {
                'total_score': result['total_score'],
                'category': result['category'],
                'severity': result['severity'],
                'interpretation': result['interpretation'],
                'warnings': result['warnings']
            }
        }), 200
        
    except STAIYAError as e:
        return jsonify({
            'success': False,
            'errors': [str(e)]
        }), 400
    except Exception as e:
        return jsonify({
            'success': False,
            'errors': ['Erreur serveur']
        }), 500

@app.route('/api/stai-ya/schema', methods=['GET'])
def get_schema():
    """Endpoint pour obtenir le schéma du questionnaire."""
    schema = stai.get_schema()
    return jsonify(schema), 200

if __name__ == '__main__':
    app.run(debug=True)
```

### Sauvegarde en base de données

```python
from questionnaires.stai_ya import STAIYA
from datetime import datetime
import json

class STAIYARepository:
    """Gestion de la persistance des évaluations STAI-YA."""
    
    def __init__(self, db_connection):
        self.db = db_connection
        self.stai = STAIYA()
    
    def save_assessment(self, patient_id, answers, clinician_id=None):
        """Sauvegarde une évaluation complète."""
        # Calculer le score
        result = self.stai.calculate_score(answers)
        
        # Préparer les données
        assessment_data = {
            'patient_id': patient_id,
            'clinician_id': clinician_id,
            'assessment_date': datetime.utcnow(),
            'answers': json.dumps(answers),
            'total_score': result['total_score'],
            'category': result['category'],
            'severity': result['severity'],
            'interpretation': result['interpretation'],
            'warnings': json.dumps(result['warnings']),
            'item_scores': json.dumps(result['item_scores'])
        }
        
        # Insérer en base
        query = """
            INSERT INTO stai_ya_assessments 
            (patient_id, clinician_id, assessment_date, answers, 
             total_score, category, severity, interpretation, warnings, item_scores)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        
        cursor = self.db.execute(query, tuple(assessment_data.values()))
        self.db.commit()
        
        return cursor.lastrowid
    
    def get_patient_history(self, patient_id, limit=10):
        """Récupère l'historique des évaluations d'un patient."""
        query = """
            SELECT assessment_date, total_score, category, severity
            FROM stai_ya_assessments
            WHERE patient_id = ?
            ORDER BY assessment_date DESC
            LIMIT ?
        """
        
        cursor = self.db.execute(query, (patient_id, limit))
        return cursor.fetchall()
    
    def get_assessment_details(self, assessment_id):
        """Récupère les détails complets d'une évaluation."""
        query = """
            SELECT * FROM stai_ya_assessments
            WHERE id = ?
        """
        
        cursor = self.db.execute(query, (assessment_id,))
        row = cursor.fetchone()
        
        if row:
            return {
                'id': row[0],
                'patient_id': row[1],
                'assessment_date': row[3],
                'answers': json.loads(row[4]),
                'total_score': row[5],
                'category': row[6],
                'severity': row[7],
                'interpretation': row[8],
                'warnings': json.loads(row[9]),
                'item_scores': json.loads(row[10])
            }
        return None

# Exemple d'utilisation
# repo = STAIYARepository(db_connection)
# assessment_id = repo.save_assessment(
#     patient_id=12345,
#     answers={f"q{i}": 2 for i in range(1, 21)},
#     clinician_id=67890
# )
```

### Export pour analyse statistique

```python
from questionnaires.stai_ya import STAIYA
import pandas as pd
import json

def export_to_dataframe(assessments_list):
    """
    Convertit une liste d'évaluations STAI-YA en DataFrame pandas.
    
    Args:
        assessments_list: Liste de dictionnaires contenant les évaluations
        
    Returns:
        DataFrame pandas avec les données structurées
    """
    stai = STAIYA()
    
    records = []
    for assessment in assessments_list:
        # Calculer le score si nécessaire
        if 'result' not in assessment:
            result = stai.calculate_score(assessment['answers'])
        else:
            result = assessment['result']
        
        # Créer un enregistrement plat
        record = {
            'patient_id': assessment.get('patient_id'),
            'assessment_date': assessment.get('date'),
            'total_score': result['total_score'],
            'category': result['category'],
            'severity': result['severity']
        }
        
        # Ajouter les scores par item
        for item_id, scores in result['item_scores'].items():
            record[f'{item_id}_raw'] = scores['raw']
            record[f'{item_id}_scored'] = scores['scored']
        
        records.append(record)
    
    return pd.DataFrame(records)

# Exemple d'utilisation
assessments = [
    {
        'patient_id': 'P001',
        'date': '2025-01-01',
        'answers': {f"q{i}": 2 for i in range(1, 21)}
    },
    {
        'patient_id': 'P002',
        'date': '2025-01-02',
        'answers': {f"q{i}": 3 for i in range(1, 21)}
    }
]

df = export_to_dataframe(assessments)
print(df.head())

# Export vers CSV
df.to_csv('stai_ya_data.csv', index=False)

# Export vers Excel
df.to_excel('stai_ya_data.xlsx', index=False, sheet_name='STAI-YA')
```

---

## Résumé

Ces exemples couvrent les principaux cas d'usage du questionnaire STAI-YA :
- ✓ Utilisation de base et accès aux métadonnées
- ✓ Scénarios cliniques variés (calme, anxieux, urgence)
- ✓ Validation et gestion robuste des erreurs
- ✓ Suivi longitudinal et comparaisons pré-post
- ✓ Intégration dans des systèmes (API, BDD, export)

Pour plus d'informations, consultez :
- `README.md` - Documentation complète
- `QUICK_REFERENCE.md` - Guide de référence rapide
- `tests/test_stai_ya.py` - Tests unitaires avec exemples additionnels

