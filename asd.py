class Meneger:
    def __init__(self, v):
        self.__v = v

    def __enter__(self):
        self.temp = self.__v[:]
        return self.temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__v[:] = self.temp
        False


v1 = [1, 2, 3]
v2 = [1, 2, 3]
try:
    with Meneger(v1) as dv1:
        for i in range(len(dv1)):
            dv1[i] = v1[i] + v2[i]
except:
    print(v1)
    print(dv1)
else:
    print(dv1)
    print(v1)
