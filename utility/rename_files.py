import os
import glob
from data import path as data_path

def serial_file_rename(categories):
    for category in categories:
        filenames = glob.glob(data_path.get() + '/images/'+ category + '/*.jpeg')
        filenames += glob.glob(data_path.get() + '/images/' + category + '/*.png')
        filenames += glob.glob(data_path.get() + '/images/' + category + '/*.jpg')

        print(category,"has",len(filenames),"filenames")
        count = 0
        for filename in filenames:
            os.rename(filename,category+'_'+str(count)+'.'+filename.split(".")[-1])
            count +=1

if __name__ == '__main__':
    categories = ['nestle']
    serial_file_rename(categories)
