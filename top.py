from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *

from panda3d.core import TextNode

class TopMenu(DirectFrame):
    def __init__(self, on_start, parent=None, **kw):
        super().__init__(parent, **kw)
        self.title = OnscreenText(
            parent=self,
            text="Layer-ZERO",
            pos=(0,0),
            scale=0.2,
            fg=(1, 0.5, 0.5, 1),
            align=TextNode.ACenter)
        self.start_button = DirectButton(
            parent=self,
            text="START",
            scale=.1,
            pos=(0, 0, -0.5),
            command=on_start)
        self.deck_botton= DirectButton(
            parent= self,
            text= "Deck",
            scale= 0.1,
            pos= (0,0,-0.8)
        )
        self.icon_button = DirectButton(
            parent=self,
            text="Icon",
            scale=.1,
            pos=(1.0, 0, 0.8))