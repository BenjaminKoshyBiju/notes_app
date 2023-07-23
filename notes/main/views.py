from django.shortcuts import render,redirect
from django.views import View
from .models import note

# Create your views here.
class index(View):
    def get(self,request,notes_id):
        noteid = note.objects.get(id=notes_id)
        notes=note.objects.all()
        context = {
           'noteid':noteid,
           'notes':notes
              }
        return render(request,"index.html",context)
    
    def post(self,request):
        notes=note.objects.create(
            body=request.POST.get('body')
        )
        notes.save()
        return redirect('notes')
