from direct.showbase.ShowBase import ShowBase
from panda3d.core import TextNode, PerspectiveLens

from models.player import Player
from repos.client import GameClientRepository
from pages.roommenu import RoomMenu
from pages.roomselect import RoomSelect
from pages.top import TopMenu
from pages.deckmenu import DeckMenu
from pages.createroom import CreateRoom

class ZeroLayer(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.font=self.loader.loadFont('./fonts/Genjyuu.ttf')
        self.disableMouse()
        self.scene = self.loader.loadModel("models/world.bam")
        if self.scene is not None:
            self.scene.reparentTo(self.render)
            self.scene.setScale(1.5, 1.5, 1.5)
            self.scene.setPos(1, 4.0, -1)
        TextNode.setDefaultFont(self.font)
        self.scenes={
            "topmenu": TopMenu(parent=self.aspect2d, on_start=lambda: self.changeScene("roommenu"), 
                                                     on_deck= lambda: self.changeScene("deckmenu")),
            "roommenu": RoomMenu(parent=self.aspect2d, on_leave=lambda: self.changeScene("topmenu"),
                                                       on_create_room=lambda: self.changeScene("createroom"),
                                                       on_select_room=lambda: self.changeScene("roomselect")),
            "createroom": CreateRoom(parent=self.aspect2d, on_leave=lambda: self.changeScene("roommenu")),
            "deckmenu": DeckMenu(parent=self.aspect2d, on_leave=lambda: self.changeScene("topmenu")),
            "roomselect":RoomSelect(parent=self.aspect2d, on_leave=lambda: self.changeScene("roommenu")),
        }
        self.changeScene("topmenu")
        self.accept("escape", self.onEscape)
        self.accept("client-joined", self.onJoin)
        self.cr=GameClientRepository(base=self)
    def onJoin(self):
        print("join!")
    def onEscape(self):
        print("exit!")
        self.cr.disconnect()
        self.userExit()
    def changeScene(self, scene:str):
        if scene not in self.scenes:
            raise ValueError("Invalid Scene name")
        for sname, s in self.scenes.items():
            if sname == scene:
                s.show()
            else:
                s.hide()

app = ZeroLayer()
app.run()