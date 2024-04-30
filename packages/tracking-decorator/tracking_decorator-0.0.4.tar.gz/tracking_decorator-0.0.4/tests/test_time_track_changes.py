from tracking_decorator.track_changes import track_changes

class ReferenceClass:
    def __init__(self):
        self.var = 0

@track_changes("base_variable", "reference")
class BaseClass():
    def __init__(self, reference: ReferenceClass):
        self.base_variable = 0
        self.reference = reference
        self.untracked = []

@track_changes("list_type_r", "set_type_r", "dict_type_r")
class CollectionClass:
    def __init__(self):
        self.list_type = [20, 40, 60, 80, 100]
        self.set_type = {1, 3, 5}
        self.dict_type = {"a": "b", "c": "d", "e": "f"}


def test_time_tracked(): # 1.18s (~8 times slower than untracked)

    ref = ReferenceClass()
    base = BaseClass(ref)

    for i in range(10000000):
        base.base_variable = i

def test_time_untracked(): # 0.14s

    ref = ReferenceClass()
    base = BaseClass(ref)

    for i in range(10000000):
        base.untracked = i


def test_list_time_tracked(): # 3. (~13 times slower than untracked)

    coll = CollectionClass()

    for i in range(10000000):
        coll.list_type = [i]

def test_list_time_untracked(): # 0.27s

    ref = ReferenceClass()
    base = BaseClass(ref)

    for i in range(10000000):
        base.untracked = [i]