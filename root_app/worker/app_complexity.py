"""
All functions in this section refer to the complexity of an application
"""

from root_app.models import Project


def environment_rating(env, complexity):
    return complexity.conditions[env] if complexity.status == 1 else 0


def architecture_rating(architecture, complexity):
    return complexity.conditions[architecture] if complexity.status == 1 else 0


def type_application_rating(type_application, complexity):
    return complexity.conditions[type_application] if complexity.status ==1 else 0


def sla_rating(sla, complexity):
    return complexity.conditions[str(sla)] if complexity.status == 1 else 0


def flux_rating(flux, complexity):
    try:
        index = (len(flux)//5 +1) * 5
        return complexity.conditions[str(index)] if complexity.status == 1 else 0
    except:
        index = list(complexity.conditions.keys())[-1]
        return complexity.conditions[str(index)] if complexity.status == 1 else 0


def data_size_rating(data_size, complexity):
    try:
        index = (data_size//5 + 1) * 5
        return complexity.conditions[str(index)] if complexity.status == 1 else 0
    except:
        index = list(complexity.conditions.keys())[-1]
        return complexity.conditions[str(index)] if complexity.status == 1 else 0


def dependencies_rating(dependencies, complexity):
    try:
        index = (len(dependencies)//5 + 1) * 5
        return complexity.conditions[str(index)] if complexity.status == 1 else 0
    except:
        index = list(complexity.conditions.keys())[-1]
        return complexity.conditions[str(index)] if complexity.status == 1 else 0


def rating(project: Project, atoms):
    rat = 0
    rat += environment_rating(project.environment, atoms.environment.complexity)
    rat += architecture_rating(project.architecture, atoms.architecture.complexity)
    rat += dependencies_rating(project.dependencies, atoms.dependencies.complexity)
    rat += flux_rating(project.flux, atoms.flux.complexity)
    rat += type_application_rating(project.type_application, atoms.type_application.complexity)
    rat += data_size_rating(project.data_size, atoms.data_size.complexity)
    return rat
