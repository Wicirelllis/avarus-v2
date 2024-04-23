from django.urls import path

from . import views

urlpatterns = [
    path('', views.AuthorsView, name='authors'),
    path('<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
]
