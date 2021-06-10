from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic import TemplateView

from account import views
from account.views import RegistrationView, ChangePasswordView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='registration'),
    path('success_registration/', views.SuccessfulRegistrationView.as_view(), name = 'successful-registration'),
    path('activation/', views.ActivationView.as_view(), name='activation'),
    path('login/', views.SignInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change_password/', ChangePasswordView.as_view(), name='change-password'),
    path('forgot_password/', views.ForgotPasswordView.as_view(), name='forgot-password'),
    path('forgot_pass_complete/', TemplateView.as_view(template_name='account/forgot_pass_complete.html'),
         name='forgot-pass-complete')

]