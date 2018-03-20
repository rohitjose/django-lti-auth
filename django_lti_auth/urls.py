from django.conf.urls import url
from . import views

app_name = 'django_lti_auth'

urlpatterns = [
    url(r'^auth/$', views.auth, name="auth"),
    url(r'^denied/$', views.denied, name="denied"),
]