# pylint: disable=all
# flake8: noqa
from django.db import models


class Vgsales(models.Model):
    rank = models.BigIntegerField(primary_key=True, db_column='Rank', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    platform = models.TextField(db_column='Platform', blank=True, null=True)  # Field name made lowercase.
    year = models.FloatField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    genre = models.TextField(db_column='Genre', blank=True, null=True)  # Field name made lowercase.
    publisher = models.TextField(db_column='Publisher', blank=True, null=True)  # Field name made lowercase.
    na_sales = models.FloatField(db_column='NA_Sales', blank=True, null=True)  # Field name made lowercase.
    eu_sales = models.FloatField(db_column='EU_Sales', blank=True, null=True)  # Field name made lowercase.
    jp_sales = models.FloatField(db_column='JP_Sales', blank=True, null=True)  # Field name made lowercase.
    other_sales = models.FloatField(db_column='Other_Sales', blank=True, null=True)  # Field name made lowercase.
    global_sales = models.FloatField(db_column='Global_Sales', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vgsales'
