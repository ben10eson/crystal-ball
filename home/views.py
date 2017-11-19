from scipy.interpolate import *
from numpy import *
import numpy as np



from django.views.generic import TemplateView
from home.forms import HomeForm
from home.models import Questions
from accounts.models import UserProfile
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import context
from django.shortcuts import render,redirect

class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self,request):
        form=HomeForm()
        posts=Questions.objects.all()

        args ={'form':form,'posts':posts}
        return render(request,self.template_name,args)
    def post(self,request):
        form=HomeForm(request.POST)

        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()

            text= form.cleaned_data['question']
            form= HomeForm()


        x=calculate(post.question,request.user)
        args = {'form': form, 'text': text,'x':x}
        return  render(request,self.template_name,args)
def profile(request):
    args={'user':request.user}
    return render(request,'accounts/profile.html',args)

def result(request):
    args = {'user': request.user}
    return render(request, 'home/result.html', args)
def home(request):
    args = {'user': request.user}
    return render(request, 'home/home.html', args)
def myview(request):
    context['your_html_variable '] = "<div><h1> Hello </h1></div>"
    return render(request, 'home/home.html', context)

def calculate(question,userid):
    data= userid.userprofile.data
    a=data.split(';')
    b=a[0]
    c=a[1]
    coefficients=c.split(',')
    d=b.split('(')
    featuresno=int(d[1])
    eqtype=int(d[0])
    
    values_str=question.split(',')
    inp_values=list(map(float,values_str))
    
    coefficients=list(map(float,coefficients))
    
    yfit=0
    
    if (eqtype==0):
        
        if(featuresno==1):
            yfit=polyval(coefficients,inp_values)
        else:
            c=np.array(coefficients)
            d=np.array(inp_values)
            yfit=sum(c*d)
            

    elif (eqtype==1):
        yfit=polyval(coefficients,inp_values)
        

    return yfit