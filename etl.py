import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "salary": [70000, 80000, 90000]
}
df = pd.DataFrame(data)
df["salary_after_tax"] = df["salary"] * 0.9
df.to_csv("data.csv", index=False)
print("ETL process completed successfully.")
