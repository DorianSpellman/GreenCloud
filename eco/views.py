from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *
from django.db.models import Q

menu = [
    {'title' : 'главная', 'url_name' : 'info'}, 
    {'title' : 'коды', 'url_name' : 'codes'}, 
    {'title' : 'карта', 'url_name' : 'map'}, 
]


#  1 PAGE

def infopage(request): #HttpRequest
    posts = Info.objects.all()

    context = {
        'title' : 'GreenCloud',
        'menu' : menu,
        'posts': posts, 
    }

    return render(request, 'eco/_main.html',  context=context)



#  2 PAGE


def codespage(request): 
    search_query = request.GET.get('search', '')

    if search_query:
        try: 
            search = int(search_query)
        except:
            material = Codes.objects.filter(Q(ident__icontains=search_query.upper()))
        else:
            material = Codes.objects.filter(Q(code=search))

        

        if len(material) == 0:
            material = ['']
    else:
        material = Codes.objects.all()

    types = Type.objects.all()

    context = {
        'title' : 'GC: Коды переработки',
        'menu' : menu,
        'types' : types,
        'material': material,
        'selected' : 0
    }
   

    return render(request, 'eco/_codes.html', context=context)

def type(request, type_name): 
    material = Codes.objects.filter(slug=type_name)
    types = Type.objects.all()

    context = {
        'title' : f'GC: {type_name}',
        'menu' : menu,
        'types' : types,
        'material': material,
        'selected' : type_name,
    }

    if len(material) == 0:
        raise Http404

    return render(request, 'eco/_codes.html', context=context)


#  3 PAGE

def mappage(request): 
    context = {
        'title' : 'GC: Карта',
        'menu' : menu,
    }

    return render(request, 'eco/_map.html', context=context)

    





def pageNotFound(request, exception):
    return HttpResponseNotFound('<center>Увы, такой страницы не существует...</center>')
