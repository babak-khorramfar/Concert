import profile
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import ticketSales
import accounts
from django.contrib.auth.decorators import login_required
from .models import ProfileModel
from .forms import ProfileRegisterForm, ProfileEditForm, UserEditForm
from django.contrib.auth.models import User


from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.contrib.auth.decorators import login_required

def LoginView(request):
    # Handles user login. If the request method is POST, it checks the submitted credentials
    # with the authenticate function. If the user exists and the credentials are correct, it logs in the user.
    # If the user does not exist or the credentials are invalid, it displays an error message.
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # If there is a 'next' parameter in the request URL (usually passed for redirect after login),
            # it redirects to the URL specified in 'next'. Otherwise, it redirects to LOGIN_REDIRECT_URL from settings.
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET.get('next'))
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        else:
            context = {
                'username': username,
                'error': 'Invalid username or password'
            }
            return render(request, 'accounts/login.html', context)
    else:
        # If the request method is not POST, it displays the login page.
        return render(request, 'accounts/login.html', {})

def LogoutView(request):
    # Handles user logout. It logs out the user and redirects to the concert list view.
    logout(request)
    return HttpResponseRedirect(reverse(ticketSales.views.concertListView))

@login_required
def ProfileView(request):
    # Displays the user's profile view if the user is authenticated and logged in.
    # It gets the user's profile using the one-to-one relationship defined in ProfileModel.
    # It passes the profile information to the 'accounts/profile.html' template for rendering.
    profile = request.user.profile
    context = {
        'profile': profile,
    }
    return render(request, 'accounts/profile.html', context)


from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.models import User
from ticketSales.models import ProfileModel
from .forms import ProfileRegisterForm, ProfileEditForm, UserEditForm

def profileRegisterView(request):
    # Handles user profile registration. If the request method is POST, it processes the submitted form data.
    # If the form data is valid, it creates a new user and saves the user and profile information.
    # It then redirects to the concert list view. If the request method is not POST, it displays the registration form.
    if request.method == 'POST':
        profileRegisterForm = ProfileRegisterForm(request.POST, request.FILES)
        if profileRegisterForm.is_valid():
            user = User.objects.create_user(username=profileRegisterForm.cleaned_data['username'],
                                            email=profileRegisterForm.cleaned_data['email'],
                                            password=profileRegisterForm.cleaned_data['password'],
                                            first_name=profileRegisterForm.cleaned_data['first_name'],
                                            last_name=profileRegisterForm.cleaned_data['last_name'])
            user.save()
            profileModel = ProfileModel(user=user, ProfileImage=profileRegisterForm.cleaned_data['ProfileImage'],
                                        Gender=profileRegisterForm.cleaned_data['Gender'],
                                        Credit=profileRegisterForm.cleaned_data['Credit'])
            profileModel.save()
            return HttpResponseRedirect(reverse(ticketSales.views.concertListView))
    else:
        profileRegisterForm = ProfileRegisterForm()
        context = {
            'formData': profileRegisterForm
        }
        return render(request, 'accounts/profileRegister.html', context)

def ProfileEditView(request):
    # Handles user profile editing. If the request method is POST, it processes the submitted form data.
    # If the form data is valid, it updates the user and profile information and redirects to the profile view.
    # If the request method is not POST, it displays the profile edit form.
    if request.method == 'POST':
        profileEditForm = ProfileEditForm(request.POST, request.FILES, instance=request.user.profile)
        userEditForm = UserEditForm(request.POST, instance=request.user)
        if profileEditForm.is_valid() and userEditForm.is_valid():
            profileEditForm.save()
            userEditForm.save()
            return HttpResponseRedirect(reverse(accounts.views.ProfileView))
    else:
        profileEditForm = ProfileEditForm(instance=request.user.profile)
        userEditForm = UserEditForm(instance=request.user)
        context = {
            'userEditForm': userEditForm,
            'profileEditForm': profileEditForm,
            'ProfileImage' : request.user.profile.ProfileImage,
        }
        return render(request, 'accounts/profileEdit.html', context)

    
    
