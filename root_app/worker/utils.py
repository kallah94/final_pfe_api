# define functions that help to sanitize data before processing
from munch import Munch


def sanitize_atoms(atoms: []):
    atoms_object = []
    atoms_names = []
    for atom in atoms:
        tmp_atom = Munch.fromDict(atom)
        atoms_object.append(tmp_atom)
        atoms_names.append(tmp_atom.name)
    return Munch.fromDict(dict(zip(atoms_names, atoms_object)))


def sanitize_attributes(attributes: []):
    attributes_object = []
    attributes_names = []
    for attribute in attributes:
        tmp_attribute = Munch.fromDict(attribute)
        attributes_object.append(tmp_attribute)
        attributes_names.append(tmp_attribute.name)
    return attributes_object, attributes_names


def sanitize_providers(providers: []):
    providers_object = []
    for prov in providers:
        tmp_prov = Munch.fromDict(prov)
        providers_object.append(tmp_prov)
    return providers_object
