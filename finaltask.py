import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#要約統計量
df = pd.read_csv("student.csv", index_col = 0)
print(df.describe())

#学生数推移のグラフ
df = pd.read_csv("student.csv")
plt.bar(df["Academic Year"], df["Undergraduate Student"], alpha=0.5)
plt.title("Changes in the number of students at Waseda University")
plt.xlabel("Academic Year")
plt.ylabel("Undergraduate Student")
plt.grid(color='black', axis='y')
plt.show()