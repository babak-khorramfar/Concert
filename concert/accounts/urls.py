from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView),
    path('profile/', views.ProfileView),
    path('profileEdit/', views.ProfileEditView),
    path('profileRegister',views.profileRegisterView),

]