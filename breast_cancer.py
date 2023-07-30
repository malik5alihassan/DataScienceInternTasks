import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Breast_Cancer.csv")

print(data.head())        
print(data.info())         

race_counts = data["Race"].value_counts()

grade_avg_survival = data.groupby("Grade")["Survival Months"].mean()

plt.figure(figsize=(8, 6))
data["Marital Status"].value_counts().plot(kind="bar")
plt.xlabel("Marital Status")
plt.ylabel("Number of Patients")
plt.title("Number of Breast Cancer Patients in Each Marital Status")
plt.xticks(rotation=45)
plt.show()


plt.figure(figsize=(10, 6))
grade_avg_survival.plot(kind="bar")
plt.xlabel("Grade")
plt.ylabel("Average Survival Months")
plt.title("Average Survival Months per Grade")
plt.xticks(rotation=0)
plt.show()