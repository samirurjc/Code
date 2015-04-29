# Create your views here.

from django.http import HttpResponse,HttpResponseNotFound
import random

firstWords = ["The table", "My uncle", "A book", "The road", "Music"]
secondWords = ["talks", "knows", "thinks", "works", "runs", "eats"]
thirdWords = ["fast", "low", "far away", "hard", "in pijama", 
              "while dances cha-cha-cha"]

def wordsprefix(prefix, words):

    listprefix = []
    for word in words:
        if word.startswith(prefix):
            listprefix.append(word)
    return listprefix

def gimmeword(request, resource):

    if resource == 'first':
        word = random.choice(firstWords)
    elif resource == 'second':
        word = random.choice(secondWords)
    elif resource == 'third':
        word = random.choice(thirdWords)
    else:
        return HttpResponseNotFound('Page not found')
    return HttpResponse(word)

def gimmewordsprefix(request, resource, prefix):

     if resource == 'first':
         words = wordsprefix(prefix, firstWords)
     elif resource == 'second':
         words = wordsprefix(prefix, secondWords)
     elif resource == 'third':
         words = wordsprefix(prefix, thirdWords)
     else:
         return HttpResponseNotFound('Page not found')
     return HttpResponse(str(words))

indexPage = """<!DOCTYPE html>
<html>
  <head>
    <style type="text/css" media="screen">
      body{
        padding:0;
        margin:50px auto;
        text-align: center;
        font:100% Verdana;
      }
      h1 {
        font-size: 1.5em;
      }
    </style>
  </head>
  <body>
    <h1>Words provider applications</h1>    <ul>
      <li><a href="/apps/sentences_generator.html">sentences_generator</a></li>
      <li><a href="/apps/async_sentences_generator.html">async_sentences_generator</a></li>
      <li><a href="/apps/list_words.html">list_words</a></li>
    </ul>
  </body>
</html>
"""

def gimmeindex(request):
    return HttpResponse(indexPage)
