from django.urls import path

from .views import movielistView,movieDetailView
urlpatterns = [
   
   path('',movielistView.as_view(), name= 'movie_list'),
   path('<int:pk>/',movieDetailView.as_view(), name= 'movie_detail')

]
