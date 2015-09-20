from django.db import models
import uuid

# Create your models here.
def get_photo_storage_path(photo_obj, filename):         
    storage_path = 'img/faces/'+str(uuid.uuid1())+"_"+filename
    return storage_path 

class HomeImages(models.Model):
    IMAGE_CHOICES = (('Happy','Happy'),('Sad','Sad'),('Fear','Fear'), 
                     ('Angry','Angry'),('Surprise','Surprise'),
                     ('Neutral','Neutral')
                     )
    image = models.ImageField(upload_to = get_photo_storage_path,null = True, blank =  True)
   
    emotion = models.CharField(max_length = 200,choices = IMAGE_CHOICES,  null = True, blank =  True)
    
    datetime = models.DateTimeField(auto_now_add = True)

lookup_table = {HomeImages.IMAGE_CHOICES[0][0]:["happy", "smile", "euphoric", "dancing", "singing", "happy songs", "happy movies", "overjoyed", "merry", "peaceful", "ecstatic"],
                HomeImages.IMAGE_CHOICES[1][0]:[ "happy songs", "happy", "cheerful", "glad", "pleasant", "lucky"],
                HomeImages.IMAGE_CHOICES[2][0]:["bold", "brave","brave songs", "fearless", "calm", "laid-back", "unworried", "composed", "extroverted"],
                HomeImages.IMAGE_CHOICES[3][0]:["content", "calm", "happy", "joyous", "mild", "nice", "cool", "peaceful" "songs"],
                HomeImages.IMAGE_CHOICES[4][0]:["calm", "composed", "coolness", "happiness", "indifference", "meditation", "meditative" "calm songs"],
                HomeImages.IMAGE_CHOICES[5][0]:["Biased", "interested", "concerned", "decided", "involved", "excited", "predisposed" , "bright" ]}


