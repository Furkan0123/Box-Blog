from django.db import models




class Category(models.Model):
    name= models.CharField(max_length=200, null = True)
    slug = models.SlugField(max_length = 100, unique = True, null = True  )


    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name= models.CharField(max_length=50, null = True)
    slug = models.SlugField(max_length = 50, unique = True, null = True  )


    def __str__(self):
        return self.name

class Class_obj(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category,  on_delete = models.DO_NOTHING)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to ='classes/%Y/%m/%d/', default ='classes/default_indir.jpeg')
    date = models.DateTimeField(auto_now = True)


    def __str__(self):
        return self.name