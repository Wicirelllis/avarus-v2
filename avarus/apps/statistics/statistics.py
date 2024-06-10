import pandas as pd
from scipy.stats import pearsonr
from sklearn import decomposition
from pca import pca


def correlation_analysis(df: pd.DataFrame, cols: tuple[str, str]):
    return pearsonr(df[cols[0]], df[cols[1]])

def pca_analysis(df: pd.DataFrame, cols: tuple[str, str]):
    model = pca(n_components=0.95)
    model.fit_transform(df[cols])
    fig, _ = model.biplot()
    file_url = '/media/tmp/pca.png'
    fig.savefig(f'/avarus{file_url}')   

def factor_analysis(df: pd.DataFrame, cols: tuple[str, str]):
    ...

def cluster_analysis(df: pd.DataFrame, cols: tuple[str, str]):
    ...
