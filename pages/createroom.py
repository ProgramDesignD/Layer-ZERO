from direct.gui.DirectGui import *
from direct.gui.OnscreenText import OnscreenText
from panda3d.core import TextNode

from .roomwait import RoomWait

class CreateRoom(DirectFrame):
    def __init__(self, parent=None, on_leave=None, **kw):
        super().__init__(parent, **kw)
        self.leave_btn = DirectButton(
            parent=self,
            text="戻る",
            scale=.1,
            pos=(-1.0, 0, 0.7),
            command=on_leave
        )

        self.textObject = OnscreenText(
            parent=self,
            text="人数 ",
            pos=(-0.05, 0.5),
            scale=0.08,
            fg=(1, 0.5, 0.5, 1),
            align=TextNode.ARight,
            mayChange=1
        )

        self.players=3
        self.number = OnscreenText(
            parent=self,
            text=str(self.players),
            pos=(0,0.5),
            scale=0.15,
            fg=(1, 0.5, 0.5, 1),
            align=TextNode.ACenter
        )

        def inc():
            global players
            players_max = 5
            if self.players >= players_max:
                return
            self.players = self.players+1
            self.number.setText(str(self.players))
        def dec():
            global players
            players_min = 1
            if self.players <= players_min:
                return
            self.players = self.players-1
            self.number.setText(str(self.players))
        self.btn_p = DirectButton(
            parent=self,
            text=("+1"),
            command=inc,
            pos=(0,0,0.65),
            scale=0.1
        )
        self.btn_m = DirectButton(
            parent=self,
            text=("-1"),
            command=dec,
            pos=(0,0,0.38),
            scale=0.1
        )

        self.frm = DirectFrame(
            parent=self,
            frameSize=(-0.05,-0.04,-0.05,0.14)
            ,frameColor=(0,0,0,1)
            ,pos=(0,0,0.5)
        )
        self.frm = DirectFrame(
            parent=self,
            frameSize=(-0.05,0.05,0.13,0.14),
            frameColor=(0,0,0,1),
            pos=(0,0,0.5)
        )
        self.frm = DirectFrame(
            parent=self,
            frameSize=(0.04,0.05,-0.05,0.14),
            frameColor=(0,0,0,1),
            pos=(0,0,0.5)
        )
        self.frm = DirectFrame(
            parent=self,
            frameSize=(-0.05,0.05,-0.05,-0.04),
            frameColor=(0,0,0,1),
            pos=(0,0,0.5)
        )

        self.v = [0]
        self.gamestat = [
            DirectRadioButton(
                parent=self,
                text='公開',
                variable=self.v,
                value=[0],
                scale=0.1,
                pos=(-0.4,0,-0.5)
            ),
            DirectRadioButton(
                parent=self,
                text='非公開',
                variable=self.v,
                value=[1],
                scale=0.1,
                pos=(0.4,0,-0.5)
            )
        ]
        for button in self.gamestat:
            button.setOthers(self.gamestat)

        self.confirm_btn = DirectButton(
            parent=self,
            text="決定",
            scale=.1,
            pos=(0, 0, -0.7),
            command=self.on_make_room
        )
    def on_make_room(self):
        self.hide()
        self.roomwait=RoomWait(parent=self.parent, on_leave=self.on_make_room_leave)
    def on_make_room_leave(self):
        self.roomwait.hide()
        self.show()