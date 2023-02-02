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

def users_allowed(roles_allowed=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None#this variable starts with nothig
            if request.user.groups.exists():#this checks if a user has a group and if the group exists
                group = request.user.groups.all()[0].name#this will check for particular user in the available groups starting with first

            if group in roles_allowed: #check if the rolls_allowed are in the availble groups created
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to link this page')
            
        return wrapper_func
    return decorator

#this an admin only decorator
def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():#checks user group
            group = request.user.groups.all()[0].name

        if group == 'customer':
            return redirect('user')

        if group == 'admin':
            return view_func(request, *args, **kwargs)

    return wrapper_function