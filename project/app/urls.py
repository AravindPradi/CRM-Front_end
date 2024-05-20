from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('delete-card/<int:card_id>/', views.delete_card, name='delete_card'),

    path('archive-card/', views.archive_card, name='archive_card'),
     
    path('restore-card/<int:card_id>/', views.restore_card, name='restore_card'),

    path('no-page/', views.no_page, name='no_page'),

    path('archives/', views.archives, name='archives'),

]
