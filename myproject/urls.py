from django.urls import path
from myapp.views import predict_paragraph
from myapp import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('Prediction/', predict_paragraph, name='predict'),
    path('hist/', views.hist_view, name='hist'),
    path('poli/', views.poli_view, name='poli'),
    path('eco/', views.eco_view, name='eco'),
    path('sport/', views.sport_view, name='sport'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('singin/', views.singin, name='singin'),
    path('logout/', views.Logout, name='logout'),
 
]


