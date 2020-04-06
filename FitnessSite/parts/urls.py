from django.urls import path
from . import views

app_name = "parts"
urlpatterns = [
    # view
    path('', views.IndexView.as_view(), name="index"),
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),
    path('create', views.CreateView.as_view(), name="create"),

    # action
    path('insert', views.insert, name='insert'),
    path('<int:pk>/delete/', views.delete, name="delete"),
    path('update/', views.update, name="update")
]
