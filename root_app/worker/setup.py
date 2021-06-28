import decimal
import operator

from . import process_value_attribute
from root_app.models import Project
import numpy as np
from topsis import topsis

"""
Compare the application vector {"complexity", "criticality", "availability"}
with the right rule vector define by the application type or the default rule 
which be used when the application type is not set
"""


def cloud_ready_rate(project: Project, atoms, rule):

    try:
        app_criticality = process_value_attribute.rating(project, atoms.criticality)
    except:
        app_criticality = 0
    try:
        app_complexity = process_value_attribute.rating(project, atoms.complexity)
    except:
        app_complexity = 0
    try:
        app_availability = process_value_attribute.rating(project, atoms.availability)
    except:
        app_availability = 0
    app_vector = [app_criticality, app_complexity, app_availability]

    rule_vector = [rule.complexity, rule.criticality, rule.availability]
    app_vector = np.array(app_vector),
    rule_vector = np.array(rule_vector)
    score = (np.dot(app_vector, rule_vector) / (np.linalg.norm(app_vector) * np.linalg.norm(rule_vector))).item(0)
    return score if score > 0 else 0


def ready_rep(project: Project, atoms, rule):
    score = cloud_ready_rate(project, atoms, rule) * 100
    if score >= 80:
        return {"score": score, "message": "votre application est parfaitement compatible avec le cloud public"}
    if score >= 50:
        return {"score": score, "message": "votre application est assez compatible avec le cloud public"}
    else:
        return {"score": score, "message":"votre application n'est pas tout a fait compatible avec le cloud public"}


def cost_compare():
    return None


def attributes_type_matrix(attributes):
    attributes_type = []
    for attr in attributes:
        attributes_type.append(1) if attr.type == 'benefit' else attributes_type.append(0)
    return attributes_type


def attributes_weight_matrix(attributes):
    attributes_weight = []
    for attr in attributes:
        attributes_weight.append(decimal.Decimal(attr.weight))
    return attributes_weight


def providers_matrix(providers, attributes_names):
    alternatives = []
    for prov in providers:
        alternatives.append(provider_matrix(prov, attributes_names))
    return alternatives


def provider_matrix(provider, attributes_names):
    attributes_rates_row = []
    for name in attributes_names:
        try:
            attributes_rates_row.append(provider[name])
        except KeyError:
            continue
    return attributes_rates_row


def get_providers_names(providers):
    names = []
    for prov in providers:
        names.append(prov.name)
    return names


def providers_raking(providers, attributes_names, attributes):
    providers_rows = providers_matrix(providers, attributes_names)
    weights = attributes_weight_matrix(attributes)
    types = attributes_type_matrix(attributes)
    providers_names = get_providers_names(providers)
    decision = topsis(providers_rows, weights, types)
    decision.calc()
    scores = decision.C.tolist()
    result = list(map(lambda item: {'provider': item[0], 'score': item[1]*100}, zip(providers_names, scores)))
    result.sort(key=operator.itemgetter('score'), reverse=True)
    return result
