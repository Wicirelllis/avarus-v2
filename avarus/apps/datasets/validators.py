import pandas as pd
from django.core.exceptions import ValidationError
from apps.datasets.utils import read_env, read_spp

def env_validator(value):
    ''' Check that env excel file can be properly read and parsed '''
    if read_env(value) is None:
        raise ValidationError('Could not parse an excel file.')

def spp_validator(value):
    ''' Check that spp excel file can be properly read and parsed '''
    if read_spp(value) is None:
        raise ValidationError('Could not parse an excel file.')
