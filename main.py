from SearchDirFlac import *
from CreateList import *

start = SearchDirFlac()
list_files = start.search_files(str(input("Give me path to check:")))


start1 = CreateList()
chceck_duplicate = start1.create_dictionary_music(list_files)

result = start1.print_duplicates(chceck_duplicate)
save_Data = start1.compare_music(result)

with open("result.txt", mode='w', encoding='utf-8') as file_s:
        separator = "\n"
        for x in save_Data:
                print(x, sep=separator, file=file_s)


