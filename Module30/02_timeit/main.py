import timeit

res: float = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(res)

res_2: float = timeit.timeit('map(lambda elem: "-".join(str(elem)), range(100))', number=10000)
print(res_2)

res_3: float = timeit.timeit('"-".join([str(elem) for elem in range(100)])', number=10000)
print(res_3)
