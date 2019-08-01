from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns =[
	path('', views.index, name='index'),
	path('entrepreneurship/', views.entrepreneurship , name='entrepreneurship'),
	path('ict/', views.ict , name='ict'),
	path('feedback/', views.feedback , name='feedback'),
	path('ict_feedback/<int:course_id>', views.ict_feedback , name='ict_feedback'),
	path('entreprenuership_feedback/<int:course_id>', views.entreprenuership_feedback , name='entreprenuership_feedback'),
	path('login/', auth_views.LoginView.as_view(), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('register/', views.register, name='register'),
	path('edit_profile/', views.edit, name='edit_profile'),
	path('profile/', views.profile, name='profile'),
]