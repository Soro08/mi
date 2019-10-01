from django.urls import path
from . import views
urlpatterns = [
    path('',views.home ),
    path('detail.mi',views.detail ),
    path('fichier.mi',views.fichier ),
    path('profile.mi',views.profile ),
]
