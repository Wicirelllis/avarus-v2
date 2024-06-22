''' This module contains auxiliary functions that parse xlsx dataset file to extract data '''
from contextlib import suppress

import dateutil
import numpy as np
import pandas as pd
from apps.datasets import species
from apps.datasets.utils import read_env, read_spp
from django.utils.translation import gettext_lazy as _

from typing import Any


def _format_data(data: dict[str, float], print_vals: bool = True) -> str:
    if len(data) > 1:
        if print_vals:
            return '; '.join((f'{k} ({100 * v:.0f} %)' for k, v in data.items()))
        else:
            return '; '.join(data)
    else:
        return next(iter(data))


def _dict_zfill_keys(data: dict[str, Any], width: int) -> dict:
    ''' Pad str keys with zeros '''
    return {str(k).zfill(width): v for k, v in data.items()}

def _dict_sort_by_vals(data: dict) -> dict:
    ''' Sort dict by values '''
    return dict(sorted(data.items(), key=lambda x: x[1]))


def _format_value_counts(df: pd.DataFrame, field: str, trans_table: dict = None, percent: bool = True, sort: bool = False) -> str:
    """
    Format string with 2 most common values
    
    :param df: datafram
    :param field: field
    :param trans_table: translatation table
    :param percent: display frequencies
    :param sort: sort by frequencies whne True

    Example: 'Subzone B (25 %), Subzone D (19 %)'
    """
    vals = df[field].fillna('No data').value_counts(normalize=True, dropna=False).nlargest(2).to_dict()
    if trans_table is not None:
        vals = _translate(vals, trans_table)
    if sort:
        vals = dict(sorted(vals.items(), key=lambda x: x[1]))
    if percent:
        return ', '.join((f'{k} ({100 * v:.0f} %)' for k, v in vals.items()))
    else:
        return ', '.join((f'{k}' for k in vals))

def _get_val_counts(df: pd.DataFrame, field: str) -> dict:
    ''' Return a dict containing counts of unique values '''
    return df[field].fillna('No data').value_counts(dropna=False).to_dict()

def _calc_completeness(df: pd.DataFrame, fields: list[str]) -> dict:
    ''' Calculate copleteness (percent of cell with data) for each column of dataframe '''
    res = (100 * df.filter(fields).notna().sum() / df.shape[0]).round().astype(int).to_dict()
    diff = set(fields) - set(res)
    if diff:
        res.update({k: 0 for k in diff})
    return res

def _translate(data: list | dict, table: dict) -> list | dict:
    ''' Replace elements of the list using translation table '''
    def _replace(s: str) -> str:
        if '/' in s:
            l = s.split('/')
            if all((i in table for i in l)):
                return ' / '.join((table[i] for i in l))
        return table.get(s, s)

    if isinstance(data, list):
        return [_replace(i) for i in data]
    elif isinstance(data, dict):
        return {_replace(k): v for k, v in data.items()}


