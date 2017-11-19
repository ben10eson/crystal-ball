

# Create your views here.
from django.shortcuts import render,redirect,render_to_response
from django.contrib.auth.models import User
from accounts.forms import RegistrationForm



from .models import UserProfile


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/info/')
        else:
            form=RegistrationForm()
            args={'form':form}
            return render(request,'accounts/signup.html',args)
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'accounts/signup.html', args)

def home_page(request):
    return render(request,'accounts/home_page.html')
def profile(request):
    args={'user':request.user}
    return render(request,'accounts/profile.html',args)
def data(request):
    args={'user':request.user}
    return render(request,'accounts/data.html',args)
def welcome(request):
    args={'user':request.user}
    return render(request,'info/home_page.html',args)







