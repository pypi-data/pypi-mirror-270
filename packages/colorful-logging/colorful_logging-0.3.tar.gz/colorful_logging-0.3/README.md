# This is just a simple library to print colorful using sys.stderr to write.

```python
from colorful_logging import color_print

# color_print(
# text: str = your text
# color: str = 'red', 'blue', ...
# fmt: bool = True or False
# lvl: str -> it's just a simple naming when using the "fmt=True"
# )


# for example:
color_print(
    text='ali is good',
    color='cyan',
    fmt=True,
    lvl='ALI LEVEL'
)
# will produce (with colored text): 
# ALI LEVEL    24-02-06 18:49:15, File "where the color print executed", Line 1, in "the module", msg: ali is good


# here also you can use it without formatting the line: 
color_print('ali is good', 'bold')
```
