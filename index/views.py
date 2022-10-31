from django.shortcuts import render

from .models import Category, Topic, Language, Library, Spell

# Create your views here.
def index_view(request):
    category_list = Category.objects.all()
    topic_list = Topic.objects.all()
    language_list = Language.objects.all()
    library_list = Library.objects.all()
    spell_list = Spell.objects.all()

    return render(request, 'index/list.html', {'category_list': category_list, \
                                                'topic_list': topic_list, \
                                                'language_list': language_list, \
                                                'library_list': library_list, \
                                                'spell_list': spell_list
                                                })

def python_view(request):
    category_list = Category.objects.all()
    library_list = Library.objects.all()
    spell_list = Spell.objects.filter(language_name__iexact='python')
    return render(request, 'index/python.html', {'category_list': category_list, \
                                                'library_list': library_list, \
                                                'spell_list': spell_list
                                                })



