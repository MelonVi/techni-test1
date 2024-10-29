import pandas as pd
import os

os.makedirs("oceny", exist_ok=True)
df = pd.read_excel("grades.xls")
grade_groups = df.groupby(df['grade'].str[0])

for grade, group in grade_groups:
	filename = f"oceny/{grade}.txt"
	with open(filename, "w") as file:
	for index, row in group.iterrows():
		file.write(f"{row['name']} {row['surname']}\n")