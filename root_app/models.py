from django.db import models
import jsonfield


class Provider(models.Model):
    name = models.CharField(max_length=30)
    flexibility = models.IntegerField()
    maturity = models.IntegerField()
    data_security = models.IntegerField()
    reliability = models.IntegerField()
    price = models.IntegerField()
    geo_dispatching = models.IntegerField()


class Attribute(models.Model):
    name = models.CharField(max_length=100)
    weight = models.IntegerField()
    type = models.CharField(max_length=10)


class Rule(models.Model):
    name = models.CharField(max_length=30)
    criticality = models.IntegerField()
    complexity = models.IntegerField()
    availability = models.IntegerField()
    type = models.CharField(max_length=30)


class Pricing(models.Model):
    provider = models.CharField(max_length=30)
    category = models.CharField(max_length=255)
    ram = models.IntegerField()
    cpu = models.IntegerField()
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    price_per_month = models.DecimalField(max_digits=10, decimal_places=2)


class Project(models.Model):
    name = models.CharField(max_length=255)
    architecture = models.CharField(max_length=30)
    costEstimation = models.DecimalField(max_digits=10, decimal_places=2)
    type_application = models.CharField(max_length=30)
    environment = models.CharField(max_length=30)
    sla = models.IntegerField()
    dependencies = jsonfield.JSONField()
    flux = jsonfield.JSONField()
    data_size = models.IntegerField()
    cpu = models.IntegerField()
    ram = models.IntegerField()
    owner = models.CharField(max_length=255)


class Criteria(models.Model):
    name = models.CharField(max_length=255)
    vl_rate = models.IntegerField()
    l_rate = models.IntegerField()
    m_rate = models.IntegerField()
    h_rate = models.IntegerField()
    vh_rate = models.IntegerField()


class Condition(models.Model):
    condition = jsonfield.JSONField()


class Atom(models.Model):
    criteria = models.CharField(max_length=255)
    condition = jsonfield.JSONField()
