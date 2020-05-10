import numpy as np
from keras.models import model_from_json
import cv2
from PIL import Image


#if pressed start video capture , 
def Capturepressed():
    cap = cv2.VideoCapture(0)
    skipFrames = 0
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        skipFrames +=1
        if(skipFrames == 11):
            #SendImage to model/Save Image
            cv2.imwrite("SavedImage.jpg",frame)
            ProcessImage()
            break

    # When everything done, release the capture
    cap.release()

def ProcessImage():
    #load model
    # load json and create model
    json_file = open('C:\MyLearnings\\DeepLearning\\Currency\\Dataset\\Resizedcurrency\\Model\\model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("C:\MyLearnings\DeepLearning\Currency\Dataset\Resizedcurrency\\Model\\model.h5")
    #Preprocess Image
    image = Image.open("SavedImage.jpg")
    image = image.resize((224,224),Image.ANTIALIAS)            
    image = np.array(image)
    image = image.astype("float32")
    image/=255.0
    image = np.expand_dims(image, axis=0)
    #Predict Image
    print(loaded_model.predict(image))

    
Capturepressed()
