from direct.gui.DirectGui import *

class RoomMenu(DirectFrame):
    def __init__(self, parent=None, on_leave=None, on_create_room=None, on_select_room=None, **kw):
        super().__init__(parent, **kw)
        self.leave_btn = DirectButton(parent=self,
                                      text="戻る",
                                      scale=.1,
                                      pos=(-1.0, 0, 0.7),
                                      command=on_leave)
        self.make_room_btn = DirectButton(parent=self,
                                          text="ルームを作る", 
                                          scale=.2,
                                          pos=(0, 0, 0.5),
                                          command=on_create_room)
        self.join_room_btn = DirectButton(parent=self,
                                          text="ルームに入る",
                                          scale=.2,
                                          pos=(0, 0, -0.5),
                                          command=on_select_room)