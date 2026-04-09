# Structured Generation Lab

## Goal
A reusable module for schema-constrained LLM output.

## Contents
- `json_output_demo.py` — basic JSON output
- `schema_demo.py` — schema-validated extraction
- Comparison report in `reports/structured_generation/`

## Usage
These demos show the pattern: define a schema, prompt the model with format instructions, validate output against schema.

## Future
- Integrate with SGLang constrained decoding
- Add Pydantic model validation
- Support nested schemas
