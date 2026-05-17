from django.urls import path
from django.contrib.auth import views as auth_views
from . import views, views_dashboard

urlpatterns = [
    path('', views.home_view, name='home'),
    path('services/', views.services_view, name='services'),
    path('portfolio/', views.portfolio_view, name='portfolio'),
    path('project/<slug:slug>/', views.project_detail_view, name='project_detail'),
    path('about/', views.about_view, name='about'),
    path('team/', views.team_view, name='team'),
    path('contact/', views.contact_view, name='contact'),
    path('pricing/', views.pricing, name='pricing'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('privacy/', views.privacy_view, name='privacy'),
    path('terms/', views.terms_view, name='terms'),
    # Blog
    path('blog/', views.blog_list_view, name='blog_list'),
    path('blog/<slug:slug>/', views.blog_detail_view, name='blog_detail'),
    
    # Dashboard Overview
    path('management/', views_dashboard.dashboard_home, name='dashboard_home'),
    path('management/messages/', views_dashboard.dashboard_messages, name='dashboard_messages'),
    path('management/messages/<int:pk>/', views_dashboard.message_detail, name='message_detail'),
    
    # Content Management (List Views)
    path('management/projects/', views_dashboard.dashboard_projects, name='dashboard_projects'),
    path('management/blog/', views_dashboard.dashboard_blog, name='dashboard_blog'),
    path('management/services/', views_dashboard.dashboard_services, name='dashboard_services'),
    path('management/testimonials/', views_dashboard.dashboard_testimonials, name='dashboard_testimonials'),
    path('management/team/', views_dashboard.dashboard_team, name='dashboard_team'),
    path('management/logos/', views_dashboard.dashboard_logos, name='dashboard_logos'),
    path('management/packages/', views_dashboard.dashboard_packages, name='dashboard_packages'),
    path('management/faq/', views_dashboard.dashboard_faq, name='dashboard_faq'),
    path('management/subscribers/', views_dashboard.dashboard_subscribers, name='dashboard_subscribers'),
    path('management/settings/', views_dashboard.dashboard_settings, name='dashboard_settings'),
    # CRUD Operations (Unified)
    path('management/content/<str:model_key>/add/', views_dashboard.content_create_edit, name='content_add'),
    path('management/content/<str:model_key>/edit/<int:pk>/', views_dashboard.content_create_edit, name='content_edit'),
    path('management/content/<str:model_key>/delete/<int:pk>/', views_dashboard.content_delete, name='content_delete'),
    
    # Auth
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

    # SEO Engine
    path('sitemap.xml', views.sitemap_view, name='sitemap'),
    path('robots.txt', views.robots_view, name='robots'),

    # Currency Engine
    path('set-currency/', views.set_currency, name='set_currency'),
]
