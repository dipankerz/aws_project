# myapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NameSearchForm, PersonForm
from .models import Person

def name_search_view(request):
    if request.method == 'POST':
        form = NameSearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            try:
                person = Person.objects.get(name=name)
                return render(request, 'myapp/person_details.html', {'person': person})
            except Person.DoesNotExist:
                return redirect('add_person', name=name)
    else:
        form = NameSearchForm()

    return render(request, 'myapp/name_search.html', {'form': form})

def add_person_view(request, name):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('name_search')
    else:
        form = PersonForm(initial={'name': name})

    return render(request, 'myapp/add_person.html', {'form': form})
