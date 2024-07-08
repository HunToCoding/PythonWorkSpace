# package
# from Travel.Thai import ThaiPackage
# import Travel.Thai as trTh
# trip_to = trTh.ThaiPackage()
# trip_to.detail()

# from Travel import vietnam
# import Travel.vietnam as vi
# trip_to = vi.VietnamPackage()
# trip_to.detail()

from Travel import *
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# trip_toto = Thai.ThaiPackage()
# trip_toto.detail()

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(Thai))  
# c:\Python312\Lib\random.py
# c:\Python312\Lib\Travel\Thai.py