import sys

import numpy as np
import re

# data = np.array(["Mon Feb 24 06:30:26.812399 2020] [proxy_fcgi:error] [pid 5644:tid 139710093543168] [client 82.145.221.90:46734] AH01071: Got error 'PHP message: PHP Warning:  count(): Parameter must be an array or an object that implements Countable in /opt/bitnami/apps/wordpress/htdocs/wp-includes/post-template.php on line 284\n', referer: https://www.google.com/search?client=ms-opera-mini-android&channel=new&q=%D8%AD%D8%A7%D8%B3%D8%A8%D8%A9+%D8%A7%D9%84%D9%88%D9%84%D8%A7%D8%AF%D8%A9+%D8%A7%D9%84%D9%82%D9%8A%D8%B5%D8%B1%D9%8A%D8%A9&sa=X&ved=2ahUKEwjFp6qdxOnnAhXMzqQKHU7rCcQQ1QJ6BAgAEAU",
# "[Mon Feb 24 06:46:36.334194 2020] [proxy_fcgi:error] [pid 23648:tid 139710169077504] [client 156.215.200.117:50308] AH01071: Got error 'PHP message: \xd8\xae\xd8\xb7\xd8\xa3 Unknown column 'clinic_type' in 'where clause' \xd9\x81\xd9\x8a \xd9\x82\xd8\xa7\xd8\xb9\xd8\xaf\xd8\xa9 \xd8\xa8\xd9\x8a\xd8\xa7\xd9\x86\xd8\xa7\xd8\xaa \xd9\x88\xd9\x88\xd8\xb1\xd8\xaf\xd8\xa8\xd8\xb1\xd9\x8a\xd8\xb3  \xd9\x84\xd9\x84\xd8\xa7\xd8\xb3\xd8\xaa\xd8\xb9\xd9\x84\xd8\xa7\xd9\x85 SELECT * FROM wp_bu_projects Where clinic_type = 0 order by sort = 0, sort asc \xd8\xa7\xd9\x84\xd9\x82\xd8\xa7\xd8\xaf\xd9\x85 \xd9\x85\xd9\x86 require('wp-blog-header.php'), require_once('wp-includes/template-loader.php'), include('/themes/andalusia_clinics/page-clinics.php')\n'",
# "[Mon Feb 24 06:46:37.604287 2020] [pagespeed:error] [pid 23648:tid 139708776576768] [mod_pagespeed 1.13.35.2-0 @23648] PageSpeed Serf fetch failure rate extremely high; only 0 of 5 recent fetches fully successful; is fetching working?",
# "[Mon Feb 24 06:46:37.857459 2020] [proxy_fcgi:error] [pid 23648:tid 139710059972352] [client 156.215.200.117:50302] AH01071: Got error 'PHP message: PHP Warning:  count(): Parameter must be an array or an object that implements Countable in /opt/bitnami/apps/wordpress/htdocs/wp-includes/post-template.php on line 284\nPHP message: PHP Warning:  count(): Parameter must be an array or an object that implements Countable in /opt/bitnami/apps/wordpress/htdocs/wp-includes/post-template.php on line 284\n'",
# "[Mon Feb 24 06:46:37.947026 2020] [proxy_fcgi:error] [pid 23648:tid 139710110328576] [client 156.215.200.117:50292] AH01071: Got error 'PHP message: PHP Warning:  count(): Parameter must be an array or an object that implements Countable in /opt/bitnami/apps/wordpress/htdocs/wp-includes/post-template.php on line 284\nPHP message: PHP Warning:  count(): Parameter must be an array or an object that implements Countable in /opt/bitnami/apps/wordpress/htdocs/wp-includes/post-template.php on line 284\nPHP message: PHP Warning:  count(): Parameter must be an array or an object that implements Countable in /opt/bitnami/apps/wordpress/htdocs/wp-includes/post-template.php on line 284\nPHP message: PHP Warning:  count(): Parameter must be an array or an object that implements Countable in /opt/bitnami/apps/wordpress/htdocs/wp-includes/post-template.php on line 284\nPHP message: PHP Warning:  count(): Parameter must be an array or an object that implements Countable in /opt/bitnami/apps/wordpress/htdocs/wp-includes/post-template.php on line 284\nPHP message: PHP Warning:  count(): Parameter must be an array or an object that implements Countable in /opt/bitnami/apps/wordpress/htdocs/wp-includes/post-template.php on line 284\nPHP message: PHP Warning:  count(): Parameter must be an array or an object that implements Countable in /opt/bitnami/apps/wordpress/htdocs/wp-includes/post-template.php on line 284\nPHP message: PHP Warning:  count(): Parameter must be an array or an object that implements Countable in /opt/bitnami/apps/wordpress/htdocs/wp-includes/post-template.php on line 284\nPHP message: PHP Warning:  count(): Parameter must be an array or an object that implements Countable in /opt/bitnami/apps/wordpress/htdocs/wp-includes/post-template.php on line 284\nPHP message: PHP Warning:  count(): Parameter must be an array or an object that implements Countable in /opt/bitnami/apps/wordpress/htdocs/wp-includes/post-template.php on line 284\nPHP message: PHP Warning:  count(): Parameter must be an array or an object that implements Countable in /opt/bitnami/apps/wordpress/htdocs/wp-includes/post-template.php on line 284\nPHP message: PHP Warning:  count(): Parameter must be an array or an object that implements Countable in /opt/bitnami/apps/wordpress/htdocs/wp-includes/post-template.php on line 284\nPHP message: PHP Warning:  count(): Parameter must be an array or an object that implements Countable in /opt/bitnami/apps/wordpress/htdocs/wp-includes/post-template.php on line 284\nPHP message: PHP Warning:  count(): Parameter must be an array or an object that implements Countable in /opt/bitnami/apps/wordpress/htdocs/wp-includes/post-template.php on line 284\n'",
# "[Mon Feb 24 06:46:38.002764 2020] [proxy_fcgi:error] [pid 23648:tid 139710093543168] [client 156.215.200.117:50308] AH01071: Got error 'PHP message: PHP Warning:  count(): Parameter must be an array or an object that implements Countable in /opt/bitnami/apps/wordpress/htdocs/wp-includes/post-template.php on line 284\nPHP message: PHP Warning:  count(): Parameter must be an array or an object that implements Countable in /opt/bitnami/apps/wordpress/htdocs/wp-includes/post-template.php on line 284\n'",
# "[Mon Feb 24 06:46:38.002764 2020] [proxy_fcgi:error] [pid 23648:tid 139710093543168] [client 156.215.200.117:50308] AH01071: Got error 'PHP message: PHP Warning:  count(): Parameter must be an array or an object that implements Countable in /opt/bitnami/apps/wordpress/htdocs/wp-includes/post-template.php on line 284\nPHP message: PHP Warning:  count(): Parameter must be an array or an object that implements Countable in /opt/bitnami/apps/wordpress/htdocs/wp-includes/post-template.php on line 284\n'"
# ])

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
