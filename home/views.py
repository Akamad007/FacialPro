# Create your views here.
from django.shortcuts import render,HttpResponse
from home.models import HomeImages
from FacialPro.settings import indicoApi
from FacialPro.settings import MEDIA_ROOT
from youtube.api import youTubeSearch

import indicoio, operator 

from django.core.files import File
indicoio.config.api_key =indicoApi
from home.models import lookup_table


import base64,uuid

def captureImage(request):
    image =  request.POST.get('image',None)
    image = image.split('data:image/png;base64,')[1]    
    imageName = str(uuid.uuid1())+"out.png"    
    imagePath = MEDIA_ROOT+"/img/person/"+imageName
    g = open(imagePath, "w")  
    g.write(base64.decodestring(image))
    g.close()  
    img = HomeImages.objects.create()
    img.image.save(imageName,File(open(imagePath, 'r')) )  
    data =  indicoio.fer(imagePath) 
   
    data = max(data.items(), key=operator.itemgetter(1))[0]   
    
    img.emotion = data   
    img.save()
    return HttpResponse("")

import random
def home(request):    
    image = HomeImages.objects.latest("datetime")
   
    data =  indicoio.fer(image.image.path) 
   
    data = max(data.items(), key=operator.itemgetter(1))[0]   
    
    image.emotion = data   
    image.save()
    
    emotion_list = lookup_table[image.emotion]
    total = len(emotion_list)
    counter = 10
    youtubVideos = []
    
    for x in range(total):
        if counter==0:            
            break
        counter = counter -1  
        someData = emotion_list[random.randrange(0,total)]
        while(someData==image.emotion):
            someData = emotion_list[random.randrange(0,total)]
        youtubVideos += youTubeSearch(someData, 3)
                             
    return render(request,"home/home.html",{"image":image,"youtubVideos":youtubVideos})

