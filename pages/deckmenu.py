from direct.gui.DirectGui import *
from .makedeck import MakeDeck

class DeckMenu(DirectFrame):
    def __init__(self, parent=None, on_leave=None, **kw):
        super().__init__(parent, **kw)
        self.leave_btn = DirectButton(parent=self,
                                      text="戻る",
                                      scale=.1,
                                      pos=(-1.0, 0, 0.7),
                                      command=on_leave)
        self.jikkohan_deck_btn= DirectButton(parent= self,
                                             text="実行犯",

                                             scale= 0.1,
                                             pos= (-0.8,1,0.4),
                                             command= lambda: self.on_make_deck("jikkohan"))
        self.kyohan_deck_btn= DirectButton(parent= self,
                                           text="共犯",
                                           scale= 0.1,
                                           pos= (0,1,0.4),
                                           command= lambda: self.on_make_deck("kyohan"))
        self.naitusha_deck_btn= DirectButton(parent= self,
                                           text="内通者",
                                           scale= 0.1,
                                           pos= (0.8,1,0.4),
                                           command= lambda: self.on_make_deck("naitusha"))

        self.kebin_deck_btn= DirectButton(parent= self,
                                           text="警備員",
                                           scale= 0.1,
                                           pos= (-0.4,1,-0.4),
                                           command= lambda: self.on_make_deck("kebin"))
        self.shain_deck_btn= DirectButton(parent= self,
                                            text="社員",
                                            scale= 0.1,
                                            pos= (0.4,1,-0.4),
                                            command= lambda: self.on_make_deck("shain"))
    def on_make_deck(self, role):
        self.hide()
        self.makedeck=MakeDeck(parent=self.parent ,role=role, on_leave=self.on_make_deck_leave)
    def on_make_deck_leave(self):
        self.makedeck.hide()
        self.show()