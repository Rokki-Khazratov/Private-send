from django.urls import path
from .views import *

urlpatterns = [
    path('messages/', MessageListCreateView.as_view(), name='message-list-create'),
    path('messages/<int:pk>/mark_as_read/', MarkAsReadView.as_view(), name='mark-as-read'),
    path('message/<slug:slug>/', MessageRetrieveUpdateDestroyView.as_view(), name='message-retrieve-update-destroy'),
]