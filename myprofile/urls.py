from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from myprofile.fb import views as fb_views
urlpatterns = [
    # Examples:
    url(r'^$', fb_views.home, name='home'),
    url(r'^account/login/$', auth_views.login, name='account.login'),
    url(r'^account/logout/$', auth_views.logout, name='account.logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--
    url(r'^admin/', include(admin.site.urls)),
]
