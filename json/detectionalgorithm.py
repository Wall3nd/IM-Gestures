import json
import os
import numpy as np
import time
import cv2
from scipy.spatial import distance
from matplotlib import pyplot as plt



# def imagesToVideo(filename):
# 	newname = filename.split(".")
# 	image_folder = 'C:\\Users\\Wall3nd\\Desktop\\Cadeiras\\OpenPose-Gesture-Recognition-master\\videos\\' + str(newname[0])
# 	video_name = 'video.avi'

# 	images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
# 	frame = cv2.imread(os.path.join(image_folder, images[0]))
# 	height, width, layers = frame.shape

# 	video = cv2.VideoWriter(video_name, 0, 1, (width,height))

# 	for image in images:
# 	    video.write(cv2.imread(os.path.join(image_folder, image)))

# 	cv2.destroyAllWindows()
# 	video.release()

def find_key_value_pairs(q, keys, dicts=None):
	if not dicts:
		dicts = [q]
		q = [q]  

	data = q.pop(0)
	if isinstance(data, dict):
		data = data.values()

	for d in data:
		dtype = type(d)
		if dtype is dict or dtype is list:
			q.append(d)
			if dtype is dict:
				dicts.append(d)

	if q:
		return find_key_value_pairs(q, keys, dicts)

	return [(k, v) for d in dicts for k, v in d.items() if k in keys]


#função delineada para verificar certas geometrias na mão que nos vai dizer se é o sinal de stop ou não



def IsItStopSign(coords):
	prob = 0
	questionsNr = 25
	p0 = (coords[0],coords[1])
	p1 = (coords[3],coords[4])
	p2 = (coords[6],coords[7])
	p3 = (coords[9],coords[10])
	p4 = (coords[12],coords[13])
	p5 = (coords[15],coords[16])
	p6 = (coords[18],coords[19])
	p7 = (coords[21],coords[22])
	p8 = (coords[24],coords[25])
	p9 = (coords[27],coords[28])
	p10 = (coords[30],coords[31])
	p11 = (coords[33],coords[34])
	p12 = (coords[36],coords[37])
	p13 = (coords[39],coords[40])
	p14 = (coords[42],coords[43])
	p15 = (coords[45],coords[46])
	p16 = (coords[48],coords[49])
	p17 = (coords[51],coords[52])
	p18 = (coords[54],coords[55])
	p19 = (coords[57],coords[58])
	p20 = (coords[60],coords[61])
	#mindinho:
	if (distance.euclidean(p20,p0) > distance.euclidean(p19,p0)):
		prob = prob+1
	if (distance.euclidean(p20,p0) > distance.euclidean(p18,p0)):
		prob = prob+1
	if (distance.euclidean(p20,p0) > distance.euclidean(p17,p0)):
		prob = prob+1
	if (distance.euclidean(p19,p0) > distance.euclidean(p18,p0)):
		prob = prob+1
	if (distance.euclidean(p19,p0) > distance.euclidean(p17,p0)):
		prob = prob+1
	if (distance.euclidean(p18,p0) > distance.euclidean(p17,p0)):
		prob = prob+1

	#anelar
	if (distance.euclidean(p16,p0) > distance.euclidean(p15,p0)):
		prob = prob+1
	if (distance.euclidean(p16,p0) > distance.euclidean(p14,p0)):
		prob = prob+1
	if (distance.euclidean(p16,p0) > distance.euclidean(p13,p0)):
		prob = prob+1
	if (distance.euclidean(p15,p0) > distance.euclidean(p14,p0)):
		prob = prob+1
	if (distance.euclidean(p15,p0) > distance.euclidean(p13,p0)):
		prob = prob+1
	if (distance.euclidean(p14,p0) > distance.euclidean(p13,p0)):
		prob = prob+1

	#médio
	if (distance.euclidean(p12,p0) > distance.euclidean(p11,p0)):
		prob = prob+1
	if (distance.euclidean(p12,p0) > distance.euclidean(p10,p0)):
		prob = prob+1
	if (distance.euclidean(p12,p0) > distance.euclidean(p9,p0)):
		prob = prob+1
	if (distance.euclidean(p11,p0) > distance.euclidean(p10,p0)):
		prob = prob+1
	if (distance.euclidean(p11,p0) > distance.euclidean(p9,p0)):
		prob = prob+1
	if (distance.euclidean(p10,p0) > distance.euclidean(p9,p0)):
		prob = prob+1

	#mindinho:
	if (distance.euclidean(p20,p0) > distance.euclidean(p19,p0)):
		prob = prob+1
	if (distance.euclidean(p20,p0) > distance.euclidean(p18,p0)):
		prob = prob+1
	if (distance.euclidean(p20,p0) > distance.euclidean(p17,p0)):
		prob = prob+1
	if (distance.euclidean(p19,p0) > distance.euclidean(p18,p0)):
		prob = prob+1
	if (distance.euclidean(p19,p0) > distance.euclidean(p17,p0)):
		prob = prob+1
	if (distance.euclidean(p18,p0) > distance.euclidean(p17,p0)):
		prob = prob+1

	# verificar que o ponto mais alto de todos os dedos estão acima da palma da mão (ponto 0)
	if (p20[1] < p0[1] and p16[1] < p0[1] and p12[1] < p0[1] and p8[1] < p0[1]):
		prob = prob+1
	else:
		prob=0

	if(prob/questionsNr > 0.90):
		return("Stop Sign")
	else:
		return("Not Stop Sign")


