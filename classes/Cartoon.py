import cv2

class Cartoon:
    def __init__(self, image_path):
        img = cv2.imread(image_path)
        self.img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    def render(self):
        img_rgb = self.img_rgb
        
        original_height, original_width = img_rgb.shape[:2]

        numDownSamples = 2 # number of downscaling steps
        numBilateralFilters = 7 # number of bilateral filtering steps

        # -- STEP 1 --
        # downsample image using Gaussian pyramid
        img_color = img_rgb
        for _ in range(numDownSamples):
            img_color = cv2.pyrDown(img_color)
        
        # repeatedly apply small bilateral filter instead of applying
        # one large filter
        for _ in range(numBilateralFilters):
            img_color = cv2.bilateralFilter(img_color, 9, 9, 7)
        
        # upsample image to original size
        for _ in range(numDownSamples):
            img_color = cv2.pyrUp(img_color)
        
        img_color = cv2.resize(img_color, (original_width, original_height))
        
        # -- STEPS 2 and 3 --
        # convert to grayscale and apply median blur
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
        img_blur = cv2.medianBlur(img_gray, 7)

        # -- STEP 4 --
        # detect and enhance edges
        img_edge = cv2.adaptiveThreshold(img_blur, 255,
        cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 2)
        
        # -- STEP 5 --
        # convert back to color so that it can be bit-ANDed
        # with color image
        img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)

        return cv2.bitwise_and(img_color, img_edge)