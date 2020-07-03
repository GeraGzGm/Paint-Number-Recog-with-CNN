from tensorflow.keras.models import load_model
import numpy as np
from scipy.signal import convolve2d

from PIL import Image,ImageOps
import matplotlib.pyplot as plt



def Resultado(imagen):
    
    imagen = imagen.convert('L')
    imagen = ImageOps.invert(imagen)
    imagen = imagen.resize((28, 28))
    imagen = np.array(imagen)/255
    
    filtro = np.array([ [0,0,0],[0,10,0],[0,0,0]])
    imagen_conv = convolve2d(imagen,filtro,mode='same')
    
    imagen = imagen_conv.reshape((1,28,28))
    imagen = np.concatenate((imagen,imagen))
    imagen = imagen.reshape(imagen.shape[0],28,28,1)

    model = load_model('ready.h5')


    prediction=model.predict(imagen)
    
    

    
    return np.argmax(prediction)
    