def IsItThumbsDownOrUp(coords):
	prob = 0
	questionsNr = 22
	p0 = (coords[0],coords[1])
	p1 = (coords[3],coords[4])
	p2 = (coords[6],coords[7])
	p3 = (coords[9],coords[10])
	p4 = (coords[12],coords[13])
	p5 = (coords[15],coords[16])
	p6 = (coords[18],coords[19])
	p7 = (coords[21],coords[22])
	p8 = (coords[24],coords[25])
	p9 = (coords[27],coords[28])
	p10 = (coords[30],coords[31])
	p11 = (coords[33],coords[34])
	p12 = (coords[36],coords[37])
	p13 = (coords[39],coords[40])
	p14 = (coords[42],coords[43])
	p15 = (coords[45],coords[46])
	p16 = (coords[48],coords[49])
	p17 = (coords[51],coords[52])
	p18 = (coords[54],coords[55])
	p19 = (coords[57],coords[58])
	p20 = (coords[60],coords[61])


	#comparar distâncias da parte exterior do punho ao topo do polegar
	if (distance.euclidean(p19,p4) > distance.euclidean(p15,p4)):
		prob = prob+1
	if (distance.euclidean(p19,p4) > distance.euclidean(p11,p4)):
		prob = prob+1
	if (distance.euclidean(p19,p4) > distance.euclidean(p7,p4)):
		prob = prob+1			
	if (distance.euclidean(p15,p4) > distance.euclidean(p11,p4)):
		prob = prob+1			
	if (distance.euclidean(p15,p4) > distance.euclidean(p7,p4)):
		prob = prob+1			
	if (distance.euclidean(p11,p4) > distance.euclidean(p7,p4)):
		prob = prob+1

	#comparar distancias da zona intermédia do punho ao topo do polegar
	if (distance.euclidean(p18,p4) > distance.euclidean(p14,p4)):
		prob = prob+1
	if (distance.euclidean(p18,p4) > distance.euclidean(p10,p4)):
		prob = prob+1
	if (distance.euclidean(p18,p4) > distance.euclidean(p6,p4)):
		prob = prob+1			
	if (distance.euclidean(p14,p4) > distance.euclidean(p10,p4)):
		prob = prob+1			
	if (distance.euclidean(p14,p4) > distance.euclidean(p6,p4)):
		prob = prob+1			
	if (distance.euclidean(p10,p4) > distance.euclidean(p6,p4)):
		prob = prob+1

	#comparar distancias da zona de dentro do punho ao topo do polegar
	if (distance.euclidean(p17,p4) > distance.euclidean(p13,p4)):
		prob = prob+1
	if (distance.euclidean(p17,p4) > distance.euclidean(p9,p4)):
		prob = prob+1
	if (distance.euclidean(p17,p4) > distance.euclidean(p5,p4)):
		prob = prob+1			
	if (distance.euclidean(p13,p4) > distance.euclidean(p19,p4)):
		prob = prob+1			
	if (distance.euclidean(p13,p4) > distance.euclidean(p5,p4)):
		prob = prob+1			
	if (distance.euclidean(p9,p4) > distance.euclidean(p5,p4)):
		prob = prob+1

	#o X da ponta dos dedos tem de ser menor que o x da articulação mais próxima
	if p4[1] < p17[1]:
		if p20[0] < p19[0]:
			prob = prob+1
		else:
			prob = prob-1
		if p16[0] < p15[0]:
			prob = prob+1
		else:
			prob = prob-1
		if p12[0] < p11[0]:
			prob = prob+1
		else:
			prob = prob-1
		if p8[0] < p7[0]:
			prob = prob+1
		else:
			prob = prob-1
	else:
		if p20[0] > p19[0]:
			prob = prob+1
		else:
			prob = prob-1
		if p16[0] > p15[0]:
			prob = prob+1
		else:
			prob = prob-1
		if p12[0] > p11[0]:
			prob = prob+1
		else:
			prob = prob-1
		if p8[0] > p7[0]:
			prob = prob+1
		else:
			prob = prob-1

	if p4[1] < p17[1]:
		if(prob/questionsNr > 0.8):
			return "Thumbs Up"
		else:
			return "Not Thumbs Up"
	else:
		if(prob/questionsNr > 0.8):
			return "Thumbs Down"
		else:
			return "Not Thumbs Down"


