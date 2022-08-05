from django.urls import path

from zones.api import views

urlpatterns = [
    path('add', views.edit),
    path('edit', views.edit),
    path('delete', views.delete),
    path('create', views.ZoneCreateView.as_view(), name='Zone-add'),
]
