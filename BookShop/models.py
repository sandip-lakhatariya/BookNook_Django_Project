from django.db import models

# Create your models here.

class Book(models.Model):
    book_id = models.AutoField
    book_name = models.CharField(max_length=50)
    front_image = models.ImageField(upload_to="images/")
    back_image = models.ImageField(upload_to="images/")
    price = models.IntegerField()
    author_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    publisher_name = models.CharField(max_length=50)
    book_language = models.CharField(max_length=10)
    book_page = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.book_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Message = models.CharField(max_length=300)

    def __str__(self):
        return self.First_name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_item = models.CharField(max_length=5000, default="")
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    city = models.CharField(max_length=50, default="")
    zip_code = models.IntegerField(default=0)
    address = models.CharField(max_length=500, default="")
    email = models.EmailField(max_length=50, default="")
    total_price = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name
    
class Customer(models.Model):
    user_id = models.CharField(max_length=10, primary_key=True, unique=True)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    mobile = models.IntegerField()
    email_address = models.EmailField(max_length=50)
    address = models.TextField(max_length=200)

class Payment(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Review(models.Model):
    review = models.TextField(max_length=200)
    rating = models.IntegerField()
    user_id = models.ForeignKey(Customer, on_delete=models.CASCADE)