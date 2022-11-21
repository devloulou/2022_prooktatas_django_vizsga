from django.urls import path
from .views import home
from .views import PostListView
                

urlpatterns = [
    # path('', home, name="blog-home"),
    # magát a PostListView-t nem lehet csak úgy odaadni, át kell convertálni view-vá, az as_view
    # segítségével
    path('', PostListView.as_view(), name="blog-home")
   
]

