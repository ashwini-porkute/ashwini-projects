import sys,os

folder1 = "/home/ashwini/TextDetection_MobilenetSSD/Object-Detection-Metrics/detections/"
folder2 = "/home/ashwini/TextDetection_MobilenetSSD/Object-Detection-Metrics/groundtruths/"

no_of_detections = os.listdir(folder1)
gts = os.listdir(folder2)

print(len(no_of_detections))

for f in gts:
  if f not in os.listdir(folder1):
    os.remove(os.path.join(folder2,f))

print("DONE...!!!")
