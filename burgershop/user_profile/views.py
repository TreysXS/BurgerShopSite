from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from .forms import UserForm, UserProfileForm


class UserProfileDetail(LoginRequiredMixin, View):

    def get(self, request):
        """"""
        return render(request, 'user_profile/profile.html', context={
                                                                'profile': request.user.profile,
                                                                'user': request.user,
                                                                    })


class UserProfileUpdate(LoginRequiredMixin, View):

    def get(self, request):
        """"""
        return render(request, 'user_profile/profile_update.html', context={
                                                                        'profile': request.user.profile,
                                                                        'user': request.user,
                                                                           })

    def post(self, request):
        """"""
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('user-profile')
