import os

def Remove_end():
    with open(#Directory to Place_report_here.txt, 'r') as report:
            with open(#Directory to Raw.txt, 'w+') as raw:
                    for line in report:
                        if "Events Detected" in line:
                            break;
                        else:
                            raw.write(line)
Remove_end();
