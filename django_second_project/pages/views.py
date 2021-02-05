from django.shortcuts import render

# Create your views here.
def home(request):
    my_context = {"my_text":"This is about home page", "my_number":123}
    return render(request, 'home.html', my_context)
