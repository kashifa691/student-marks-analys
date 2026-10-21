import pandas as pd

# CSV file ko read karna
df = pd.read_csv("students.csv")

# Data ko table mein show karna
print("Student Data:")
print(df)
# Average marks
average = df["Marks"].mean()

# Highest marks
highest = df["Marks"].max()

# Lowest marks
lowest = df["Marks"].min()

print("\nData Analysis:")
print("Average Marks:", average)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
import matplotlib.pyplot as plt

# Bar chart banana
plt.bar(df["Name"], df["Marks"])

# Chart ka title aur labels
plt.title("Student Marks Analysis")
plt.xlabel("Student Name")
plt.ylabel("Marks")

# Chart ki layout
plt.tight_layout()

# Chart ko image file mein save karna
plt.savefig("student_marks_chart.png")

# Chart screen par show karna
plt.show()