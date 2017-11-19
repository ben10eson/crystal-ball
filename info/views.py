

# Create your views here.
from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from .forms import information
from .models import info

class infoview(TemplateView):
    template_name = 'info/home_page.html'

    def get(self,request):
        form=information()
        posts=info.objects.all()

        args ={'form':form,'posts':posts}
        return render(request,self.template_name,args)
    def post(self,request):
        form=information(request.POST)

        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()

            text1= form.cleaned_data['Name']
            text2 = form.cleaned_data['Email']
            text3 = form.cleaned_data['Subject']
            text4 = form.cleaned_data['Message']
            form= information()

        args = {'form': form}
        return  render(request,self.template_name,args)
def home_page(request):
    return render(request,'accounts/home_page.html')