from django.shortcuts import render
from django.views import View


class GeneralView(View):

    def get(self, request):
        """Displays the home page."""
        return render(request, 'info/general.html')