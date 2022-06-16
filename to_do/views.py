from django.shortcuts import redirect, render
from .models import add

# Create your views here.
def index(request):
  todo=add.objects.all()
  if request.method=="POST":
        todo=request.POST['title']
        if todo:
          a=add(
          todo=todo
         )
        
          a.save()
          todo=add.objects.all()
          return render(request,"to_do/index.html",{
    "todo":todo,
  }
  )
        else:
         return redirect('index')
  return render(request,"to_do/index.html",{
    "todo":todo,
  }
  )

def delete(request,pk):


    
  todo=add.objects.get(id=pk)
    
  todo.delete()
  todo=add.objects.all()
  return redirect('index')


