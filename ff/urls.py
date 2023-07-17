from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('home/',views.home,name='home'),
    path('croprecomendation/',views.croprecomendation),
    path('login/',views.login,name='login'),
    path('about/',views.about,name='about'),
    path('video/',views.video,name='video'),
    path('login/register',views.register,name='register'),
    path('login/login',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('rice/',views.rice,name='rice'),
    path('wheat/',views.wheat,name='wheat'),
    path('sugarcane/',views.sugarcane,name='sugarcane'),
    path('cotton/',views.cotton,name='cotton'),
    path('maize/',views.maize,name='maize'),
    path('crops/',views.crops,name='crops'),
    path('indexform/',views.indexform,name='indexform'),
    path('tea/',views.tea,name='tea'),
    path('coffee/',views.coffee,name='coffee'),
    path('barley/',views.barley,name='barley'),
    path('coconut/',views.coconut,name='coconut'),
    path('cashew/',views.cashew,name='cashew'),
    path('fruits/',views.fruits,name='fruits'),
    path('millets/',views.millets,name='millets'),
    path('pulses/',views.pulses,name='pulses'),
    path('jowar/',views.jowar,name='jowar'),
    path('groundnut/',views.groundnut,name='groundnut'),
    path('jute/',views.jute,name='jute'),
    path('cereals/',views.cereals,name='cereals'),
    path('sunflower/',views.sunflower,name='sunflower'),
    path('oilseeds/',views.oilseeds,name='oilseeds'),
    path('indexform/',views.indexform,name='indexform'),
    path('contact/',views.contact,name='contact'),
    path('vegetables/',views.vegetables,name='vegetables'),
    path('potato/',views.potato,name='potato'),

]
