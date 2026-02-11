import pandas as pd
import os


df = pd.read_csv("data/review.csv")
df_real = pd.read_csv("data/review.csv",encoding="utf-8") 
df_fake = pd.read_csv("data/manual_fake_review.csv", encoding="utf-8")

df = pd.concat([df_real, df_fake], ignore_index=True)


df["review_length"] = df["review_text"].astype(str).str.len()
df["word_count"] = df["review_text"].astype(str).str.split().apply(len)

df["exclamation_count"] = df["review_text"].astype(str).str.count("!")
df["capital_word_count"] = df["review_text"].astype(str).str.findall(r"\b[A-Z]{2,}\b").str.len()

extreme_words = ["best", "worst", "amazing", "excellent", "perfect", "terrible"]

df["extreme_word_count"] = df["review_text"].astype(str).str.lower().apply(
    lambda x: sum(word in x for word in extreme_words)
)


def repetition_ratio(text):
    words = str(text).lower().split()
    if len(words) == 0:
        return 0
    return 1 - len(set(words)) / len(words)

df["repetition_ratio"] = df["review_text"].apply(repetition_ratio)


df["fake_score"] = (
    (df["exclamation_count"] > 2).astype(int) +
    (df["capital_word_count"] > 1).astype(int) +
    (df["extreme_word_count"] > 1).astype(int) +
    (df["repetition_ratio"] > 0.3).astype(int)
)

df["final_label"] = df["fake_score"].apply(
    lambda x: "Likely Fake" if x >= 2 else "Likely Genuine"
)


os.makedirs("output", exist_ok=True)

final_output = df[
    [
        "review_text",
        "rating",
        "sentiment",
        "fake_score",
        "final_label"
    ]
]

final_output.to_csv("output/fake_review_summary.csv", index=False)

print("Fake review analysis completed successfully")
print(final_output.head())
