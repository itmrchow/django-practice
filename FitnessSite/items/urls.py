from django.urls import path
from . import views

app_name = "items"
urlpatterns = [
    # view
    path('', views.IndexView.as_view(), name="index"),
    path('<int:pk>', views.IndexView.as_view(), name="index_Part"),
    path('create', views.CreateView.as_view(), name="create"),
    path('detail/<int:pk>', views.DetailView.as_view(), name="detail"),

    # action
    path('insert', views.insert, name="insert"),
    path('update', views.update, name="update"),
]
