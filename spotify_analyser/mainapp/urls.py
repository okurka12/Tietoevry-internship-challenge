from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("proceed_with_auth_code/", views.process_redirect_from_api),
    path("analysed_data", views.view_analysed_data)
]
