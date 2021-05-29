from django.http import Http404


class AdminHasPermissionsMixin:
    """
    Checking on admin IF True redirects to page ELSE 404 error.
    """
    def has_permissions(self):
        return self.request.user.groups.values_list('name', flat=True).first() == 'Админ'

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            raise Http404()
        return super().dispatch(request, *args, **kwargs)