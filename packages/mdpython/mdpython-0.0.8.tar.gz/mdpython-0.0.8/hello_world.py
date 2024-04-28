import pandas as pd
from mdpython.debugutils import find

a = [1,2]
b = {"k": 1}
s = pd.Series(range(10))

find.search_function(pd, "")
find.list_elements(s, "truncate", showdoc=True)

