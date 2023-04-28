from django.shortcuts import render, redirect, get_object_or_404
from index.models import Category, Notes
from index.forms import NotesForm


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


# @login_required
def add_note(request):
    """add notes"""

    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            result_note = form.save(commit=False)
            result_note.save()
            return redirect('index:category', result_note.category_id)
    else:
        form = NotesForm
    return render(request, 'index/forms/add_note.html', {'form': form})


# @login_required
def edit_note(request, id):
    note = get_object_or_404(Notes, pk=id)
    form = NotesForm(request.POST, instance=note)
    if request.method == 'POST':
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('index:category', note.category_id)
    else:
        form = NotesForm(instance=note)
    return render(request, 'index/forms/edit_note.html', {'form': form,
                                                          'notes': note})


# @login_required
def delete_notes(request, id):
    """delete note"""
    note_del = get_object_or_404(Notes, id=id)
    note_id = note_del.id
    note_del.delete()
    return redirect('index:category', note_del.category_id)
