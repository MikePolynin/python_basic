class MyDict(dict):
    def get(self, key):
        result = super().get(key)
        if result is None:
            return 0
        else:
            return result
