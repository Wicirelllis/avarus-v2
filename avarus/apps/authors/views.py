from django.shortcuts import render
from django.views import generic

from .models import Author

def AuthorsView(request):
    authors = Author.objects.all()
    return render(request, 'authors/authors.html', {'authors': authors})

class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'authors/author_detail.html'
