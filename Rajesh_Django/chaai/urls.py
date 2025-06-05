from django.urls import path
from . import views

# localhost:8000/chaai/
#localhost:8000/chaai/order/
urlpatterns = [   
    path('', views.chaai, name='chaai'),  # Added this line
]
