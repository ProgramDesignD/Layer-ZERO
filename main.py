from direct.showbase.ShowBase import ShowBase

from roommenu import RoomMenu
from top import TopMenu
from deckmenu import DeckMenu
from makedeck import MakeDeck
class ZeroLayer(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.scenes={
            "topmenu": TopMenu(parent=self.aspect2d, on_start=lambda: self.changeScene("roommenu"), 
                                                     on_deck= lambda: self.changeScene("deckmenu")),
            "roommenu": RoomMenu(parent=self.aspect2d, on_leave=lambda: self.changeScene("topmenu")),
            "deckmenu": DeckMenu(parent=self.aspect2d, on_leave=lambda: self.changeScene("topmenu"),
                                                       on_make_deck= lambda role: self.changeScene("makedeck")),
            "makedeck": MakeDeck(parent= self.aspect2d, on_leave=lambda: self.changeScene("deckmenu"))
        }
        self.changeScene("topmenu")
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