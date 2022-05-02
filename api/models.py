from django.db import models
from django.contrib.auth.models import User


class Subject(models.Model):

    name = models.CharField(max_length=255, null=True, blank=True)
    code = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Assignment(models.Model):

    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='assignment_files/')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ManyToManyField(User, through='AssignmentUser')
    due_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def get_num_of_days(self):
        from datetime import datetime, timezone

        now = datetime.now(timezone.utc)

        return abs((self.due_date-now).days)


class AssignmentUser(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="user_set")
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, null=True, blank=True, related_name="assignment_set")

    def __str__(self):
        return '{} | {}'.format(self.user, self.assignment)

