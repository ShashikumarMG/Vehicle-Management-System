from django.contrib.auth.decorators import login_required
from django.shortcuts import reverse


def login_exempt(view):
    view.login_exempt = True
    return view


class LoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        if getattr(view_func, 'login_exempt', False):
            return

        if request.user.is_authenticated:
            if 'dialogs' in request.path:
                request.user.online_status = True
                a = request.user.save()
            elif 'admin' in request.path:
                pass
            else:
                request.user.online_status = False
                request.user.save()
            return

        if request.path.startswith(reverse('accounts:login')) or request.path.startswith(reverse('accounts:logout')):
            return



        # You probably want to exclude the login/logout views, etc.

        return login_required(view_func)(request, *view_args, **view_kwargs)
