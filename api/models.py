from django.db import models

# Create your models here.


class Header(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    background_image = models.ImageField(upload_to='header_background_img/')

    def __str__(self):
        return self.title
    
class Popular_destination(models.Model):
    sub_heading = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Popular_destination_img/')
    city = models.CharField(max_length=200)
    stars = models.PositiveIntegerField()
    heading = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.heading
    
class Packages(models.Model):
    sub_heading = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Popular_destination_img/')
    heading = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    days_nights = models.CharField(max_length=100)
    pax = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    review_count = models.CharField(max_length=100)
    stars = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.heading
    
class Photo_gallery(models.Model):
    sub_heading = models.CharField(max_length=100)
    images = models.ImageField(upload_to='Photo_gallery/')

    def __str__(self):
        return f'Photos'
    
    
class Call_to_action(models.Model):
    heading = models.CharField(max_length=100)
    sub_heading = models.CharField(max_length=100)

    def __str__(self):
        return self.heading

    
class footer(models.Model):
    description = models.CharField(max_length=100)
    date = models.CharField(max_length=10)

    def __str__(self):
        return self.date
    

    






    

