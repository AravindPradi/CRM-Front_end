from django.urls import path
from . import views



urlpatterns = [
    path('',views.home,name='home'),

    path('dashboard',views.dashboard,name='dashboard'),

    path('delete-card/<int:card_id>/', views.delete_card, name='delete_card'),

    path('restore-card/<int:card_id>/', views.restore_card, name='restore_card'),

    path('no_page',views.no_page,name='no_page'),

    path('archieves',views.archieves,name='archieves'),
]