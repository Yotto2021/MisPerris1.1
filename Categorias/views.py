from django.shortcuts import render
from Categorias.models import Category, Article

# Create your views here.
def articles(request):

    articles = Article.objects.all()

    return render(request, 'Articulos.html', {
        'articles' : articles
 })