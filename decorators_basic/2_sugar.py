from datetime import datetime

def not_during_the_night(func):

    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass
        
    return wrapper


@not_during_the_night
def say_whee():
    print("Sugar Whee!")


say_whee()