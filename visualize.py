import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/student_scores.csv")

sns.heatmap(df.corr(), annot=True)
plt.show()
