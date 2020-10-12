class AGameObject:
    def __init__(self, x, y, width, height, image):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__image = image

    def getX(self):
        return self.__x

    def setX(self, newX):
        self.__x = newX

    def getY(self):
        return self.__y

    def setY(self, newY):
        self.__y = newY

    def getWidth(self):
        return self.__width

    def setWidth(self, newWidth):
        self.__width = newWidth

    def getHeight(self):
        return self.__height

    def setHeight(self, newHeight):
        self.__height = newHeight

    def draw(self, window, additionalMove={"x": 0, "y": 0}):
        window.blit(
            self.__image,
            (
                self.getX() + additionalMove["x"],
                self.getY() + additionalMove["y"]
            )
        )

    def setImage(self, newImage):
        self.__image = newImage
