import glob
import CreateList


class SearchDirFlac:

    def search_files(self, pathFolder):
        list_files = []
        files_list = [".mp3", ".flac", ".wav"]
        for fileType in files_list:
            for file in glob.glob(pathFolder + "/*" + fileType, recursive=True):  # "**/*"+fileType
                list_files.append(file)

        # create data about file
        complete_data = CreateList.CreateList()
        result = complete_data.create_list_music(list_files)
        return result
