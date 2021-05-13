from django.http import HttpResponse
from django.shortcuts import render
from .forms import CardForm

# Create your views here.


def append_strike(request):
    if request.method == 'POST':
        form = CardForm(request.POST)
        test = request.POST.getlist('files')
        if form.is_valid():
            # card = Cards.objects.create(**form.cleaned_data)
            print(test)
            # print(request.POST)
            # card = form.save()
    else:
        form = CardForm()
    return render(request, 'strike/append_strike.html', {'form': form})
