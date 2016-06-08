# CREDIT: Peter Norvig's Udacity CS212 Course on Design of Computer Programs. All credit goes to him.
def memoize(f):
    """
    A decorator that caches the return value for each call to f(args).
    Then when called again with some arguments, we can just look it up.
    """
    cache = {}

    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            """Some elements of args cannot be a dict key"""
            return f(args)
        return _f
