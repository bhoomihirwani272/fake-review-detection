import pandas as pd

df = pd.read_csv(
    "data/review.csv",
    engine="python",
    on_bad_lines="skip",   # skip broken rows
)

print(df.shape)
print(df.head())
print(df.columns)
