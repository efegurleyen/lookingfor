from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "product"

urlpatterns = [
    path('dashboard/',views.dashboard,name="dashboard"),
    path('addproduct/',views.addproduct,name="addproduct"),
    path('product/<int:id>',views.detail,name="detail"),
    path('update/<int:id>',views.updateProduct,name="update"),
    path('delete/<int:id>',views.deleteProduct,name="delete"),
    path('',views.products,name="products"),
    path('comment/<int:id>',views.addComment,name="comment"),
]
