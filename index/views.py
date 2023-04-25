from django.shortcuts import render
from index.models import Category, Notes


def index(request):
    """list of countries"""
    hello = "hello world"
    category_list = Category.objects.all()
    context_dict = {'categories': category_list}

    for category in category_list:
        category.url = category.title.replace(' ', '_')

    return render(request, 'index/list_categorys.html', context_dict)



def category(request, category_id):

    context_dict = {}

    try:

        category = Category.objects.get(id=category_id)
        notes = Notes.objects.filter(category=category)
        context_dict['notes'] = notes
        context_dict['category'] = category


    except Category.DoesNotExist:
        pass

    return render(request, 'index/category.html', context_dict)