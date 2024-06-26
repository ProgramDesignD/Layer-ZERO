from direct.gui.DirectGui import *

class RoomMenu(DirectFrame):
    def __init__(self, parent=None, on_leave=None, **kw):
        super().__init__(parent, **kw)
        self.font = loader.loadFont('./fonts/Genjyuu.ttf') # type: ignore
        self.leave_btn = DirectButton(parent=self,
                                      text="戻る",
                                      text_font=self.font,
                                      scale=.1,
                                      pos=(-1.0, 0, 0.7),
                                      command=on_leave)
        self.make_room_btn = DirectButton(parent=self,
                                          text="ルームを作る", 
                                          text_font=self.font,
                                          scale=.2,
                                          pos=(0, 0, 0.5))
        self.join_room_btn = DirectButton(parent=self,
                                          text="ルームに入る",
                                          text_font=self.font,
                                          scale=.2,
                                          pos=(0, 0, -0.5))