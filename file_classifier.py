"""
This program classifies all mp4,txt,pdf files in the current directory
and writes them to a separate txt file.
"""

import os

pdf = list()
mp4 = list()
txt = list()

for path, folders, files in os.walk("/Users/yusufs/"):
    for i in files:
        if i.endswith(".pdf"):
            pdf.append(i)
        elif i.endswith(".mp4"):
            mp4.append(i)
        elif i.endswith(".txt"):
            txt.append(i)


def file(file_name, file_list):
    with open(file_name, "w", encoding="utf-8") as files:
        for file in file_list:
            files.write(file)
            files.write("\n")


file("pdf_files.txt", pdf)
file("mp4_files.txt", mp4)
file("txt_files.txt", txt)
