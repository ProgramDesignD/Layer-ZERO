from direct.gui.DirectGui import *

from .roomwait import RoomWait

class RoomSelectItem(DirectFrame):
    def __init__(self, text, parent=None, on_submit=None, **kw):
        super().__init__(parent, frameSize=(-1.0,1.0,-0.1,0.1),**kw)
        self.iconLabel=DirectLabel(parent=self, text="icon", text_scale=.1,pos=(-0.8,0,0),frameSize=(-0.2,0,-0.03,0.07))
        self.nameButton=DirectButton(parent=self,text_scale=.1,text=text,frameSize=(-0.8,1.0,-0.03,0.07), borderWidth=(0.002,0.002),command=lambda: on_submit(text))
        self.bounds=self["frameSize"]

class RoomSelect(DirectFrame):
    def __init__(self, parent=None, on_leave=None, items=[], **kw):
        super().__init__(parent, **kw)
        self.leave_btn = DirectButton(
            parent=self,
            text="戻る",
            scale=.1,
            pos=(-1.0, 0, -0.8),
            command=on_leave
        )
        self.room_input = DirectEntry(
            parent=self,
            command=lambda:self.on_select_room(self.room_input.get(plain=True)),
            pos=(-0.5, 0, -0.75),
            text_scale=.1,
            frameSize=(0, 1.0, -0.1, 0.1)
        )
        self.submit_btn = DirectButton(
            parent=self,
            text="決定",
            scale=.1,
            pos=(1.0, 0, -0.8),
            command=lambda: self.on_select_room(self.room_input.get(plain=True))
        )
        
        self.scroll_list=DirectScrolledList(
            items=items,
            parent=self,
            decButton_pos=(0, 0, -0.65),
            decButton_text="Dec",
            decButton_text_scale=0.1,
            decButton_borderWidth=(0.005, 0.005),

            incButton_pos=(0, 0, 0.6),
            incButton_text="Inc",
            incButton_text_scale=0.1,
            incButton_borderWidth=(0.005, 0.005),

            frameSize=(-1.0, 1.0, -0.7, 0.7),
            pos=(0, 0, 0.25),
            itemFrame_frameSize=(-1.0, 1.0, -0.9, 0.1),
            itemFrame_pos=(0, 0, 0.4),
            numItemsVisible=5,
            forceHeight=0.1
        )
        if len(items)==0:
            for i in range(50):self.scroll_list.addItem(RoomSelectItem(str(i), on_submit=lambda v: self.on_select_room(v)))
    def on_select_room(self, roomid):
        print(roomid)
        self.hide()
        self.roomwait=RoomWait(parent=self.parent, on_leave=self.on_select_room_leave, on_submit=self.on_room_submit)
    def on_select_room_leave(self):
        self.roomwait.hide()
        self.show()
    def on_room_submit(self):
        self.roomwait.hide()