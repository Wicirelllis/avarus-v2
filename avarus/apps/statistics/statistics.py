import pandas as pd
from scipy.stats import pearsonr


def correlation_analysis(df: pd.DataFrame, cols: tuple[str, str]):
    return pearsonr(df[cols[0]], df[cols[1]])
