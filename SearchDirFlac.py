import glob
import CreateList


class SearchDirFlac:

    def search_files(self):
        list_files = []

        for file in glob.glob("**/*.flac", recursive=True):
            list_files.append(file)
        # create data about file
        complete_data = CreateList.CreateList()
        result = complete_data.create_list_music(list_files)
        return result