# Opening JSON files and loading 
# with open('755.json') as f:
# 	data1 = json.load(f)
# with open('1023.json') as e:
# 	data2 = json.load(e)
# with open('1406.json') as g:
# 	data3 = json.load(g)

keys = ['hand_right_keypoints_2d', 'hand_left_keypoints_2d', "label"]
# results = find_key_value_pairs(data2,keys)
  

#print(json.dumps(results, indent = 4, sort_keys=True))
#print(data1)
count=0


#print(results[12][1])


# Iterar os ficheiros json no diretório
directory = 'C:\\Users\\Wall3nd\\Desktop\\Cadeiras\\OpenPose-Gesture-Recognition-master\\json'

IdentifiedStop = 0
IdentifiedIrreconhecivel = 0
IdentifiedThumbsUp = 0
IdentifiedThumbsDown = 0
allfilescount = 0
ActualStop = 0
ActualThumbsUp = 0
ActualThumbsDown = 0
CorrectlyIdentifiedStop = 0
CorrectlyIdentifiedThumbsUp = 0
CorrectlyIdentifiedThumbsDown = 0

for filename in os.listdir(directory):
	#print(filename)
	if filename != "detectionalgorithm.py" and filename != "StopSignNumbers.json" and filename != "ThumbsDownNumbers.json" and filename != "ThumbsUpNumbers.json" and filename != "00012.jpg":
		with open(filename, encoding="utf8") as json_file:
			data = json.load(json_file)			
			results = find_key_value_pairs(data,keys)
			allfilescount = allfilescount+1
			#imagesToVideo(filename)

			#Consulta da label real do gesto que está a ser avaliado
			GestoAtual = str(results[0][1])
			GestoAtual = GestoAtual.replace(',','')
			if(GestoAtual == "Thumb Up"):
				GestoAtual = "Thumbs Up"
			if(GestoAtual == "Thumb Down"):
				GestoAtual = "Thumbs Down"

			print("--------------------------------------------------------------------------")
			print("File name: " + str(filename))
			print("Gesture to be identified: " + GestoAtual)
			
			# img = cv2.imread('00012.jpg',0)
			# cv2.imshow('image',img)
			# cv2.waitKey(200)
			# cv2.destroyAllWindows()

			folderName = filename.split(".")[0]

			StopSignCount = 0
			ThumbsUpCount = 0
			ThumbsDownCount = 0			
			countFramesZeros = 0

			jpgDir = 'C:\\Users\\Wall3nd\\Desktop\\Cadeiras\\OpenPose-Gesture-Recognition-master\\videos\\' + str(folderName)
			jpgCount=1
			imagecount = len([name for name in os.listdir(jpgDir) if os.path.isfile(os.path.join(jpgDir, name))])


			for x in results[1:]:
				#print(x[1])
				countZeros = 0
				for ind in x[1]:
					if ind == 0:
						countZeros = countZeros+1
						#print(countZeros)

				
				#print(len(results))
				if(countZeros < 60):
					if(jpgCount < 10 and jpgCount<imagecount):
						jpgNewDir = str(jpgDir) +  "\\0000" + str(jpgCount) + ".jpg"
					else:
						jpgNewDir = str(jpgDir) +  "\\000" + str(jpgCount) + ".jpg"

					img = cv2.imread(os.path.join(jpgDir, jpgNewDir))
					try:
						scale_percent = 220 # percent of original size
						width = int(img.shape[1] * scale_percent / 100)
						height = int(img.shape[0] * scale_percent / 100)
						dim = (width, height)
						img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
						cv2.imshow('image',img)
						cv2.waitKey(100)
						cv2.destroyAllWindows()	
						jpgCount = jpgCount+1
					except:
						pass
					#print(jpgCount)	
					#print(x)
					veredito1 = IsItStopSign(x[1])
					veredito2 = IsItThumbsDownOrUp(x[1])
					if(veredito1 == "Stop Sign"):
						StopSignCount = StopSignCount+1
						print("Algorithm: This frame is a Stop Sign")
					elif(veredito2 == "Thumbs Up"):
						ThumbsUpCount = ThumbsUpCount+1
						print("Algorithm: This frame is a Thumbs Up")
					elif(veredito2 == "Thumbs Down"):
						ThumbsUpCount = ThumbsDownCount+1
						print("Algorithm: This frame is a Thumbs Down")
					else:
						pass
						#print("Irreconhecível")
				else:
					#print("É tudo zeros")
					countFramesZeros = countFramesZeros+1
					if(jpgCount < 10 and jpgCount<imagecount):
						jpgNewDir = str(jpgDir) +  "\\0000" + str(jpgCount) + ".jpg"
					else:
						jpgNewDir = str(jpgDir) +  "\\000" + str(jpgCount) + ".jpg"
					img = cv2.imread(os.path.join(jpgDir, jpgNewDir))
					try:
						scale_percent = 220 # percent of original size
						width = int(img.shape[1] * scale_percent / 100)
						height = int(img.shape[0] * scale_percent / 100)
						dim = (width, height)
						img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
						cv2.imshow('image',img)
						cv2.waitKey(100)
						cv2.destroyAllWindows()	
						jpgCount = jpgCount+1
					except:
						pass
					#print(jpgCount)	
			#print(countFramesZeros)

			#print(len(results))
			#print(countFramesZeros)
			if((len(results) - countFramesZeros) > 2):
				if(GestoAtual == "Stop Sign"):
						ActualStop = ActualStop+1
				elif(GestoAtual == "Thumbs Up"):
						ActualThumbsUp = ActualThumbsUp+1
				elif(GestoAtual == "Thumbs Down"):
						ActualThumbsDown = ActualThumbsDown+1
				if(StopSignCount > ThumbsUpCount and StopSignCount > ThumbsDownCount):
					print("Algorithm: The gesture identified is the Stop Sign")
					IdentifiedStop = IdentifiedStop+1
					if(GestoAtual == "Stop Sign"):
						CorrectlyIdentifiedStop = CorrectlyIdentifiedStop+1
				elif(ThumbsUpCount > StopSignCount and ThumbsUpCount > ThumbsDownCount):
					print("Algorithm: The gesture identified is a Thumbs Up")
					IdentifiedThumbsUp = IdentifiedThumbsUp+1
					if(GestoAtual == "Thumbs Up"):
						CorrectlyIdentifiedThumbsUp = CorrectlyIdentifiedThumbsUp+1
				else:
					print("Algorithm: The gesture identified is a Thumbs Down")
					IdentifiedThumbsDown = IdentifiedThumbsDown+1
					if(GestoAtual == "Thumbs Down"):
						CorrectlyIdentifiedThumbsDown = CorrectlyIdentifiedThumbsDown+1
			else:
				print("Algorithm: Unrecognizable due to json not having enough information about hand coordinates")
				IdentifiedIrreconhecivel = IdentifiedIrreconhecivel+1


	#time.sleep(1)

