from django.urls import path
from . import views

app_name = "Janitor"
urlpatterns = [
    path("", views.default, name="default"),
    path("messages/", views.contactList, name="messageList"),
    path("member/", views.memberList, name="memberList"),
]