from django.db import models

# Create your models here.
class ItemList(models.Model):
    category_name = models.CharField(max_length=15)
    def __str__(self):
        return self.category_name
 

class Item(models.Model):
    item_name = models.CharField(max_length=15)
    description = models.TextField(blank=False)
    price = models.IntegerField()
    category = models.ForeignKey(
        ItemList,
        related_name="category_items",  # Use a unique related_name
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='items/')
    def __str__(self):
        return self.item_name

class AboutUs(models.Model):
    description = models.TextField(blank=False)

class FeedBack(models.Model):
    user_name = models.CharField(max_length=15)
    description = models.TextField(blank=False)
    rating = models.IntegerField()
    image = models.ImageField(upload_to='items/',blank=True)
    def __str__(self):
        return self.user_name
    

class BookTable(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    total_person = models.IntegerField()
    booking_data = models.DateField()

    def __str__(self):
        # Return a meaningful string representation of the object
        return f"{self.name} - {self.booking_data.strftime('%Y-%m-%d')}"
