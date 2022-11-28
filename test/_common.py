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

def assert_close_enough(a, b, exclude=[], mapping={}):
    if not isinstance(a, dict):
        a = a.to_dict()
    if not isinstance(b, dict):
        b = b.to_dict()
    for key in a:
        if key in exclude:
            continue
        key_b = key
        if key in mapping:
            key_b = mapping[key]
        assert key_b in b, fail_str(a, b, key)
        if is_number(a[key]):
            diff = abs(a[key] - b[key_b])
            assert diff < 0.0001, fail_str(a, b, key)
        else:
            assert a[key] == b[key_b], fail_str(a, b, key)

