import os
import re
import sys
import cv2
import fitz
import numpy
import shutil


path = os.path.dirname(sys.argv[0])
if len(sys.argv) < 2:
	folder = input("Input folder: ")
else:
	folder = sys.argv[1]

# Temp folder
if not os.path.exists(os.path.join(path, "temp")):
	os.makedirs(os.path.join(path, "temp"))

# Input templates and images
template = os.path.join(path, "template.pdf")

# Get images
files = [folder + "/" + i for i in os.listdir(folder) if i.endswith(".png")]
files.sort(key=lambda f: int(re.sub('\D', '', f)))
if files == []:
	exit()

# Create base template
doc = fitz.open(template)
doc2 = fitz.open(template)
for i in range(len(files)-1):
	doc.insert_pdf(doc2)

# Add images onto base
print("[", end="")
for (count, page) in enumerate(doc):
	# shrink images
	image = cv2.imread(files[count])
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray2 = 255 * (gray < 250).astype(numpy.uint8)
	coordinates = cv2.findNonZero(gray2)
	x, y, w, h = cv2.boundingRect(coordinates)

	border = 24
	shrink = cv2.copyMakeBorder(image[y:y+h, x:x+w], border, border, border, border, cv2.BORDER_CONSTANT, value=[255, 255, 255])
	cv2.imwrite(os.path.join(path, "temp", f"{count}.png"), shrink)

	w = shrink.shape[1]
	h = shrink.shape[0]
	if h > 842:
		percent = h / 842
		h = 842
		w = int(w / percent)
	if w > 595:
		percent = w / 595
		w = 595
		h = int(h / percent)
	rect = fitz.Rect(0, 0, w, h)
	page.insert_image(rect, filename=os.path.join(path, "temp", f"{count}.png"))

	print(">", end="")
print("]")
doc.save(folder + ".pdf")

# clean up
shutil.rmtree(os.path.join(path, "temp"))
print("Saved as: " + folder + ".pdf")
