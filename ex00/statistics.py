

def check_args(args: list) -> bool:
    """checks if args and kwargs are ok"""
    try:
        for i in args:
            float(i)
    except Exception:
        print("ERROR args only numbers are allowed")
        return 1
    return 0


def ft_mean(args: list):
    """calculates mean"""
    counter = 0
    total = 0
    for i in args:
        counter += 1
        total += i
    return total / counter


def ft_mean_p(args: list, length: int):
    """prints mean"""
    if not length:
        print("ERROR")
        return
    print(f"mean: {ft_mean(args)}")


def ft_median(args: list, length: int):
    """prints median"""
    if not length:
        print("ERROR")
        return
    if length % 2:
        med = args[int(length // 2)]
    else:
        med = (args[int(length // 2)] + args[int(length // 2) + 1]) / 2.0
    print(f"median: {med}")


def ft_quartile(args: list, length: int):
    """prints quartiles"""
    if not length:
        print("ERROR")
        return
    length -= 1
    ind = length / 4
    q = []
    if (ind == int(ind)):
        ind = int(ind)
        q.append(args[ind])
    else:
        factor = ind - int(ind)
        ind = int(ind)
        q.append(args[ind] * factor + args[ind + 1] * factor)
    ind = length / 4.0 * 3.0
    if (ind == int(ind)):
        ind = int(ind)
        q.append(args[ind])
    else:
        factor = ind - int(ind)
        ind = int(ind)
        q.append(args[ind] * factor + args[ind + 1] * factor)
    print(f"quartile : {q}")


def my_abs(number):
    """implemented custom abs"""
    if number < 0:
        return -number
    return number


def square_roots(number):
    """square roots function"""
    mini = 0
    maxi = int(number > 1) * number + int(number <= 1)
    error = 1e-7
    while (1):
        mid = (maxi + mini) / 2.0
        if my_abs(mid * mid - number) <= error:
            break
        elif mid * mid > number:
            maxi = mid
        else:
            mini = mid
    return mid


def ft_std(args: list, length: int):
    """prints std"""
    if not length:
        print("ERROR")
        return
    mean = ft_mean(args)
    total = 0
    for i, e in enumerate(args):
        total += (mean - args[i]) ** 2
    total /= length
    std = square_roots(total)
    print(f"std : {std}")


def ft_var(args: list, length: int):
    """prints var"""
    if not length:
        print("ERROR")
        return
    mean = ft_mean(args)
    total = 0
    for i, e in enumerate(args):
        total += (mean - args[i]) ** 2
    var = total / length
    print(f"var : {var}")


def ft_statistics(*args: any, **kwargs: any) -> None:
    """outputs statistics"""
    args = list(args)
    if check_args(args):
        return
    lenght = 0
    for i, e in enumerate(args):
        args[i] = float(args[i])
        lenght += 1
    args = sorted(args)
    kwargs = list(kwargs.values())
    for i in kwargs:
        if i == "mean":
            ft_mean_p(args, lenght)
        if i == "median":
            ft_median(args, lenght)
        if i == "quartile":
            ft_quartile(args, lenght)
        if i == "std":
            ft_std(args, lenght)
        if i == "var":
            ft_var(args, lenght)
