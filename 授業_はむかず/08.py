import pandas as pd

df = pd.read_csv("winequality-red.csv", sep=";")
df["volatile acidity"].hist()

import seaborn as sns