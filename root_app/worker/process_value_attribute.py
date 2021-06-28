"""
All functions in this section refer to the criticality of an application
"""
from root_app.models import Project


def item_no_numeric_rating(attr, conditions, item):
    rate = 0
    env_conditions = [cond for cond in conditions if ((cond.condField == item) & (cond.condSeuil == attr))]
    try:
        for cond in env_conditions:
            rate += cond.condValue
        rate = rate / len(env_conditions)
        return rate
    except:
        return rate


def item_numeric_rating(attr, conditions, item):
    results = []
    try:
        sla_conditions = [cond for cond in conditions if (cond.condField == item)]
        for cond in sla_conditions:
            temp_bound = compare_item(attr, cond)
            if temp_bound:
                if temp_bound[1] == 0:
                    return temp_bound[0]
                results.append(temp_bound)
        return min(results, key=lambda t: t[1])[0]
    except:
        return 0


def rating(project: Project, attribute):
    rat = 0
    rat += item_no_numeric_rating(project.environment, attribute.condition, "environment")
    rat += item_no_numeric_rating(project.architecture, attribute.condition, "architecture")
    rat == item_no_numeric_rating(project.type_application, attribute.condition, "type_application")
    rat += item_numeric_rating(project.sla, attribute.condition, "sla")
    rat += item_numeric_rating(len(project.flux), attribute.condition, "flux")
    rat += item_numeric_rating(len(project.dependencies), attribute.condition, "dependencies")
    rat += item_numeric_rating(project.data_size, attribute.condition, "data_size")
    return rat


def compare_item(item, cond):
    try:
        bound = int(cond.condSeuil)
        if cond.condOp == '<':
            if item < bound:
                return cond.condValue, bound - item
        if cond.condOp == "==":
            if item == bound:
                return cond.condValue, 0
    except:
        return None
