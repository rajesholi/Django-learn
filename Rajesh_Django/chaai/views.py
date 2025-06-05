# from django.shortcuts import render

# # Create your views here.
# def chaai(request):
#     return render(request='chaai/chai-index.html')

from django.shortcuts import render

def chaai(request):
    # Provide the template name here, e.g., 'chaai/index.html'
    return render(request, 'chaai/chai-index.html')  # Add your correct template path