from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework.response import Response
from .worker import setup, utils
from munch import Munch
from root_app.models import Provider, Rule, Pricing, Project, Attribute, Criteria, Atom, Condition
from rest_framework import permissions, viewsets, status
from rest_framework.decorators import action
from root_app.serializers import UserSerializer, \
    GroupSerializer, ProviderSerializer, RuleSerializer, PricingSerializer, ProjectSerializer, AttributeSerializer, \
    CriteriaSerializer, AtomSerializer, ConditionSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by('-date_joined')
    serializers_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited
    """
    queryset = Group.objects.all().order_by('-permissions')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProviderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows providers to be viewed or edited
    """
    queryset = Provider.objects.all().order_by('-price')
    serializer_class = ProviderSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False)
    def rating(self, request):
        try:
            providers = Provider.objects.all()
            attributes = Attribute.objects.all()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        providers = self.get_serializer(providers, many=True)
        attributes = AttributeSerializer(attributes, many=True, context={'request': request})
        attributes, attributes_names = utils.sanitize_attributes(attributes.data)
        all_providers = utils.sanitize_providers(providers.data)
        response = setup.providers_raking(all_providers, attributes_names, attributes)
        return Response(response, status=status.HTTP_200_OK)


class RuleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows rules to be viewed or edited
    """
    queryset = Rule.objects.all().order_by('-type')
    serializer_class = RuleSerializer
    permission_classes = [permissions.IsAuthenticated]


class PricingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows pricing to be viewed or edited
    """
    queryset = Pricing.objects.all().order_by('-price_per_hour')
    serializer_class = PricingSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited
    """
    queryset = Project.objects.all().order_by('-sla')
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True)
    def rating(self, request, pk=None):
        try:
            project = Project.objects.get(id=pk)
            atoms = Atom.objects.all()
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(project)
        serializer_atom = AtomSerializer(atoms, many=True, context={'request': request})
        project = Munch.fromDict(serializer.data)
        try:
            rule = Rule.objects.get(type=project.type_application)
        except:
            rule = Rule.objects.get(type="default")

        serializer_rule = RuleSerializer(rule, many=False, context={'request': request})
        rule = Munch.fromDict(serializer_rule.data)
        atoms = serializer_atom.data
        all_atoms = utils.sanitize_atoms(atoms)
        response = setup.ready_rep(project, all_atoms, rule)
        return Response(response, status=status.HTTP_200_OK)


class AttributeViewSet(viewsets.ModelViewSet):
    queryset = Attribute.objects.all().order_by('-type')
    serializer_class = AttributeSerializer
    permission_classes = [permissions.IsAuthenticated]


class CriteriaViewSet(viewsets.ModelViewSet):
    queryset = Criteria.objects.all().order_by('-name')
    serializer_class = CriteriaSerializer
    permission_classes = [permissions.IsAuthenticated]


class AtomViewSet(viewsets.ModelViewSet):
    queryset = Atom.objects.all().order_by('id')
    serializer_class = AtomSerializer
    permission_classes = [permissions.IsAuthenticated]


class ConditionViewSet(viewsets.ModelViewSet):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer
    permission_classes = [permissions.IsAuthenticated]
