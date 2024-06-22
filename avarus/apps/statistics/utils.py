import re
from typing import Iterable

import pandas as pd
from apps.datasets.models import Dataset
from apps.datasets.utils import read_env, read_spp
from django.db.models.query import QuerySet


def _normalize(s: str) -> str:
    ''' Pad numbers in string with zeros so alphabetical sort will work as natural sort '''
    return ''.join([i.zfill(8) if i.isdecimal() else i for i in re.split(r'([0-9]+)', s)])


def get_available_datasets(user):
    return (
        Dataset.objects.filter(status='pu').exclude(in_preparation=True).distinct() |
        Dataset.objects.filter(available_to=user).exclude(in_preparation=True).distinct()
    )


def make_choices(iter: QuerySet | Iterable[str], sort: bool = True) -> tuple[str, str]:
    ''' Create tuple of pairs of choices for form. '''
    if isinstance(iter, QuerySet):
        result = tuple((str(i.pk), str(i)) for i in iter)
    else:
        result = tuple((str(i), str(i)) for i in iter)
    return sorted(result, key=lambda x: _normalize(x[1])) if sort else result


def get_spp_df_by_id(id: int | str) -> pd.DataFrame:
    dataset = Dataset.objects.filter(id=id).first()
    return read_spp(dataset.spp.path)


def get_env_df_by_id(id: int | str) -> pd.DataFrame:
    dataset = Dataset.objects.filter(id=id).first()
    return read_env(dataset.env.path)
