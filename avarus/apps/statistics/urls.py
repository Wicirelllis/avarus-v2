from django.urls import path

from . import views

urlpatterns = [
    path('', views.StatisticsView, name='statistics'),
    path('correlation-analysis', views.correlation_analysis_view, name='correlation-analysis'),
    path('correlation-analysis-result', views.correlation_analysis_result_view, name='correlation-analysis-result'),
    path('filter-env', views.filter_env_view, name='filter-env'),
    path('filter-env-result', views.filter_env_result_view, name='filter-env-result'),
    path('filter-spp', views.filter_spp_view, name='filter-spp'),
    path('filter-spp-result', views.filter_spp_result_view, name='filter-spp-result'),
    path('species-analysis', views.species_analysis_view, name='species-analysis'),
    path('species-analysis-result', views.species_analysis_result_view, name='species-analysis-result'),
    path('dataset-species-analysis', views.dataset_species_analysis_view, name='dataset-species-analysis'),
    path('dataset-species-analysis-result', views.dataset_species_analysis_result_view, name='dataset-species-analysis-result'),
]
