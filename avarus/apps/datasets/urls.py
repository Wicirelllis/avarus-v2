from django.urls import path

from . import views

urlpatterns = [
    path('', views.DatasetsView, name='datasets'),
    path('<int:pk>', views.DatasetDetailView.as_view(), name='dataset-detail'),
]
