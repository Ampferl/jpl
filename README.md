# Welcome to JPL
## About
![](https://i.imgur.com/lPuSHq5.png) 
> 
> JPL is a own little fun project. Here I code a own Programming Language with an Interpreter. 
>

### What can you do with it?
- variables (Strings, Numbers(Int/Float) and Lists)
- if statements (comparisons and locical operations)
- for/while loops (with break and continue)
- functions (with and without return)
- run code files(.jpl)
### How do you start?
First, download the repository with git:`git clone https://github.com/Ampferl/jpl.git`
You also need to download [Python 3](https://www.python.org/downloads/release/python-380/)!


If everything is installed, you can go to the downloaded folder and enter `python3 shell.py` into the console.
Or execute a program immediately: `python3 shell.py example/functions.jpl`

Now you can use the programming language!

For Example enter: `print("Hello World")`

### Explanations:
#### Variables
`var :identifier = :expr`

#### If statements
You can use only if:
```
if(:expr){
    :statements
}
```
or with elif:
```
if(:expr){
    :statements
}elif(:expr){
    :statements
}
```
or also a else at the end:
```
if(:expr){
    :statements
}else{
    :statements
}
```
#### For/While Loops
##### For-Loops:
```
for(:start_value;:end_value[;:step]){
    :statements
}
```
For Example:
```
for(i=1;10){
    print(i)
}
```
##### While-Loops:
```
while(:expr){
    :statements
}
```
For Example:
```
var i = 0
while(i<=10){
    print(i)
    var i = i + 1
}
```
Also you can use a `break` or a `continue`!
#### Functions
```
function :func_name(:args){
    :statements
}
```
Also you can use a `return`!
#### Run Code Files
```
run(:path_to_file)
```
### Some Extra Functions
#### I/O Functions
- `print(expr)`
- `input()`
#### Check expr Type
- `is_number(expr)`
- `is_string(expr)`
- `is_list(expr)`
- `is_function(expr)`
#### Lists
- `append_l(list, value)`
- `pop_l(list, index)`
- `extend_l(listA, listB)`
- `len_l(list)`
- `get_l(list, index)`
- `set_l(list, index, string)`
- `split(string, separator)`
- `join(list, separator)`
- `search_l(list, search_string)`
#### Math
- `pow(base, exponent)`
- `mod(num, divisor)`
- `rand(start_value, end_value)`
- `pi()`
- `round(:number, :digits)`
- `cos(:number)`
- `sin(:number)`
- `tan(:number)`
#### Formats
- `int(:string)`
- `str(:number)`
- `float(:string/:number)`
- `hash(:string, :type)` `(Types: md5, sha1, sha256, sha512)`
#### Date
- `datetime()`
- `date()`
- `date_year()`
- `date_month()`
- `date_month_name()`
- `date_day()`
- `time()`
#### String
- `replace(string, replace_this, replacer)`
#### File I/O
- `read_file(:path)` `(output -> list)`
- `write_file(:path, :list, :append)` `(:append: true/false)`
