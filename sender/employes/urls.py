from django.urls import path
from . import api_views


urlpatterns = [
    path('api/employes/', api_views.Employes_list.as_view()),
]