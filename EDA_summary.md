# EDA Summary — Intelligent EHR QA Project

## Dataset: indiana_reports.csv
- Total Rows: 3851
- Total Columns: 8
- Columns: ['uid', 'MeSH', 'Problems', 'image', 'indication', 'comparison', 'findings', 'impression']
- Null Values:
  - 'comparison' → some missing values
  - 'findings' → some missing values
- Duplicates: 0
- Text Columns (for semantic processing): findings, impression, indication, comparison
- Remarks: Data is mostly clean, rich in clinical text. Suitable for QA tasks.

## Dataset: indiana_projections.csv
- Total Rows: 7466
- Total Columns: 3
- Details: Supporting file for projections or image references.
- Usage: Will decide later if relevant for RAG or just metadata.

## Summary:
The primary dataset `indiana_reports.csv` will be used for question-answer generation. Text fields will be combined into one `combined_text` column for semantic similarity. Missing values will be handled in preprocessing.