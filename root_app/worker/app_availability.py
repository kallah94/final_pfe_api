"""
All functions in this section refer to the availability of an application
"""
from root_app.models import Project


def sla_rating(sla, availability):
    return availability.conditions[str(sla)] if availability.status == 1 else 0


def flux_rating(flux, availability):
    try:
        index = (len(flux)//5 + 1) * 5
        return availability.conditions[str(index)] if availability.status == 1 else 0
    except:
        index = list(availability.conditions.keys())[-1]
        return availability.conditions[str(index)] if availability.status == 1 else 0


def rating(project: Project, atoms):
    rat = 0
    rat += sla_rating(project.sla, atoms.sla.availability)
    rat += flux_rating(project.flux, atoms.flux.availability)
    return rat
