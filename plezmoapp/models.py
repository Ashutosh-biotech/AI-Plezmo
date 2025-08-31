from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here
Gender = ((1, "Male"), (2, "Female"), (3, "others"), (4, "unknown"))

status = ((1, "pending"), (2, "close"), (3, "working"), (4, "done"))


class user_data(models.Model):
    sno = models.AutoField(primary_key=True, null=False)
    username = models.CharField(max_length=150, blank=False, null=False)
    email = models.EmailField(max_length=254, unique=True, null=False, blank=False)
    gender = models.IntegerField(choices=Gender, default=4)
    first_name = models.CharField(null=True, max_length=50)
    last_name = models.CharField(null=True, max_length=50)
    logo = models.CharField(default="/assets/img/svg/D.svg", max_length=100)
    verified = models.CharField(default="False", max_length=6)
    one_time_password = models.IntegerField(default=000000)

    def __str__(self):
        return f"{self.username}"


class appdatabase(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False)
    request_by = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True
    )
    desc = models.TextField()
    file_name = models.CharField(max_length=50, blank=False)
    web_app_url = models.URLField(blank=False)
    date_and_time = models.DateTimeField(default=now)

    def __str__(self):
        return self.name


class requested_app(models.Model):
    sno = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    app_name = models.CharField(max_length=150, blank=False)
    app_desc = models.TextField(blank=False)
    status = models.IntegerField(choices=status, default=1)
    date = models.DateField(default=now)

    def __str__(self):
        return self.app_name


class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.CharField(max_length=250)
    logo = models.CharField(default="/assets/img/svg/D.svg", max_length=100)
    timeStamp = models.DateTimeField(blank=True, default=now)

    class Meta:
        ordering = ["-timeStamp"]

    def __str__(self):
        return self.title


class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    logo = models.CharField(default="/assets/img/svg/D.svg", max_length=100)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.user.username


class message(models.Model):
    sno = models.AutoField(primary_key=True)
    error = models.CharField(max_length=255)
    error_to = models.CharField(max_length=30)
    error_from = models.CharField(max_length=30)
    action=models.CharField(default="Not Taken", max_length=25)
    timeStamp = models.DateTimeField(blank=True, default=now)

    def __str__(self):
        return  self.error + ' - by - ' + self.error_to + ', Action = ' + self.action
