from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ReviewView.as_view(), name='review'),
    #url(r'^view-product$', views.ProductView.as_view(), name='view-product'),
    url(r'^view-product/(?P<beer_id>[0-9]+)/$', views.ProductView.as_view(), name='view-product'),

    #review form
    #url(r'^view-product/addreview/$', views.ProductView.review_form, name='addreview')
    #url(r'^view-product/addreview/$', views.ProductView.review_form, name='addreview')

    #product form
    #url(r'^(?P<pk>\d+)/$', views.addproduct, name='addproduct')
]
