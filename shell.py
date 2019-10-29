import jpl

while True:
    text = input('jpl > ')
    result, error = jpl.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)