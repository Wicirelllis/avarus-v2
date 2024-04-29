from django.shortcuts import render
from django.views import generic

from .models import Publication


def PublicationsView(request):
    publications = Publication.objects.all()
    return render(request, 'publications/publications.html', {'publications': publications})


class PublicationDetailView(generic.DetailView):
    model = Publication
    template_name = 'publications/publication_detail.html'
