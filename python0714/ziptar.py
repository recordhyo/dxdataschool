import zipfile
'''
filelist = ['./data/text.txt','./data/test.bin']

with zipfile.ZipFile('./data/test.zip', 'w') as myzip:
    for temp in filelist:
        myzip.write(temp)
'''

zipfile.ZipFile('./data/test.zip').extractall()