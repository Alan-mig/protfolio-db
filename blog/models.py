from django.db import models

class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    pub_data = models.DateField(max_length=250)
    body = models.TextField()
    def __str__(self):
        return self.title

    def summery(self):
        return self.body[:100]
    def pub_date_better(self):
        return self.pub_data.strftime('%b %e %Y')