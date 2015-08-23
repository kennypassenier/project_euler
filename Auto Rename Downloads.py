from os import listdir, rename
from os.path import isfile, join, isdir

workdir = 'I:/Downloads uTorrent/'


def namesplit(example):
    result = ''
    for i in example:
        if i.lower() in 'abcdefghijklmnopqrstuvwxyz0123456789':
            result += i
        else:
            result += " "


    showname = ''
    counter = 0
    cutoff = False
    while cutoff == False:
        if splitcheck(str.split(result)[counter]) == True:
            showname += '- '
            showname += str.split(result)[counter]
            showname += '.'
            showname += str.split(result)[-1]
            cutoff = True
            return showname
        else:
            showname += str.split(result)[counter]
            showname += ' '
            counter += 1


def splitcheck(whateverstring):
    if whateverstring[0].lower() == 's' and whateverstring[-3].lower() == 'e':
        if len(whateverstring) == 6:
            try:
                int(whateverstring[1])
                int(whateverstring[2])
                int(whateverstring[4])
                int(whateverstring[5])
                return True
            except:
                return False

def filerenamer(workdir):
    for i in listdir(workdir):
        if isdir(workdir + i):
            print(i + ' is a directory')
            for j in listdir(workdir+i):
                if isdir(workdir + i + '/' + j):
                    print(j + ' is a directory')
                    for k in listdir(workdir + i + '/' +j):
                        if isdir(workdir + i + '/' + j + '/' +k):
                            print(k + ' is a directory')
                        elif isfile(workdir + i + '/' + j + '/' + k):
                            try:
                                namesplit(k)
                                rename(workdir+i+'/'+j+'/'+k, workdir+i+'/'+j+'/'+ namesplit(k))
                                print(k + ' is a file and is renamed to: ' + namesplit(k))
                            except:
                                print('The rename function did not work with item: ' + k)

                elif isfile(workdir + i + '/' +j):
                    try:
                        namesplit(j)
                        rename(workdir+i+'/'+j, workdir+i+'/'+namesplit(j))
                        print(j + ' is a file and is renamed to: ' + namesplit(j))
                    except:
                        print('The rename function did not work with item: ' + j)
        elif isfile(workdir + i):
            try:
                namesplit(i)
                rename(workdir+i, workdir+namesplit(i))
                print(i + ' is a file and is renamed to: ' + namesplit(i))
            except:
                print('The rename function did not work with item: ' + i)


#-----------------------------


"""
downloadfiles = [f for f in listdir(workfolder) if isfile(join(workfolder, f))]
"""
filerenamer(workdir)
