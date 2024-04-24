from json import dumps

from apps.map_locations.models import MapLocation
from django.shortcuts import render


def HomeView(request):
    locations = MapLocation.objects.all()
    data = [dict()]
    for loc in locations:
        placemark = {
            'center': [loc.dataset.latitude, loc.dataset.longitude],
            'name': f'{loc.name}',
            'ContentHeader': [f'<a href="{loc.dataset.get_absolute_url()}">{loc.name}</a><br>{', '.join(str(a) for a in loc.authors.all())}<hr>'],
            'ContentBody': [f'<img src="/media/{loc.dataset.image.name}" class="img-fluid p-2" alt="Image">'],
            'ContentFooter': [f'{loc.dataset.n_plots} plots'],
            'hint': [f'{loc.name}'],
        }
        data.insert(0, placemark)

    json_data = dumps(data)
    return render(request, 'home.html', {'json_data': json_data, 'locations': locations})

def AboutView(request):
    return render(request, 'about.html')
