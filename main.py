from direct.showbase.ShowBase import ShowBase

from roommenu import RoomMenu
from top import TopMenu

class ZeroLayer(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.topmenu=TopMenu(on_start=self.show_room_menu)
        self.roommenu=RoomMenu()
        self.roommenu.hide()
    def show_room_menu(self):
        self.topmenu.hide()
        self.roommenu.show()
        

app = ZeroLayer()
app.run()