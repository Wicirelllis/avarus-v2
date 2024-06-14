from json import dumps

from apps.map_locations.models import MapLocation
from django.shortcuts import render
from apps.feedback.forms import FeedbackForm
from django.conf import settings


def HomeView(request):
    locations = MapLocation.objects.all()
    data = []
    for loc in locations:
        if loc.dataset.in_preparation or not (loc.dataset.latitude and loc.dataset.longitude):
            continue
        placemark = {
            'center': [loc.dataset.latitude, loc.dataset.longitude],
            'name': loc.name,
            'ContentHeader': [f'<a href="{loc.dataset.get_absolute_url()}">{loc.dataset}</a><br>{', '.join(a.get_short_name() for a in loc.dataset.authors.all())}, {loc.dataset.year}<hr>'],
            'ContentBody': [f'<img src="/media/{loc.dataset.image.name}" class="img-fluid" alt="{loc.name} image" height="150" width="200">'],
            'ContentFooter': [f'{loc.dataset.n_plots} plots'],
            'hint': [loc.name],
        }
        data.append(placemark)

    json_data = dumps(data)
    return render(request, 'home.html', {'json_data': json_data, 'locations': locations, 'ya_maps_token': settings.YANDEX_MAPS_TOKEN})

def AboutView(request):
    ctx = {'feedback_form': FeedbackForm()}
    return render(request, 'about.html', ctx)

def ServicesView(request):
    return render(request, 'services.html')