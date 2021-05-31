from django.db import models

# Create your models here.

class Todo(models.Model):
    todo= models.CharField(max_length=120, blank=False)
    is_Completed= models.BooleanField(default=False)
    published_On= models.DateTimeField('auto_now_add'==True ,blank=True )

    def __str__(self):
        return self.todo