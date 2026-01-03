from django.urls import path
from . import api_views


urlpatterns = [
    path('api/v1/employes/', api_views.Employes_list.as_view()),
    path('api/v2/employes/', api_views.Employes_details.as_view()),
    
]