from django.shortcuts import render,redirect
from .models import tutorial,Chapter,Unit,UnitAndChapter,UnitAndTutorial,collection,Request
from .form import requestForm
from django.shortcuts import get_object_or_404
# Create your views here.
def home(request):
    tutorials = tutorial.objects.all()
    req_obj = Request.objects.all()
    return render(request,'home/index.html',{'obj':tutorials,'req':req_obj})

def tut(request):
    tutorials = tutorial.objects.all()
    return render(request,'tutorial/index.html',{'obj':tutorials}) 

def showTut(request,name):
    tut = get_object_or_404(tutorial,id=name)
    try:
        f_unit =UnitAndTutorial.objects.get(Tutorial=tut,index=1)
    except:
        return redirect('tutorial:comming')
    try:
        f_chapter = UnitAndChapter.objects.get(unit=f_unit.unit,index=1).Chapter
    except:
        return redirect('tutorial:comming')
    return redirect('tutorial:chapter',name=name ,slug=f_chapter.slug)

def showchap(request,name,slug):
    obj = []
    next = False
    previous = False
    tut = get_object_or_404(tutorial,id=name)
    chapter = get_object_or_404(Chapter,slug=slug)
    units = tut.units.all()
    c_unit = get_object_or_404(Unit,chapters=chapter)
    index = get_object_or_404(UnitAndTutorial,Tutorial=tut,unit=c_unit).index
    index_2 = get_object_or_404(UnitAndChapter,unit=c_unit,Chapter=chapter).index
    if(index == 1):
        if(index_2 == 1):
            previous = False
        else:
            previous_ch = get_object_or_404(UnitAndChapter,unit=c_unit,index=index_2-1)
            previous ={
                "id":name,
                'chapter':previous_ch.Chapter
            }
        if(not UnitAndChapter.objects.filter(unit=c_unit,index=index_2+1).exists()):
            if(UnitAndTutorial.objects.filter(Tutorial=tut,index=index+1).exists()):
                next_unit = get_object_or_404(UnitAndTutorial,Tutorial=tut,index=index+1).unit
                next_ch = get_object_or_404(UnitAndChapter,unit=next_unit,index=1).Chapter  
                next = {
                "id":name,
                'chapter':next_ch
                }      
        elif(UnitAndChapter.objects.filter(unit=c_unit,index=index_2+1).exists()):
            next_ch = get_object_or_404(UnitAndChapter,unit=c_unit,index=index_2+1).Chapter  
            next = {
                "id":name,
                'chapter':next_ch
            }  
        else:
            next =False
    else:
        if(index_2 == 1):
            c_unit_previos =get_object_or_404(UnitAndTutorial,Tutorial=tut,index=index-1)
            previous_ch = get_object_or_404(UnitAndChapter,unit=c_unit_previos.unit).last()
            previous ={
                "id":c_unit_previos.Tutorial.id,
                'chapter':previous_ch.Chapter
            }
        else:
            previous_ch = get_object_or_404(UnitAndChapter,unit=c_unit,index=index_2-1)
            previous ={
                "id":name,
                'chapter':previous_ch.Chapter
            }
        if(not UnitAndChapter.objects.filter(unit=c_unit,index=index_2+1).exists() and UnitAndTutorial.objects.filter(Tutorial=tut,index=index+1).exists()):
            c_unit_next =get_object_or_404(UnitAndTutorial,Tutorial=tut,index=index+1)
            next_ch = get_object_or_404(UnitAndChapter,unit=c_unit_next.unit,index=1).Chapter
            next ={
                "id":c_unit_next.Tutorial.id,
                'chapter':next_ch
            }           
        elif(UnitAndChapter.objects.filter(unit=c_unit,index=index_2+1).exists()):
            next_ch =get_object_or_404(UnitAndChapter,unit=c_unit,index=index_2+1).Chapter  
            next = {
                "id":name,
                'chapter':next_ch
            }        
    for i in units:
        chapters = i.chapters.all()
        objs = {
            "id" : i.id,
            'title':i.title,
            "chapters" : chapters
        }
        obj.append(objs)
    return render(request,'chapter.html',{'data':obj,'ch':chapter,'tutorialname':tut.name,'name':name,"next":next,"previous":previous})

def showCollection(request):
    obj = collection.objects.all()
    return render(request,'collection/collection.html',{'obj':obj})
def collectionDetail(request,id):
    obj = get_object_or_404(collection,id=int(id)).courses.all()
    return render(request,'collection/collection_detail.html',{'obj':obj})
def sorryPagenotFound(request):
    return render(request,'404.html')
def CommingSoon(request):
    return render(request,'Comming Soon.html')
def courseRequest(request):
    myform = requestForm()
    if(request.method == "POST"):
        form =requestForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect("tutorial:home")
        return render(request,"request.html",{'form':form})
    return render(request,"request.html",{'form':myform})
def privacy(request):
    return render(request,'privacy.html')