from django.db import models
from wall.users.models import UserProfile
from django.contrib.auth.models import User

class Post(models.Model):
  title        = models.CharField(max_length=1000)
  content      = models.TextField()
  creator      = models.CharField(max_length=100)
  creators     = models.ForeignKey(UserProfile)
  date_created = models.DateTimeField()
  date_bumped  = models.DateTimeField() #Last time someone posted a comment

  #flags = models.IntegerField() #Before I uncomment this line, I should 
  #probably go buy champaigne or something.

  #Challenge comments
  challenge          = models.BooleanField()
  challenged_user    = models.ForeignKey(User, null=True, blank=True)
  challenge_answered = models.BooleanField()

  #num_likes #LOL

  def __unicode__(self):
    return self.content

class Comment(models.Model):
  parent       = models.ForeignKey(Post)
  content      = models.TextField()
  creator      = models.CharField(max_length=100)
  creators     = models.ForeignKey(UserProfile)
  date_created = models.DateTimeField()
  notifying    = models.ManyToManyField(UserProfile, related_name="notifying_set")


  def __unicode__(self):
    return self.content