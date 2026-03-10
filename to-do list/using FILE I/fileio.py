
txt = "i like pizza"

file_path =  'output.txt'

with open(file_path , "w") as  file:
    file.write(txt)
    print(f"txt file {file_path} was written")

# w for writing the  whole  file , overwriting 
# a for appending 
#  r for reading 

with open(file_path, "r") as file:
        content = file.read()
        print(content)