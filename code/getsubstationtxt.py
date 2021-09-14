import os
import shutil


dir1=r'F:\foranno\labels'
dir2=r'F:\foranno\classfied'


for txt_name in os.listdir(dir1):
    if txt_name.split('_',3)[1]=='substation':
        # if txt_name.split('_',3)[2]=='29':
        dst = os.path.join(dir2,txt_name.split('_',3)[2])
        if not os.path.exists(dst):
            os.mkdir(dst)
        path1=os.path.join(dir1,txt_name)
        path2=os.path.join(dst,txt_name)
        shutil.copy(path1, path2)