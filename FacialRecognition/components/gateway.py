import os

#Main directory
mainDir = os.path.dirname(os.path.abspath(__file__))

#Algorithmy
cascadePath = "haarcascade_frontalface_default.xml"

#Data directory
dataPath = os.path.join(mainDir, "../dataset")
#DataUser directory
dataUser = os.path.join(mainDir, "../dataset/User.")
#Trainer directory
trainPath = os.path.join(mainDir, "../trainer")
#Trainer files
trainFile = os.path.join(mainDir, "../trainer/trainer.yml")
