import numpy as np, cv2
img = cv2.imread('Subtracted Image decrease in brightness.jpeg')
cv2.imshow('original image', img)
cv2.waitKey()
img2 = np.zeros((700, 300, 3), np.uint8)
cv2.imshow('Zeros image', img2)
cv2.waitKey()
img3 = np.concatenate((img, img2), axis = 1)
img3 = np.concatenate((img2, img3), axis = 1)
cv2.imshow('concatenate', img3)
cv2.waitKey()
#img3.shape
img2 = np.zeros((100, 1112, 3), np.uint8)
img3 = np.concatenate((img2, img3), axis = 0)
img3 = np.concatenate((img3, img2), axis = 0)
cv2.imshow('concatenate', img3)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imwrite('wtsapp.jpeg', img3)



#by function
def wtsappcrop():
    img_path = input('Please enter the path of image :--')
    img_path = list(("\\" if i == '\\' + '\\' else i for i in img_path))
    img_path = ''.join(img_path)
    img_name = input('Please enter the name of image:-- ')
    img = img_path + '\\' + img_name
    #print(img)
    import cv2, numpy as np
    img = cv2.imread(img)
    height, width = img.shape[:2]
    n = 2
    z = np.zeros((height, 150, 3), np.uint8)
    while n > 0:
        img = np.concatenate((img, z), axis = 1)
        n -= 1
        if n != 0:
            img, z = z, img
            n -= 1
        else:
            del z
            del n
    n = 2
    height, width = img.shape[:2]
    z = np.zeros((100, width, 3), np.uint8)
    while n > 0:
        img = np.concatenate((img, z), axis = 0)
        n -= 1
        if n != 0:
            img, z = z, img
        else:
            del z
            del n
    cv2.destroyAllWindows()
    return cv2.imwrite('wtsapp2.jpeg', img)

#wtsappcrop()
