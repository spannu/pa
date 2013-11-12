import pygame
from OpenGL.GL import *

# based on code in http://pyui.cvs.sourceforge.net/viewvc/pyui/PyUIcvs/pyui/renderers/openglPygame.py?view=markup&content-type=text%2Fvnd.viewcvs-markup&revision=HEAD
class TextureManager:

    def __init__ (self):
        self.textures = {}
        
    def bindTexture(self, name):
        glBindTexture(GL_TEXTURE_2D, self.textures[name])
    
    def loadTexture(self, filename, label):
        """This loads images without using P.I.L! Yay."""

        surface = pygame.image.load(filename)

        data = pygame.image.tostring(surface, "RGBA", 1)
        ix = surface.get_width()
        iy = surface.get_height()

        # Create Texture
        texture = glGenTextures(1)
        self.textures[label] = texture
        glBindTexture(GL_TEXTURE_2D, texture)   # 2d texture (x and y size)
        glPixelStorei(GL_UNPACK_ALIGNMENT,1)
        glTexImage2D(GL_TEXTURE_2D,
                     0, 4, ix, iy, 0,
                     GL_RGBA, GL_UNSIGNED_BYTE, data)

        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
        #glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER,
                        GL_LINEAR_MIPMAP_LINEAR)
        #glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER,
                        GL_LINEAR_MIPMAP_LINEAR)
