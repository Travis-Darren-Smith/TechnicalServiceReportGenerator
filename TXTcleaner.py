import os

def Raw_Minus_Trash():
    is_not_trash = True
    i = ''
    line_number = 0
    # opening text file
    with open(#directory to Raw.txt, 'r') as raw:
        with open(#directory to Cleaned.txt , 'w+') as time:
            with open(#directory to trash.txt', 'r') as trash:
                for line in raw: #filter through raw data in textFile
                    line_number += 1
                    line = line.replace('Service Name % Available','')
                    for i in trash: #filter through unwanted data in trash file
                        x = i.rstrip()
                        if x in line.rstrip():
                            is_not_trash = False
                    if(is_not_trash):
                        time.write(line.rstrip())
                        time.write("\n")

                    is_not_trash = True
                    trash.seek(0)
    return 0
