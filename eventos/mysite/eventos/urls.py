from django.urls import path

from . import views

app_name = 'eventos'
urlpatterns = [
    # ex: /
    path('', views.index, name='index'),
    # ex: /eventos/list
    path('list/', views.ListEvent.as_view(), name='list'),
    # ex: /eventos/register
    path('register/', views.registerEvent, name='register'),
    # ex: /eventos/5/
    path('<int:pk>/', views.DetailEvent.as_view(), name='detail'),

]
