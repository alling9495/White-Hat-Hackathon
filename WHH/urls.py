from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WHH.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'game.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^game/', include('game.urls')),
    url(r'^login/', 'auth.views.login_user'),
    url(r'^2fa/', include('two_factor.urls', 'two_factor')),
    url(r'^accounts/profile/', include('game.urls')),
)
