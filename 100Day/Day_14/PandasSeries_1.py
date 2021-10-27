import numpy as np
import pandas as pd

labels_list = ["anton","sarah","maria","jeremy","ali"]
data_list = [1,2,3,4,5]
a=pd.Series(data = data_list,index=labels_list )
print(a)
b = pd.Series(data_list) #index gondermedigimiz icin indexi kendisi otomatik olarak atamis oldu
print(b)


npArray = np.array([23,34,25,45,56,67])

print(pd.Series(npArray))


datadict = {"ali":30,"kemal":80, "mahmut":99}
print(pd.Series(datadict))
