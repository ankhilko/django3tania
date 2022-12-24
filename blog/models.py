from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        null=True,
        primary_key=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'blog_cities'
        verbose_name = 'city'
        verbose_name_plural = 'cities'


class Country(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        null=True,
        primary_key=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'blog_countries'
        verbose_name = 'country'
        verbose_name_plural = 'countries'


class EducationalInstitution(models.Model):
    title = models.CharField(
        verbose_name='ei title',
        unique=True,
        blank=True,
        null=True,
        primary_key=True,
    )
    city = models.ManyToManyField(City)
    country = models.ManyToManyField(Country)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blog_educationalinstitutions'
        verbose_name = 'educational institution'
        verbose_name_plural = 'educational institutions'


class Teacher(models.Model):

    first_name = models.CharField(
        verbose_name='first name',
        unique=False,
        blank=True,
        null=True,
    )
    family_name = models.CharField(
        verbose_name='family name',
        unique=False,
        blank=True,
        null=True,
    )
    passport = models.CharField(
        verbose_name='teachers passport',
        unique=True,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.passport

    class Meta:
        db_table = 'blog_teachers'
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'


class Student(models.Model):
    pass


class Subject(models.Model):
    pass


class Schedule(models.Model):
    pass


class News(models.Model):
    pass






