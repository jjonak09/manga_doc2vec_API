import copy
import json


def alchemyrowtodict(obj):
    entity = copy.deepcopy(obj)    # ※２
    objdict = entity.__dict__
    if '_sa_instance_state' in objdict:        # ※１
        del objdict['_sa_instance_state']
    return objdict


def alchemytodict(obj):
    if isinstance(obj, list):
        dicts = []
        for row in obj:
            rowdict = alchemyrowtodict(row)
            dicts.append(rowdict)
        return dicts
    else:
        return alchemyrowtodict(obj)


def alchemytojson(obj):
    dictobj = alchemytodict(obj)
    return json.dumps(dictobj, indent=2, ensure_ascii=False)
