"""
All functions in this section refer to the criticality of an application
"""
from root_app.models import Project


def environment_rating(env, criticality):
    return criticality.conditions[env] if criticality.status == 1 else 0


def architecture_rating(architecture, criticality):
    return criticality.conditions[architecture] if criticality.status == 1 else 0


def type_application_rating(type_application, criticality):
    return criticality.conditions[type_application] if criticality.status == 1 else 0


def sla_rating(sla, criticality):
    return criticality.conditions[str(sla)] if criticality.status == 1 else 0


def flux_rating(flux, criticality):
    try:
        index = (len(flux)//5 + 1) * 5
        return criticality.conditions[str(index)] if criticality.status == 1 else 0
    except:
        index = list(criticality.conditions.keys())[-1]
        return criticality.conditions[str(index)] if criticality.status == 1 else 0


def data_size_rating(data_size, criticality):
    try:
        index = (data_size//5 + 1) * 5
        return criticality.conditions[str(index)] if criticality.status == 1 else 0
    except:
        index = list(criticality.conditions.keys())[-1]
        return criticality.conditions[str(index)] if criticality.status == 1 else 0


def rating(project: Project, atoms):
    rat = 0
    rat += environment_rating(project.environment, atoms.environment.criticality)
    rat += architecture_rating(project.architecture, atoms.architecture.criticality)
    rat += sla_rating(project.sla, atoms.sla.criticality)
    rat += type_application_rating(project.type_application, atoms.type_application.criticality)
    rat += flux_rating(project.flux, atoms.flux.criticality)
    rat += data_size_rating(project.data_size, atoms.data_size.criticality)
    print(" project criticality rate ", rat)
    return rat
