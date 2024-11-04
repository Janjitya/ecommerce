from django.shortcuts import render
from .models import Products, Order
from django.core.paginator import Paginator

# Create your views here.
def index(request):

    products = Products.objects.all()

    #searching code
    item_name = request.GET.get("item_name")
    if item_name != '' and item_name is not None:
        products = products.filter(title__icontains=item_name)

    #pagination code
    pagi = Paginator(products,4)
    page = request.GET.get('page')
    products = pagi.get_page(page)

    context = {'products':products}
    return render(request, "shop/index.html", context=context)

def detail(request, product_id):

    product = Products.objects.get(id=product_id)
    context = {'product':product}
    return render(request, "shop/product-detail.html", context=context)

def checkout(request):

    if(request.method == "POST"):
        items = request.POST.get("items","")
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        address = request.POST.get('address',"")
        city = request.POST.get('city',"")
        state = request.POST.get('state',"")
        zip = request.POST.get('zip',"")
        total = request.POST.get('total',"")

        order = Order(items=items, name=name, email=email, address=address, city=city, state=state, zip=zip, total=total)
        order.save()

    return render(request, "shop/checkout.html")
