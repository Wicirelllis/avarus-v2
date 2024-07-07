import pandas as pd
from matplotlib import pyplot as plt
from pca import pca
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.stats import pearsonr
from sklearn.metrics import jaccard_score, pairwise_distances


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
    data = df[cols].eq('0').astype(int).T
    distances = pairwise_distances(data, metric=jaccard_score)
    Z = linkage(distances)

    _ = plt.figure(dpi=300)
    _ = dendrogram(Z, labels=cols, orientation='left')

    plt.tight_layout()
    file_url = '/media/tmp/cluster.png'
    plt.savefig(f'/avarus{file_url}')
