from django.shortcuts import render

# Create your views here.
def dashboard(request):
    c_p = request.GET.get('query','home')

    c= {
        "c": c_p
    }

    if c_p == 'orders':
        pass
    if c_p == "wishlist":
        pass

    return render(request,'pages/dashboard.html',c)