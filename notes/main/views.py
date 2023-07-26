from django.shortcuts import render,redirect,get_object_or_404,redirect
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


class modify(View):
    def get(self,request,note_id):
        
        notes=get_object_or_404(note, id=note_id)
        text=notes.desc
        return render(request,"modify.html",{'text':text})
    
    def post(self,request,note_id):
         if 'form' in request.POST:
            notes=note.objects.get(id=note_id)
            notes.desc=request.POST.get('body')
            notes.save()
         else:
           notes=note.objects.get(id=note_id)
           notes.delete()
             
         return redirect('notes')

class Delete(View):
    def get(self,request):
        notes=note.objects.all()
        

      
        return render(request,"index.html",{'texts':notes})
    
    def post (self,request,note_id):
        notes=note.objects.get(id=note_id)
        notes.delete()
        return redirect('del', notes.id)