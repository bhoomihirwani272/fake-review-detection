# Fake Review Detection System (Rule-Based NLP)

A Python-based Fake Review Detection system that identifies **Likely Fake** and **Likely Genuine** reviews using rule-based Natural Language Processing (NLP) techniques and heuristic scoring.

---

## Project Overview

Online platforms often suffer from fake or misleading reviews that influence customer decisions.  
This project aims to **detect suspicious reviews** by analyzing textual patterns commonly found in spam or fake content.

Instead of using black-box machine learning models, this project focuses on:
- explainable rules
- interpretable features
- clear scoring logic



---

## Key Features

- Rule-based fake review detection
- Text feature extraction
- Heuristic fake score calculation
- Clear classification logic
- CSV output generation
- Visualization using Matplotlib

---

## Dataset Description

This project uses **two types of datasets**:

1. **Real Reviews**  
   - Collected from online sources
   - Stored in `data/review.csv`

2. **Manually Created Fake Reviews**  
   - Added intentionally to simulate fake patterns
   - Stored in `data/manual_fake_review.csv`
   - Includes exaggerated language, repetition, excessive capitalization, etc.

> ⚠️ Manually added fake reviews are used **only for testing and validation purposes**

---

## Feature Engineering

The following features are extracted from each review:

- **Review Length** – total number of characters
- **Word Count** – total number of words
- **Exclamation Count** – number of `!`
- **Capital Word Count** – fully capitalized words (e.g., AMAZING)
- **Extreme Word Count** – words like `best`, `worst`, `perfect`
- **Repetition Ratio** – measures repeated word usage

---

## Fake Score Logic

Each suspicious condition contributes **1 point** to the fake score:

| Condition |             |Score|
| Exclamation count > 2   | +1 |
| Capital words > 1       | +1 |
| Extreme words > 1       | +1 |
| Repetition ratio > 0.3  | +1 |

### Final Classification
- **Fake Score ≥ 2 → Likely Fake**
- **Fake Score < 2 → Likely Genuine**

---

## Project Structure
fake_review_detection/
│
├── data/
│ ├── review.csv
│ └── manual_fake_review.csv
│
├── output/
│ └── fake_review_summary.csv
│
├── analysis.py # Feature extraction & scoring
├── visualization.py # Matplotlib visualizations
├── cleaning.py # preprocessing
└── README.md
 
Conclusion: 
This project applies basic NLP techniques and rule-based logic to identify suspicious review patterns. It demonstrates how textual features can be converted into measurable signals to classify reviews as likely fake or genuine. Future improvements include implementing machine learning models for better accuracy.
