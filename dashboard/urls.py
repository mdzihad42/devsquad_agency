from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dashboard_home'),
    path('messages/', views.message_list, name='dashboard_messages'),
    path('messages/<int:pk>/', views.message_detail, name='dashboard_message_detail'),
    path('finances/', views.finance_list, name='dashboard_finances'),
    path('finances/add/', views.finance_add, name='dashboard_finance_add'),
    path('seo/', views.seo_list, name='dashboard_seo'),
    path('seo/add/', views.seo_add, name='dashboard_seo_add'),
    path('seo/edit/<int:pk>/', views.seo_edit, name='dashboard_seo_edit'),
    path('portfolio/', views.portfolio_list, name='dashboard_portfolio'),
]
