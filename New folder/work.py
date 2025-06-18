import pandas as pd

df = pd.read_csv("DataSet.csv")

grouped = df.groupby('post_code')

with open('manifest_file.txt', 'w') as f:
    for post_code, group in grouped:
        unique_dobs = sorted(group['dob'].unique())
        total_unique_dobs = len(unique_dobs)
        total_records = len(group)

        f.write(f"post_code: {post_code} dob: {', '.join(map(str, unique_dobs))}\n")
        f.write(f"total_unique_dob: {total_unique_dobs}\n")
        f.write(f"total_records: {total_records}\n\n")

print("Manifest file written to manifest_file.txt")
