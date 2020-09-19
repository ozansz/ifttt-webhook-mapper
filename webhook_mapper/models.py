from django.db import models

class GetToPostRequestMapping(models.Model):
    tag = models.CharField(max_length=50)
    trigger_action = models.CharField(max_length=50)
    trigger_key = models.CharField(max_length=50)

    def __str__(self):
        return self.tag

    def __repr__(self):
        return self.__str__()