from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Product(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Kullanıcı Adı" )
    title = models.CharField(max_length = 50,verbose_name = "Ürün Adı")
    properties = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name = "İlan Tarihi")
    product_image = models.FileField(blank = True,null = True,verbose_name="Ürün fotoğrafı ekleyin")
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_date']
class Comment(models.Model):
    product = models.ForeignKey(Product,on_delete = models.CASCADE,verbose_name = "Ürün",related_name="comments")
    comment_author = models.CharField(max_length= 50,verbose_name = "İsim")
    comment_content = models.CharField(max_length= 200,verbose_name = "Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']