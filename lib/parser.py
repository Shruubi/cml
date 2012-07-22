import shlex

class parser:
    def __init__(self, list):
        self.cmlList = list
        self.generated = ["//this is a file generated from the cml parser"]

    def getGenerated(self):
        return self.generated

    def parse(self):
        for line in self.cmlList:
            self.generated.append(self.convert(line))
        print(self.generated) #printline debugging ftw?

    def convert(self, line):
        if(line == "<br />"):
            return "\n"
        else: #this is where the magic happens...
            #now we need to get the tag name and atrributes etc
            workingVals = []
            workingVals.append(line[line.find("<")+1:line.find(">")])
            workingVals.append(line[line.find(">")+1:line.find("</")])

            #headers
            if(workingVals[0].find("include") > -1):
                return "#" + workingVals[0] + " <" + workingVals[1] + ">"

            elif(workingVals[0].find("prototype") > -1):
                attributes = shlex.split(workingVals[0])
                funcType = attributes[1][attributes[1].find("=")+1:]
                funcName = attributes[2][attributes[1].find("=")+1:]
                funcParams = attributes[3][attributes[1].find("=")+1:]
                return funcType + " " + funcName + "(" + funcParams + ");"

            elif(workingVals[0] == "return"):
                return "return " + workingVals[1] + ";"

            #opening main tag
            elif(workingVals[0] == "main"):
                return "int main(int argc, char* argv[]) {"
            #closing main tag
            elif(workingVals[0] == "/main"):
                return "return(0);\n}"

            elif(workingVals[0].find("call") > -1):
                return workingVals[1] + ";"

            #setting variables
            elif(workingVals[0].find("set") > -1):
                attributes = shlex.split(workingVals[0])
                varName = attributes[1][attributes[1].find("=")+1:]
                return varName + " = " + workingVals[1] + ";"

            #vars = working :D
            elif(workingVals[0].find("var") > -1):
                attributes = shlex.split(workingVals[0])
                varType = attributes[1][attributes[1].find("=")+1:]
                varName = attributes[2][attributes[1].find("=")+1:]
                return varType + " " + varName + " = " + workingVals[1] + ";"

            #all tags with child tags go below this elif
            elif(workingVals[0] == "/function" or workingVals[0] == "/if" or workingVals[0] == "/while" or workingVals[0] == "/for"):
                return "}"

            elif(workingVals[0] == "/struct" or workingVals[0] == "/union" or workingVals[0] == "/enum"):
                return "};"

            elif(workingVals[0].find("struct") > -1 or workingVals[0].find("union") > -1 or workingVals[0].find("enum") > -1):
                attributes = shlex.split(workingVals[0])
                structName = attributes[1]
                return attributes[0] + " " + attributes[1] + " {"

            elif(workingVals[0] == "enum-val"):
                return workingVals[1] + ","

            elif(workingVals[0] == "enum-val-last"):
                return workingVals[1]

            elif(workingVals[0].find("function") > -1):
                attributes = shlex.split(workingVals[0])
                funcType = attributes[1][attributes[1].find("=")+1:]
                funcName = attributes[2][attributes[1].find("=")+1:]
                funcParams = attributes[3][attributes[1].find("=")+1:]
                return funcType + " " + funcName + "(" + funcParams + ") {"

            elif(workingVals[0].find("if") > -1 or workingVals[0].find("while") > -1 or workingVals[0].find("for") > -1):
                attributes = shlex.split(workingVals[0])
                cond = attributes[1][attributes[1].find("=")+1:]
                return attributes[0] + "(" + cond + ") {"
