from django.db import models
from django.contrib.auth.models import User
from books.models import Book

class Borrowing(models.Model):
    borrower_name = models.CharField(max_length=100)
    borrowed_on = models.DateField(auto_now_add=True)
    return_date = models.DateField()

    def __str__(self):
        return self.borrower_name
