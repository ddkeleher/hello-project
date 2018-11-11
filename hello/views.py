from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):

    fulltext = request.GET['fulltext']

    wordCount = fulltext.split()

    wordDictionary = {}

    for word in wordCount:
        if word in wordDictionary:
            #Increase
            wordDictionary[word] += 1
        else:
            #Add to dictionary
            wordDictionary[word] = 1
    
    sortedDictionary = sorted(wordDictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext, 'wordcount':len(wordCount), 'sortedDictionary':sortedDictionary})

def about(request):
    return render(request, 'about.html')