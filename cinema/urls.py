from django.urls import path

from cinema.views import movies_list

urlpatterns = [
    path("movies/", movies_list, name="movie-list"),
]

app_name = "cinema"
