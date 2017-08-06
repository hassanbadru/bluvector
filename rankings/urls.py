from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^view-product$', views.ProductView.as_view(), name='view-product'),
]
