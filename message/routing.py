from django.urls import path
from .views import *

urlpatterns = [
    path('messages/', MessageListCreateView.as_view(), name='message-list-create'),
    path('message/<slug:slug>/', MessageRetrieveUpdateDestroyView.as_view(), name='message-retrieve-update-destroy'),
]