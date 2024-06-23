"""from django.shortcuts import render
from .models import Data
import folium
from folium import plugins
# Create your views here.


def index(request):
    data = Data.objects.all()
    data_list = Data.objects.values_list('latitude', 'longitude', 'population')

    map1 = folium.Map(location=[19, -12],
                      tiles='CartoDB Dark_Matter', zoom_start=2)

    plugins.HeatMap(data_list).add_to(map1)
    plugins.Fullscreen(position='topright').add_to(map1)
    map1 = map1._repr_html_()
    context = {
        'map1': map1
    }
    return render(request, 'dashboard/index.html', context)"""

##affichage des country
"""from django.shortcuts import render
from .models import Data
import folium
from folium.plugins import MarkerCluster

# Create your views here.

def index(request):
    data = Data.objects.all()
    data_list = Data.objects.values_list('latitude', 'longitude', 'population', 'country')

    map1 = folium.Map(location=[19, -12], tiles='CartoDB Dark_Matter', zoom_start=2)

    marker_cluster = MarkerCluster().add_to(map1)

    for lat, lon, population, country in data_list:
        folium.Marker(
            location=[lat, lon],
            popup=f'Country: {country}<br>Population: {population}',
        ).add_to(marker_cluster)

    folium.plugins.Fullscreen(position='topright').add_to(map1)
    map1 = map1._repr_html_()

    context = {
        'map1': map1
    }
    return render(request, 'dashboard/index.html', context) """""



##affichage des ecoles

from django.shortcuts import render
from .models import Ecoles  # Importez le modèle Ecoles au lieu de Data
import folium
from folium.plugins import MarkerCluster

def index(request):
    ecoles = Ecoles.objects.all()  # Récupérez toutes les écoles depuis le modèle Ecoles
    ecoles_list = Ecoles.objects.values_list('lat', 'long', 'name')  # Liste des écoles avec latitude, longitude et nom

    map1 = folium.Map(location=[19, -12], tiles='CartoDB Dark_Matter', zoom_start=2)

    marker_cluster = MarkerCluster().add_to(map1)

    for lat, lon, name in ecoles_list:
        folium.Marker(
            location=[lat, lon],
            popup=f'Ecole: {name}',
        ).add_to(marker_cluster)

    folium.plugins.Fullscreen(position='topright').add_to(map1)
    map1 = map1._repr_html_()

    context = {
        'map1': map1
    }
    return render(request, 'dashboard/index.html', context)
