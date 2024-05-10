from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout

# Create your views here.
def users_app(request):
    return render(request,'users/users.html')

def register_user(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #form.save()
            login(request,form.save())
            return redirect("posts:list")
    else:
        form = UserCreationForm()
    
    return render(request,"users/register.html",{"form":form})
    


def login_user(request):
    if request.method=="POST":
        form=AuthenticationForm(data= request.POST)#the from data comes from data kwarg.
        
        if form.is_valid():
            login(request,form.get_user())
            if "next" in request.POST :
                return redirect(request.POST.get('next'))
            else:
                return redirect("posts:list")
    else:
        form = AuthenticationForm()
        
    return render(request,'users/login.html',{"form":form})


def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")
        
    