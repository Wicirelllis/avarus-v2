''' This module contains auxiliary functions that parse xlsx dataset file to extract data '''
import pandas as pd
import json
import numpy as np
import dateutil

class ParseDataset:
    def __init__(self, dataset) -> None:
        self.dataset = dataset
        self.df: pd.DataFrame = self.read_excel()

    def read_excel(self) -> pd.DataFrame:
        path = self.dataset.env.path
        df = pd.read_excel(path, header=None, dtype={'REGION': str})
        for row_idx in range(df.shape[0]):
            if df.iloc[row_idx, 0] == 'RELEVE_NR':
                new_header = df.iloc[row_idx]
                df = df[row_idx + 1:]
                df.columns = new_header
                return df

    def fill_fields(self, fields: list[str]):
        ...

    def _fill_n_plots(self):
        self.dataset.n_plots = len(self.df.loc[:, 'SOIL_TEXT'])

    def _fill_disturban(self):
        self.dataset.disturban = json.dumps(self.df['DISTURBAN'].fillna('NONE').value_counts(dropna=False).to_dict())

    def _fill_position(self):
        self.dataset.position = json.dumps(self.df['POSITION'].fillna('NONE').value_counts(dropna=False).to_dict())

    def _fill_soil_text(self):
        self.dataset.soil_text = json.dumps(self.df['SOIL_TEXT'].fillna('NONE').value_counts(dropna=False).to_dict())

    def _fill_year(self):
        self.dataset.year = int(np.floor(self.df['DATE'].apply(lambda x: dateutil.parser.parse(str(x)).year).mean()))

    def _fill_coverscale(self):
        translate = {
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
        val_counts = self.df['COVERSCALE'].replace(translate).fillna('NONE').value_counts(dropna=False).to_dict()
        self.dataset.coverscale = ','.join(val_counts.keys())

    def _fill_region(self):
        translate = {
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
        val_counts = self.df['REGION'].fillna(0).replace(translate).value_counts(dropna=False).to_dict()
        self.dataset.region = ','.join(val_counts.keys())

    def _fill_location(self):
        val_counts = self.df['LOCATION'].fillna('NONE').value_counts(dropna=False).to_dict()
        self.dataset.location = ','.join(val_counts.keys())
    
    def _fill_subzone(self):
        translate = {
            'A': 'Subzone A',
            'B': 'Subzone B',
            'C': 'Subzone C',
            'D': 'Subzone D',
            'E': 'Subzone E',
            'O': 'Treeless Oceanic Boreal',
            'FT': 'Forest-Tundra Transition',
            'BO': 'Boreal',
        }
        val_counts = self.df['SUBZONE'].replace(translate).fillna('NONE').value_counts(dropna=False).to_dict()
        self.dataset.subzone = ','.join(val_counts.keys())

    def _fill_mosses(self):
        val_counts = self.df['MOSS_IDENT'].fillna('NONE').value_counts(dropna=False).to_dict()
        self.dataset.mosses = str(val_counts)

    def _fill_liverworts(self):
        val_counts = self.df['LIV_IDENT'].fillna('NONE').value_counts(dropna=False).to_dict()
        self.dataset.liverworts = str(val_counts)

    def _fill_liches(self):
        val_counts = self.df['LICH_IDENT'].fillna('NONE').value_counts(dropna=False).to_dict()
        self.dataset.liches = str(val_counts)

    def _fill_vascular(self):
        translate = {
            1: 'Highest',
            2: 'High',
            3: 'High but incomplete',
            4: 'Moderate',
            5: 'Moderate and incomplete',
            6: 'Low',
        }
        val_counts = self.df['FLOR_QUAL'].fillna('NONE').replace(translate).value_counts(dropna=False).to_dict()
        self.dataset.vascular = str(val_counts)

    def _fill_cryptogam(self):
        translate = {
            1: 'Highest',
            2: 'High',
            3: 'High but incomplete',
            4: 'Moderate',
            5: 'Moderate and incomplete',
            6: 'Low',
        }
        val_counts = self.df['CRYP_QUAL'].fillna('NONE').replace(translate).value_counts(dropna=False).to_dict()
        self.dataset.cryptogam = str(val_counts)
