from django.db import models
import jsonfield


class Provider(models.Model):
    """
    Model that hold the provider criterion values
    """
    name = models.CharField(max_length=30, unique=True)
    flexibility = models.IntegerField()
    maturity = models.IntegerField()
    data_security = models.IntegerField()
    reliability = models.IntegerField()
    price = models.IntegerField()
    geo_dispatching = models.IntegerField()


class Attribute(models.Model):
    name = models.CharField(max_length=100, unique=True)
    weight = models.IntegerField()
    percentage = models.DecimalField(max_digits=4, decimal_places=2)
    type = models.CharField(max_length=10)


class Rule(models.Model):
    name = models.CharField(max_length=30, unique=True)
    criticality = models.IntegerField()
    complexity = models.IntegerField()
    availability = models.IntegerField()
    type = models.CharField(max_length=30, unique=True)


class Pricing(models.Model):
    provider = models.CharField(max_length=30)
    category = models.CharField(max_length=255)
    ram = models.IntegerField()
    cpu = models.IntegerField()
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_month = models.DecimalField(max_digits=10, decimal_places=2)


class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)
    architecture = models.CharField(max_length=30)
    costEstimation = models.DecimalField(max_digits=10, decimal_places=2)
    type_application = models.CharField(max_length=30)
    environment = models.CharField(max_length=30)
    sla = models.IntegerField()
    dependencies = jsonfield.JSONField()
    flux = jsonfield.JSONField()
    data_size = models.IntegerField()
    owner = models.CharField(max_length=255)


class Criteria(models.Model):
    name = models.CharField(max_length=255, unique=True)
    vl_rate = models.IntegerField()
    l_rate = models.IntegerField()
    m_rate = models.IntegerField()
    h_rate = models.IntegerField()
    vh_rate = models.IntegerField()


class Atom(models.Model):
    name = models.CharField(max_length=255, unique=True)
    complexity = jsonfield.JSONField()
    criticality = jsonfield.JSONField()
    availability = jsonfield.JSONField()
