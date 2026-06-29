import pandas as pd
import os

data_folder = "data"
output_file = "data/processed_data.csv"

all_data = []

for filename in os.listdir(data_folder):
    if filename.endswith(".csv") and filename.startswith("daily_sales_data"):
        file_path = os.path.join(data_folder, filename)
        df = pd.read_csv(file_path)
        all_data.append(df)

combined = pd.concat(all_data, ignore_index=True)

pink_only = combined[combined["product"] == "pink morsel"].copy()

pink_only["price"] = pink_only["price"].astype(str).str.replace(r"[$,]", "", regex=True).astype(float)
pink_only["quantity"] = pd.to_numeric(pink_only["quantity"])
pink_only["sales"] = pink_only["price"] * pink_only["quantity"]

result = pink_only[["sales", "date", "region"]]

result.to_csv(output_file, index=False)

print("Done! Processed data saved to", output_file)
print("Total rows:", len(result))
