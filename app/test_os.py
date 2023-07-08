import os
import base64
from typing import IO

path = "year"

try:
    os.mkdir(path)
except OSError:
    print ("Создать директорию %s не удалось" % path)
else:
    print ("Успешно создана директория %s" % path)
#
# certif = b'''C\x96\x00\n\x00\x00\x00\x00C\x96\x00\x1b\x00\x00\x00\x00C\x96\x00-\x00\x00\x00\x00C\x96\x00?\x00\x00\x00\x00C\x96\x07M\x00\x00\x00\x00C\x96\x07_\x00\x00\x00\x00C\x96\x07p\x00\x00\x00\x00C\x96\x07\x82\x00\x00\x00\x00C\x96\x07\x94\x00\x00\x00\x00C\x96\x07\xa6Cq\xf0\x7fC\x96\x07\xb8DJ\x81\xc7C\x96\x07\xcaD\xa5\x9dtC\x96\x07\xdcD\xb6\x97\x11C\x96\x07\xeeD\x8b\x8flC\x96\x07\xffD\x03\xd4\xaaC\x96\x08\x11B\x05&\xdcC\x96\x08#\x00\x00\x00\x00C\x96\x085C\x0c\xc9\xb7C\x96\x08GCy\xc0\xebC\x96\x08YC\x81\xa4xC\x96\x08kC\x0f@\x9bC\x96\x08}\x00\x00\x00\x00C\x96\x08\x8e\x00\x00\x00\x00C\x96\x08\xa0\x00\x00\x00\x00C\x96\x08\xb2\x00\x00\x00\x00C\x96\x86\xf9\x00\x00\x00\x00C\x96\x87\x0b\x00\x00\x00\x00C\x96\x87\x1d\x00\x00\x00\x00C\x96\x87/\x00\x00\x00\x00C\x96\x87AA\x0b\xe7PC\x96\x87SCI\xf5gC\x96\x87eC\xd4J\xeaC\x96\x87wD\r\x17EC\x96\x87\x89D\x00F6C\x96\x87\x9bC\x9cg\xdeC\x96\x87\xadB\xd56\x0cC\x96\x87\xbf\x00\x00\x00\x00C\x96\x87\xd1\x00\x00\x00\x00C\x96\x87\xe3\x00\x00\x00\x00C\x96\x87\xf5\x00\x00\x00\x00C\x9cY}\x00\x00\x00\x00C\x9cY\x90\x00\x00\x00\x00C\x9cY\xa4\x00\x00\x00\x00C\x9cY\xb7\x00\x00\x00\x00C\x9cY\xcbC\x1f\xbd\xa3C\x9cY\xdeCCz{C\x9cY\xf1CD\x02\xa7C\x9cZ\x05C+\x9d\x97C\x9cZ\x18C\x03R\xe3C\x9cZ,\x00\x00\x00\x00C\x9cZ?
# [stuff omitted as it exceeded SO's body length limits]
# \xbb\x00\x00\x00\x00D\xc5!7\x00\x00\x00\x00D\xc5!\xb2\x00\x00\x00\x00D\xc7\x14x\x00\x00\x00\x00D\xc7\x14\xf6\x00\x00\x00\x00D\xc7\x15t\x00\x00\x00\x00D\xc7\x15\xf2\x00\x00\x00\x00D\xc7\x16pC5\x9f\xf9D\xc7\x16\xeeC[\xb5\xf5D\xc7\x17lCG\x1b;D\xc7\x17\xeaB\xe3\x0b\xa6D\xc7\x18h\x00\x00\x00\x00D\xc7\x18\xe6\x00\x00\x00\x00D\xc7\x19d\x00\x00\x00\x00D\xc7\x19\xe2\x00\x00\x00\x00D\xc7\xfe\xb4\x00\x00\x00\x00D\xc7\xff3\x00\x00\x00\x00D\xc7\xff\xb2\x00\x00\x00\x00D\xc8\x001\x00\x00\x00\x00'''

with open('year/test.txt', 'w') as filehandle:
    filehandle.write('Hello, world!\n')
    filehandle.close()