import pandas as pd


def _rename_duplicates(l: list[str]) -> list[str]:
    if len(set(l)) == len(l):
        return l
    return [a if not (s:=sum(j == a for j in l[:i])) else f'{a}-{s+1}' for i, a in enumerate(l)]

def _read_file(file, *args, **kwargs):
    if isinstance(file, str):
        filename = file
    else:
        filename = file.path

    if filename.endswith('xlsx'):
        return pd.read_excel(file, *args, **kwargs)
    if filename.endswith('csv'):
        return pd.read_csv(file, encoding='cp1252', encoding_errors='ignore', *args, **kwargs)


def read_env(path: str) -> pd.DataFrame:
    ''' Read an env excel file into a pandas dataframe '''
    df = _read_file(path, header=None, dtype=str)
    for row_idx in range(df.shape[0]):
        if (df.iloc[row_idx] == 'FIELD_NR').any():
            header = df.iloc[row_idx]
            header = _rename_duplicates(header)
            return _read_file(path, skiprows=row_idx+1, names=header)


def read_spp(path: str) -> pd.DataFrame:
    ''' Read an env excel file into a pandas dataframe '''
    df = _read_file(path, header=None, dtype=str, na_values=[0, 0.])
    for row_idx in range(df.shape[0]):
        if (df.iloc[row_idx] == 'PASL TAXON SCIENTIFIC NAME NO AUTHOR(S)').any():
            header = df.iloc[row_idx]
            if 'AUTHOR PLOT NUMBER' in df.values:
                header_vals = df[df.isin(["AUTHOR PLOT NUMBER"]).any(axis=1)].squeeze()
                header.fillna(header_vals, inplace=True)
            header = _rename_duplicates(header)
            return _read_file(path, skiprows=row_idx+1, names=header).fillna(0).convert_dtypes()
