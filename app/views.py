from django.shortcuts import render

# Create your views here.
def hai(request):
    return render(request,'hai.html',context={'name':'DHONI','a':None})