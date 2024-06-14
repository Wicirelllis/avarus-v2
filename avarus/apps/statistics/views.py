from apps.datasets.models import Dataset
from apps.statistics.forms import ChoiceFieldForm, MultipleChoiceFieldForm
from apps.statistics.statistics import correlation_analysis, pca_analysis, factor_analysis, cluster_analysis
from apps.statistics.utils import (make_choices, get_available_datasets,
                                   get_env_df_by_id, get_spp_df_by_id)
from django import forms
from django.shortcuts import redirect, render


def StatisticsView(request):
    return render(request, 'statistics/statistics.html')


def correlation_analysis_view(request):
    def _make_form_dataset(data = None):
        datasets = get_available_datasets(request.user)
        choices = make_choices(datasets)
        return ChoiceFieldForm(data, field='dataset', choices=choices, widget=forms.RadioSelect)

    def _make_form_cols(data = None):
        id = request.session['correlation_analysis']['dataset_id']
        dataset = Dataset.objects.filter(id=id).first()
        choices_data = make_choices(dataset.get_spp_cols(True, True))
        return MultipleChoiceFieldForm(data, field='cols', choices=choices_data, widget=forms.CheckboxSelectMultiple)

    if request.method == 'POST':
        if 'dataset' in request.POST:
            form_dataset = _make_form_dataset(request.POST)
            if form_dataset.is_valid():
                request.session['correlation_analysis'].update({'dataset_id': request.POST['dataset']})
                form_cols = _make_form_cols()
                return render(request, 'statistics/correlation_analysis.html', {'form': form_cols})
            else:
                return render(request, 'statistics/correlation_analysis.html', {'form': form_dataset})
        if 'cols' in request.POST:
            form_cols = _make_form_cols(request.POST)
            if form_cols.is_valid():
                request.session['correlation_analysis'].update({'cols': request.POST.getlist('cols')})
                return redirect('correlation-analysis-result')
            else:
                return render(request, 'statistics/correlation_analysis.html', {'form': form_cols})
    else:
        request.session['correlation_analysis'] = {}
        form_dataset = _make_form_dataset()
        return render(request, 'statistics/correlation_analysis.html', {'form': form_dataset})

def correlation_analysis_result_view(request):
    params = request.session.get('correlation_analysis')
    df = get_spp_df_by_id(params['dataset_id'])
    cols = params['cols']
    result = correlation_analysis(df, cols)
    return render(request, 'statistics/correlation_analysis_result.html', {'result': result})



def pca_analysis_view(request):
    def _make_form_dataset(data = None):
        datasets = get_available_datasets(request.user)
        choices = make_choices(datasets)
        return ChoiceFieldForm(data, field='dataset', choices=choices, widget=forms.RadioSelect)

    def _make_form_cols(data = None):
        id = request.session['pca_analysis']['dataset_id']
        dataset = Dataset.objects.filter(id=id).first()
        choices_data = make_choices(dataset.get_spp_cols(True, True))
        return MultipleChoiceFieldForm(data, field='cols', choices=choices_data, widget=forms.CheckboxSelectMultiple)

    if request.method == 'POST':
        if 'dataset' in request.POST:
            form_dataset = _make_form_dataset(request.POST)
            if form_dataset.is_valid():
                request.session['pca_analysis'].update({'dataset_id': request.POST['dataset']})
                form_cols = _make_form_cols()
                return render(request, 'statistics/pca_analysis.html', {'form': form_cols})
            else:
                return render(request, 'statistics/pca_analysis.html', {'form': form_dataset})
        if 'cols' in request.POST:
            form_cols = _make_form_cols(request.POST)
            if form_cols.is_valid():
                request.session['pca_analysis'].update({'cols': request.POST.getlist('cols')})
                return redirect('pca-analysis-result')
            else:
                return render(request, 'statistics/pca_analysis.html', {'form': form_cols})
    else:
        request.session['pca_analysis'] = {}
        form_dataset = _make_form_dataset()
        return render(request, 'statistics/pca_analysis.html', {'form': form_dataset})

