from django.db import models
from django.contrib.auth.hashers import make_password, check_password
import base64

class UserDriver(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    username = models.TextField()
    email = models.EmailField(unique=True)
    password = models.TextField()
    hp = models.TextField()
    photo = models.ImageField(upload_to='static/user_photos/', default='default_user.png')
    lat = models.DecimalField(max_digits=9, decimal_places=6, default=-6.1661686)
    lon = models.DecimalField(max_digits=9, decimal_places=6, default=106.8717686)
    level = models.TextField(default="driver")
    created_at = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        # Hash password sebelum menyimpan
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
    def get_photo_base64(self):
        if self.photo:
            with open(self.photo.path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode('utf-8')
        return None
    
class UserCustomer(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    customer_name = models.TextField()
    address  = models.TextField()
    cp = models.TextField()
    hp = models.TextField()
    photo = models.ImageField(upload_to='static/customer_photo/', default='default_user.png')
    lat = models.DecimalField(max_digits=9, decimal_places=6, default=-6.1661686, blank=True, null=True)
    lon = models.DecimalField(max_digits=9, decimal_places=6, default=106.8717686, blank=True, null=True)
    created_at = models.DateField(auto_now=True)
    
    def get_photo_base64(self):
        if self.photo:
            with open(self.photo.path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode('utf-8')
        return None
    
class Delivery(models.Model):
    no_delivery = models.TextField(primary_key=True,unique=True)
    date = models.DateField()
    customer_name = models.TextField(null=True)
    address = models.TextField()
    cust_lat = models.DecimalField(max_digits=9, decimal_places=6,null=True)
    cust_lon = models.DecimalField(max_digits=9, decimal_places=6,null=True)
    cp = models.TextField()
    hp = models.TextField()
    driver_name = models.TextField()
    driver_lat = models.DecimalField(max_digits=9, decimal_places=6, default=-6.1661686)
    driver_lon = models.DecimalField(max_digits=9, decimal_places=6, default=106.8717686)
    photo = models.ImageField(upload_to='static/delivery_image/', default='default_user.png')
    status = models.TextField(default="Pickup")
    def get_photo_base64(self):
        if self.photo:
            with open(self.photo.path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode('utf-8')
        return None
    