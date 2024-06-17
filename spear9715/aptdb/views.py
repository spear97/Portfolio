from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'aptdb_index.html')

def search(request):
    return render(request, 'aptdb_results.html')