def pca_analysis_result_view(request):
    params = request.session.get('pca_analysis')
    df = get_spp_df_by_id(params['dataset_id'])
    cols = params['cols']
    result = pca_analysis(df, cols)
    return render(request, 'statistics/pca_analysis_result.html', {'result': result})



def factor_analysis_view(request):
    def _make_form_dataset(data = None):
        datasets = get_available_datasets(request.user)
        choices = make_choices(datasets)
        return ChoiceFieldForm(data, field='dataset', choices=choices, widget=forms.RadioSelect)

    def _make_form_cols(data = None):
        id = request.session['factor_analysis']['dataset_id']
        dataset = Dataset.objects.filter(id=id).first()
        choices_data = make_choices(dataset.get_spp_cols())
        return MultipleChoiceFieldForm(data, field='cols', choices=choices_data, widget=forms.CheckboxSelectMultiple)

    if request.method == 'POST':
        if 'dataset' in request.POST:
            form_dataset = _make_form_dataset(request.POST)
            if form_dataset.is_valid():
                request.session['factor_analysis'].update({'dataset_id': request.POST['dataset']})
                form_cols = _make_form_cols()
                return render(request, 'statistics/factor_analysis.html', {'form': form_cols})
            else:
                return render(request, 'statistics/factor_analysis.html', {'form': form_dataset})
        if 'cols' in request.POST:
            form_cols = _make_form_cols(request.POST)
            if form_cols.is_valid():
                request.session['factor_analysis'].update({'cols': request.POST.getlist('cols')})
                return redirect('factor-analysis-result')
            else:
                return render(request, 'statistics/factor_analysis.html', {'form': form_cols})
    else:
        request.session['factor_analysis'] = {}
        form_dataset = _make_form_dataset()
        return render(request, 'statistics/factor_analysis.html', {'form': form_dataset})

def factor_analysis_result_view(request):
    params = request.session.get('factor_analysis')
    df = get_spp_df_by_id(params['dataset_id'])
    cols = params['cols']
    result = factor_analysis(df, cols)
    return render(request, 'statistics/factor_analysis_result.html', {'result': result})



def cluster_analysis_view(request):
    def _make_form_dataset(data = None):
        datasets = get_available_datasets(request.user)
        choices = make_choices(datasets)
        return ChoiceFieldForm(data, field='dataset', choices=choices, widget=forms.RadioSelect)

    def _make_form_cols(data = None):
        id = request.session['cluster_analysis']['dataset_id']
        dataset = Dataset.objects.filter(id=id).first()
        choices_data = make_choices(dataset.get_spp_cols())
        return MultipleChoiceFieldForm(data, field='cols', choices=choices_data, widget=forms.CheckboxSelectMultiple)

    if request.method == 'POST':
        if 'dataset' in request.POST:
            form_dataset = _make_form_dataset(request.POST)
            if form_dataset.is_valid():
                request.session['cluster_analysis'].update({'dataset_id': request.POST['dataset']})
                form_cols = _make_form_cols()
                return render(request, 'statistics/cluster_analysis.html', {'form': form_cols})
            else:
                return render(request, 'statistics/cluster_analysis.html', {'form': form_dataset})
        if 'cols' in request.POST:
            form_cols = _make_form_cols(request.POST)
            if form_cols.is_valid():
                request.session['cluster_analysis'].update({'cols': request.POST.getlist('cols')})
                return redirect('cluster-analysis-result')
            else:
                return render(request, 'statistics/cluster_analysis.html', {'form': form_cols})
    else:
        request.session['cluster_analysis'] = {}
        form_dataset = _make_form_dataset()
        return render(request, 'statistics/cluster_analysis.html', {'form': form_dataset})

