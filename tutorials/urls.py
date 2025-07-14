
from django.urls import path
from .views import *
app_name = 'tutorial'
urlpatterns = [
    path('',home,name='home'),
    path('tutorials',tut,name='main'),
    path('tutorial/<int:name>',showTut,name='course'),
    path('tutorial/<int:name>/<str:slug>',showchap,name='chapter'),
    path('collection',showCollection,name='collection'),
    path('404',sorryPagenotFound,name='404'),
    path('comming-soon/',CommingSoon,name="comming"),
    path('request',courseRequest,name='request'),
    path('privacy',privacy),
    path('collection/<int:id>',collectionDetail,name="collection-tut")
]