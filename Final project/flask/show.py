def image_processing(path):
    import cv2
    # import matplotlib.pyplot as plt
    # import matplotlib.image as mpimg
    import numpy as np
    from PIL import Image
    import os
    import PIL
    import glob
    # def show_img(path):
    #     img = mpimg.imread(path)
    #     img = plt.imshow(img)
    #     plt.show()    
    
    #Load model
    from keras.models import load_model
    vgg19 = load_model('vgg19-2.h5')

    def predict_ans(prediction):
        ans = ""
        covid, normal, pneumonia = prediction[0][0],prediction[0][1],prediction[0][2]
        # print(covid, normal, pneumonia)
        ans += "COVID-19 : " + str(round(covid * 100, 2)) + "%"
        ans += '\n'
        ans += "Normal : " + str(round(normal * 100, 2)) + "%"
        ans += '\n'
        ans += "Pneumonia : " + str(round(pneumonia * 100, 2)) +"%"
        ans += '\n'
        return ans

    def predict(path):
#         img = Image.open(path)
        img = cv2.imread(path)
        img = cv2.resize(img,(480,480))
        img = np.reshape(img,[1,480,480,3])
        ans = ""
        #Predict 
        prediction = vgg19.predict(img)
        ans = predict_ans(prediction)
        return ans
    return predict(path)