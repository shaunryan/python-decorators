def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice


@do_twice
def return_greet(name:str):
    print("Creating greeting")
    return f"Hello {name}"

hi_shaun = return_greet(name="Shaun")

print(hi_shaun)