from django.urls import path
from .views import *

urlpatterns = [
    path('messages/', MessageListCreateView.as_view(), name='message-list-create'),
    path('message/<int:pk>/mark_read/', MarkAsReadView.as_view(), name='mark-as-read'),
    path('message/<slug:slug>/', MessageRetrieveUpdateDestroyView.as_view(), name='message-retrieve-update-destroy'),

    path('content/<slug:slug>',ContentRetrieveUpdateDestroyView.as_view(), name='content-retrieve-update-destroy'),
    path('content/',ContentListCreateView.as_view(), name='content-list'),
]