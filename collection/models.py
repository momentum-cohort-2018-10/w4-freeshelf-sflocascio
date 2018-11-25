from django.db import models

# Create your models here.


BOOK_CATAGORY = (
    ('python', 'Python'),
    ('ruby', 'Ruby'),
    ('javascript', "Javascript"),
)


class Book(models.Model):
    name = models.CharField(max_length=255, null=True, blank=False)
    author = models.CharField(max_length=255, null=True, blank=False)
    description = models.TextField(max_length=255, null=True, blank=False)
    catagory = models.CharField(max_length=20, null=True, blank=False, choices=BOOK_CATAGORY)
    date_added = models.DateField(auto_now=False, auto_now_add=True)
    slug = models.SlugField(unique=True)

def save(self, *args, **kwargs):
        #this line below give to the instance slug field a slug name
        self.slug = slugify(self.name)
        #this line below save every fields of the model instance
        super(Book, self).save(*args, **kwargs)

    # def get_details(self):
    #     details = []
    #     details.append