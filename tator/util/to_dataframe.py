import pandas as pd

def to_dataframe(objects):
    """ Converts list of objects to :class:`pandas.DataFrame`.

    :param object: List of objects.
    :returns: Pandas dataframe.
    """
    out = None
    if objects:
        dict_objects = [obj.to_dict() for obj in objects]
        out = pd.DataFrame(data=dict_objects,
                           columns=dict_objects[0].keys())
    return out
