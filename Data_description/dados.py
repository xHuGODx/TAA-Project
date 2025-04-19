import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Constants
TOTAL_FNLWGT = 9263575662
US_POPULATION = 269_700_000
SCALING_FACTOR = US_POPULATION / TOTAL_FNLWGT

def summarize_and_generate_graphs(csv_path='base_data/adultdataset.csv', output_path='info.txt'):
    # Load the dataset
    df = pd.read_csv(csv_path, skipinitialspace=True)

    if 'fnlwgt' not in df.columns:
        raise ValueError("Column 'fnlwgt' not found in dataset.")

    # Add scaled fnlwgt column
    df['fnlwgt_scaled'] = df['fnlwgt'] * SCALING_FACTOR

    # Open file to save results
    with open(output_path, 'w') as f:
        f.write(f"📊 Dataset Summary with fnlwgt scaling to U.S. population (269.7M)\n")
        f.write(f"{'-'*60}\n")
        f.write(f"Total fnlwgt sum: {TOTAL_FNLWGT:,.0f}\n")
        f.write(f"Scaling factor to U.S. population (269.7M): {SCALING_FACTOR:.8f}\n\n")

        # Numerical distributions (Unweighted vs. Weighted)
        for col in ['age', 'hours-per-week', 'capital-gain', 'capital-loss']:
            f.write(f"\n🔢 Column: {col}\n")
            f.write(f"Unweighted Mean: {df[col].mean():,.2f}\n")
            f.write(f"Weighted Mean (using fnlwgt_scaled): { (df[col] * df['fnlwgt_scaled']).sum() / US_POPULATION:,.2f}\n")

        # Categorical Distributions (Unweighted vs. Weighted)
        categorical_cols = ['sex', 'income', 'education', 'race', 'workclass', 'marital-status']
        for col in categorical_cols:
            f.write(f"\n📂 Column: {col}\n")

            f.write("\n-- Unweighted Distribution --\n")
            unweighted = df[col].value_counts(normalize=True) * 100
            for val, pct in unweighted.items():
                f.write(f"{val}: {pct:.2f}%\n")

            f.write("\n-- Weighted Distribution (scaled to 269.7M) --\n")
            weighted = df.groupby(col)['fnlwgt_scaled'].sum()
            weighted_pct = (weighted / US_POPULATION) * 100
            for val, pct in weighted_pct.items():
                f.write(f"{val}: {pct:.2f}%\n")

    print(f"✅ Summary written to {output_path}")

    # --- Graphs ---
    plt.figure(figsize=(12, 6))

    # 1. Age Distribution (Histogram)
    plt.subplot(2, 2, 1)
    sns.histplot(df['age'], kde=True, color='skyblue')
    plt.title('Age Distribution (Unweighted)', fontsize=14)
    plt.xlabel('Age', fontsize=12)
    plt.ylabel('Count', fontsize=12)

    # 2. Hours per week (Histogram)
    plt.subplot(2, 2, 2)
    sns.histplot(df['hours-per-week'], kde=True, color='lightcoral')
    plt.title('Hours per Week Distribution (Unweighted)', fontsize=14)
    plt.xlabel('Hours per Week', fontsize=12)
    plt.ylabel('Count', fontsize=12)

    # 3. Education Level (Barplot)
    plt.subplot(2, 2, 3)
    education_dist = df.groupby('education')['fnlwgt_scaled'].sum().sort_values(ascending=False)
    education_dist = (education_dist / US_POPULATION) * 100  # Convert to percentage
    education_dist.plot(kind='bar', color='lightgreen', edgecolor='black')
    plt.title('Education Distribution (Weighted)', fontsize=14)
    plt.xlabel('Education Level', fontsize=12)
    plt.ylabel('Percentage of Population', fontsize=12)
    plt.xticks(rotation=45, ha='right')

    # 4. Income Distribution (Barplot)
    plt.subplot(2, 2, 4)
    income_dist = df.groupby('income')['fnlwgt_scaled'].sum().sort_values(ascending=False)
    income_dist = (income_dist / US_POPULATION) * 100  # Convert to percentage
    income_dist.plot(kind='bar', color='lightblue', edgecolor='black')
    plt.title('Income Distribution (Weighted)', fontsize=14)
    plt.xlabel('Income Group', fontsize=12)
    plt.ylabel('Percentage of Population', fontsize=12)

    plt.tight_layout()
    plt.savefig('weighted_distribution_graphs.png')
    plt.show()

if __name__ == '__main__':
    summarize_and_generate_graphs()
