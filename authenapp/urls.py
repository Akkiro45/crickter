
from django.conf.urls import url
from .views import loginUser, registerUser, logoutUser

urlpatterns = [
    url(r'login/$',  loginUser),
    url(r'logout/$', logoutUser),
    url(r'reg/$', registerUser)
]
