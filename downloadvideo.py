import os

import pandas as pd
import requests

filenamelist=os.listdir(r'H:\Peachpie')
filenamelist=[file[:20] for file in filenamelist]

data=pd.read_csv(r'C:\Users\GMH\Desktop\peachpie.csv',header=None,index_col=None)
data=data.values.tolist()
filesitelist=[da[1] for da in data]

notdownload_filelist=[]
download_filelist=[]
for filename in filenamelist:
    ifin=False
    current_filesite=''
    for filesite in filesitelist:
        if filename in filesite:
            current_filesite=filesite
            ifin=True
    if ifin:
        download_filelist.append(current_filesite)

for filesite in filesitelist:
    if filesite not in download_filelist:
        notdownload_filelist.append(filesite)
for filesite in notdownload_filelist:
    print(filesite)

# for filesite in notdownload_filelist:
#     filename=filesite[32:52]
#     print(filesite)
#     response = requests.get(filesite)
#
#     with open(rf'H:\Peachpie\test\{filename}.m4v', 'wb') as f:
#         f.write(response.content)