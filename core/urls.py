
from django.urls import path
from .views import HomeView, login_view, cadastro_view, logout_view
urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('login/', login_view, name='login'),
    path('cadastro/', cadastro_view, name='cadastro'),
    path('logout/', logout_view, name='logout'),
]
