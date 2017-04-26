from django.shortcuts import render
from django_web.models import ItemInfo
from django.core.paginator import Paginator

# Create your views here.

#responsible to get data from url request

def index(request):
    limit = 10
    info= ItemInfo.objects
    paginator = Paginator(info,limit)
    page = request.GET.get('page', 1)
    loaded = paginator.page(page)

    context ={
        'ItemInfo': loaded
    }
    return render(request,'index.html',context)