import core.main as jpl
import sys 
result, error = jpl.run('<stdin>', 'run("core/main.jpl")')
try:
    if sys.argv[1]:
        result, error = jpl.run('<stdin>', 'run("'+ sys.argv[1] +'")')
except:
    pass
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