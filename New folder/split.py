import pandas as pd
import os

df = pd.read_csv("DataSet.csv")

output_dir = "split_datasets"
os.makedirs(output_dir, exist_ok=True)

for post_code, group in df.groupby('post_code'):
    filename = f"{output_dir}/dataset_{post_code}.csv"
    group.to_csv(filename, index=False)

print("Files have been successfully split and saved.")