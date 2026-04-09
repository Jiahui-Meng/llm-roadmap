# Structured Generation Comparison

## Goal
Compare free-form prompting vs structured (JSON-constrained) generation on output stability and usability.

## Dimensions
- format consistency (does output always parse?)
- content accuracy
- downstream usability (can code consume it directly?)

## Expected finding
Structured generation significantly reduces format errors and makes outputs more reliable for downstream systems, at the cost of slightly more rigid prompt design.

## Suggested experiment
Run 10 identical queries:
1. free-form prompt → check if output is valid JSON
2. schema-constrained prompt → check same

Record parse success rate and format stability.
