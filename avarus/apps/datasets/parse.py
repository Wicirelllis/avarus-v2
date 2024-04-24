''' This module contains auxiliary functions that parse xlsx dataset file to extract data '''
import dateutil
import numpy as np
import pandas as pd


def _calc_completeness(df: pd.DataFrame):
    ''' Calculate copleteness (percent of cell with data) for each column of dataframe '''
    return (100 * df.notna().sum() / df.shape[0]).round().astype(int).to_dict()

def _translate(data: list | dict, table: dict) -> list | dict:
    ''' Replace elements of the list using translation table '''
    if isinstance(data, list):
        return [table.get(i, i) for i in data]
    elif isinstance(data, dict):
        return {table.get(k, k): v for k, v in data.items()}


class ParseDataset:
    def __init__(self, dataset) -> None:
        self.dataset = dataset
        self.df: pd.DataFrame = self._read_excel()
        self._fix_header()

    def fill_fields(self, fields: list[str]):
        ''' Fill dataset's attributes '''
        for field in fields:
            # if not getattr(self.dataset, field):
            if True:
                setattr(self.dataset, field, getattr(self, f'_get_{field}')())

    def _read_excel(self) -> pd.DataFrame:
        ''' Read an excel file into a pandas dataframe '''
        path = self.dataset.env.path
        df = pd.read_excel(path, header=None, dtype={'REGION': str})
        for row_idx in range(df.shape[0]):
            if df.iloc[row_idx, 0] == 'RELEVE_NR':
                new_header = df.iloc[row_idx]
                df = df[row_idx + 1:]
                df.columns = new_header
                return df

    def _fix_header(self):
        ''' Rename column names for consistency '''
        table = {
            'SITE_MOIST': 'SITE_MST',
        }
        self.df.rename(str.strip, axis='columns', inplace=True)
        self.df.rename(table, axis='columns', inplace=True)
    
    def _get_val_counts(self, field: str | list[str]):
        ''' Return a dict containing counts of unique values '''
        return self.df[field].fillna('NONE').value_counts(dropna=False).to_dict()
    
    # chart data fields
    def _get_disturban(self):
        data = self.df['DISTURBAN'].fillna('NONE').value_counts(dropna=False).to_dict()
        table = {
            'DIS': 'Disturbed',
            'NAT': 'Natural',
            'NONE': 'No data',
        }
        return {
            'title': 'Disturbance',
            'labels': _translate(list(data.keys()), table),
            'data': list(data.values()),
        }

    def _get_position(self):
        data = self.df['POSITION'].fillna('NONE').value_counts(dropna=False).to_dict()
        data = self._get_val_counts('POSITION')
        table = {
            'EL_PLN': 'Flat elevated plain',
            'CRST': 'Hill crest',
            'SHLD': 'Shoulder',
            'BACK': 'Backslope',
            'FOOT': 'Foot slope',
            'LW_PLN': 'Flat low plain',
            'RIPZN': 'Riparian zone',
            'LAKE': 'Lake or pond',
        }
        return {
            'title': 'Relief chart',
            'labels': _translate(list(data.keys()), table),
            'data': list(data.values()),
        }

    def _get_soil_text(self):
        data = self.df['SOIL_TEXT'].fillna('NONE').value_counts(dropna=False).to_dict()
        table = {
            'GRV': 'Gravel or coarser',
            'SND': 'Sand',
            'SLT': 'Silt',
            'CLY': 'Clay',
            'LOM': 'Loam',
            'ORG': 'Organic (if no mineral soil)',
        }
        return {
            'title': 'Soil chart',
            'labels': _translate(list(data.keys()), table),
            'data': list(data.values()),
        }

    def _get_ecotope(self):
        fields = [
            'ELEVATION',
            'SLOPE',
            'ASPECT',
            'POSITION',
            'SURF_GEOL',
            'HAB_TYPE',
            'SITE_MST',
            'DISTURBAN',
            'ORG_DEPTH',
            'SOIL_TEXT',
            'SOIL_PH',
        ]
        data = _calc_completeness(self.df[fields])
        table = {
            'ELEVATION': 'Altitude, m',
            'SLOPE': 'Slope, degree',
            'ASPECT': 'Aspect, degree',
            'POSITION': 'Topographic position',
            'SURF_GEOL': 'Surfial geology',
            'HAB_TYPE': 'Habitat type',
            'SITE_MST': 'Site moisture',
            'DISTURBAN': 'Disturbance',
            'ORG_DEPTH': 'Organic layer depth, cm',
            'SOIL_TEXT': 'Soil texture',
            'SOIL_PH': 'Soil pH',
        }
        return {
            'title': 'Ecotope data completeness, %',
            'labels': _translate(list(data.keys()), table),
            'data': list(data.values()),
        }

    def _get_phytocoenosis(self):
        fields = [
            'MEAN_HT',
            'TREE_HT',
            'SHRUB_HT',
            'HERB_HT',
            'MOSS_HT',
        ]
        data = _calc_completeness(self.df[fields])
        table = {
            'MEAN_HT': 'Mean canopy height',
            'TREE_HT': 'Mean tree height',
            'SHRUB_HT': 'Mean shrub height',
            'HERB_HT': 'Mean herb height',
            'MOSS_HT': 'Mean moss height',
        }
        return {
            'title': 'Phytocoenosis data completeness, %',
            'labels': _translate(list(data.keys()), table),
            'data': list(data.values()),
        }

    def _get_phytocoenosis_cover(self):
        fields =[
            'COV_TREES',
            'COV_SHRUBS',
            'COV_TSHRUB',
            'COV_LSHRUB',
            'COV_DSHRUB',
            'COV_PSHRUB',
            'COV_GRAM',
            'COV_TGRAM',
            'COV_FORB',
            'COV_SLVAS',
            'COV_MOSS',
            'COV_LICH',
            'COV_CRUST',
            'COV_ALGAE',
            'COV_SOIL',
            'COV_ROCK',
            'COV_WATER',
            'COV_LITTER',
            'COV_TOTAL',
        ]
        data = _calc_completeness(self.df[fields])
        table = {
            'COV_TREES': 'Tree layer',
            'COV_SHRUBS': 'Shrub layer',
            'COV_TSHRUB': 'Tall shrubs',
            'COV_LSHRUB': 'Low shrubs',
            'COV_DSHRUB': 'Erect dwarf-shrubs',
            'COV_PSHRUB': 'Prostrate dwarf-shrubs',
            'COV_GRAM': 'Graminoids',
            'COV_TGRAM': 'Tussock graminoids',
            'COV_FORB': 'Forbs',
            'COV_SLVAS': 'Seedless vascular plants',
            'COV_MOSS': 'Mosses & liverworts',
            'COV_LICH': 'Lichens',
            'COV_CRUST': 'Crust',
            'COV_ALGAE': 'Algae layer',
            'COV_SOIL': 'Bare soil',
            'COV_ROCK': 'Bare rock',
            'COV_WATER': 'Open water',
            'COV_LITTER': 'Litter layer',
            'COV_TOTAL': 'Total',
        }
        return {
            'title': 'Phytocoenosis data completeness (cover), %',
            'labels': _translate(list(data.keys()), table),
            'data': list(data.values()),
        }


    # regular data description fields
    def _get_n_plots(self):
        return len(self.df.loc[:, 'SOIL_TEXT'])

    def _get_year(self):
        return int(np.floor(self.df['DATE'].apply(lambda x: dateutil.parser.parse(str(x)).year).mean()))

    def _get_coverscale(self):
        table = {
            '00': 'Percentage',
            '01': 'Braun/Blanquet (old)',
            '02': 'Braun/Blanquet (new)',
            '03': 'Londo',
            '04': 'Presence/Absence',
            '05': 'Ordinal scale (1-9)',
            '06': 'Barkman, Doing & Segal',
            '07': 'Doing',
            '08': 'Constancy classes',
            '09': 'Domin',
            '10': 'Colin',
            '11': 'Tansley',
            '12': 'Didukh',
            '13': 'Hult-Sernander-Du Rietz (Daniels)',
            '14': 'Br-Bl (enlarge)',
            '15': 'Westhoff and van der Maarel',
            '98': 'Numbers (<65025)',
            '99': 'Numbers (<24000)',
        }
        val_counts = self._get_val_counts('COVERSCALE')
        return ','.join(_translate(val_counts, table).keys())

    def _get_region(self):
        table = {
            '000': 'No region specified',
            '001': 'Prudhoe Bay Oilfield',
            '002': 'Kuparuk Oilfield',
            '003': 'Kadleroshilik River',
            '004': 'Toolik River',
            '005': 'Dalton Highway',
            '006': 'Arctic National Wildlife Refuge',
            '007': 'Gates of the Arctic National Park and Preserve',
            '008': 'Kobuk Valley National Park',
            '009': 'National Petroleum Reserve-Alaska',
            '010': 'Yamal Peninsula',
            '011': 'Seward Peninsula',
            '012': 'West Siberian Plain',
            '013': 'Polar Ural Mountain Foothills',
            '014': 'Franz Jozef Land Archipelago',
            '015': 'Beaufort Coast',
            '016': 'Brooks Range',
            '017': 'Western Arctic, Canada',
            '018': 'Cape Krusenstern',
            '019': 'Bering Land Bridge Natural Peserve',
            '020': 'Noatak National Preserve',
            '021': 'Arctic Foothills of the Brooks Range',
            '022': 'Aleutian Islands',
            '023': 'Colville River',
            '024': 'Gydan Peninsula',
            '025': 'Canadian Arctic Archipelago',
            '026': 'Mainland Northwest Territories, Canada',
        }
        val_counts = self._get_val_counts('REGION')
        return ','.join(_translate(val_counts, table).keys())

    def _get_location(self):
        val_counts = self._get_val_counts('LOCATION')
        return ','.join(val_counts.keys())
    
    def _get_subzone(self):
        table = {
            'A': 'Subzone A',
            'B': 'Subzone B',
            'C': 'Subzone C',
            'D': 'Subzone D',
            'E': 'Subzone E',
            'O': 'Treeless Oceanic Boreal',
            'FT': 'Forest-Tundra Transition',
            'BO': 'Boreal',
        }
        val_counts = self._get_val_counts('SUBZONE')
        return ','.join(_translate(val_counts, table).keys())

    def _get_mosses(self):
        val_counts = self._get_val_counts('MOSS_IDENT')
        return str(val_counts)

    def _get_liverworts(self):
        val_counts = self._get_val_counts('LIV_IDENT')
        return str(val_counts)

    def _get_liches(self):
        val_counts = self._get_val_counts('LICH_IDENT')
        return str(val_counts)

    def _get_vascular(self):
        table = {
            1: 'Highest',
            2: 'High',
            3: 'High but incomplete',
            4: 'Moderate',
            5: 'Moderate and incomplete',
            6: 'Low',
        }
        val_counts = self._get_val_counts('FLOR_QUAL')
        return str(_translate(val_counts, table))

    def _get_cryptogam(self):
        table = {
            1: 'Highest',
            2: 'High',
            3: 'High but incomplete',
            4: 'Moderate',
            5: 'Moderate and incomplete',
            6: 'Low',
        }
        val_counts = self._get_val_counts('CRYP_QUAL')
        return str(_translate(val_counts, table))
