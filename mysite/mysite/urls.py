from django.conf.urls import url,include
from django.contrib import admin
from webapp import views
urlpatterns = [
    url(r'^admin/$',admin.site.urls),
    url(r'^home/$',include('webapp.urls')),
    url(r'^$', views.index, name='index'),

]


