from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

#--------------------------------------------- All Urls With Caching ---------------------------------------------#

urlpatterns = [
    path('' , cache_page(60)(IndexListView.as_view()) , name='home'),
    path('menu/', cache_page(60)(MenuListView.as_view()) , name='menu'),
    path('about/' , cache_page(60)(AboutUsListView.as_view()) , name = 'about'),
    path('contact/' , cache_page(60)(ContactListView.as_view()) , name = 'contact'),
    path('post/ajax/message', postMessage, name = "post_friend"),
]
