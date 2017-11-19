from django.shortcuts import redirect,render

def Home_page(request):
    return redirect('/info/')