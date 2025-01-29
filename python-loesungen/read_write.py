import pandas as pd
from sklearn.datasets import load_iris


def main():
    # Load the Iris dataset from scikit-learn
    iris = load_iris()

    # Create a DataFrame with feature columns
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

    # Add the species (target) column
    df["species"] = iris.target

    # Map the numeric species labels to their actual names
    species_map = dict(enumerate(iris.target_names))
    df["species"] = df["species"].map(species_map)

    # Show some quick info
    print("DataFrame shape:", df.shape)
    print("First 5 rows:\n", df.head())
    print("\nSummary stats:\n", df.describe())

    # Write the DataFrame to a CSV file
    csv_file = "iris.csv"
    df.to_csv(csv_file, index=False)
    print(f"\nSaved Iris dataset to {csv_file}.")

    # Read the CSV back into a DataFrame
    df_loaded = pd.read_csv(csv_file)
    print(f"Read DataFrame shape from {csv_file}:", df_loaded.shape)


if __name__ == "__main__":
    main()
