import pandas as pd

def sum_fnlwgt(csv_path='base_data/adultdataset.csv'):
    df = pd.read_csv(csv_path, skipinitialspace=True)
    
    if 'fnlwgt' not in df.columns:
        print("❌ Error: 'fnlwgt' column not found.")
        return

    total_weight = df['fnlwgt'].sum()
    print(f"✅ Total fnlwgt sum: {total_weight:,.0f}")

if __name__ == '__main__':
    sum_fnlwgt()
