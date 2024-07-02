from direct.gui.DirectGui import *

class DeckMenu(DirectFrame):
    def __init__(self, parent=None, on_leave=None, on_make_deck=None, **kw):
        super().__init__(parent, **kw)
        self.font = loader.loadFont('./fonts/Genjyuu.ttf') # type: ignore
        self.leave_btn = DirectButton(parent=self,
                                      text="戻る",
                                      text_font=self.font,
                                      scale=.1,
                                      pos=(-1.0, 0, 0.7),
                                      command=on_leave)
        self.jikkohan_deck_btn= DirectButton(parent= self,
                                             text="実行犯",
                                             text_font= self.font,
                                             scale= 0.1,
                                             pos= (-0.8,1,0.4),
                                             command= lambda: on_make_deck("jikkohan"))
        self.kyohan_deck_btn= DirectButton(parent= self,
                                           text="共犯",
                                           text_font= self.font,
                                           scale= 0.1,
                                           pos= (0,1,0.4),
                                           command= lambda: on_make_deck("kyohan"))
        self.naitusha_deck_btn= DirectButton(parent= self,
                                           text="内通者",
                                           text_font= self.font,
                                           scale= 0.1,
                                           pos= (0.8,1,0.4),
                                           command= lambda: on_make_deck("naitusha"))

        self.kebin_deck_btn= DirectButton(parent= self,
                                           text="警備員",
                                           text_font= self.font,
                                           scale= 0.1,
                                           pos= (-0.4,1,-0.4),
                                           command= lambda: on_make_deck("kebin"))
        self.shain_deck_btn= DirectButton(parent= self,
                                           text="社員",
                                           text_font= self.font,
                                           scale= 0.1,
                                           pos= (0.4,1,-0.4),
                                           command= lambda: on_make_deck("shain"))