from configparser import ConfigParser
import os

# create config file class
class CreateConfig:

    # init config
    def configInit(self):
        folders = []
        while True:
            pathToAdd = str(input(f"Give me paths to add, if you don't need more path write 0:\n"))
            if pathToAdd == "0":
                break
            else:
                folders.append(pathToAdd)
        if len(folders) > 0:
            config = ConfigParser()
            resultConfig = ""
            for x in folders:
                resultConfig += x + ";"

            # put and save config folders to search

            os.makedirs("configs", exist_ok=True)
            config['folder_list'] = {'musicFolder': str(resultConfig)}
            with open("configs/config_folders.ini", 'w') as configfile:
                config.write(configfile)
