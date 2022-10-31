from django.shortcuts import render

from .models import Category, Topic, Language, Library, Spell

# Create your views here.
def index_view(request):
    category_list = Category.objects.all().order_by('name')
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
    language_list = Language.objects.filter(name__iexact='python')
    library_list = Library.objects.filter(language_name__iexact='python')
    spell_list = Spell.objects.filter(language_name__iexact='python').order_by('forwhat')
    return render(request, 'index/python.html', {'category_list': category_list, \
                                                'language_list': language_list, \
                                                'library_list': library_list, \
                                                'spell_list': spell_list
                                                })

def git_view(request):
    category_list = Category.objects.all()
    language_list = Language.objects.filter(name__iexact='git')
    library_list = Library.objects.filter(language_name__iexact='git')
    spell_list = Spell.objects.filter(language_name__iexact='git').order_by('forwhat')
    return render(request, 'index/git.html', {'category_list': category_list, \
                                                'language_list': language_list, \
                                                'library_list': library_list, \
                                                'spell_list': spell_list
                                                })

def solidity_view(request):
    category_list = Category.objects.all()
    language_list = Language.objects.filter(name__iexact='solidity')
    library_list = Library.objects.filter(language_name__iexact='solidity')
    spell_list = Spell.objects.filter(language_name__iexact='solidity').order_by('forwhat')
    return render(request, 'index/solidity.html', {'category_list': category_list, \
                                                'language_list': language_list, \
                                                'library_list': library_list, \
                                                'spell_list': spell_list
                                                })

def js_view(request):
    category_list = Category.objects.all()
    language_list = Language.objects.filter(name__iexact='js')
    library_list = Library.objects.filter(language_name__iexact='js')
    spell_list = Spell.objects.filter(language_name__iexact='js').order_by('forwhat')
    return render(request, 'index/js.html', {'category_list': category_list, \
                                                'language_list': language_list, \
                                                'library_list': library_list, \
                                                'spell_list': spell_list
                                                })

def ruby_view(request):
    category_list = Category.objects.all()
    language_list = Language.objects.filter(name__iexact='ruby')
    library_list = Library.objects.filter(language_name__iexact='ruby')
    spell_list = Spell.objects.filter(language_name__iexact='ruby').order_by('forwhat')
    return render(request, 'index/ruby.html', {'category_list': category_list, \
                                                'language_list': language_list, \
                                                'library_list': library_list, \
                                                'spell_list': spell_list
                                                })

def rust_view(request):
    category_list = Category.objects.all()
    language_list = Language.objects.filter(name__iexact='rust')
    library_list = Library.objects.filter(language_name__iexact='rust')
    spell_list = Spell.objects.filter(language_name__iexact='rust').order_by('forwhat')
    return render(request, 'index/rust.html', {'category_list': category_list, \
                                                'language_list': language_list, \
                                                'library_list': library_list, \
                                                'spell_list': spell_list
                                                })

def linux_view(request):
    category_list = Category.objects.all()
    language_list = Language.objects.filter(name__iexact='linux')
    library_list = Library.objects.filter(language_name__iexact='linux')
    spell_list = Spell.objects.filter(language_name__iexact='linux').order_by('forwhat')
    return render(request, 'index/linux.html', {'category_list': category_list, \
                                                'language_list': language_list, \
                                                'library_list': library_list, \
                                                'spell_list': spell_list
                                                })
