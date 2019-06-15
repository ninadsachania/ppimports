# Pretty Print Python `import`s

`imt.py` takes all the `import <mod>[, <mod>]` lines out of a `.py` file, and sorts them length-wise. It servers no other purpose than to make `import`s in a python source file look all nice and pretty.


## Usage

For now, it prints to `STDOUT` rather than making a change in the source file.

```shell
$ imt.py <file>
import .
import ..
import ...
```

Example:

We have a file called `test.py`:

```python
import os
import sys
import re
import flask
import requests
import pygame
import random
import math

import os, sys, imp

try:
    import sqlite3
except:
    pass
finally:
    pass


def main():
    # Doesn't work on comments
    # import mate
    print('Hello World')

if __name__ == '__main__':
    main()
```

Now,

```shell
$ ./imt.py test.py
import re
import os
import sys
import imp
import math
import flask
import random
import pygame
import sqlite3
import requests
```
