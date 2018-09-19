import folium


map_1 = folium.Map(location=[-22.8163900, -45.1925000], zoom_start=13,
                   tiles='Stamen Terrain')
map_1.simple_marker([-22.78538858, -45.18132697], popup='Fatec Guaratinguetá')
map_1.create_map(path='mark_fatec.html')
