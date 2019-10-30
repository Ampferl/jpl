import jpl

while True:
    text = input('jpl > ')
    result, error = jpl.run('<stdin>', text)

    if error: print(error.as_string())
    elif result: print(result)