# Questionnaires API

FastAPI service for accessing clinical questionnaires and computing scores from submitted answers.

## Overview

This API provides access to a collection of clinical questionnaires extracted from EMR applications (eBipolar, eSchizo, Asperger, CEDR). It allows external applications to:

1. List available questionnaires
2. Retrieve questionnaire details (questions and possible answers)
3. Submit answers and receive computed scores

## Installation

```bash
pip install -r requirements.txt
```

## Running the API

```bash
# Using uvicorn directly
uvicorn api.main:app --reload

# Or run the main module
python -m api.main
```

The API will be available at `http://localhost:8000`

## API Documentation

Once running, interactive API documentation is available at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Endpoints

### GET `/`

Get API information and version.

**Response:**
```json
{
  "name": "Questionnaires API",
  "version": "1.0.0",
  "description": "API for accessing clinical questionnaires and computing scores",
  "endpoints": {
    "list_questionnaires": "/questionnaires",
    "get_questionnaire": "/questionnaires/{questionnaire_id}",
    "calculate_score": "/questionnaires/{questionnaire_id}/score"
  }
}
```

### GET `/questionnaires`

List all available questionnaires.

**Response:**
```json
[
  {
    "id": "madrs",
    "name": "MADRS - Montgomery-Åsberg Depression Rating Scale",
    "description": "Échelle d'évaluation de la dépression en 10 items...",
    "num_items": 10,
    "used_in_applications": ["cedr", "ebipolar", "eschizo"]
  },
  ...
]
```

### GET `/questionnaires/{questionnaire_id}`

Get detailed information about a specific questionnaire including all questions and answer options.

**Parameters:**
- `questionnaire_id`: Questionnaire identifier (e.g., `madrs`, `qids`, `abc`)

**Response:**
```json
{
  "id": "madrs",
  "name": "MADRS - Montgomery-Åsberg Depression Rating Scale",
  "description": "...",
  "num_items": 10,
  "used_in_applications": ["cedr", "ebipolar", "eschizo"],
  "questions": [
    {
      "id": "MADRS1",
      "number": 1,
      "text": "Tristesse apparente : Correspond au découragement...",
      "type": "radio",
      "options": {
        "0": "0 Pas de tristesse.",
        "1": "1",
        "2": "2 Semble découragé mais peut se dérider sans difficulté.",
        ...
      },
      "required": true,
      "mutually_exclusive_with": null,
      "subscale": null
    },
    ...
  ]
}
```

### POST `/questionnaires/{questionnaire_id}/score`

Submit responses and calculate questionnaire score.

**Parameters:**
- `questionnaire_id`: Questionnaire identifier

**Request Body:**
```json
{
  "responses": {
    "MADRS1": 3,
    "MADRS2": 4,
    "MADRS3": 2,
    ...
  }
}
```

**Response Format Options:**

The API accepts responses in two formats:

1. **Numeric values** (recommended):
```json
{
  "responses": {
    "MADRS1": 3,
    "MADRS2": 4
  }
}
```

2. **Option text** (also supported):
```json
{
  "responses": {
    "MADRS1": "3",
    "MADRS2": "4 Paraît triste et malheureux la plupart du temps."
  }
}
```

**Response:**
```json
{
  "score": 24,
  "valid": true,
  "errors": [],
  "interpretation": "Dépression modérée",
  "subscales": null,
  "item_scores": null,
  "details": {}
}
```

## Usage Examples

### Example 1: Get MADRS Questionnaire Details

```bash
curl http://localhost:8000/questionnaires/madrs
```

### Example 2: Calculate MADRS Score (Numeric Format)

```bash
curl -X POST http://localhost:8000/questionnaires/madrs/score \
  -H "Content-Type: application/json" \
  -d '{
    "responses": {
      "MADRS1": 3,
      "MADRS2": 4,
      "MADRS3": 2,
      "MADRS4": 3,
      "MADRS5": 2,
      "MADRS6": 3,
      "MADRS7": 2,
      "MADRS8": 2,
      "MADRS9": 2,
      "MADRS10": 1
    }
  }'
```

