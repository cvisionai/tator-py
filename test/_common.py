import json

def is_number(x):
    try:
        float(x)
        return True
    except:
        return False

def print_fail(a, b, key):
    a.pop('created_datetime', None)
    b.pop('created_datetime', None)
    a.pop('modified_datetime', None)
    b.pop('modified_datetime', None)
    print(f"Failed on key: {key}")
    print(f"a: {json.dumps(a, indent=4)}")
    print(f"b: {json.dumps(b, indent=4)}")

def assert_vector_equal(a,b):
    assert(len(a)==len(b))
    for idx,v in enumerate(a):
        assert(a[idx] == b[idx])

def assert_close_enough(a, b, exclude=[]):
    if not isinstance(a, dict):
        a = a.to_dict()
    if not isinstance(b, dict):
        b = b.to_dict()
    for key in a:
        if key in exclude:
            continue
        if key not in b:
            print_fail(a, b, key)
        assert key in b
        if is_number(a[key]):
            diff = abs(a[key] - b[key])
            if diff > 0.0001:
                print_fail(a, b, key)
            assert diff < 0.0001
        else:
            if a[key] != b[key]:
                print_fail(a, b, key)
            assert a[key] == b[key]

