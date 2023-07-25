from django.shortcuts import render,redirect
from django.views import View
from .models import note

# Create your views here.

class index(View):
    
    def get(self,request):
        notes=note.objects.all()
        
        
        return render(request,"index.html",{'texts':notes})
    
    def post(self,request):
        notes=note.objects.create(
            desc=request.POST.get('body')
        )
        notes.save()
        return redirect('notes')
