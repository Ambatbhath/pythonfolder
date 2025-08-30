from pathlib import Path



with open("preproinsulin-seq.txt", "r") as file:
    lines = file.readlines()
    print(lines)
    lines = [line.replace(" ", "").replace("\n","").replace("61","").replace("1","").strip("//").strip("ORIGIN") for line in lines]
    
print(lines)

with open("preproinsulin-seq-clean.txt", "w") as file:
    file.writelines(lines)
    
with open("preproinsulin-seq-clean.txt", "r") as file:
    newline = file.readlines()
    mystring = ("".join(lines).strip())
    print(mystring)
    count = len(mystring)
    print(count)
    
string1to24=mystring[0:24]
print(string1to24)
print(len(string1to24))

file_path = Path("lsinsulin-seq-clean.txt")
file_path.write_text(string1to24)

string25to54=mystring[24:54]
print(string25to54)
print(len(string25to54))

file_path2 = Path("binsulin-seq-clean.txt")
file_path2.write_text(string25to54)

string55to89=mystring[54:89]
print(string55to89)
print(len(string55to89))

file_path3 = Path("cinsulin-seq-clean.txt")
file_path3.write_text(string55to89)

string90to110=mystring[89:110]
print(string90to110)
print(len(string90to110))

file_path4 = Path("ainsulin-seq-clean.txt")
file_path4.write_text(string90to110)