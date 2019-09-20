from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:wdgt_id>', views.delete_wdgt, name='delete_wdgt'),
]