class ParseDataset:
    def __init__(self, dataset) -> None:
        self.dataset = dataset
        self.df: pd.DataFrame = read_env(dataset.env.path)
        self.spp: pd.DataFrame = read_spp(dataset.spp.path)
        self._fix_header()

    def fill_fields(self, fields: list[str]):
        ''' Fill dataset's attributes '''
        for field in fields:
            with suppress(Exception):
                setattr(self.dataset, field, getattr(self, f'_get_{field}')())

    def _fix_header(self):
        ''' Rename column names for consistency '''
        table = {
            'SITE_MOIST': 'SITE_MST',
        }
        self.df.rename(str.strip, axis='columns', inplace=True)
        self.df.rename(table, axis='columns', inplace=True)

    # chart data fields
    def _get_disturban(self):
        data = _get_val_counts(self.df, 'DISTURBAN')
        table = {
            'DIS': 'Disturbed',
            'NAT': 'Natural',
        }
        return {
            'title': 'Disturbance',
            'labels': _translate(list(data.keys()), table),
            'data': list(data.values()),
        }

    def _get_position(self):
        data = _get_val_counts(self.df, 'POSITION')
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
        data = _get_val_counts(self.df, 'SOIL_TEXT')
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
        data = _calc_completeness(self.df, fields)
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
        data = _calc_completeness(self.df, fields)
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
        data = _calc_completeness(self.df, fields)
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
        return len(self.df)

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
        # return _format_value_counts(self.df, 'COVERSCALE', table, False, True)
        data = self.df['COVERSCALE'].fillna('No data').value_counts(normalize=True, dropna=False).nlargest(2).to_dict()
        data = _dict_zfill_keys(data, 2)
        data = _translate(data, table)
        return _format_data(data, print_vals=False)

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
        # return _format_value_counts(self.df, 'REGION', table, False, True)
        data = self.df['REGION'].fillna('No data').value_counts(normalize=True, dropna=False).nlargest(2).to_dict()
        data = _dict_zfill_keys(data, 3)
        data = _translate(data, table)
        return _format_data(data, print_vals=False)

    def _get_location(self):
        # return _format_value_counts(self.df, 'LOCATION', None, False, True)
        data = self.df['LOCATION'].fillna('No data').value_counts(normalize=True, dropna=False).nlargest(2).to_dict()
        return _format_data(data, print_vals=False)

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
        # return _format_value_counts(self.df, 'SUBZONE', table, True, True)
        data = self.df['SUBZONE'].fillna('No data').value_counts(normalize=True, dropna=False).nlargest(2).to_dict()
        data = _translate(data, table)
        return _format_data(data, print_vals=True)

    def _get_mosses(self):
        data = self.df['MOSS_IDENT'].value_counts(normalize=True, dropna=False).get('Y', 0)
        return f'{100 * data:.0f} %'

    def _get_liverworts(self):
        data = self.df['LIV_IDENT'].value_counts(normalize=True, dropna=False).get('Y', 0)
        return f'{100 * data:.0f} %'

    def _get_liches(self):
        data = self.df['LICH_IDENT'].value_counts(normalize=True, dropna=False).get('Y', 0)
        return f'{100 * data:.0f} %'

    def _get_vascular(self):
        table = {
            1: 'Highest',
            2: 'High',
            3: 'High but incomplete',
            4: 'Moderate',
            5: 'Moderate and incomplete',
            6: 'Low',
        }
        data = self.df['FLOR_QUAL'].fillna('No data').value_counts(normalize=True, dropna=False).nlargest(2).to_dict()
        data = _translate(data, table)
        return _format_data(data, print_vals=True)

    def _get_cryptogam(self):
        table = {
            1: 'Highest',
            2: 'High',
            3: 'High but incomplete',
            4: 'Moderate',
            5: 'Moderate and incomplete',
            6: 'Low',
        }
        data = self.df['CRYP_QUAL'].fillna('No data').value_counts(normalize=True, dropna=False).nlargest(2).to_dict()
        data = _translate(data, table)
        return _format_data(data, print_vals=True)

    def _get_latitude(self):
        data = self.df['LATITUDE'].dropna().astype(float)
        if len(data) == 0:
            return
        return (np.max(data) + np.min(data)) / 2.

    def _get_longitude(self):
        data = self.df['LONGITUDE'].dropna().astype(float)
        if len(data) == 0:
            return
        data = data.apply(lambda x: x + 360 if x < 0 else x)
        res = (np.max(data) + np.min(data)) / 2.
        # make sure res in (-180; 180]
        res %= 360
        if res > 180:
            res -= 360
        return res

    def _get_species_total(self):
        return self.spp['PASL TAXON SCIENTIFIC NAME NO AUTHOR(S)'].count()

    def _get_species_liches(self):
        return self.spp['PASL TAXON SCIENTIFIC NAME NO AUTHOR(S)'].isin(species.LICHEN).sum()

    def _get_species_liverworts(self):
        return self.spp['PASL TAXON SCIENTIFIC NAME NO AUTHOR(S)'].isin(species.LIVERWORT).sum()

    def _get_species_mosses(self) -> int:
        return self.spp['PASL TAXON SCIENTIFIC NAME NO AUTHOR(S)'].isin(species.MOSS).sum()

    def _get_species_vascular(self):
        return self.spp['PASL TAXON SCIENTIFIC NAME NO AUTHOR(S)'].isin(species.VASCULAR).sum()

    def _get_species_unknown(self):
        return self._get_species_total() - self._get_species_liches() - self._get_species_liverworts() - self._get_species_mosses() - self._get_species_vascular()
