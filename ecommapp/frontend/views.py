from django.shortcuts import render
from products.serializers import ProductSerializer
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.test import APIRequestFactory
from products.models import Products
from django.core.paginator import Paginator
from django.db.models import Max,Min

def main(request):
    return render(request,'pages/index.html')

class ProductsSerial(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Products.objects.all()
    permission_classes = (AllowAny,)

def productview(request):
    search_q = request.GET.get('search','')
    price_from_request = request.GET.get('price')
    factory_object = APIRequestFactory()
    api_call = factory_object.get("/products/api")

    api_view = ProductsSerial.as_view()
    api_response = api_view(api_call)

    api_data = api_response.data
    prices = [float(i.get('price',0)) for i in api_data if i.get('price') is not None]
    max_limit = max(prices) if prices else 88
    min_limit = min(prices) if prices else 0

    try:
        input_price = float(price_from_request) if price_from_request is not None and price_from_request != '' else min_limit
    except ValueError:
        input_price = max_limit

    filtered_data_from_api = []

    for a in api_data:
        name = a.get('name','')
        price = float(a.get('price',0))

        matches_search = not search_q or (search_q.lower() in name.lower())
        matches_price = price >= input_price

        if matches_search and matches_price:
            filtered_data_from_api.append(a)
        
    paginator = Paginator(filtered_data_from_api,3)
    p_n = request.GET.get('page',1)
    page_obj = paginator.get_page(p_n)

    c = {
        'page_obj':page_obj,
        'q': search_q,
        'min_p': min_limit,
        'max_p': max_limit,
        'input_pr': input_price
    }

    return render(request,"pages/products.html",c)

def contact(request):
    return render(request,"pages/contact.html")


