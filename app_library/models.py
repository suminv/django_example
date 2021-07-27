from django.db import models




class Publisher(models.Model):
    name = models.CharField(max_length=30)
    genre = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    is_active = models.BooleanField()

    def __str__(self):
        return f'{self.id}. {self.name} ({self.country}, {self.city})'


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    biography = models.TextField()
    city = models.CharField(max_length=30, null=True)
    country = models.CharField(max_length=30, null=True)
    university = models.CharField(max_length=30, null=True)
    birth_date = models.DateTimeField(null=True)
    description = models.TextField(max_length=300, null=True)
    phone = models.IntegerField(null=True)
    personal_page = models.URLField(null=True)
    facebook = models.CharField(max_length=50, null=True)
    twitter = models.CharField(max_length=50, null=True)



    def __str__(self):
        return f'{self.id}. {self.first_name} {self.last_name}'



class Book(models.Model):
    STATUS_CHOICES = [
    ('d', 'Draft'),
    ('r', 'Review'),
    ('p', 'Published'),
]
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_data = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')
    