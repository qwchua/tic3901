#scanner.py

import subprocess
import os
from os import walk

class Scanner:
    def __init__(self,type):
        self.type = type
        pass

    def findFiles(self,path):
        files = []

        if path == "ALL":
            files = self.__findAllFilesTracked()
        
        #if path is a file
        elif os.path.isfile(path):
            trackedfiles = self.__findAllFilesTracked()

            if path in trackedfiles:
                files.append(path)

        #if path is a directory
        elif os.path.isdir(path):
            trackedfiles = self.__findAllFilesTracked()
            filesfound = self.__findallFilesInDirectoy(path)
            
            for f in filesfound:
                f = f.replace("\\", "/")
                if f in trackedfiles:
                      files.append(f)

        return files


    def __findAllFilesTracked(self):
        if self.type == "git":
            command = 'git ls-tree --full-tree --name-only -r HEAD'

            unparsedlog = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                )

            unparsedlog = unparsedlog.stdout
            lines = unparsedlog.split("\n")
            
            textchars = bytearray({7,8,9,10,12,13,27} | set(range(0x20, 0x100)) - {0x7f})
            is_binary_string = lambda bytes: bool(bytes.translate(None, textchars))

            output = []

            for line in lines:
                if len(line) == 0:
                    continue
                if line.startswith("."):
                    continue
                #remove binary files
                if is_binary_string(open(line, 'rb').read(1024)):
                    continue
                else:
                    output.append(line)

            return output

    def __findallFilesInDirectoy(self,directory):

        all_files = [os.path.join(path, name) for path, subdirs, files in os.walk(directory) for name in files]

        return all_files
    

                    





