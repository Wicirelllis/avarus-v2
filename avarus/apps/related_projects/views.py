from django.shortcuts import render
from django.views import generic

from .models import RelatedProject


def RelatedProjectssView(request):
    related_projects = RelatedProject.objects.all()
    return render(request, 'related_projects/related_projects.html', {'related_projects': related_projects})


class RelatedProjectDetailView(generic.DetailView):
    model = RelatedProject
    template_name = 'related_projects/related_project_detail.html'
