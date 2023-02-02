from django.http import HttpResponse
from django.shortcuts import redirect

#write a decorator function to restrict access of none authenticated users to the dashboard
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func