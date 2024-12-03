from direct.gui.DirectGui import *
from direct.distributed.ClientRepository import ClientRepository
from direct.showbase import ShowBaseGlobal

from models.player import Player
from .rolenotice import RoleNotice
from repos.room import Room

class RoomWaitItem(DirectFrame):
    def __init__(self, text, parent=None, **kw):
        super().__init__(parent, frameSize=(-1.0,1.0,-0.1,0.1),**kw)
        self.iconLabel=DirectLabel(parent=self, text="icon", text_scale=.1,pos=(-0.8,0,0),frameSize=(-0.2,0,-0.03,0.07))
        self.nameButton=DirectButton(parent=self,text_scale=.1,text=text,frameSize=(-0.8,1.0,-0.03,0.07), borderWidth=(0.002,0.002))
        self.bounds=self["frameSize"]


class RoomWait(DirectFrame):
    def __init__(self, room:Room, parent=None, on_leave=None, **kw):
        super().__init__(parent, **kw)
        self.room=room
        self.on_leave=on_leave
        cr: ClientRepository = ShowBaseGlobal.base.cr # type: ignore
        ShowBaseGlobal.player = Player(cr, ShowBaseGlobal.base, room_id=self.room.id) # type: ignore
        self.room.joinPlayer(ShowBaseGlobal.player.doId) # type: ignore
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
            text=room.name,
            scale=.2,
            pos=(0.5, 0, -0.1),
        )
        if self.room.isLocal():
            self.submit_btn = DirectButton(
                parent=self,
                text="決定",
                scale=.1,
                pos=(1.0, 0, -0.8),
                command=self.on_start_button
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
        self.scroll_list.addItem(RoomWaitItem(str(ShowBaseGlobal.player.doId))) # type: ignore
        self.accept("room_deleted", self.on_room_delete)
        self.accept("player_update", self.on_player_update)
        self.accept("game_start", self.on_start)
    def on_start_button(self):
        self.room.start()
    def on_start(self, room:Room):
        ShowBaseGlobal.player.start() # type: ignore
        self.hide()
        self.role_notice=RoleNotice(parent=self.parent)
    def on_room_delete(self, room:Room):
        if room is self.room:
            self.leave_btn.commandFunc(None)
            #self.ignore("room_deleted")
    def on_player_update(self, room:Room):
        if room is self.room:
            self.scroll_list.removeAllItems()
            #print(room.id, [(p.getDoId(),p.getLocation()) for p in room.players.values()])
            for player_id in room.players:
                self.scroll_list.addItem(RoomWaitItem(str(player_id))) # type: ignore