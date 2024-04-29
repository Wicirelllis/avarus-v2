from apps.datasets.forms import DatasetRequestForm
from django.shortcuts import redirect, render
from django.views import generic

from .models import Dataset


def DatasetsView(request):
    datasets = Dataset.objects.all()
    return render(request, 'datasets.html', {'datasets': datasets})

class DatasetDetailView(generic.DetailView):
    model = Dataset
    template_name = 'dataset_detail.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            initial = {
                'name': str.strip(f'{self.request.user.last_name} {self.request.user.first_name}') or '',
                'organization': self.request.user.profile.organization,
                'position': self.request.user.profile.position,
                'email': self.request.user.email,
                'dataset': self.get_object(),
                'user': self.request.user,
            }
        else:
            initial = None
        form = DatasetRequestForm(initial=initial)
        data['request_form'] = form
        return data


class DatasetRequestFormView(generic.View):
    def post(self, request):
        form = DatasetRequestForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('dataset-request-done')

    def get(self, request):
        return redirect('/')
