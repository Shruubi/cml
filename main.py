import sys
import os
from lib.filehandler import FileHandler
from lib.parser import parser

#ensure that we have more than one command line argument
if(len(sys.argv) == 1):
	print("error, no file specified")
	sys.exit()

#continue on here
file = FileHandler(sys.argv[1], "r")
contents = file.fetchList()

#init our parser
parser = parser(contents)
parser.parse()

outputFilename = sys.argv[1][:sys.argv[1].find(".")+1]
outputFile = outputFilename + "c"
output = FileHandler(outputFile, "w+")
for line in parser.getGenerated():
    output.getFile().write("%s\n" % line)
output.cleanup()

os.system("gcc " + outputFile + " -o " + outputFilename + "o")
print("successfully converted and compiled")
