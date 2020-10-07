from SearchDirFlac import *
from CreateList import *

start = SearchDirFlac()
list_files = start.search_files()
print(list_files)

start1 = CreateList()
chceck_duplicate = start1.create_dictionary_music(list_files)
print("listfiles:",chceck_duplicate)
result = start1.print_duplicates(chceck_duplicate)
save_Data = start1.compare_music(result)
print("save_data:",save_Data)
with open("result.txt", mode='w', encoding='utf-8') as file_s:
        separator = "\n"
        for x in save_Data:
                print(x, sep=separator, file=file_s)


