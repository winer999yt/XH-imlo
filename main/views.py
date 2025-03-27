from django.shortcuts import render
from .models import *

def index_view(request):
    correct = None
    incorrects = None

    word = request.GET.get('word')

    if word is not None:

        if 'x' not in word and 'h' not in word.lower():
            context = {
                'word': word,
                'message': "So'z tarkibida 'Hh' yoki 'Xx' mavjud emas!",
            }
            return render(request, 'index.html', context)

        word = word.lower()
        corrects = Correct.objects.filter(word=word)
        if corrects.exists():
            correct = corrects.first()
            incorrects = Incorrect.objects.filter(correct=correct)
        else:
            incorrects = Incorrect.objects.filter(word=word)
            if incorrects.exists():
                correct = incorrects.first().correct
                incorrects = Incorrect.objects.filter(correct=correct)
            else:
                context = {
                    'word': word,
                    'message': "Ushbu so'z mavjud emas!",
                }
                return render(request, 'index.html', context)

    context = {
        'correct' : correct,
        'incorrects' : incorrects,
    }
    return  render(request, 'index.html', context)
