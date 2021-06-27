"""
All functions in this section refer to the complexity of an application
"""

from root_app.models import Project


def environment_rating(env, conditions):
    env_rate = 0
    env_conditions = [cond for cond in conditions if ((cond.condField == 'environment') & (cond.condSeuil == env))]
    try:
        for cond in env_conditions:
            env_rate += cond.condValue
        env_rate = env_rate / len(env_conditions)
        print(env_rate)
        return env_rate
    except:
        return env_rate


def architecture_rating(architecture, complexity):
    return complexity.conditions[architecture] if complexity.status == 1 else 0


def type_application_rating(type_application, conditions):
    ta_rate = 0
    ta_conditions = [cond for cond in conditions if
                     ((cond.condField == 'type_application') & (cond.condSeuil == type_application))]
    try:
        for cond in ta_conditions:
            ta_rate += cond.condValue
        ta_rate = ta_rate / len(ta_conditions)
        print(ta_rate)
        return ta_rate
    except:
        return ta_rate


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


def rating(project: Project, complexity):
    rat = 0
    rat += environment_rating(project.environment, complexity.condition)
    rat += architecture_rating(project.environment, complexity.condition)
    return rat
