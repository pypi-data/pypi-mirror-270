class Bunch(dict):
    def __init__(self, *args, **kwargs):
        super(Bunch, self).__init__(*args, **kwargs)
        for key, value in self.items():
            if isinstance(value, dict):
                self[key] = Bunch(value)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError as e:
            raise AttributeError(e)

    def __setattr__(self, key, value):
        if isinstance(value, dict):
            value = Bunch(value)
        self[key] = value

    def __delattr__(self, item):
        try:
            del self[item]
        except KeyError as e:
            raise AttributeError(e)

    def to_dict(self):
        return {key: self._to_dict(value) for key, value in self.items()}

    @staticmethod
    def _to_dict(value):
        if isinstance(value, Bunch):
            return value.to_dict()
        elif isinstance(value, list):
            return [Bunch._to_dict(item) for item in value]
        else:
            return value
