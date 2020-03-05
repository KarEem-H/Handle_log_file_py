import sys

import numpy as np
import re

# data = np.array(["#" ])

# t=np.where(data == data[1], np.delete(re.split("]", 1),[0,1,2,3]), data)
# print(t)

fileData = open('error_log.log', 'r')
outF = open("outLogs.log", "w")

n=0
for i in fileData:
    line=np.delete(re.split("]", i),[0,1,2,3])
    outF.write(line[0]+"\n")
    n = n + 1
    sys.stdout.write(" progressed line: %d%%   \r" % (n))
    sys.stdout.flush()


outF.close()
fileData.close()

outF2 = open("outLogs.log", "r")

# arrayOfUniquesErrorMessagesWithoutTime = np.unique(arrayErrorMessagesWithoutTime)

# counter=0

# for uniqueLine in arrayErrorMessagesWithoutTime:
#         outF.write(uniqueLine)
#
#         counter = counter +1
#         sys.stdout.write(" saved progressed line: %d%%   \r" % (counter))
#         sys.stdout.flush()

print('\n**********')

# outF.close()
# fileData.close()

# f = open('error_log.log', 'r')

# for line in (f,10):
#     print line.split('PHP message:')[0]

#     break

# data = []
# with open("error_log.log","r") as f:
#     data = f.readlines() # readlines() returns a list of items, each item is a line in your file

# print(data[3]) # print line 5

# for i in range(5):
#     x[i]=data[i]split("message: ")
#     print(x[i])

# import re
# import time
# from time import strftime
 
# log_file_path = r"D:\Python\error_log.log"
# export_file_path = r"D:\Python\filtered"
 
# time_now = str(strftime("%Y-%m-%d %H-%M-%S", time.localtime()))
 
# file = "\\" + "Parser Output " + time_now + ".log"
# export_file = export_file_path + file
 
# regex = '(<property name="(.*?)">(.*?)<\/property>)'
# read_line = False
 
# with open(log_file_path, "r") as file:
#     match_list = []
#     if read_line == True:
#         for line in file:
#             for match in re.finditer(regex, line, re.S):
#                 match_text = match.group()
#                 match_list.append(match_text)
#                 print (match_text)
#     else:
#         data = file.read()
#         for match in re.finditer(regex, data, re.S):
#             match_text = match.group();
#             match_list.append(match_text)
# file.close()
 
# with open(export_file, "w+") as file:
#     file.write("EXPORTED DATA:\n")
#     match_list_clean = list(set(match_list))
#     for item in xrange(0, len(match_list_clean)):
#         print (match_list_clean[item])
#         file.write(match_list_clean[item] + "\n")
# file.close()
