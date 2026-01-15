from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Public pages
    path('', views.home, name='home'),
    
    # Auth
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='learning/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Learner dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Topics & Chapters
    path('topics/', views.topic_list, name='topic_list'),
    path('topic/<int:topic_id>/', views.topic_detail, name='topic_detail'),
    path('chapter/<int:chapter_id>/', views.chapter_detail, name='chapter_detail'),
    
    # Progress tracking
    path('chapter/<int:chapter_id>/start/', views.start_chapter, name='start_chapter'),
    path('chapter/<int:chapter_id>/complete/', views.complete_chapter, name='complete_chapter'),
    
    # Profile
    path('profile/', views.profile, name='profile'),

    path('profile/edit/', views.edit_profile, name='edit_profile'),

]