menu = {'sushi' : 5,'tempura':4,'mochi': 3,'onigiri': 4,'takoyaki': 4}

def reverse_Lookup(dictionary, value):
    if dictionary == menu:
        for food, price in menu:
            if value == price:
                print (food)

reverse_Lookup (input(),int(input()))