from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306275014',
        'name': 'Vincent Davis Leonard Tjoeng',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
# Create your views here.
