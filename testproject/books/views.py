# Create your views here.

from django.http import HttpResponse
from books.models import Books
from django.template import Context, loader

def index(request):
	books_list = Books.objects.all()
	t = loader.get_template('books/index.html')
	c = Context({'books_list': books_list,})
	return HttpResponse(t.render(c))
