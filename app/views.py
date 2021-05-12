from django.shortcuts import render, redirect
from app.forms import StoresForm
from app.models import Stores
from app.gmaps import Cords
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Stores.objects.filter(city__icontains=search)
    else:
        data['db'] = Stores.objects.all()
    return render(request, 'index.html', data)
    all = Stores.objects.all()
    paginator = Paginator(all, 2)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    return render(request, 'index.html', data)


def form(request):
    data = {'form': StoresForm()}
    return render(request, 'form.html', data)


def create(request):
    form = StoresForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


def view(request, pk):
    data = {'db': Stores.objects.get(pk=pk), 'location': Cords.locations }
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {'db': Stores.objects.get(pk=pk)}
    data['form'] = StoresForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {'db': Stores.objects.get(pk=pk)}
    form = StoresForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
    return redirect('home')


def delete(request, pk):
    db = Stores.objects.get(pk=pk)
    db.delete()
    return redirect('home')