def cluster_analysis_result_view(request):
    params = request.session.get('cluster_analysis')
    df = get_spp_df_by_id(params['dataset_id'])
    cols = params['cols']
    result = cluster_analysis(df, cols)
    return render(request, 'statistics/cluster_analysis_result.html', {'result': result})




def filter_spp_view(request):
    def _make_form_dataset(data = None):
        datasets = get_available_datasets(request.user)
        choices = make_choices(datasets)
        return ChoiceFieldForm(data, field='dataset', choices=choices, widget=forms.RadioSelect)

    def _make_form_rows(data = None):
        id = request.session['filter_spp']['dataset_id']
        dataset = Dataset.objects.filter(id=id).first()
        choices = make_choices(dataset.get_spp_rows())
        return MultipleChoiceFieldForm(data, field='rows', choices=choices, widget=forms.CheckboxSelectMultiple)

    if request.method == 'POST':
        if 'dataset' in request.POST:
            form_dataset = _make_form_dataset(request.POST)
            if form_dataset.is_valid():
                request.session['filter_spp'].update({'dataset_id': request.POST['dataset']})
                form_rows = _make_form_rows()
                return render(request, 'statistics/filter_spp.html', {'form': form_rows})
            else:
                return render(request, 'statistics/filter_spp.html', {'form': form_dataset})
        if 'rows' in request.POST:
            form_rows = _make_form_rows(request.POST)
            if form_rows.is_valid():
                request.session['filter_spp'].update({'rows': request.POST.getlist('rows')})
                return redirect('filter-spp-result')
            else:
                return render(request, 'statistics/filter_spp.html', {'form': form_rows})
    else:
        request.session['filter_spp'] = {}
        form_dataset = _make_form_dataset()
        return render(request, 'statistics/filter_spp.html', {'form': form_dataset})
    
def filter_spp_result_view(request):
    params = request.session.get('filter_spp')
    df = get_spp_df_by_id(params['dataset_id'])
    rows: list[str] = params['rows']

    result = df.loc[df['PASL TAXON SCIENTIFIC NAME NO AUTHOR(S)'].isin(rows)]
    file_url = '/media/tmp/filter_spp.xlsx'
    result.to_excel(f'/avarus{file_url}', index=False)
    return render(request, 'statistics/filter_spp_result.html', {'result': result, 'file_url': file_url})



def filter_env_view(request):
    def _make_form_dataset(data = None):
        datasets = get_available_datasets(request.user)
        choices = make_choices(datasets)
        return ChoiceFieldForm(data, field='dataset', choices=choices, widget=forms.RadioSelect)
    
    def _make_form_col(data=None):
        dataset_id = request.session['filter_env']['dataset_id']
        dataset = Dataset.objects.filter(id=dataset_id).first()
        choices = make_choices(dataset.get_env_cols(True))
        return ChoiceFieldForm(data, field='col', choices=choices, widget=forms.RadioSelect)

    def _make_form_values(data = None):
        dataset_id = request.session['filter_env']['dataset_id']
        dataset = Dataset.objects.filter(id=dataset_id).first()
        col = request.session['filter_env']['col']
        choices = make_choices(dataset.get_env_col_values(col))
        return MultipleChoiceFieldForm(data, field='values', choices=choices, widget=forms.CheckboxSelectMultiple)
    
    if request.method == 'POST':
        if 'dataset' in request.POST:
            form_dataset = _make_form_dataset(request.POST)
            if form_dataset.is_valid():
                request.session['filter_env'].update({'dataset_id': request.POST['dataset']})
                form_col = _make_form_col()
                return render(request, 'statistics/filter_env.html', {'form': form_col})
            else:
                return render(request, 'statistics/filter_env.html', {'form': form_dataset})
        if 'col' in request.POST:
            form_col = _make_form_col(request.POST)
            if form_col.is_valid():
                request.session['filter_env'].update({'col': request.POST['col']})
                form_values = _make_form_values()
                return render(request, 'statistics/filter_env.html', {'form': form_values})
            else:
                return render(request, 'statistics/filter_env.html', {'form': form_col})
        if 'values' in request.POST:
            form_values = _make_form_values(request.POST)
            if form_values.is_valid():
                request.session['filter_env'].update({'values': request.POST.getlist('values')})
                return redirect('filter-env-result')
            else:
                return render(request, 'statistics/filter_env.html', {'form': form_values})
    else:
        request.session['filter_env'] = {}
        form_dataset = _make_form_dataset()
        return render(request, 'statistics/filter_env.html', {'form': form_dataset})

