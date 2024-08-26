import folium

mapa = folium.Map(location=[-15.793889, -47.882778], zoom_start=4)

folium.Marker([-15.793889, -47.882778], popup="Brasilia, Brazil").add_to(mapa)

folium.CircleMarker(
    location=[-22.9068, -43.1729],
    radius=50,
    popup="Rio de Janeiro",
    color="crimson",
    fill=True,
    fill_color="crimson"
).add_to(mapa)

mapa.save("/home/sciuser/OUTPUT/south_america_map_folium.html")

print("Folium map saved to /home/sciuser/OUTPUT/south_america_map_folium.html")