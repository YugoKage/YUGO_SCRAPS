
from Scrap17_dictStore import data


Mdata = {"User3": "Cool"}

data.update(Mdata)

combined_dict = data | Mdata

print(*data.items(), sep=", ",)