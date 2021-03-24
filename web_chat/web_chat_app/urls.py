from django.conf.urls import url, include
from web_chat_app.views import dashboard, register

from django.contrib.auth import views as log_views

urlpatterns = [
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^register/", register, name="register"),
]