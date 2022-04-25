from django.db import models
from django.forms.models import model_to_dict
from planaday_developer_test.users.models import User

'''
MODELS
----
You may create as many or as few models as needed in
order to fulfill the requirements and to implement your solution.

We are very focused on your strategy and approach
'''

class Attraction(models.Model):
    name = models.CharField("Name", max_length=32, null=False, blank=False)
    description = models.CharField("Description", max_length=512, null=False, blank=False)


    updated = models.DateTimeField("Updated", auto_now=True, null=False)
    created = models.DateTimeField("Created", auto_now_add=True, null=False)

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }

class Inventory(models.Model):

    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE)
    date = models.DateTimeField("Updated", auto_now=True, null=False)
    tickets = models.IntegerField()
    remain_tickets = models.IntegerField(default=0, blank=True, null=True)
    rate = models.FloatField()

class Booking(models.Model):

    attraction = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    date = models.DateTimeField("Updated", auto_now=True, null=False)
    noftickets = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
