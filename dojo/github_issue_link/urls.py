from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^webhook', views.webhook, name='web_hook'),
    url(r'^github/add', views.new_github, name='add_github'),
    url(r'^github/(?P<tid>\d+)/delete$', views.delete_github,
        name='delete_github'),
    url(r'^github$', views.github, name='github')]
