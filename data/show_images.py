def show_images(images = None, names = None, grayscale = False, width = None, height = None, ticks = False, cmap = None):
    import cv2, numpy as np
    import matplotlib.pyplot as plt
    #%matplotlib inline
    if not width:
        width = min(12, len(images) * 5)
    if not height:
        height = len(images) * 2
    
    if names:
        if len(names) != len(images):
            print(len(names), len(images))
            raise ValueError ('length of names and images are not same')
    n = 1
    if images:
        if names:
            plt.figure(figsize = (width, height))
            for name, image in zip(names, images):
                if grayscale:
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                plt.subplot(max(1, int(len(images) / 2)), 3 , n)
                plt.title(name)
                plt.imshow(image, cmap = cmap)
                if not ticks:
                    plt.xticks([])
                    plt.yticks([])
                n += 1
            plt.show()
        else:
            plt.figure(figsize = (width, height))
            for image in images:
                if grayscale:
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                plt.subplot(max(1, int(len(images) / 2)), min(len(images), 3) , n)
                plt.imshow(image, cmap = cmap)
                if not ticks:
                    plt.xticks([])
                    plt.yticks([])
                n += 1
            plt.show()
    else:
        raise ValueError ('Their are no images to show')
        
        
