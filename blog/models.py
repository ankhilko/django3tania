from django.db import models

# Create your models here.


class Subject(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        blank=False,
        null=False,
        primary_key=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'blog_subjects'
        verbose_name = 'subject'
        verbose_name_plural = 'subjects'


class City(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        blank=False,
        null=False,
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
        blank=False,
        null=False,
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
        max_length=100,
        verbose_name='title',
        unique=False,
        blank=True,
        null=True,
    )
    # ei_index = models.SmallAutoField()
    city = models.ForeignKey(City, null=True, blank=True, on_delete=models.DO_NOTHING)
    country = models.ForeignKey(Country, null=True, blank=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'blog_educationalinstitutions'
        verbose_name = 'educational institution'
        verbose_name_plural = 'educational institutions'


class School(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='school',
        unique=False,
    )
    # school_index = models.SmallAutoField()
    city = models.ForeignKey(City, null=True, blank=True, on_delete=models.DO_NOTHING)
    country = models.ForeignKey(Country, null=True, blank=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'blog_schools'
        verbose_name = 'school'
        verbose_name_plural = 'schools'


class People(models.Model):

    first_name = models.CharField(
        max_length=100,
        verbose_name='name',
        unique=False,
        blank=True,
        null=True,
    )
    family_name = models.CharField(
        max_length=100,
        verbose_name='family name',
        unique=False,
        blank=True,
        null=True,
    )
    passport = models.CharField(
        max_length=15,
        verbose_name='passport',
        unique=True,
        blank=True,
        null=True,
    )

    city = models.ForeignKey(City, null=True, blank=True, on_delete=models.DO_NOTHING)
    country = models.ForeignKey(Country, null=True, blank=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.family_name + ' ' + self.first_name


class Teacher(People):

    education = models.ForeignKey(EducationalInstitution, null=True, blank=True, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'blog_teachers'
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'


class Student(People):

    school = models.ForeignKey(School, null=True, blank=True, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'blog_students'
        verbose_name = 'student'
        verbose_name_plural = 'students'


class Schedule(models.Model):
    pass


class News(models.Model):
    pass






