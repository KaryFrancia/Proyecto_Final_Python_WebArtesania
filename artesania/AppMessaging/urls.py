from django.urls import path
from . import views

urlpatterns = [
    path('messages/inbox/', views.inbox, name='inbox'),
    path('messages/compose/', views.compose, name='compose'),
    path('messages/chat/<int:user_id>/', views.chat, name='chat'),
]
