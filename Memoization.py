from functools import wraps, lru_cache, cache
from time import perf_counter


def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        key = str(args)
        if key not in cache:
            cache[key] = func(*args)
        return cache[key]
    return wrapper


@memoize
def addToDict():
    beatRecord = 0
    time, dist = 49877895, 356137815021882
    for j in range(time):
        if j*(time-j) > dist:
            beatRecord += 1
    return beatRecord


# ulimit = 8176
if __name__ == "__main__":
    start = perf_counter()
    f = addToDict()
    end = perf_counter()
    print(f)
    print(f"{end - start} seconds")
