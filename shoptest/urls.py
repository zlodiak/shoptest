from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shoptest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'shoptest.views.index', name='index'),
    url(r'^contacts/', 'shoptest.views.contacts', name='contacts'),
    url(r'^custom_products/', 'shoptest.views.custom_products', name='custom_products'),
    url(r'^shop/', include('shop.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
