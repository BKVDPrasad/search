from django.shortcuts import render,redirect
from .models import Person
from django.db.models import Q
from django.contrib.postgres.search import SearchVector
from django.contrib import messages


# Create your views here.
def show(request):
    return render(request,'main.html',{'p':Person.objects.all()})


def article_overview(request):
    search_term = ''

    if 'search' in request.GET:
        search_term = request.GET['search']
        articles = Person.objects.all().filter(feeder__icontains=search_term)

    articles = Person.objects.filter(name=search_term)

    #return render(request, 'main.html', {'articles' : articles, 'search_term': search_term })
    return render(request, 'main.html', {'articles': articles, 'search_term': search_term})

def search(request):
    your_search_query=''
    #res = Person.objects.annotate(search=SearchVector('name', 'pho', 'age'),).filter(search=your_search_query)
    if request.method =='GET':
        data=request.GET.get('search')
        print(data)
        if data:
            res=Person.objects.all().filter(Q(name__icontains=data)|Q(gender__istartswith=data))
            if res:
                return render(request,'search.html',{'res':res})
            else:
                messages.error(request,'no data found')
                return render(request,'search.html')
        else:
            return redirect('/')

    else:
        return redirect('/')