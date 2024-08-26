class DotDict(dict):
    def __init__(self, *args, **kwargs):
        super(DotDict, self).__init__(*args, **kwargs)
        for key, value in self.items():
            if isinstance(value, dict):
                self[key] = DotDict(value)

    def __setitem__(self, key, value):
        if isinstance(value, dict) and not isinstance(value, DotDict):
            value = DotDict(value)
        super(DotDict, self).__setitem__(key, value)

    def update(self, *args, **kwargs):
        for key, value in dict(*args, **kwargs).items():
            if isinstance(value, dict) and not isinstance(value, DotDict):
                self[key].update(value)
            else:
                self[key] = value

    def merge(self, other):
        for key, value in other.items():
            if isinstance(value, dict) and isinstance(self.get(key), DotDict):
                self[key].merge(value)
            else:
                self[key] = value

    def to_dict(self):
        result = {}
        for key, value in self.items():
            if isinstance(value, DotDict):
                result[key] = value.to_dict()
            else:
                result[key] = value
        return result

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            if key in dir(dict):
                return getattr(self.to_dict(), key)
            return None

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError:
            raise AttributeError(f"'DotDict' object has no attribute '{key}'")
