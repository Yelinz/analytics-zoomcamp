# E2E Stock Market Analysis

## Description

This project is a simple stock market analysis tool that allows users to analyze stock prices and make predictions based on historical data. The tool uses the Yahoo Finance API to retrieve historical stock prices and scikit-learn for predictions.

The historic prices of the largest US, EU and JP companies are used, next to a varienty of Indexes and ETFs, additionally some Macro conditions such as GDP are also analyzed.

The output is which of the input stocks will perform better in the future.

This project was made in the DTC Course [Stock Market Analytics](https://github.com/DataTalksClub/stock-markets-analytics-zoomcamp)
Solution based on week 5 content. 

## Installation

Needed system dependencies:
- conda
- more than 8 GB RAM

To install the necessary dependencies, run the following command:

```bash
conda create -n stock-zoomcamp-env
conda activate stock-zoomcamp-env
conda install -c conda-forge libta-lib
conda install pip
pip install -r requirements.txt
```

If issues arise with TA-lib installation refer to their [README](https://pypi.org/project/TA-Lib/) for soluttions

## Usage
To run the application, use the following command:

```bash
python main.py
```

Per default data is assumed to be local.

To enable download, transformation and training use the cli arguments:
```bash
python main.py --download --transform --train
```

Example data is available here: https://drive.google.com/file/d/1EQ4Ss8mlRHaX48uU_uqMX5qHMm9dRrqv/view?usp=drive_link

Put the downloaded files into the `local_data` folder in the project root.

### Cron

To use the script as a cronjob add this to the crontab:
```
0 1 * * * python /path/to/main.py --download --transform
```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your proposed changes.

Code style and checking with [ruff](https://docs.astral.sh/ruff/)

Install the development requirements in the conda environment with the following command:
```bash
pip install -r requirements-dev.txt
```


