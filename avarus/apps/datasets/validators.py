import pandas as pd
from django.core.exceptions import ValidationError


def env_validator(value):
    ''' Check that env excel file can be properly read and parsed '''
    try:
        df = pd.read_excel(value, header=None, dtype={'REGION': str})
    except:
        raise ValidationError('Can not open excel file. Please make sure you uploading excel file.')
    names = ('RELEVE_NR', 'FIELD_NR')
    for name in names:
        if name not in df.values.flatten():
            raise ValidationError(f'{name} is not found in the file. Please make sure you uploading correct excel file.')
