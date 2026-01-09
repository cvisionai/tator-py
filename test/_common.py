import json

def is_number(x):
    try:
        float(x)
        return True
    except:
        return False

def fail_str(a, b, key):
    a.pop('created_datetime', None)
    b.pop('created_datetime', None)
    a.pop('modified_datetime', None)
    b.pop('modified_datetime', None)
    return f"Failed on key: {key}\na: {json.dumps(a, indent=4)}\nb: {json.dumps(b, indent=4)}"

def assert_vector_equal(a,b):
    assert(len(a)==len(b))
    for idx,v in enumerate(a):
        assert(a[idx] == b[idx])

def is_numeric_list(x):
    """Check if x is a list of numbers (like geopos coordinates)"""
    if not isinstance(x, list):
        return False
    if len(x) == 0:
        return True
    return all(is_number(item) for item in x)

def is_nested_numeric_list(x):
    """Check if x is a list of lists of numbers (like points)"""
    if not isinstance(x, list):
        return False
    if len(x) == 0:
        return True
    return all(is_numeric_list(item) for item in x)

def compare_numeric_lists(a, b, tolerance=0.0001):
    """Compare two lists of numbers with tolerance"""
    if len(a) != len(b):
        return False
    for val_a, val_b in zip(a, b):
        diff = abs(float(val_a) - float(val_b))
        if diff >= tolerance:
            return False
    return True

def compare_nested_numeric_lists(a, b, tolerance=0.0001):
    """Compare two nested lists of numbers with tolerance"""
    if len(a) != len(b):
        return False
    for list_a, list_b in zip(a, b):
        if not compare_numeric_lists(list_a, list_b, tolerance):
            return False
    return True

def assert_close_enough(a, b, exclude=[], mapping={}):
    if not isinstance(a, dict):
        a = a.to_dict()
    if not isinstance(b, dict):
        b = b.to_dict()
    for key in a:
        if key in exclude:
            continue
        # Skip datetime fields - they may have minor differences
        if key in ['created_datetime', 'modified_datetime']:
            continue
        key_b = key
        if key in mapping:
            key_b = mapping[key]
        assert key_b in b, fail_str(a, b, key)
        if is_number(a[key]):
            diff = abs(a[key] - b[key_b])
            assert diff < 0.0001, fail_str(a, b, key)
        elif isinstance(a[key], dict):
            assert_close_enough(a[key], b[key_b])
        elif is_nested_numeric_list(a[key]) and is_nested_numeric_list(b[key_b]):
            # Compare nested lists of numbers with tolerance (e.g., points)
            assert compare_nested_numeric_lists(a[key], b[key_b]), fail_str(a, b, key)
        elif is_numeric_list(a[key]) and is_numeric_list(b[key_b]):
            # Compare lists of numbers with tolerance (e.g., geopos, float_array)
            assert compare_numeric_lists(a[key], b[key_b]), fail_str(a, b, key)
        else:
            assert a[key] == b[key_b], fail_str(a, b, key)
