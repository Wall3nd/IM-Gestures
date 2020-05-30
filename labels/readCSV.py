import csv
import shutil
import os
import json


#função para copiar ficheiros
def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

#leitura do ficheiro csv train - Cópia para ir buscar os numeros dos videos com os gestos que pretendo

f = open('train - Cópia.csv')
csv_f = csv.reader(f)

g = open('validation.csv', 'w', newline='')
writer = csv.writer(g)



StopSignNumbers = []
ThumbsUpNumbers = []
ThumbsDownNumbers = []
for row in csv_f:
	if("Stop Sign" in str(row)):
		writer.writerow(row)
		newstr=(str(row).split(";"))
		StopSignNumbers.append(newstr[0][2:])
	if("Thumb Up"in str(row)):
		writer.writerow(row)
		newstr=(str(row).split(";"))
		ThumbsUpNumbers.append(newstr[0][2:])
	if("Thumb Down"in str(row)):
		writer.writerow(row)
		newstr=(str(row).split(";"))
		ThumbsDownNumbers.append(newstr[0][2:])

#sort dos arrays e escrita num txt na pasta json para possivel utilização no algoritmo

StopSignStr = StopSignNumbers
StopSignNumbers = [int(x) for x in StopSignNumbers]
StopSignNumbers.sort()
SSNjson = json.dumps(StopSignNumbers)

try:
	with open('C:\\Users\\Wall3nd\\Desktop\\Cadeiras\\OpenPose-Gesture-Recognition-master\\json\\StopSignNumbers.json', 'w+') as outfile:
		json.dump(SSNjson,outfile)
except:
	print()

ThumbsUpStr = ThumbsUpNumbers
ThumbsUpNumbers = [int(x) for x in ThumbsUpNumbers]

ThumbsUpNumbers.sort()
TUNjson = json.dumps(ThumbsUpNumbers)

try:
	with open('C:\\Users\\Wall3nd\\Desktop\\Cadeiras\\OpenPose-Gesture-Recognition-master\\json\\ThumbsUpNumbers.json', 'w+') as outfile:
		json.dump(TUNjson,outfile)
except:
	print()

ThumbsDownStr = ThumbsDownNumbers
ThumbsDownNumbers = [int(x) for x in ThumbsDownNumbers]
ThumbsDownNumbers.sort()
TDNjson = json.dumps(ThumbsDownNumbers)

try:
	with open('C:\\Users\\Wall3nd\\Desktop\\Cadeiras\\OpenPose-Gesture-Recognition-master\\json\\ThumbsDownNumbers.json', 'w+') as outfile:
		json.dump(TDNjson,outfile)
except:
	print()


# vou percorrer os meus videos, e todos os números que eu tiver no meu dataset que sejam thumbs up / thumbs down / stop sign, vão ser copiados para a pasta de videos


directory = r'C:\\Users\\Wall3nd\\Desktop\\20bn-jester-v1'

for filename in os.listdir(directory):
	if filename in ThumbsUpStr:
		direc1 = 'C:\\Users\\Wall3nd\\Desktop\\Cadeiras\\OpenPose-Gesture-Recognition-master\\videos\\' + filename
		direc2 = 'C:\\Users\\Wall3nd\\Desktop\\20bn-jester-v1\\' + filename
		try:
			os.mkdir(direc1)
			copytree(direc2, direc1)
		except OSError:
			pass
			#print("error or dir already exists")

		

	elif filename in ThumbsDownStr:
		direc1 = 'C:\\Users\\Wall3nd\\Desktop\\Cadeiras\\OpenPose-Gesture-Recognition-master\\videos\\' + filename
		direc2 = 'C:\\Users\\Wall3nd\\Desktop\\20bn-jester-v1\\' + filename
		try:
			os.mkdir(direc1)
			copytree(direc2, direc1)
		except OSError:
			pass
			#print("error or dir already exists")

		
	elif filename in StopSignStr:
		direc1 = 'C:\\Users\\Wall3nd\\Desktop\\Cadeiras\\OpenPose-Gesture-Recognition-master\\videos\\' + filename
		direc2 = 'C:\\Users\\Wall3nd\\Desktop\\20bn-jester-v1\\' + filename
		try:
			os.mkdir(direc1)
			copytree(direc2, direc1)
		except OSError:
			pass
			#print("error or dir already exists")


		


