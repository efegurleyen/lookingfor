from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import ProductForm
from django.contrib import messages
from .models import Product,Comment
from django.contrib.auth.decorators import login_required
# Create your views here.
def products(request):
    keyword = request.GET.get("keyword")
    if keyword:
        products = Product.objects.filter(title__contains = keyword)
        return render(request,"products.html",{"products":products})

    products = Product.objects.all()
    return render(request,"products.html",{"products":products})
def index(request):

    return render(request,"index.html")

def about(request):
    return render(request,"about.html")
@login_required(login_url="user:login")
def dashboard(request):
    products = Product.objects.filter(author = request.user)
    context = {
        "products":products
    }
    return render(request,"dashboard.html",context)
@login_required(login_url="user:login")
def addproduct(request):
    form = ProductForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        product = form.save(commit=False)
        product.author = request.user
        product.save()
        messages.success(request,"Ürün eklendi.")
        return redirect("product:dashboard")
    return render(request,"addproduct.html",{"form":form})

def detail(request,id):

    product = get_object_or_404(Product,id=id)
    comments = product.comments.all()
    return render(request,"detail.html",{"product":product,"comments":comments})
@login_required(login_url="user:login")
def updateProduct(request,id):
    product = get_object_or_404(Product,id=id)
    form = ProductForm(request.POST or None,request.FILES or None,instance=product)
    if form.is_valid():
        product = form.save(commit=False)
        product.author = request.user
        product.save()
        messages.success(request,"Ürün güncellendi.")
        return redirect("product:dashboard")
    return render(request,"update.html",{"form":form})
@login_required(login_url="user:login")
def deleteProduct(request,id):
    product = get_object_or_404(Product,id=id)
    product.delete()
    messages.success(request,"Ürün silindi.")
    return redirect("product:dashboard")

def addComment(request,id):
    product = get_object_or_404(Product,id = id)
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        newComment = Comment(comment_author = comment_author,comment_content=comment_content)
        newComment.product = product
        newComment.save()
    return redirect(reverse("product:detail",kwargs={"id":id}))