from django.shortcuts import render
from django.views import generic

from .models import Dataset

def DatasetsView(request):
    datasets = Dataset.objects.all()
    return render(request, 'datasets.html', {'datasets': datasets})

class DatasetDetailView(generic.DetailView):
    model = Dataset
    template_name = 'dataset_detail.html'
