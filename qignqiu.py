import numpy as np
import re
import requests
url='http://localhost:63342/PythonProject/shijainhuoqu.html?_ijt=9mjngd8instqigpfmtm91kdg87&_ij_reload=RELOAD_ON_SAVE'
re=requests.get(url)
print(re.json())