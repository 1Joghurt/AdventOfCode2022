from folderinfo import FolderInfo

with open("07/inputs.txt", "r") as f:
    input = f.read().split("\n")


def part1():
    resolvedFolder = GetFoldersWithSize()

    sum = 0
    for x in resolvedFolder:
        if (x != "/" and resolvedFolder[x] <= 100000):
            sum += resolvedFolder[x]
    print(sum)

def part2():
    resolvedFolder = GetFoldersWithSize()

    diskSize = 70000000
    necessaryDiskSize = 30000000

    unusedSpace = diskSize - resolvedFolder["/"]
    spaceToClean = necessaryDiskSize - unusedSpace

    fileSize = diskSize
    for size in resolvedFolder.values():
        if (size >= spaceToClean and fileSize > size):
            fileSize = size 

    print(fileSize)


def GetFoldersWithSize():
    folders = {} # path and size
    path = ""
    for x in input:
        if (x.startswith("$ cd")):
            new_subpath = x[5:]

            if (new_subpath == ".."):
                path = path[0 : path.rindex("/")]
            elif (new_subpath == "/" or path == ""):
                print(path)
                print(new_subpath)
                path = new_subpath
            else: 
                path += "/"  + new_subpath

            if path not in folders:
                folders[path] = FolderInfo()
        elif (x.startswith("dir")):
            folders[path].SubFolders.append(path + "/"  + x.split(" ")[1])
        elif (x[0:1].isnumeric()):
            folders[path].Size += int(x.split(" ")[0])

    resolvedFolder = {}
    for x in folders:
        resolvedFolder[x] = GetFolderSize(x, folders, resolvedFolder)

    return resolvedFolder


def GetFolderSize(folder, folders, absolutSized):
    if (folder in absolutSized):
        return absolutSized[folder]
    else:
        size = folders[folder].Size
        for subfolder in folders[folder].SubFolders:
            absolutSized = GetFolderSize(subfolder, folders, absolutSized)
            size += absolutSized[subfolder]    
        absolutSized[folder] = size
    return absolutSized

part1()
part2()
