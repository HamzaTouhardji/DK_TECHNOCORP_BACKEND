from django.db import models
from django.utils import timezone
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Entreprise(models.Model):

    class EntrepriseObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='in progress')

    options = (
        ('in progress', 'in progress'),
        ('created', 'created'),

    )
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1)
    name = models.CharField(max_length=250)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='created')
    created = models.DateTimeField(default=timezone.now)
    founder = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='entreprises_posts')
    status = models.CharField(
        max_length=11, choices=options, default='in progress')
    objects = models.Manager()  # default manager
    entreprisebbjects = EntrepriseObjects()  # custom manager

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name
