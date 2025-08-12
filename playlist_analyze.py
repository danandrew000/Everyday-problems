import os
import xlsxwriter

'''
#same as what is higher, but only as function

def sorted_dict_of_music(path):
    results = [each for each in os.listdir(path) if each.endswith('.mp3')]
    result = []
    for i in results:
        result.append(i.split("-")[0])
    
    dsong = {}
    sorted_dsong = {}
    
    for i in range(len(result)):
        dsong[result[i]] = result.count(result[i])
    
    for key in sorted(dsong, key=dsong.get, reverse = True):
        sorted_dsong[key] = dsong[key]
    
 
    return sorted_dsong
    

'''

path = "C:/Andrew/MUSIC"
list = []
new_list = []
new_new_list = []
dsong = {}
sorted_dsong = {}

for (root, dirs, file) in os.walk(path):
    for f in file:
        if '.mp3' in f:
            list.append(f)
            print(f)

for i in list:
    new_list.append((i.split("-")[0]).lower())

for i in new_list:
    if i.endswith('_'):
        new_new_list.append(i[0:-1].title())

for i in range(len(new_new_list)):
    dsong[new_new_list[i]] = new_new_list.count(new_new_list[i])
 
for key in sorted(dsong, key=dsong.get, reverse = True):
        sorted_dsong[key] = dsong[key]
        
        
dkeys = []
dvalues = []
for key,value in sorted_dsong.items():
    if value >= 5:
        dkeys.append(key)
        dvalues.append(value)
        
 
workbook = xlsxwriter.Workbook('C:/Andrew/music_artists.xlsx')
 
worksheet = workbook.add_worksheet("My sheet")

worksheet.write(0, 0, "Artist")
worksheet.write(0, 1, "Amount")
 
for i in range(len(dvalues)):
    worksheet.write(i+1, 0, dkeys[i])
    worksheet.write(i+1,1, dvalues[i])
'''
for name, score in (scores):
    worksheet.write(row, col, name)
    worksheet.write(row, col + 1, score)
    row += 1
'''
workbook.close()

