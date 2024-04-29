# This is just a simple library to print colorful using sys.stderr to write.

```python
from colorful_logging.colorful_logging import color_print, c_print

# color_print(*values: tuple[Any, ...])
# c_print(*values: tuple[Any, ...])
# ['red', 'green', 'yellow', 'blue', 'pink', 'cyan', 'gray', 'black', 'dark red', 'dark green', 'dark yellow', 'dark blue', 'dark pink', 'dark cyan', 'bright black', 'underline']

l = [1, 2, 3]

# === FOR EXAMPLE === #

color_print('ali is good', l, 'cyan')
# will produce (with colored text): 
# ali is good [1, 2, 3]


c_print(l, 'sample text', 'green')
# will produce (with colored text): 
# [1, 2, 3] sample text
```

### If your input color not found, function will print the color name. for example:

```python
from colorful_logging.colorful_logging import color_print, c_print

color_print('ali is good', 'cyann')
# will produce
# ali is good cyann
```

## To get specific color:

```python
from colorful_logging.colorful_logging import get_color

c = get_color("dark blue")
r = get_color("reset")

text = f"hello {c}Ali{r}"
print(text)
```

## You can also colorize you object:

```python
from colorful_logging.colorful_logging import colorize

p = Person(name="ali", age=18)

colorized_elem = colorize("pink", p)

print(f"hello {colorized_elem}")
```

## Possible colors:

```
['red', 'green', 'yellow', 'blue', 'pink', 'cyan', 'gray', 'black', 'dark red', 'dark green', 'dark yellow', 'dark blue', 'dark pink', 'dark cyan', 'bright black', 'underline']
```

