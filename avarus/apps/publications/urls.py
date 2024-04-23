from django.urls import path

from . import views

urlpatterns = [
    path('', views.PublicationsView, name='publications'),
    path('<int:pk>', views.PublicationDetailView.as_view(), name='publication-detail'),
]
