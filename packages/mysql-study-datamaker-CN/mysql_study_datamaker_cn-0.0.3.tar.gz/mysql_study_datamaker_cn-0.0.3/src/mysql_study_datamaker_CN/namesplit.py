# with open("source/names.txt", encoding="utf-8") as f:
#     names = f.read().split()
#
# with open("source/new_names.txt", "w", encoding="utf-8") as f:
#     f.write("\n".join(names))

# with open("source/family.txt", encoding="utf-8") as f:
#     names = f.read().split()
#     line = [item[-1] if len(item) < 5 else item[-2:] for item in names]
#     # print(line, len(line))
#
# with open("source/new_family.txt", "w", encoding="utf-8") as f:
#     f.write("\n".join(line))

import tarfile
import os


with tarfile.open('mysql_study_datamaker_cn-0.0.2.tar.gz', 'w:gz') as tar:
    for file in os.listdir():
        if not file.endswith(".tar.gz"):
            tar.add(file, arcname=file)
