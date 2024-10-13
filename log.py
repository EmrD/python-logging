import logging

logging.basicConfig(
    filename="app.log",
    encoding="utf-8",
    filemode="a",
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)

def plus(x , y):
    logging.warning("add function called with " + str(x) + " and " + str(y))
    return x + y

def minus(x , y):
    logging.warning("minus function called with "+ str(x) + " and " + str(y))
    return x - y

def multiply(x , y):
    logging.warning("multiply function called with "+ str(x) + " and " + str(y))
    return x * y

def divide(x , y):
    logging.warning("divide function called with "+ str(x) + " and " + str(y))
    return x / y

print(plus(10,20))
print(minus(10,20))
print(multiply(10,20))
print(divide(10,20)) # Example Usage