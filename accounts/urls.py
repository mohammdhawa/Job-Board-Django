from django.urls import path
from . import views
from .api import SignupAPIView

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('profile/', views.profile, name="profile"),
    path('profile/edit', views.profile_edit, name="edit"),
    path('api-signup/', SignupAPIView.as_view(), name="api-signup"),
]
