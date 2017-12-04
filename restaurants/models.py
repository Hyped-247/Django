from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from django.conf import settings


USER = settings.AUTH_USER_MODEL


class RestaurantsLocations(models.Model):
    owner = models.ForeignKey(USER)  # django models unleashed JOINCFE.com
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120, null=True, blank=True)
    category = models.CharField(max_length=120, null=True, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # This is the bad way to do it.
        # return f"/restaurants/{self.slug}/"

        # This is the good way to do it.
        return reverse('restaurant-detail', kwargs={'slug':self.slug})

    @property
    def title(self):
        return self.name  # This will give us the ability to add obj.title


def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    print("saving... ")
    print(instance.timestamp)
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


# Evey time something is added to the data base the pre_save and the post_save are called
# This can be very useful for telling the prof on how far each student is on the test.


pre_save.connect(rl_pre_save_receiver, sender=RestaurantsLocations)
