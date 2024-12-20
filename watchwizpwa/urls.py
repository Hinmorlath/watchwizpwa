from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from watchwizpwa.views.auth_views import home_view, login_view, principal_view, registro_view, logout_view
from watchwizpwa.views.trabajos_views import registro_trabajos, trabajos_views
from watchwizpwa.views.refac_views import categoria_view, refacciones_view
from watchwizpwa.views.invet_views import inventario_view

urlpatterns = [
    path('', principal_view, name='principal'),
    path('login/', login_view, name='login'),
    path('home/', home_view, name='home'),
    path('registro/', registro_view, name='registro'),
    path('logout/', logout_view, name='logout'),
    path('registro_trabajos/', registro_trabajos, name='registro_trabajos'),
    path('refacciones/', refacciones_view, name='refacciones'),
    path('trabajos/', trabajos_views, name='trabajos'),
    path('registrar_categoria/', categoria_view, name='registrar_categoria'),
    path('inventario/', inventario_view, name='inventario'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
