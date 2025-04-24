from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from fileuploads.forms import UserDataForm
from relationships.settings import MEDIA_ROOT
from fileuploads.models import UserData

# Create your views here.
def home(request):
    print("MEDIA_ROOT is:", MEDIA_ROOT)
    try:
        if request.method == 'POST':
            form = UserDataForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/f/home/')
        else:
            form = UserDataForm()
        return render(request, 'fileuploads/home.html', {'form':form})
    except:
        raise Exception("There is some error while saving")
    
def serve(request):
    files = UserData.objects.all()
    return render(request, 'fileuploads/image_list.html', {'files':files})