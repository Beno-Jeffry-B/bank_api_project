import pandas as pd
import os

INPUT_CSV = "bank_branches.csv"

# o/p files
BANKS_CSV = "banks.csv"
BRANCHES_CSV = "branches.csv"

def main():
    if not os.path.exists(INPUT_CSV):
        print(f"Input file '{INPUT_CSV}' not found.")
        return

    print("Loading combined bank + branch data...")
    df = pd.read_csv(INPUT_CSV)

    # Extract unique banks
    print("Separating unique banks...")
    banks_df = df[['bank_id', 'bank_name']].drop_duplicates()
    banks_df.columns = ['id', 'name']
    banks_df.to_csv(BANKS_CSV, index=False)
    print(f" Saved {len(banks_df)} banks to '{BANKS_CSV}'")

    # Extract branch data
    print(" extracting branch details...")
    branches_df = df[['ifsc', 'bank_id', 'branch', 'address', 'city', 'district', 'state']]
    branches_df.to_csv(BRANCHES_CSV, index=False)
    print(f" Saved {len(branches_df)} branches to '{BRANCHES_CSV}'")

    print(" done..!")

if __name__ == "__main__":
    main()
