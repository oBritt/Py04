

def callLimit(limit: int):
    count = 0

    def callLimiter(function):
        def limit_function(*args: any, **kwds: any):
            """limit function"""
            nonlocal count
            count += 1
            if count > limit:
                print("Error", function, "call too many times")
                return
            return function(*args, **kwds)
        return limit_function
    return callLimiter
