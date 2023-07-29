import pandas as pd


def to_parquet(file="./dataset/Distance_Matrix.csv",outfile = "./dataset/distance_matrix.parquet"):
    df = pd.read_csv(file)
    df.drop(columns=["Unnamed: 0"], inplace=True)
    print(df.head())
    df.to_parquet(outfile, index=False)


to_parquet()
