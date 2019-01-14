from django.db import models
from django.utils.text import slugify
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
    slug = models.SlugField(max_length=140, unique=True)
    link = models.CharField(max_length=255, null=True, blank=False)
    address = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
 
    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Book.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)



# def save(self, **kwargs):
#     slug_str = "%s %s" % (self.name, self.author, self.author, self.author, self.author,) 
#     unique_slugify(self, slug_str) 
#     super(Need, self).save(**kwargs)

    # def get_details(self):
    #     details = []
    #     details.append