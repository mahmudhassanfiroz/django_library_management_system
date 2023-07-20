from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13)
    publication_date = models.DateField()
    genre = models.CharField(max_length=255)
    availability = models.BooleanField(default=True)
    num_available_books = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.title

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reservation_date = models.DateField()

class Borrowed_book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    returned_date = models.DateField(null=True, blank=True)
    fine_amount = models.DecimalField(max_digits=6, decimal_places=2)
    
    def calculate_fine(self):
        
        if self.returned_date: 
            self.fine_amount = self.due_date - self.returned_date
            self.save()
        else:
            self.fine_amount = 0

        
        
    
    def save(self, *args, **kwargs):
        if self.returned_date:
            self.calculate_fine()
        super(Borrowed_book, self).save(*args, **kwargs)

class Borrow_request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    request_date = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)

class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reminder_date = models.DateField(auto_now_add=True)


class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    books = models.ManyToManyField('Book')

    def __str__(self):
        return self.user.username + " 's Wishlist"