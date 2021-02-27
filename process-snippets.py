inputfile = open("snippets.riley-snippets", "r")
outputdirectory = "C:/Users/rorih/AppData/Roaming/Sublime Text 3/Packages/User/"
currentsnippet = []
snippetname = ""
def writesnippet():
    if len(currentsnippet) > 0:
        f = open(outputdirectory + snippetname + ".sublime-snippet", "w")
        f.write("<snippet> \n")
        f.write("<content><![CDATA[\n")
        for line in currentsnippet:
            for i in range(len(line)):
                if line[i] == "$" and not line[i+1].isnumeric():
                    f.write("\\")
                f.write(line[i])
        f.write("]]></content>\n")
        f.write("<tabTrigger>" + snippetname + "</tabTrigger>\n</snippet>")
        f.close()
for line in inputfile:
    if line.startswith("--"):
        writesnippet()
        currentsnippet = []
        snippetname = line.split("--")[1]
        print(snippetname)
    else:
        currentsnippet.append(line)

writesnippet()
