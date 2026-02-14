import math

def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: {object} {type(object)}")
    elif isinstance(object, float) and math.isnan(object):
        print(f"Cheese: {object} {type(object)}")
    elif object is False:
        print(f"Fake: {object} {type(object)}")
    elif object == 0 and isinstance(object, int):
        print(f"Zero: {object} {type(object)}")
    elif object == "" and isinstance(object, str):
        print(f"Empty: {type(object)}")
    else:
        print("Type not Found")
        return 1
    return 0
