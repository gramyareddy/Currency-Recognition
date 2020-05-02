from PIL import Image
import glob

file_path = "C:\MyLearnings\DeepLearning\Currency\\Test2\\"
file_paths = glob.glob("C:\MyLearnings\DeepLearning\Currency\\Test1\\*.jpg")
for image_path in file_paths:
    image = Image.open(image_path)
    image = image.resize((224,224),Image.ANTIALIAS)
    new_path = file_path+(image_path.rsplit('\\')[-1])
    image.save(new_path,quality = 95)
