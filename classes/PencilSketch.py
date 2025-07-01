import cv2

class PencilSketch():
    def __init__(self, resolution=(640, 380), bg_gray=None):

        self.width , self.height = resolution

        try:
            self.canvas = cv2.imread(bg_gray, cv2.IMREAD_GRAYSCALE) 
            if self.canvas is not None:
                self.canvas = cv2.resize(self.canvas, (self.width, self.height))
                print(f"Canvas de fundo carregado: {bg_gray}")
            else:
                print(f"Canvas de fundo não encontrado: {bg_gray}")
        except:
            self.canvas = None
            print(f"Erro ao carregar canvas de fundo: {bg_gray}")
        
    def render(self, img_rgb):
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        img_blur = cv2.GaussianBlur(img_gray, (21,21), 0, 0)
        img_blend = cv2.divide(img_gray, img_blur, scale=256)

        if self.canvas is not None:
            img_blend = cv2.multiply(img_blend, self.canvas, scale=1./256)
            return cv2.cvtColor(img_blend, cv2.COLOR_GRAY2RGB)

        return img_blend
    
    def dodgeV2(image, mask):
        return cv2.divide(image, 255-mask, scale=256)

    def burnV2(image, mask):
        return 255 - cv2.divide(255-image, 255-mask, scale=256)