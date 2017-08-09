from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ReviewView.as_view(), name='review'),
    #url(r'^view-product$', views.ProductView.as_view(), name='view-product'),
    url(r'^view-product/(?P<oid>[0-9]+)/$', views.ProductView.as_view(), name='view-product')
]
