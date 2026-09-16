from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('legal_frameworks/', views.legal_frameworks, name='legal_frameworks'),
    path('incentives_facilities/', views.incentives_facilities, name='incentives_facilities'),
    path('our_service/', views.our_service, name='our_service'),
    path('compliance/', views.compliance_view, name='compliance'),
    path('key_management/', views.key_management_view, name='key_management'),
    path('gallery/', views.gallery, name='gallery'),
    path('news_event/', views.news_event, name='news_event'),
    path('request_investor/', views.request_investor, name='request_investor'),
    path('contact/', views.contact, name='contact'),
]