import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("output/fake_review_summary.csv")

if "prediction" not in df.columns:
    df["prediction"] = df["fake_score"].apply(
        lambda x: "Likely Fake" if x >= 3 else "Likely Genuine"
    )

counts = df["prediction"].value_counts()

plt.figure()
counts.plot(kind="bar")
plt.title("Fake vs Genuine Reviews")
plt.xlabel("Review Type")
plt.ylabel("Count")
plt.tight_layout()
plt.show()
