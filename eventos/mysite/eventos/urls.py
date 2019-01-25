from django.urls import path

from . import views

app_name = 'eventos'
urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    # ex: /eventos/list
    path('list/', views.listEvent, name='list'),
    # ex: /eventos/register
    path('register/', views.registerEvent, name='register'),
    # ex: /eventos/5/
    path('<int:event_id>/', views.detailEvent, name='detail'),
        
    ]   