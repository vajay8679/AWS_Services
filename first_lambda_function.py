import json

def sum_two_int(a,b):
    return (a+b)

def lambda_handler(event, context):
    # TODO implement
    print("event :",event)
    print("context :",context)
    print("Hello this is my first function !!!")
    print(sum_two_int(2,3))