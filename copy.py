import sys
import os
import shutil
import time

if not sys.argv[1]:
    print("Please enter proper source file")
else:
    start=time.time()
    filename=sys.argv[1]
    targetPath=sys.argv[2]
    targetPath=os.path.join(targetPath,filename)
    shutil.copyfile(filename,targetPath)
    done=time.time()
    finalTime=done-start
    print("File copied at {}".format(targetPath))
    print("File copied in {}".format(finalTime))

