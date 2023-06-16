from django.urls import path, include
from rest_framework.routers import DefaultRouter
from API import views

router = DefaultRouter()
router.register('productos',viewset=views.ProdctoViewSet, basename='producto')
router.register('contactos',viewset=views.ContactoViewSet, basename='contacto')
router.register('marcas',viewset=views.MarcaViewSet, basename='marca')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]
