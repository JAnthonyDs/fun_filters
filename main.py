import urllib.request
from classes.PencilSketch import PencilSketch
import cv2

urllib.request.urlretrieve(
    'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Golde33443.jpg/800px-Golde33443.jpg',
    'dog.jpg'
)

img = cv2.imread('dog.jpg')
bg = cv2.imread('grama.jpg')

sketch = PencilSketch(resolution=(800, 965),bg_gray = "grama.jpg")
output = sketch.render(img)

cv2.imshow("Pencil Sketch", output)
cv2.waitKey(0)
cv2.destroyAllWindows()