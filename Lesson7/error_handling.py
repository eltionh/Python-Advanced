try:
    result = 10/0
except ZeroDivisionError:
    print("Error, Tried to divide by zero.")





text = "This is not a number"

try:
    text_to_int = int(text)
except Exception as e:
    print("An error occured while parsing the data:  ", e)



try:
    result = 10/2
except ZeroDivisionError:
    print("Error, tried to divide by zero.")
else:
    print("Division succesful.result: ", result)
