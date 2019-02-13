#from TSreport_to_txt import convertMultiple
from TXTcleaner import Raw_Minus_Trash
from Reduce_raw import Remove_end
import  os

#convertMultiple(pdfDir, txtDir);
Remove_end();
Raw_Minus_Trash();

my_list = []
with open(#directory to Cleaned.txt, 'r') as time:
    with open(#directory to Final_timesheet.txt, 'w+') as final:
        for line in time:
            my_list.append(line.rstrip())
        i = 0
        file_list = []
        while i < (len(my_list)):
            if (my_list[i] == "\n" or my_list[i].rstrip() == ""):
                i += 1
                continue
            if my_list[i].endswith('%'):

                service_considered = my_list[i].split()
                service_percent = float((service_considered[len(service_considered)-1])[:-1])
                if service_percent < 88.0:
                    service_considered = " ".join(service_considered[:-1])
                    file_list.append(service_considered)

            else:
                if my_list[i+1].endswith('%') and len(my_list[i+1].split()) == 1:

                    service_considered = (my_list[i+1][:-1])
                    service_percent = float(service_considered)
                    if service_percent < 88.0:
                        file_list.append((my_list[i]))
                    i += 1
                else:

                    file_list.append("  - "  + my_list[i] + " shows low availability on:")


            i += 1
        i = 0
        while i < len(file_list)-1:

            if (file_list[i][2] == "-" and file_list[i+1][2] == "-"):
                i += 1
            else:
                if (file_list[i][2] == "-"):
                    final.write("\n")
                if (file_list[i] == "Patch Status"):
                    file_list[i] = "Patch Status - Status shows service disabled"
                if (file_list[i] == "MS17-010 (wannacry) Patch Installed"):
                    file_list[i] = "MS17-010 (wannacry) Patch Installed - service no longer in monitoring"
                final.write(file_list[i])
                final.write('\n')
                i += 1
time.close()
os.remove(#directory to Cleaned.txt)
os.remove(#directory to Raw.txt')
