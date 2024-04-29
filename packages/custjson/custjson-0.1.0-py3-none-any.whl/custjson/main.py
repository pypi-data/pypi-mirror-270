import os

class Init:
    def __init__(self):
        self.file = ""
    def create_file(self,filename):
        with open(str(filename)+".jn", "w") as F:
            F.write("")
            F.close()
        self.file = str(filename)+".jn"
    def open_file(self,pathtofile):
        if os.path.isfile(pathtofile):
            self.file = pathtofile
    def write_line(self,valueName: str,value):
        if self.file != "":
            with open(self.file, "a") as F:
                if type(value) is int:
                    F.write("{\"" + valueName + "\":" + str(value) + "}\n")
                elif type(value) is str:
                    F.write("{\"" + valueName + "\":\"" + str(value) + "\"}\n")
                else:
                    raise TypeError("Cannot write values that are not string or integer properly using the CustJSON package. Please use a string or int value.")
                F.close()
        else:
            raise FileNotFoundError("No file has been opened for CustJSON to write to.")
    def read_line(self,lineNumber):
        if self.file != "":
            with open(self.file, "r") as F:
                i = 1
                for line in F:
                    if i == lineNumber:
                        return line
                    else:
                        continue
        else:
            raise FileNotFoundError("No file has been opened for CustJSON to read from.")
    def read_value_from_name(self,name):
        if self.file != "":
            with open(self.file,"r") as F:
                for line in F:
                    splitLine = line.split(":")
                    if splitLine[0] == "{"+name+"}":
                        spLine = splitLine[1].split('{','}')
                        return spLine[1]
                    else:
                        continue
                F.close()
        else:
            raise FileNotFoundError("No file has been opened for CustJSON to read from.")
    def delete_file(self):
        if self.file != "":
            os.remove(self.file)
            self.file = ""
        else:
            raise FileNotFoundError("No file has been opened for CustJSON to delete.")
    def close_file(self):
        self.file = ""



    