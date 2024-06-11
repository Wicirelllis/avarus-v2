import pandas as pd


def _read_env(path: str) -> pd.DataFrame:
    ''' Read an env excel file into a pandas dataframe '''
    df = pd.read_excel(path, header=None, dtype={'REGION': str})
    for row_idx in range(df.shape[0]):
        if (df.iloc[row_idx] == 'FIELD_NR').any():
            new_header = df.iloc[row_idx]
            df = df[row_idx + 1:]
            df.columns = new_header
            return df

# def _read_env(path: str) -> pd.DataFrame:
#     ''' Read an env excel file into a pandas dataframe '''
#     df = pd.read_excel(path, header=None, dtype={'REGION': str})
#     for row_idx in range(df.shape[0]):
#         if df.iloc[row_idx, 0] == 'RELEVE_NR':
#             new_header = df.iloc[row_idx]
#             df = df[row_idx + 1:]
#             df.columns = new_header
#             return df

def _read_spp(path: str) -> pd.DataFrame:
    ''' Read an env excel file into a pandas dataframe '''
    df = pd.read_excel(path, header=None)
    for row_idx in range(df.shape[0]):
            if (df.iloc[row_idx] == 'PASL TAXON SCIENTIFIC NAME NO AUTHOR(S)').any():
                new_header = df.iloc[row_idx]
                df = df[row_idx + 1:]
                df.columns = new_header
                return df

# def _read_spp(path: str) -> pd.DataFrame:
#     ''' Read an env excel file into a pandas dataframe '''
#     df = pd.read_excel(path)
#     return df
