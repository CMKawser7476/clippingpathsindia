from django.urls import path
from django.conf.urls import url
from testapp import views
app_name = "testapp"
urlpatterns = [
    path('', views.homeview, name='home'),
    path('about/', views.aboutview, name='about'),
    path('clippingpaths/', views.clippingpathsview, name='clipping_paths'),
    path('backgroundremover/', views.background_remover_view, name='background_remover'),
    path('colorcorrection/', views.color_correction_view, name='color_correction'),
    path('dropshadow/', views.drop_shadow_view, name='drop_shadow'),
    path('imageretuch/', views.image_retuch_view, name='image_retuch'),
    path('invisiblemannequine/', views.invisible_mannequine_view, name='invisble_mannequine'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('pricing/', views.pricing, name='pricing'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
    path('getfreedemo/', views.getfredemo, name='getfreedemo'),
    path('bloglist/', views.bloglist, name='bloglist'),
    path('blogdetails/', views.blogdetails, name='blogdetails'),

] 