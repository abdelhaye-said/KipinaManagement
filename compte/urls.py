from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.dashboard, name='dash'),
    path('Cantine/', views.cantine, name='Cantine'),
    path('Assurance/', views.assurance, name='Assurance'),
    path('Garde/', views.garde, name='Garde'),
    path('Search/', views.search, name='Search'),
    path('Forfait/', views.forfait, name='Forfait'),
    path('Create_Profil/', views.Create_profil, name='Create_Profil'),
    path('Update_Profil/<str:pk>/', views.update_profil, name='Update_Profil'),
    path('Remove_Profil/<str:pk>/', views.remove_profil, name='Remove_Profil'),
    path('Remove_Cantine/<str:pk>/', views.remove_cantine, name='Remove_Cantine'),
    path('View_Profil/<str:pk>/', views.view_profil, name='View_Profil'),
    path('Create_other/', views.create_other, name='Create_other'),
    path('Suivi_Profil/<str:pk>/', views.suivi_profil, name='Suivi_Profil'),
    path('Suivi_Fotfait/', views.suivi_forfait, name='Suivi_Fotfait'),
    path('Suivi_Can/', views.suivi_cantine, name='Suivi_Can'),
    path('Suivi_Trans/', views.suivi_transport, name='Suivi_Trans'),
    path('Suivi_Garde/', views.suivi_garde, name='Suivi_Garde'),
    path('Suivi_Assur/', views.suivi_assur, name='Suivi_Assur'),
]