print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
print("There were " + str(IdentifiedStop) + " recognized in total but from the " + str(ActualStop) + " Stop Sign showed there were " + str(CorrectlyIdentifiedStop) + " correctly identified (" + str((CorrectlyIdentifiedStop/ActualStop)*100) + "%)")
print("There were " + str(IdentifiedThumbsUp) + " recognized in total but from the " + str(ActualThumbsUp) + " Thumbs Up showed there were " + str(CorrectlyIdentifiedThumbsUp) + " correctly identified (" + str((CorrectlyIdentifiedThumbsUp/ActualThumbsUp)*100) + "%)")
print("There were" + str(IdentifiedThumbsDown) + " recognized in total but from the " + str(ActualThumbsDown) + " Thumbs Down showed there were " + str(CorrectlyIdentifiedThumbsDown) + " correctly identified (" + str((CorrectlyIdentifiedThumbsDown/ActualThumbsDown)*100) + "%)")
print("From all "  + str(allfilescount) + " there were " + str(IdentifiedIrreconhecivel) + " jsons considered unrecognizable due to the lack of information")



# print(results[1])
# zeros = 0
# for x in results:
# 	for a in x[1]:
# 		if a == 0:
# 			zeros = zeros+1
# 	count = count+1
# 	print(x[1])




# count = 0
# for k, v in results:
# 	if(count%2==0 or count == 0):
# 		print("-------- Image number: " + str(count/2) + "-----------")
# 	count = count + 1
# 	print(f'{k}: {v}')

#coords = [51.4402, 85.2405, 0.162075, 61.6894, 81.2985, 0.284878, 73.7783, 73.1517, 0.402258, 82.9763, 61.3257, 0.577386, 89.8091, 59.7489, 0.650057, 69.0479, 57.6465, 0.577585, 72.7271, 45.8204, 0.683052, 73.2527, 37.148, 0.706292, 73.5154, 30.3152, 0.746845, 61.4266, 54.7557, 0.496196, 66.157, 41.3528, 0.556506, 67.2082, 33.9944, 0.684216, 68.785, 25.322, 0.548583, 55.3822, 53.9673, 0.41443, 58.7986, 42.404, 0.465185, 60.6382, 35.834, 0.643764, 61.6894, 30.0524, 0.645615, 49.075, 56.3325, 0.307804, 49.6006, 46.8717, 0.306907, 50.6518, 41.09, 0.522794, 51.9658, 36.3596, 0.6406]

#IsItStopSign(coords)
#IsItThumbsDownOrUp(coords)



