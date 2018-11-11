length_lambda=lambda data:len(data)


def addition(data):
    return sum(data)


def lengthElement(data):
    return length_lambda(data)


def higher(f,data):
    return f(data)

d=[1,2,3,4,5]
print("Sum ",higher(addition,d))
print("length of array ",higher(lengthElement,d))