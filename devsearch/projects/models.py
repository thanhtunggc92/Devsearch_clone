from django.db import models
import uuid
# Create your models here.


class Tags(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4 , unique=True, primary_key=True, editable=False)



    def  __str__(self) -> str:
        return self.name

class Projects(models.Model):
    title = models.CharField(max_length=255)
    descriptions= models.TextField(null=True,blank=True)
    demo_link = models.CharField(max_length=2000,null=True,blank=True)
    source_link= models.CharField(max_length=2000,null=True,blank=True)
    tags= models.ManyToManyField(Tags, blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True) # generate the time when we created.
    id = models.UUIDField(default=uuid.uuid4 , unique=True, primary_key=True, editable=False)


    def __str__(self) -> str:
        return self.title
    


class Reviews(models.Model):
    VOTE_TYPE = (
        ('Like','up'),
        ('Dislike','down'),
    )

    project= models.ForeignKey(Projects,on_delete=models.CASCADE)
    body = models.TextField(null= True , blank= True)
    value = models.CharField(max_length=200 , choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4 , unique=True, primary_key=True, editable=False)


    def  __str__(self) -> str:
        return self.value
    

