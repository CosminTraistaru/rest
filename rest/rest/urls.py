"""rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import url, include
from store import views
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns


router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^items/$', views.ItemViewSet.as_view(), name='items-list'),
    url(r'^items/search/(?P<pk>[a-zA-Z0-9]+)/$',
        views.SearchItemsViewSet.as_view(),
        name='item-list'),
    url(r'^users/$', views.UserViewSet.as_view(), name='users-list'),
    url(r'^items/tag/(?P<pk>[a-z]+)/$',
        views.TagsViewSet.as_view(),
        name='tags-list'),
    url(r'^item/(?P<pk>[a-zA-Z0-9]+)/$',
        views.SingleItemViewSet.as_view(),
        name='item-list'),
    url(r'^api-auth/',
        include('rest_framework.urls',
                namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
