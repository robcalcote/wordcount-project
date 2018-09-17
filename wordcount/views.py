from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def eggs(request):
    return HttpResponse('<h1>YO WHATSUP</h1>')

def count(request):
    #variable that receives the text from fulltext form
    fulltext = request.GET['fulltext']

    #variable WORDLIST splits the text from fulltext
    wordlist = fulltext.split()

    worddict = {}

    #This loop will increment words that are added to the library if they have previously appeared
    for word in wordlist:
        if word in worddict:
            #Increase
            worddict[word] += 1
        else:
            #add to the dictionary and don't increment
            worddict[word] = 1

    sortedwords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

    #the redirect to the results after you're clicked "count the words!"
    #also creates a new dictionary containing "fulltext", and "count" - gives the amount of words
    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'sortedwords':sortedwords})

def about(request):
    return render(request, 'about.html')