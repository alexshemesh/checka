from django.db import models

class Shop(models.Model):
    """Single shop from which you receive check"""
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns string representation of Shop"""
        return self.name

class Check(models.Model):
    """Single check"""
    # shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    shop = models.CharField(max_length=200, default='Unknown')
    photo = models.ImageField(upload_to= 'check_files')
    total_amount = models.FloatField(default=0.0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns string representatioin of Check"""
        return "{} {} at {} ".format(self.shop ,str(self.total_amount), self.date_added)


