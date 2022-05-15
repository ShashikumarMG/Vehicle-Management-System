from django.urls import path
from django.contrib.auth import views as auth_views

from .import views
app_name = "accounts"
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.UsereDataList.as_view(), name='user_data'),
    path('users_update/<pk>', views.UserUpdate.as_view(),name='users_update'),
    path('delete/<pk>', views.DeleteUser.as_view(),name='delete'),
]