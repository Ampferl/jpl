import jpl
result, error = jpl.run('<stdin>', 'run("core/main.jpl")')
while True:
    text = input('jpl > ')
    if text.strip() == "": continue
    result, error = jpl.run('<stdin>', text)

    if error: print(error.as_string())
    elif result: 
        if len(result.elements) == 1:
            print(repr(result.elements[0]))
        else: 
            print(repr(result))