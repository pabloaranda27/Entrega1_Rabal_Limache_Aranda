from django.shortcuts import render, redirect
from articulos.models import Articles
from articulos.forms import Form_articles

def nuevo_articulo(request):
    if request.method == 'POST':
        form=Form_articles(request.POST)
        if form.is_valid():
            Articles.objects.create(
                name=form.cleaned_data['name'],
                price=form.cleaned_data['price'],
                description=form.cleaned_data['description'],
                stock=form.cleaned_data['stock'],
            )
            return redirect(lista_articulos)

    elif request.method == 'GET':
        form=Form_articles()
        context={'form':form}
        return render (request,'articulos/nuevo_articulo.html',context=context)

def lista_articulos(request):
    articles=Articles.objects.all()
    context={'articles':articles}
    return render (request,'articulos/lista_articulos.html',context=context)

def buscar_articulo(request):
    search=request.GET['search']
    articles=Articles.objects.filter(name__icontains=search)
    context={'articles':articles}
    return render (request,'articulos/buscar_articulo.html',context=context)