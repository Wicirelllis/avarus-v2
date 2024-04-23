from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import gettext as _
from json import dumps

from apps.map_locations.models import MapLocation

def HomeView(request):
    new_place = MapLocation.objects.all()

    data = [{}]
    for i in range(new_place.count()):
        place = {
        "center": [float(new_place[i].latitude), float(new_place[i].longitude)],
        "name": f"{new_place[i].num}. {new_place[i].name} ({new_place[i].authors})",
        "ContentHeader":[f"<a>{new_place[i].name}</a><br><span class='description'>{new_place[i].authors}</span><hr class='hr1'/>"],
        "ContentBody": [f"<a>Location Map</a><br/><img src='../media/pictures/{new_place[i].url_photo}' height='150' width='200'><br/><br/><a id='btn-preview' type='button' class='btn btn-info'  href={ new_place[i].url_page } style='color:white;'>Open</a>"],
        "ContentFooter": [f"Number of Plots:<br/>{new_place[i].plots}"],
        "hint": [f"<div class='map__hint'>{new_place[i].name}</div>"]
        }
        data.insert(0, place)

    # locations = MapLocation.objects.extra(select={'myinteger': "CAST(substring(num FROM '^[0-9]+') AS INTEGER)"}).order_by('myinteger')
    # locations = MapLocation.objects.all()

    # data = [{}]
    # for i in range(locations.count()):
    # # for location in locations
    #     place = {
    #         "center": [float(locations[i].latitude), float(locations[i].longitude)],
    #         "name": "name",
    #         "ContentHeader":[f"<a>{locations[i].name}</a><br><span class='description'>{locations[i].authors}</span><hr class='hr1'/>"],
    #         "ContentBody": [f"<p>sad</p>"],
    #         "ContentFooter": [""],
    #         "hint": [f"<div class='map__hint'>{locations[i].name}</div>"]
    #     }
    #     data.insert(0, place)

    jsondata = dumps(data)
    return render(request, 'home.html', {'json_data': jsondata, 'locations': new_place})
    # return render(request, 'home.html')

def AboutView(request):
    return render(request, 'about.html')
