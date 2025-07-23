from django.db import models

class Field(models.Model):
    name = models.CharField(max_length=255, unique=True)
    focus = models.TextField()

class Subfield(models.Model):
    name = models.CharField(max_length=255, unique=True)
    field = models.ForeignKey(Field, related_name='subfields', on_delete=models.CASCADE)
    common_job_titles = models.JSONField(default=list)  # List of strings
    key_tools_skills = models.JSONField(default=list)   # List of strings

class Skill(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class JobExample(models.Model):
    field = models.ForeignKey(Field, related_name='jobs', on_delete=models.CASCADE)
    subfield = models.ForeignKey(Subfield, related_name='job_examples', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    key_skills = models.ManyToManyField(Skill, related_name='job_examples')

class LearningResource(models.Model):
    job_example = models.ForeignKey(JobExample, related_name='learning_resources', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    url = models.URLField()

class RealWorldProject(models.Model):
    job_example = models.ForeignKey(JobExample, related_name='real_world_projects', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)