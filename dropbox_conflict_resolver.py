import os
import re

'''
    This is used to revert back a Dropbox conflict. So in this case I want to keep all the files that were
    converted to conflict copies. So I just strip out the conflict string ie (some computer names's conflict copy some date) .ext
    and remove that conflict part of the string, and override the original file by that name.
'''
for root, dirs, files, in os.walk(r"path to your drop box file with conflicts"):
    for file in files:
        file_matcher = re.search(r"(.+) (\(.+'s conflicted copy \d{4}-\d{2}-\d+\))(.+)?", file)
        if file_matcher:
            full_path = os.path.join(root, file)
            conflict_file_name = file_matcher.group(0)
            clean_file_name = file_matcher.group(1)
            conflict_string = file_matcher.group(2)
            file_ext = file_matcher.group(3)

            new_name_file_name = clean_file_name

            if file_ext:
                new_name_file_name += file_ext

            new_path = os.path.join(root, new_name_file_name)

            print("from: " + full_path + "  to: " + new_path)
            os.replace(full_path, new_path)