### Example 3: Calculate MADRS Score (Text Format)

```bash
curl -X POST http://localhost:8000/questionnaires/madrs/score \
  -H "Content-Type: application/json" \
  -d '{
    "responses": {
      "MADRS1": "3",
      "MADRS2": "4 Paraît triste et malheureux la plupart du temps.",
      "MADRS3": "2 Sentiments occasionnels d'\''irritabilité et de malaise mal défini.",
      "MADRS4": "3",
      "MADRS5": "2 Appétit légèrement réduit.",
      "MADRS6": "3",
      "MADRS7": "2 Difficultés à commencer des activités.",
      "MADRS8": "2 Capacité réduite à prendre du plaisir à ses intérêts habituels.",
      "MADRS9": "2 Idées intermittentes d'\''échec, d'\''auto-accusation ou d'\''autodépréciation.",
      "MADRS10": "1"
    }
  }'
```

### Example 4: Calculate ABC Score (Text Format)

```bash
curl -X POST http://localhost:8000/questionnaires/abc/score \
  -H "Content-Type: application/json" \
  -d '{
    "responses": {
      "ABC1": "C'\''est un problème peu important",
      "ABC2": "C'\''est un problème moyennement important",
      ...
    }
  }'
```

### Example 5: Calculate ADHD-RS Score (List Format)

ADHD-RS uses a List[int] format internally, but the API still accepts a dictionary:

```bash
curl -X POST http://localhost:8000/questionnaires/adhd-rs/score \
  -H "Content-Type: application/json" \
  -d '{
    "responses": {
      "ADHDRS1": 2,
      "ADHDRS2": 3,
      "ADHDRS3": 2,
      ...
      "ADHDRS18": 1
    }
  }'
```

## Error Handling

### Validation Errors (HTTP 400)

When validation fails, the API returns a 400 Bad Request with detailed error messages:

```json
{
  "detail": {
    "errors": [
      "Missing required question: MADRS1 (Item 1)",
      "Invalid response for MADRS2 (Item 2): '99'. Valid options: [0, 1, 2]..."
    ],
    "valid": false
  }
}
```

### Questionnaire Not Found (HTTP 404)

```json
{
  "detail": "Questionnaire 'invalid-id' not found"
}
```

### Internal Server Error (HTTP 500)

```json
{
  "detail": "Error calculating score: ..."
}
```

## Response Format Conversion

The API automatically handles conversion between different response formats:

- **Text to Numeric**: Converts option text strings to their corresponding numeric values
- **Numeric Pass-through**: Validates and passes numeric values directly
- **List Format**: Converts dictionary responses to ordered lists for questionnaires that require `List[int]`

## Available Questionnaires

The API supports all questionnaires in the `Questionnaires` module. Common questionnaires include:

- **MADRS** - Montgomery-Åsberg Depression Rating Scale
- **QIDS-SR16** - Quick Inventory of Depressive Symptomatology
- **ABC** - Aberrant Behavior Checklist
- **ADHD-RS** - ADHD Rating Scale
- **YMRS** - Young Mania Rating Scale
- **PANSS** - Positive and Negative Syndrome Scale
- And many more...

Use `GET /questionnaires` to see the complete list.

## Questionnaire Aliases

Questionnaires can be accessed using multiple identifiers. For example:

- `madrs` or `montgomery` → MADRS
- `qids` or `qids-sr16` → QIDS-SR16
- `abc` or `aberrant-behavior` → ABC

See the `Questionnaires/__init__.py` file for the complete list of aliases.

## Development

### Project Structure

```
QuestionnairesAPI/
├── api/
│   ├── __init__.py
│   ├── main.py          # FastAPI app and routes
│   ├── models.py        # Pydantic models
│   └── utils.py         # Response format conversion
├── Questionnaires/      # Questionnaire classes
└── requirements.txt
```

### Adding New Questionnaires

New questionnaires should be added to the `questionnaires/` directory and registered in `questionnaires/__init__.py`. The API will automatically detect and expose them.

## License

[Add your license here]

