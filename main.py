from pathlib import Path
from configparser import ConfigParser
from createConfig import *
from SearchDirFlac import *
from CreateList import *

# #list_files = start.search_files(str(load_config['folder_list']))
# check are config files already exist
my_file = Path("configs/config_folders.ini")
if my_file.is_file():
    start = SearchDirFlac()
    #

    # read config
    config = ConfigParser()
    config.read('configs/config_folders.ini')
    foldersFromConfig = dict(config.items('folder_list'))
    #details_dict['musicfolder']

    list_files = start.search_files(str(foldersFromConfig['musicfolder']))


    start1 = CreateList()
    chceck_duplicate = start1.create_dictionary_music(list_files)

    result = start1.print_duplicates(chceck_duplicate)
    save_Data = start1.compare_music(result)

    with open("last_result.txt", mode='w', encoding='utf-8') as file_s:
        separator = "\n"
        for x in save_Data:
            print(x, sep=separator, file=file_s)
else:
    x = CreateConfig()
    x.configInit()
