from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'sentiment_index.html') 

# Define the sentiment_analysis view
def sentiment_analysis(request):

    if request.method == 'POST':
        return render(request, 'sentiment_index.html')
    
    if request.method == 'GET':
        return render(request, 'sentiment_index.html')
    
    return render(request, 'sentiment_index.html')