from django.urls import path

# Importar APP con mis vistas

from Categorias import views

urlpatterns = [
    path('Articulos/', views.articles, name="Articulos"),
]
