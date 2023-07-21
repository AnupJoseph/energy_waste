import pandas as pd


def to_parquet(file="./dataset/Distance_Matrix.csv"):
    df = pd.read_csv(file)
    df.drop(columns=["Unnamed: 0"], inplace=True)
    print(df.head())
    df.to_parquet("./dataset/distance_matrix.parquet", index=False)


to_parquet()
