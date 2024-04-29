from django.urls import path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('', views.DatasetsView, name='datasets'),
    path('<int:pk>', views.DatasetDetailView.as_view(), name='dataset-detail'),
    path('access-request', views.DatasetRequestFormView.as_view(), name='dataset-request-form'),
    path('access-request-complete', TemplateView.as_view(template_name='datasets/dataset_request_done.html'), name='dataset-request-done'),
]
