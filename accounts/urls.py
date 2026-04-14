from django.urls import path
from . import views

urlpatterns = [
   path('login/', views.login_view, name='login'),
   path('signup/', views.signup_view, name='signup'),
   path('profile/', views.profile_view, name='profile'),
   path('logout/', views.logout_view, name='logout'),
   path('profile/edit/', views.edit_profile, name='edit-profile'),
   path('password_change/', views.CustomPasswordChangeView.as_view(), name='password-change'),
]