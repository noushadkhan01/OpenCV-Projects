def cv2_imshow(a):
  import cv2
  import numpy as np
  import PIL
  from IPython.display import display
  """A replacement for cv2.imshow() for use in Jupyter notebooks."""
  a = a.clip(0, 255).astype('uint8')
  # cv2 stores colors as BGR; convert to RGB
  if a.ndim == 3:
    if a.shape[2] == 4:
      a = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)
    else:
      a = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  display(PIL.Image.fromarray(a))
