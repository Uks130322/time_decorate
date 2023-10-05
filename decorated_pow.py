import time


def decorator_time(fn):
    def wrapper(*args):
        print(fn)
        t0 = time.time()
        for i in range(100):
            result = fn(*args)
        dt = (time.time() - t0) / 100
        print(f"Delta time: {dt:.10f}")
        return result
    return wrapper


def power(n=2):
    return 10_000_000 ** n

def in_build_pow():
    return pow(10_000_000, 100)

power = decorator_time(power)
in_build_pow = decorator_time(in_build_pow)

#print(power())
#in_build_pow


def counter(func):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Function was called {count} times")
        return func(*args, **kwargs)
    return wrapper


@counter
def big_letters(word: str) -> str:
    return word.upper()

#print(big_letters("hello"))
#print(big_letters("bye"))
#print(big_letters("see you soon"))


def save_in_dict(func):
    dct = dict()

    def wrapper(n):
        nonlocal dct
        result = dct.setdefault(n, func(n))
        print(f"Function was called witn {n}")
        print(dct)
        return result
    
    return wrapper

@save_in_dict
def f(n):
   return n * 123456789

print(f(5))
print(f(3))
print(f(1))
print(f(0))
print(f(5))
