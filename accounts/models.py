from django.db import models

#class CreateAccount(models.Model):
#    email_addres = models.CharField(max_length = 50)
#    full_name = models.CharField(max_length = 50)
#    password = models.CharField()
#    confirm_password = models.CharField()
#    user_name = models.CharField()
#
#    def __unicode__(self):
#        return user_name





#class Category(models.Model):
#    category_name = models.CharField(max_length = 30)
#
#    def cat_name(self):
#        return self.category_name
#
#    def __unicode__(self):
#        return self.category_name
#
#class FileUpload(models.Model):
#    file_upload = models.FileField(upload_to = 'files')
#
#class Product(models.Model):
#    product_name = models.CharField(max_length = 50)
#    category = models.ForeignKey(Category)
#    files = models.ManyToManyField(FileUpload)
#
#    def __unicode__(self):
#        return self.product_name
#
#
#class User(models.Model):
#    user_name = models.CharField(max_length = 60)
#    user_email = models.EmailField()
#    categories = models.ManyToManyField(Category)
#
#    def __unicode__(self):
#        return self.user_name
#
#class Basket(models.Model):
#    user = models.ForeignKey(auth.models.User)
#    product = models.ForeignKey(Product)
#
#    def __unicode_(self):
#        return self.auth_user
