from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from .forms import UserForm, UserProfileForm
from .service import save_user_profile


class UserProfileDetail(LoginRequiredMixin, View):

    def get(self, request):
        """"""
        return render(request, 'user_profile/profile.html', context={
                                                                'profile': request.user.profile,
                                                                'user': request.user,
                                                                    })


class UserProfileUpdate(LoginRequiredMixin, View):

    def get(self, request):
        """Displays a page with user data."""
        return render(request, 'user_profile/profile_update.html', context={
                                                                        'profile': request.user.profile,
                                                                        'user': request.user,
                                                                           })

    def post(self, request):
        """IF the forms are valid saves the data about the user ELSE doesn't change anything."""
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            save_user_profile(user_form, profile_form)

            return redirect('user-profile')

        else:
            return redirect('user-change')
