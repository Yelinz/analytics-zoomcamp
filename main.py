from scripts.data_repo import DataRepository
from scripts.transform import TransformData
from scripts.train import TrainModel

import argparse
import pandas as pd
import warnings


def main(fetch, transform, train):
    print("Step 1: Getting data from APIs or Load from disk")

    repo = DataRepository()
    if fetch:
        # Fetch All 3 datasets for all dates from APIs
        repo.fetch()
        # save data to a local dir
        repo.persist(data_dir="local_data/")
    else:
        # OR Load from disk
        repo.load(data_dir="local_data/")

    print("Step 2: Making data transformations (combining into one dataset)")

    transformed = TransformData(repo=repo)
    if transform:
        transformed.transform()
        transformed.persist(data_dir="local_data/")
    else:
        transformed.load(data_dir="local_data/")

    print("Step 3: Training the model or loading from disk")

    # Suppress all warnings (not recommended in production unless necessary)
    warnings.filterwarnings("ignore")

    trained = TrainModel(transformed=transformed)
    if train:
        trained.prepare_dataframe()  # prepare dataframes
        trained.train_random_forest()  # train the model
        trained.persist(data_dir="local_data/")  # save the model to disk
    else:
        trained.prepare_dataframe()  # prepare dataframes (incl. for inference)
        trained.load(data_dir="local_data/")

    print("Step 4: Making inference")

    prediction_name = "pred_rf_best"
    trained.make_inference(pred_name=prediction_name)
    COLUMNS = [
        "Adj Close",
        "Ticker",
        "Date",
        prediction_name,
        prediction_name + "_rank",
    ]

    print("Results of the estimation (last 10 days):")
    # Set display options to prevent truncation
    pd.set_option("display.max_rows", None)
    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_colwidth", None)

    print(
        trained.df_full[trained.df_full[f"{prediction_name}_rank"] <= 2]
        .sort_values(by=["Date", f"{prediction_name}_rank"])
        .tail(10)[COLUMNS]
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='Stock Analysis', description='Download, transform, train and infere on stock data')
    parser.add_argument('--fetch', action='store_true', help='Fetch data from APIs')
    parser.add_argument('--transform', action='store_true', help='Transform data')
    parser.add_argument('--train', action='store_true', help='Train the model')
    args = parser.parse_args()
    main(args.fetch, args.transform, args.train)
