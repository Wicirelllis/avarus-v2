from django.urls import path

from . import views

urlpatterns = [
    path('', views.RelatedProjectssView, name='related-projects'),
    path('<int:pk>', views.RelatedProjectDetailView.as_view(), name='related-project-detail'),
]
