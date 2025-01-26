from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from .api import SignupAPIView, ProfileAPIView

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('profile/', views.profile, name="profile"),
    path('profile/edit', views.profile_edit, name="edit"),
    path('api-signup/', SignupAPIView.as_view(), name="api-signup"),
    path('api-profile/', ProfileAPIView.as_view(), name="api-profile"),
    path('api-login/', obtain_auth_token, name='api-login'),
]
