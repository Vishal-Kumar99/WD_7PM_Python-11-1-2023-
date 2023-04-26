from first import intro
def super(arg):
    def inner():
        print("This is krishna")
        arg()
    return inner

val=super(intro)
val()
