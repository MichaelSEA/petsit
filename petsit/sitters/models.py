import numpy as np
import re

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


class Owner(models.Model):
    name = models.CharField(db_index=True, max_length=512)
    email = models.EmailField(db_index=True, unique=True, max_length=254)
    phone_number = models.CharField(db_index=True, max_length=30)
    image = models.URLField()


class Sitter(models.Model):
    name = models.CharField(db_index=True, max_length=512)
    email = models.EmailField(db_index=True, unique=True, max_length=254)
    phone_number = models.CharField(db_index=True, unique=True, max_length=30)
    image = models.URLField()
    sitter_score = models.DecimalField(db_index=True, null=True, decimal_places=2, max_digits=3)
    ratings_score = models.DecimalField(db_index=True, null=True, decimal_places=2, max_digits=3)
    overall_sitter_rank = models.DecimalField(db_index=True, null=True, decimal_places=2, max_digits=4)


class Stay(models.Model):
    rating = models.IntegerField(db_index=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    comments = models.TextField()
    start_date = models.DateField()e
    end_date = models.DateField()
    sitter = models.ForeignKey(Sitter)
    owner = models.ForeignKey(Owner)
    dogs = models.CharField(max_length=1024,default='')


@receiver(pre_save, sender=Sitter)
def compute_sitter_score(sender, **kwargs):
    sitter = kwargs['instance']
    name = sitter.name
    regex = re.compile('[^a-zA-Z]')
    alpha = regex.sub('', name).lower()
    sitter.sitter_score = 5*(len(''.join(set(alpha))) / 26)
    if sitter.pk is None:
        sitter.overall_sitter_rank = sitter.sitter_score


@receiver(post_save, sender=Stay)
def compute_ratings_score(sender, **kwargs):
    # ratings score for sitter is the average of stay ratings.
    # add this one and recompute.
    instance_object = kwargs['instance']
    sitter = instance_object.sitter
    ratings = [s.rating for s in Stay.objects.all().filter(sitter=sitter)]
    sitter.ratings_score = sum(ratings) / float(len(ratings))
    sitter.save()
    return

@receiver(post_save, sender=Stay)
def compute_overall_sitter_rank(sender, **kwargs):
    '''
    The Overall Sitter Rank is a weighted average of the Sitter Score and
    Ratings Score, weighted by the number of stays. When a sitter has no
    stays, their Overall Sitter Rank is equal to the Sitter Score.
    When a sitter has 10 or more stays, their Overall Sitter Rank is equal
    to the Ratings Score.
    :param sender: Stay model
    :param kwargs: instance etc.
    :return: None
    '''
    instance_object = kwargs['instance']
    sitter = instance_object.sitter
    ratings = [s.rating for s in Stay.objects.all().filter(sitter=sitter)]

    if len(ratings) >= 10:
        sitter.overall_sitter_rank = sitter.ratings_score
    else:
        sitter.overall_sitter_rank = weighted_average(sitter.sitter_score, ratings)

    sitter.save()
    return


def weighted_average(sitter_score, ratings):
    values = [sitter_score]
    sitter_weight = 100 - (10*len(ratings))
    weights = [sitter_weight]
    for r in ratings:
        values.append(r)
        weights.append(10)

    return np.average(values, weights=weights)