def filter_env_result_view(request):
    params = request.session.get('filter_env')
    df = get_env_df_by_id(params['dataset_id'])
    col = params['col']
    values = params['values']

    result = df.loc[df[col].astype('str').isin(values)]
    file_url = '/media/tmp/filter_env.xlsx'
    result.to_excel(f'/avarus{file_url}', index=False)
    return render(request, 'statistics/filter_env_result.html', {'file_url': file_url})



def species_analysis_view(request):
    def _make_form_group(data = None):
        choices = (
            ('total', 'Total plants species'),
            ('liches', 'Lichens'),
            ('liverworts', 'Liverworts'),
            ('mosses', 'Mosses'),
            ('vascular', 'Vascular plants'),
            ('unknown', 'Unknown'),
        )
        return ChoiceFieldForm(data, field='group', choices=choices, widget=forms.RadioSelect)

    if request.method == 'POST':
        if 'group' in request.POST:
            form_group = _make_form_group(request.POST)
            if form_group.is_valid():
                request.session['species_analysis'].update({'group': request.POST['group']})
                return redirect('species-analysis-result')
            else:
                return render(request, 'statistics/species_analysis.html', {'form': form_group})
    else:
        request.session['species_analysis'] = {}
        form_group = _make_form_group()
        return render(request, 'statistics/species_analysis.html', {'form': form_group})


def species_analysis_result_view(request):
    params = request.session.get('species_analysis')
    field = f'species_{params['group']}'
    datasets = Dataset.objects.all().order_by('number')
    result = [
        {
            'name': str(i),
            'count': getattr(i, field),
            'percent': round(100 * getattr(i, field) / i.species_total) if i.species_total != 0 else 0,
            'url': i.get_absolute_url(),
        } for i in datasets
    ]
    return render(request, 'statistics/species_analysis_result.html', {'result': result})



def dataset_species_analysis_view(request):
    def _make_form_dataset(data = None):
        datasets = get_available_datasets(request.user)
        choices = make_choices(datasets)
        return ChoiceFieldForm(data, field='dataset', choices=choices, widget=forms.RadioSelect)
    
    if request.method == 'POST':
        if 'dataset' in request.POST:
            form_dataset = _make_form_dataset(request.POST)
            if form_dataset.is_valid():
                request.session['dataset_species_analysis'].update({'dataset_id': request.POST['dataset']})
                return redirect('dataset-species-analysis-result')
            else:
                return render(request, 'statistics/dataset_species_analysis.html', {'form': form_dataset})
    else:
        request.session['dataset_species_analysis'] = {}
        form_dataset = _make_form_dataset()
        return render(request, 'statistics/dataset_species_analysis.html', {'form': form_dataset})


def dataset_species_analysis_result_view(request):
    params = request.session.get('dataset_species_analysis')
    dataset = Dataset.objects.filter(id=params['dataset_id']).first()

    result = [
        {
            'name': name,
            'count': getattr(dataset, field),
            'percent': round(100 * getattr(dataset, field) / dataset.species_total),
        } for name, field in (
            ('Total', 'species_total'),
            ('Liches', 'species_liches'),
            ('Liverworts', 'species_liverworts'),
            ('Mosses', 'species_mosses'),
            ('Vascular plants', 'species_vascular'),
            ('Unknown', 'species_unknown'),
        )
    ]
    return render(request, 'statistics/dataset_species_analysis_result.html', {'result': result})
