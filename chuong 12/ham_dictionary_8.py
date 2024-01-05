
def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}

def get_value(dict_, key, default=None):
    return dict_.get(key, default)

def remove_key(dict_, key):
    if key in dict_:
        del dict_[key]

def update_dict(dict_, other_dict):
    dict_.update(other_dict)

def keys_as_list(dict_):
    return list(dict_.keys())

def values_as_list(dict_):
    return list(dict_.values())

def items_as_list(dict_):
    return list(dict_.items())
