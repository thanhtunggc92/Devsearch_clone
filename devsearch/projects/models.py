from django.db import models
import uuid
from users.models import Profile
# Create your models here.


class Tags(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    # id = models.AutoField(primary_key=True,unique=True,editable=False)



    def  __str__(self) -> str:
        return self.name

class Project(models.Model):
    owner = models.ForeignKey(Profile,null=True , blank=True , on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    descriptions= models.TextField(null=True,blank=True)
    feature_image = models.ImageField(null=True, blank=True,
                                      default='default.jpg')
    demo_link = models.CharField(max_length=2000,null=True,blank=True)
    source_link= models.CharField(max_length=2000,null=True,blank=True)
    tags= models.ManyToManyField(Tags, blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True) # generate the time when we created.
    # id = models.AutoField(primary_key=True,unique=True,editable=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['-vote_total','-vote_ratio','-title']


    @property
    def reviewers(self):
        queryset= self.reviews_set.all().values_list('owner_name__id',flat=True)
        return queryset
    @property  
    def ImgUrl(self):      #another way to get the image.url
        try:
            img = self.feature_image.url     
        except:
            img=''
        return img
    @property
    def getVoteCount(self):
        review = self.reviews_set.all()
        upvotes = review.filter(value='Like').count()
        totalvotes = review.count()

        ratio = (upvotes/totalvotes) *100
        self.vote_total = totalvotes
        self.vote_ratio = ratio
        self.save() 
       

class Reviews(models.Model):
    VOTE_TYPE = (
        ('Like','up'),
        ('Dislike','down'),
    )
   
    owner_name = models.ForeignKey(Profile,on_delete=models.CASCADE , null=True)
    project= models.ForeignKey(Project,on_delete=models.CASCADE)
    body = models.TextField(null= True , blank= True)
    value = models.CharField(max_length=200 , choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

   
    class Meta:
        unique_together=[['owner_name', 'project']]


    def  __str__(self) -> str:
        return self.value
    
 

