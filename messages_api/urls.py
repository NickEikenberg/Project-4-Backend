from django.urls import path
from . import views

urlpatterns = [
    path('api/messages', views.MessageList.as_view(), name='messages_list'),
    path('api/messages/<int:pk>', views.MessageDetail.as_view(), name='message_detail'),
]