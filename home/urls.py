from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Anasayfa
    path('hakkimizda/', views.hakkimizda, name='hakkimizda'),  # Hakkımızda sayfası
    path('iletisim/', views.iletisim, name='iletisim'),  # İletişim sayfası
]
