from direct.gui.DirectGui import *

from pages.rolenotice import RoleNotice

class RoomWaitItem(DirectFrame):
    def __init__(self, text, parent=None, **kw):
        super().__init__(parent, frameSize=(-1.0,1.0,-0.1,0.1),**kw)
        self.iconLabel=DirectLabel(parent=self, text="icon", text_scale=.1,pos=(-0.8,0,0),frameSize=(-0.2,0,-0.03,0.07))
        self.nameButton=DirectButton(parent=self,text_scale=.1,text=text,frameSize=(-0.8,1.0,-0.03,0.07), borderWidth=(0.002,0.002))
        self.bounds=self["frameSize"]


class RoomWait(DirectFrame):
    def __init__(self, parent=None, on_leave=None, items=[], **kw):
        super().__init__(parent, **kw)
        self.leave_btn = DirectButton(
            parent=self,
            text="戻る",
            scale=.1,
            pos=(-1.0, 0, -0.8),
            command=on_leave
        )
        self.room_label_frame=DirectFrame(
            parent=self,
            pos=(-0.5, 0, -0.75),
            frameSize=(0, 1.0, -0.2, 0.2)
        )
        self.room_label = DirectLabel(
            parent=self.room_label_frame,
            text="ルーム",
            scale=.1,
            pos=(0.2, 0, 0.1),
        )
        self.room_num_label = DirectLabel(
            parent=self.room_label_frame,
            text="5444",
            scale=.2,
            pos=(0.5, 0, -0.1),
        )
        self.submit_btn = DirectButton(
            parent=self,
            text="決定",
            scale=.1,
            pos=(1.0, 0, -0.8),
            command=self.on_start
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
            for i in range(10):self.scroll_list.addItem(RoomWaitItem(str(i)))
    def on_start(self):
        self.hide()
        self.role_notice=RoleNotice(parent=self.parent)

        