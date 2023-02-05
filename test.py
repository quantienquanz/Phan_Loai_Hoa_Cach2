name = ["Daisy, Dandelion, Rose, Sunflower, Tulip"]
prediction =["1,2,3,4,5"]
index = 0
max_value = 0
for i in range (0, len(prediction[0])):
	if max_value < prediction[0][i]:
		max_value = prediction[0][i]
		index == i
print ("Ket qua: ", name[index])
print ("Chinh xac: ", max_value)