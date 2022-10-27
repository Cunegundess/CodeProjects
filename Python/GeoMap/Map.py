import folium 
import pandas

# Variáveis
data = pandas.read_csv("Dia11/Webmap_datasources/Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

map = folium.Map(location = [42, -114.3], zoom_start = 5, tiles = "Stamen Terrain")


# coloração baseada na altitude 
def colorMarker(elevation):

    if elevation < 2000:
        return "green" 

    elif elevation >= 2000 and elevation <= 3000:
        return "orange"

    else: 
        return "red"


# layer volcanoes
markerV = folium.FeatureGroup(name = "Volcanoes")

for na, lt, ln, el in zip(name, lat, lon, elev):    
    markerV.add_child(folium.CircleMarker(
        location = [lt, ln], 
        popup = na + ": " + str(el) + "m", 
        color = colorMarker(el), 
        radius = 6, 
        fill = True, 
        fill_color = colorMarker(el), 
        fill_opacity = 0.7)
        )


# layer population
markerP = folium.FeatureGroup(name = "Population")

markerP.add_child(folium.GeoJson(
    data = open("Dia11/Webmap_datasources/world.json", "r", 
    encoding = "utf-8-sig").read(),
    style_function = lambda x: {
        "fillColor": "green" 
        if x["properties"]["POP2005"] < 10000000 else "orange" 
        if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red"}
        )
        )


# adicionando os "layers" no mapa
map.add_child(markerV)
map.add_child(markerP)
map.add_child(folium.LayerControl()) 


# salvando/criando o mapa 
map.save("Dia11/Map.html")
 





