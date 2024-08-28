from django.shortcuts import render # type: ignore

# Create your views here.
def conditions(request):
    d={'a':2000,'b':300,'c':4000}
    return render(request,'conditions.html',context=d)
def loop(request):
    d={'name':'Parvez','mobilenumber':[12345,45678]}
    return render(request,'loop.html',context=d)