from django.urls import path
from . import views
urlpatterns = [
path("moviehome", views.movie, name='moviehome'),
path("", views.home, name='home'),
path('<int:movie_id>', views.moviedetail, name='moviedetail'),
path("other",views.other,name='other'),
path('<int:movie_id>/createmoviereview', views.createmoviereview, name='createmoviereview'),
path('review/<int:review_id>', views.updatemoviereview, name='updatemoviereview'),
path('review/<int:review_id>/delete', views.deletemoviereview, name='deletemoviereview'),
]