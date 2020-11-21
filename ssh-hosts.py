import os
import re
import colorama
from colorama import Fore, Back, Style
from pathlib import Path


class SSH_Host_Lister:

    # Array to store config files.
    files = []

    home = str(Path.home())
    directory_in_str = f"{home}/.ssh/config.d/"

    # Keyword in config file.
    KeyWord = "[Host]"
    directory = os.fsencode(directory_in_str)

    # Print main config file data (~/.ssh/config
    main_config = f"{home}/.ssh/config"

    # Class constructor
    def __init__(self):
        # Get $HOME directory
        home = str(Path.home())
        print(home)
        self.configfilebrowser()
        self.printcontent(self.main_config)

        # Files in subdirectory...
        for f in self.files:
            self.printcontent(f)

    # Config file browser method
    def configfilebrowser(self):
        # r=root, d=directories, f = files
        for r, d, f in os.walk(self.directory_in_str):
            for file in f:
                if '.conf' in file:
                    self.files.append(os.path.join(r, file))
                elif 'config' in file:
                    self.files.append(os.path.join(r, file))

    #
    def printcontent(self, file):
        try:
            with open(file, "r") as reader:
                file_content = reader.readlines()
                print("")
                print(Style.DIM + 'File being listed: ')
                print(Fore.YELLOW + file)
                print(Style.RESET_ALL, end="")
                for x in file_content:
                    val = re.match(self.KeyWord, x)
                    if (val):
                        print(x, end="")
            pass

        except IOError as e:
            print(e)
            pass
        finally:
            pass
        pass


obj = SSH_Host_Lister()
# obj.printcontent(main_file)

# printcontent(main_config)
# for f in files:
#     printcontent(f)
