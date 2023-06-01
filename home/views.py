from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from .models import UserActivity


# user - karan pass - Karan@talent
# Create your views here.
from .models import UserActivity
from datetime import datetime

# def loginUser(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             # Set login time in UserActivity
#             user_activity, created = UserActivity.objects.get_or_create(user=user, defaults={'login_time': datetime.now()})
#             if not created and user_activity.login_time is None:
#                 user_activity.login_time = datetime.now()
#                 user_activity.save()
#             return redirect("/")
#         else:
#             return render(request, 'login.html')
#     return render(request, 'login.html')

from django.utils import timezone

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)

            # Retrieve the existing UserActivity object for the user
            try:
                user_activity = UserActivity.objects.get(user=user)
                # Update the login_time of the existing UserActivity object
                user_activity.login_time = datetime.now()
                user_activity.save()
            except UserActivity.DoesNotExist:
                user_activity = UserActivity.objects.create(user=user)
                # Update the login_time of the existing UserActivity object
                user_activity.login_time = datetime.now()
                user_activity.save()


            return redirect("/")
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')



def logoutUser(request):
    try:
        user_activity = UserActivity.objects.get(user=request.user)
        user_activity.logout_time = datetime.now()
        user_activity.save()
    except UserActivity.DoesNotExist:
        pass

    logout(request)
    return redirect("/")


def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    
    try:
        user_activity = UserActivity.objects.filter(user=request.user).latest('login_time')
        login_time = user_activity.login_time
        #logout_time = user_activity.logout_time
    except UserActivity.DoesNotExist:
        login_time = None
        # logout_time = None
    
    context = {
        'login_time': login_time,
        # 'logout_time': logout_time
    }
    return render(request, 'index.html', context)