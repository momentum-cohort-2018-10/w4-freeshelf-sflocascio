# from django.core.management.base import BaseCommand
# from django.conf import settings
# import os.path
# import csv
# from books.models import Book
# from django.core.files import File

# def get_path(file):
#     return os.path.join(settings.BASE_DIR, 'freeshelf', file)

# class Command(BaseCommand):
#     help = "My shiny new management command."

#     def add_arguments(self, parser):
#         # parser.add_argument('sample', nargs='+')
#         pass

#     def handle(self, *args, **options):
#         print("deleting books...")
#         Book.objects.all().delete()
#         with open(os.path.join(settings.BASE_DIR, 'initial_data', 
#                                 'books.csv')) as file:
#             reader = csv.DictReader(file)
#             for row in reader:
#                 book = Book(
#                     name=row['name'],
#                     author=row['author'],
#                     description=row['description'],
#                     catagory=row['catagory'],
#                 )
#                 book.picture.save(row['image'],
#                                 File(open(get_path(row['image']), 'rb')))
#                 book.save()
#         print("books loaded!")

