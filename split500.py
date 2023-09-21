import os, sys

directory = "./{}/MIJIA_RECORD_VIDEO".format(sys.argv[1])

maxFiles = 0
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isdir(f):
        if maxFiles == 0:
            print(os.path.basename(f), end = " -----> ")

        current = len([name for name in os.listdir(f) if os.path.isfile(os.path.join(f, name))])
        maxFiles += current

        if maxFiles > 500:
            if pre:
                print(os.path.basename(pre) + ' ' + str(maxFiles - current) + os.linesep)
            else:
                print(os.path.basename(f) + ' ' + str(maxFiles - current) + os.linesep)
            maxFiles = current
            print(os.path.basename(f), end = " -----> ")
        pre = f

if maxFiles <= 500:
    print(os.path.basename(pre) + ' ' + str(maxFiles) + os.linesep)
