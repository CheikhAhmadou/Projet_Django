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
"""""
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
    return render(request, 'dashboard/index.html', context)"""


###script  pour ajouter les basemap
"""from django.shortcuts import render
from .models import Ecoles
import folium
from folium.plugins import MarkerCluster

def index(request):
    ecoles = Ecoles.objects.all()
    ecoles_list = Ecoles.objects.values_list('lat', 'long', 'name')

    # Créer la carte de base
    map1 = folium.Map(location=[14.634328717590597, -14.940601323380719], tiles=None, zoom_start=7.40)

    # Ajouter différentes couches de tuiles
    folium.TileLayer('CartoDB Dark_Matter', name='Dark Matter').add_to(map1)
    folium.TileLayer('OpenStreetMap', name='OpenStreetMap').add_to(map1)
    folium.TileLayer('Stamen Terrain', name='Terrain').add_to(map1)
    folium.TileLayer('Stamen Toner', name='Toner').add_to(map1)
    folium.TileLayer('Stamen Watercolor', name='Watercolor').add_to(map1)

    # Créer un cluster de marqueurs
    marker_cluster = MarkerCluster(name='Cluster d\'Ecoles').add_to(map1)

    # Ajouter des marqueurs au cluster
    for lat, lon, name in ecoles_list:
        folium.Marker(
            location=[lat, lon],
            popup=f'Ecole: {name}',
        ).add_to(marker_cluster)

    # Ajouter la fonctionnalité plein écran
    folium.plugins.Fullscreen(position='topright').add_to(map1)

    # Ajouter le contrôle des couches
    folium.LayerControl().add_to(map1)

    # Générer le HTML de la carte
    map1 = map1._repr_html_()

    context = {
        'map1': map1
    }
    return render(request, 'dashboard/index.html', context)"""


##pour afficher les information sur les ecoles dans un interfaces
from django.shortcuts import render
from .models import Ecoles
import folium
from folium.plugins import MarkerCluster

def index(request):
    ecoles = Ecoles.objects.all()
    ecoles_list = Ecoles.objects.values_list('id', 'lat', 'long', 'name', 'ville')  # Ajout de 'id' pour identifier chaque école

    # Créer la carte de base
    map1 = folium.Map(location=[14.634328717590597, -14.940601323380719], tiles=None, zoom_start=7.40)

    # Ajouter différentes couches de tuiles
    folium.TileLayer('CartoDB Dark_Matter', name='Dark Matter').add_to(map1)
    folium.TileLayer('OpenStreetMap', name='OpenStreetMap').add_to(map1)
    folium.TileLayer('Stamen Terrain', name='Terrain').add_to(map1)
    folium.TileLayer('Stamen Toner', name='Toner').add_to(map1)
    folium.TileLayer('Stamen Watercolor', name='Watercolor').add_to(map1)

    # Créer un cluster de marqueurs
    marker_cluster = MarkerCluster(name='Cluster d\'Ecoles').add_to(map1)

    # Ajouter des marqueurs au cluster avec un popup contenant les informations de l'école
    for ecole in ecoles_list:
        folium.Marker(
            location=[ecole[1], ecole[2]],
            popup=f'<b>{ecole[3]}</b><br>Ville: {ecole[4]}',
            tooltip='Cliquez pour plus de détails',
            icon=folium.Icon(color='blue', icon='info-sign')
        ).add_to(marker_cluster)

    # Ajouter la fonctionnalité plein écran
    folium.plugins.Fullscreen(position='topright').add_to(map1)

    # Ajouter le contrôle des couches
    folium.LayerControl().add_to(map1)

    # Générer le HTML de la carte
    map1 = map1._repr_html_()

    context = {
        'map1': map1,
        'ecoles': ecoles  # Passer les écoles à contexte pour accéder aux détails dans le template
    }
    return render(request, 'dashboard/index.html', context)
