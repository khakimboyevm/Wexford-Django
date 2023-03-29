from django.shortcuts import render, redirect
from .models import Category, Seakers, Buy
from .forms import ChoiceForm
# Create your views here.

def home(requests):
    ctg = Category.objects.all()
    seaker = Seakers.objects.all()
    ctx = {
        'ctg':ctg,
        'seaker':seaker
    }
    return render(requests, 'blog/index.html', ctx)

def contact(requests):
    ctx = {}
    return render(requests, 'blog/contact.html', ctx)

def products(requests, slug=None):
    ctg = Category.objects.all()
    category = Category.objects.get(slug=slug)
    seaker = Seakers.objects.all().filter(type_id=category.id)
    ctx = {
        'ctg':ctg,
        'category':category,
        'seaker':seaker
    }
    return render(requests, 'blog/products.html', ctx)

def register(requests):
    ctx = {}
    return render(requests, 'blog/register.html', ctx)

def single(requests, pk=None):
    ctg = Category.objects.all()
    products_pk = Seakers.objects.get(pk=pk)
    form = ChoiceForm()
    if requests.POST:
        forms = ChoiceForm(requests.POST or None,
                           requests.FILES or None)
        if forms.is_valid():
            root = forms.save()
            root = Buy.objects.get(pk=root.id)
            root.products = products_pk
            root.save()
            return redirect('home')
        else:
            print(forms.errors)
    ctx = {
        'ctg':ctg,
        'product_pk':products_pk,
        'form':form,
    }
    return render(requests, 'blog/single.html', ctx)