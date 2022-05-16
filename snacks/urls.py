from django.urls import path
from .views import (HomeView,
                    SnackListView,
                    SnackDetailView,
                    SnackCreateView,
                    SnackUpdateView,
                    SnackDeleteView,
                    FormView)

urlpatterns = [
    path('', HomeView.as_view(), name='Home'),
    path('snack_list/',SnackListView.as_view(), name='snack_list'),
    path('<int:pk>', SnackDetailView.as_view(), name='snack_detail'),
    path('create/', SnackCreateView.as_view(), name = "create_thing"),
    path('update/<int:pk>', SnackUpdateView.as_view(), name = "update_thing"),
    path('delete/<int:pk>', SnackDeleteView.as_view(), name = "delete_thing"),
    path('form/', FormView.as_view(), name = "form_thing"),
]