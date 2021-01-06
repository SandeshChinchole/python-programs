
def get_bark(weight):
    if weight > 20:
        return 'WOOF WOOF'
    else:
        return 'woof woof'

codies_bark = get_bark(10)
print("codie's bark is", codies_bark)
