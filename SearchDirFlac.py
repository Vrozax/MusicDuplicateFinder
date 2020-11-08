import glob
import CreateList


class SearchDirFlac:

    def search_files(self, pathFolder):
        listFolders = pathFolder.split(";")

        list_files = []
        files_list = [".mp3", ".flac", ".wav"]
        for fileType in files_list:
            for folder in listFolders:
                try:
                    for file in glob.glob(folder + "/*" + fileType, recursive=True):  # "**/*"+fileType
                        list_files.append(file)
                except:
                    print(f"Folder {folder} not exist")


        # create data about file
        complete_data = CreateList.CreateList()
        result = complete_data.create_list_music(list_files)
        return result
