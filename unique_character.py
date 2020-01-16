
def is_unique(char1):

    return len(char1) == len(set(char1))

print(is_unique("unique"))
print(is_unique("bear"))
