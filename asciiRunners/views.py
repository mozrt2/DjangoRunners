from django.shortcuts import render
from django.http import HttpResponse
from .forms import RunnerForm

from asciiRunners.convert import grayscale_array, grayscale_array_to_string, select_characters
from asciiRunners.getsvg import get_converted_svg

# Create your views here.
def index(request):
    return render(request, 'index.html')

def runner(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RunnerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            id = form.cleaned_data['runner_id']
            contrast_mode = form.cleaned_data['contrast_mode']
            character_type = form.cleaned_data['character_type']
            ascii = select_characters(character_type)
            step1 = grayscale_array(get_converted_svg(id),ascii,0)
            print(step1, "STEP1")
            output = grayscale_array_to_string(step1[0],step1[1],step1[2],step1[3],ascii,int(contrast_mode))
            print(output, "OUTPUT")
            # redirect to a new URL:
            return HttpResponse(output)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RunnerForm()

    return render(request, 'index.html', {'form': form})

def results(request):
    return render(request, 'results.html', {'result':id})

