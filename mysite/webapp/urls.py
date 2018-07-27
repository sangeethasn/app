from django.conf.urls import url,include
from django.contrib import admin
from webapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
        url(r'^hey/$', views.index, name='index'),
    url(r'^admin/$', admin.site.urls),
]