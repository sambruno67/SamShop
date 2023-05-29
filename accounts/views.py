from django.contrib.auth import get_user_model, login, logout, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from store.models import Product, Cart, Order

# Create your views here.

User = get_user_model()


def signup(request):
    if request.method == "POST":
        # Traiter le formulaire
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create_user(username=username,
                                        password=password)
        login(request, user)
        return redirect('index')
    return render(request, 'accounts/signup.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse("Fas te faire foutre mec!")
    return render(request, 'accounts/login.html')


def logout_user(request):
    logout(request)
    return redirect('index')


def add_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    cart, _ = Cart.objects.get_or_create(user=user)
    #Verifier si une commande pour ce produit existe
    order, created = Order.objects.get_or_create(user=user,
                                                 ordered= False,
                                                 product=product)

    if created:
        #Si une nouvelle commande est creee,l'ajoute au panier
        cart.orders.add(order)
        order.save() #Enregistre les modifications de l'ojet order
    else:
        #Si une commande existe deja, l'incremente
        order.quantity +=1
        order.save() #Enregistre les modificstions de l'objet order

    return redirect(reverse("product", kwargs={"slug":slug}))

def cart(request):
    cart = get_object_or_404(Cart, user=request.user)

    return render(request, 'store/cart.html', context={"orders":cart.orders.all()})

def delete_cart(request):
    if cart:= request.user.cart:
        cart.delete()
    return redirect('index')
