from django.db import models


class Application(models.Model):
    Objective = models.TextField(max_length=128)
    skills_required = models.TextField(max_length=128)

    def __str__(self):
        return 'Application' + str(self.id)


class Applicant(models.Model):
    name = models.CharField(max_length=64)
    Applying_for = models.ForeignKey(Application, related_name="application", on_delete=models.CASCADE)
    skills = models.TextField(max_length=128)

    def __str__(self):
        return self.name
