from unittest import result
from direct.gui.DirectGui import *

class Result(DirectFrame):
    def __init__(self, role:str, result, parent=None, on_leave=None, **kw):     #resultをゲームから受け取る
        super().__init__(parent=None, **kw)
        self.font = loader.loadFont('./fonts/Genjyuu.ttf') # type: ignore
        self.leave_btn = DirectButton(parent=self,
                                      text="戻る",
                                      text_font=self.font,
                                      scale=.1,
                                      pos=(-1.0, 0, 0.7),
                                      command=on_leave)
