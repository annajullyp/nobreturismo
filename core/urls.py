
from django.urls import path
from .views import HomeView, login_view, cadastro_view, logout_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('login/', login_view, name='login'),
    path('cadastro/', cadastro_view, name='cadastro'),
    path('logout/', logout_view, name='logout'),
]

# Para tratar do DEBUG=False, garantindo que as imagens em /media sejam exibidas
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
