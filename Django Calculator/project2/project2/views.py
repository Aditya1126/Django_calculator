from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def fun(request):
    return render(request,'index.html')

def submitquery(request):
    q=request.POST['query']
    
    try:
        ans=eval(q)
        mydict={
            'q':q,
            'ans':ans,
            'error':False
        }
        return render(request,'index.html',context=mydict)
    except:
        mydict={
            'error':True
        }
        return render(request,'index.html',context=mydict)