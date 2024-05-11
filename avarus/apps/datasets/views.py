from apps.datasets.forms import DatasetRequestForm
from django.shortcuts import redirect, render
from django.views import generic
from django.core.mail import send_mail

from .models import Dataset
from django.conf import settings


def DatasetsView(request):
    datasets = Dataset.objects.all()
    return render(request, 'datasets/datasets.html', {'datasets': datasets})

class DatasetDetailView(generic.DetailView):
    model = Dataset
    template_name = 'datasets/dataset_detail.html'

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
            dataset_request = form.save()
            if settings.DATASET_REQUEST_SEND_EMAIL:
                send_mail(
                    f'Dataset access request from {dataset_request.user}',
                    (
                        f'User {dataset_request.user} (email: {dataset_request.email}) has requested access to dataset {dataset_request.dataset}\n\n'
                        f'Name: {dataset_request.name}\n'
                        f'Organization: {dataset_request.organization}\n'
                        f'Position: {dataset_request.position}\n\n'
                        f'Purpose:\n{dataset_request.purpose}'
                    ),
                    settings.EMAIL_HOST_USER,
                    settings.DATASET_REQUEST_EMAIL_RECIPIENTS
                )
        return redirect('dataset-request-done')

    def get(self, request):
        return redirect('/')
