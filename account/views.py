from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView

from account.forms import RegistrationForm, ChangePasswordForm, ForgotPasswordForm

User = get_user_model()

class RegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'account/registration.html'
    success_url = reverse_lazy('successful-registration')


class SuccessfulRegistrationView(TemplateView): # when we use templates, html
    template_name = 'account/success_registration.html'

#http://127.0.0.1:8000/account/activate/?u=24weaf25
class ActivationView(View):
    def get(self, request):
        code = request.GET.get('u')
        user = get_object_or_404(User, activation_code=code)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return render(request, 'account/activation.html', {})


class SignInView(LoginView):
    template_name = 'account/login.html'
    success_url = reverse_lazy('index-page')


class ChangePasswordView(View):
    def post(self, request):
        form = ChangePasswordForm(request.POST, request=request)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('index-page'))
        return render(request, 'account/change_password.html', {'form': form})

    def get(self, request):
        form = ChangePasswordForm(request=request)
        return render(request, 'account/change_password.html', {'form': form})

class ForgotPasswordView(View):
    def post(self, request):
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            form.send_new_password()
            return redirect(reverse_lazy('forgot-pass-complete'))
        return render(request, 'account/forgot_password.html', {'form': form})

class ForgotPassCompleteView(View):

    def get(self, request):
        form = ForgotPasswordForm()
        return render(request, 'account/forgot_password.html', {'form': form})



