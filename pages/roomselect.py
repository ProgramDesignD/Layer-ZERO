from direct.gui.DirectGui import *

from repos.room import Room

from .roomwait import RoomWait

class RoomSelectItem(DirectFrame):
    def __init__(self, text:str, value=None, parent=None, on_submit=None, **kw):
        if value is None:
            value=text
        self.value=value
        super().__init__(parent, frameSize=(-1.0,1.0,-0.1,0.1),**kw)
        self.iconLabel=DirectLabel(parent=self, text="icon", text_scale=.1,pos=(-0.8,0,0),frameSize=(-0.2,0,-0.03,0.07))
        if on_submit is not None:
            self.nameButton=DirectButton(parent=self,text_scale=.1,text=text,frameSize=(-0.8,1.0,-0.03,0.07), borderWidth=(0.002,0.002),command=lambda: on_submit(value))
        self.bounds=self["frameSize"]
    def __hash__(self):
        return self.value

class RoomSelect(DirectFrame):
    def __init__(self, parent=None, on_leave=None, **kw):
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
        self.room_items={}
        self.accept("room_generated", self.on_add_room)
        self.accept("room_deleted", self.on_remove_room)
    def on_add_room(self, room:Room):
        self.room_items[room.id]=RoomSelectItem(str(room.name), value=room.id, on_submit=lambda v: self.on_select_room(v))
        self.scroll_list.addItem(self.room_items[room.id]) # type: ignore
    def on_remove_room(self, room:Room):
        if room.id not in self.room_items:
            print("warn: conflict room", room.id)
            return
        self.scroll_list.removeItem(self.room_items[room.id])
    def on_select_room(self, roomid):
        self.hide()
        self.roomwait=RoomWait(room=Room.rooms[roomid], parent=self.parent, on_leave=self.on_select_room_leave)
    def on_select_room_leave(self):
        self.roomwait.hide()
        self.show()