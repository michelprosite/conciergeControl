from django.urls import path
from .views import index, jointOwners, produto

urlpatterns = [
    path('', index, name='index'),
    path('jointOwners', jointOwners, name='jointOwners'),
    path('produto/<int:pk>', produto, name='produto'),
]
