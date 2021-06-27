"""
All functions in this section refer to the criticality of an application
"""
from root_app.models import Project


def environment_rating(env, conditions):
    env_rate = 0
    env_conditions = [cond for cond in conditions if ((cond.condField == 'environment') & (cond.condSeuil == env))]
    try:
        for cond in env_conditions:
            env_rate += cond.condValue
        env_rate = env_rate/len(env_conditions)
        print(env_rate)
        return env_rate
    except:
        return env_rate


def architecture_rating(architecture, conditions):
    arch_rate = 0
    arch_conditions = [cond for cond in conditions if ((cond.condField == 'architecture') & (cond.condSeuil == architecture))]
    try:
        for cond in arch_conditions:
            arch_rate += cond.condValue
        arch_rate = arch_rate / len(arch_conditions)
        print(arch_rate)
        return arch_rate
    except:
        return arch_rate


def type_application_rating(type_application, conditions):
    ta_rate = 0
    ta_conditions = [cond for cond in conditions if ((cond.condField == 'type_application') & (cond.condSeuil == type_application))]
    try:
        for cond in ta_conditions:
            ta_rate += cond.condValue
        ta_rate = ta_rate / len(ta_conditions)
        print(ta_rate)
        return ta_rate
    except:
        return ta_rate


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


def rating(project: Project, criticality):
    rat = 0
    rat += environment_rating(project.environment, criticality.condition)
    rat += architecture_rating(project.architecture, criticality.condition)
    print(" project criticality rate ", rat)
    return rat
