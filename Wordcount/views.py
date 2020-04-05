from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html');

def count(request):
    data = request.GET['fulltextarea']
    word_list = data.split()
    print(word_list)
    word_list_length = len(word_list)
    word_dictioary = {}
    for word in word_list:
        if word in word_dictioary:
            word_dictioary[word] += 1
        else:
            word_dictioary[word] = 1
    
    sorted_word_dictioary = sorted(word_dictioary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': word_list_length, 'word_dictioary':sorted_word_dictioary});

def contact(request):
    return HttpResponse("<h1>Contact US</h1>");