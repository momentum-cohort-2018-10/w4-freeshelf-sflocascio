from django.shortcuts import render
from collection.models import Book
# from collection.forms import SearchForm


# Create your views here.
def index(request):
    # form = SearchForm()
    books = Book.objects.all()
    address = "6 Ozark Court Durham North Carolina"
    

    response = render(request, 'index.html', {
        'books': books,
        'address': address, 
        # 'form': form,
    })

    return response

def book_detail(request, slug):
    book = Book.objects.get(slug=slug)
    return render(request, 'books/book_detail.html', {
        'book': book,
    })


def browse_by_name(request, initial=None):
    if initial:
        books = Book.objects.filter(
            name__istartswith=initial).order_by('name')
    else:
        books = Book.objects.all().order_by('name')
    return render(request, 'search/search.html', {
        'books': books,
        'intitial': initial,
    })
        
