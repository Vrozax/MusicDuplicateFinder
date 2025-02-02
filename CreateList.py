from tinytag import TinyTag

"""
create_list_music()

"""


class CreateList:
    def create_dictionary_music(self, list_files):
        dict_music = {}

        for x in list_files:
            try:
                path = str(x[0]) + "\n"
                add = x[1].lower() + ";" + x[2].lower()
                if add not in dict_music:
                    dict_music[add] = {"quantity": 0, "path": ""}
                if add in dict_music:
                    dict_music[add]["quantity"] += 1
                    dict_music[add]["path"] += path
            except AttributeError:
                path = str(x[0]) + "\n"

                add = "unknown"
                if add not in dict_music:
                    dict_music[add] = {"quantity": 0, "path": ""}
                if add in dict_music:
                    dict_music[add]["quantity"] += 1
                    dict_music[add]["path"] += path

        return dict_music

    def create_list_music(self, list_files):
        complete_list = []
        for x in list_files:
            try:
                path = x
                tag = TinyTag.get(x)
                artist = tag.artist
                title = tag.title
                bit_rate = tag.bitrate
                file_size = tag.filesize
                data = [path, artist, title, bit_rate, file_size]
                complete_list.append(data)

            except:
                print("error")
        return complete_list

    def print_duplicates(self, list_files):
        list_duplicates = []
        for check in list_files:
            if list_files[check]["quantity"] > 1:
                result = list_files[check]["path"].split("\n")
                for x in result:
                    list_duplicates.append(x)

        return list_duplicates

    def compare_music(self, source):
        data_to_save = []
        for path in source:
            try:

                x = path
                tag = TinyTag.get(x)
                artist = tag.artist
                title = tag.title
                bit_rate = tag.bitrate
                file_size = tag.filesize
                data = [path, artist, title, bit_rate, file_size]
                print("data", data)
                data_to_save.append(data)

            except:
                print("Brak danych")
        return data_to_save
