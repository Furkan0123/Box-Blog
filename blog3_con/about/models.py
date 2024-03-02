from django.db import models



class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank = True)
    image = models.ImageField(upload_to ='classes/%Y/%m/%d/', default ='classes/default_indir.jpeg')

    def __str__(self):
        return self.title
    


class StudentReview(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank = True)
    image = models.ImageField(upload_to ='StudentReview/%Y/%m/%d/', default ='classes/default_indir.jpeg')

    def __str__(self):
        return self.name