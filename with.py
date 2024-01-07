class Meneger:
    def __init__(self, v):
        self.temp = v[:]

    def __enter__(self):
        return self.temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            False


v1 = [1, 2, 3]
v2 = [1, 2, 3]
try:
	with Meneger(v1) as dv1:
		for i in range(len(dv1)):
			dv1[i] = v1[i] + v2[i]
except:
	print(dv1)
	print(v1)
else:
	print(dv1)
	print(v1)
