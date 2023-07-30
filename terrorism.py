import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("terrorism.csv")

print(data.head())        
print(data.info())  

country_counts = data["COUNTRY"].value_counts()

total_injured = data["INJURED"].sum()
total_dead = data["DEAD"].sum()

category_stats = data.groupby("CATEGORY")[["INJURED", "DEAD"]].mean()

plt.figure(figsize=(12, 6))
country_counts.plot(kind="bar")
plt.xlabel("Country")
plt.ylabel("Number of Incidents")
plt.title("Number of Terrorism Incidents in Each Country")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8, 8))
labels = ["Injured", "Dead"]
sizes = [total_injured, total_dead]
plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Proportion of Injured and Dead in Terrorism Incidents")
plt.show()

plt.figure(figsize=(10, 6))
category_stats.plot(kind="bar")
plt.xlabel("Category")
plt.ylabel("Average Count")
plt.title("Average Injured and Dead per Category")
plt.xticks(rotation=45)
plt.show()
