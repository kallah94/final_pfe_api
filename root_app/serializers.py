from django.contrib.auth.models import User, Group
from root_app.models import Provider, Rule, Pricing, Project, Attribute, Criteria, Atom
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ProviderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'


class RuleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rule
        fields = '__all__'


class PricingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pricing
        fields = '__all__'


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class AttributeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attribute
        fields = '__all__'


class CriteriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Criteria
        fields = '__all__'


class AtomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Atom
        fields = '__all__'
