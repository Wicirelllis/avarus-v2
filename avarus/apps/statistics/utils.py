from typing import Iterable

import pandas as pd
from apps.datasets.models import Dataset
from apps.datasets.utils import _read_env, _read_spp
from django.db.models.query import QuerySet


def _get_available_datasets(user):
    return (
        Dataset.objects.filter(status='pu').exclude(in_preparation=True).distinct() |
        Dataset.objects.filter(available_to=user).exclude(in_preparation=True).distinct()
    )


def _choices(iter: QuerySet | Iterable[str], sort: bool = True) -> tuple[str, str]:
    ''' Create tuple of pairs of choices for form. '''
    if isinstance(iter, QuerySet):
        result = tuple((str(i.pk), str(i)) for i in iter)
    else:
        result = tuple((str(i), str(i)) for i in iter)
    return sorted(result, key=lambda x: x[1]) if sort else result


def _get_spp_df_by_id(id: int | str) -> pd.DataFrame:
    dataset = Dataset.objects.filter(id=id).first()
    return _read_spp(dataset.spp.path)


def _get_env_df_by_id(id: int | str) -> pd.DataFrame:
    dataset = Dataset.objects.filter(id=id).first()
    return _read_env(dataset.env.path)
