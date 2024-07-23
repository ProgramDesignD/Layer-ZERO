from direct.gui.DirectGui import *

kyotu_name_list= ["移動", "聞き込み"]
all_koyu_name_list= {"jikkohan":["盗む", "戦闘", "物理的破壊"],
                    "kyohan":["ハッキング(妨害)", "経路把握", "ピッキング"],
                    "naitusha":["偽の通報", "牢屋の開放"],
                    "kebin":["戦闘", "確保", "シャッター展開"],
                    "shain":["通報", "警備機能の追加"]}
item_name_list= ["けむりだま", "ドローン", "透明マント", "はしご"]

class MakeDeck(DirectFrame):
    def __init__(self, role:str, parent=None, on_leave=None, **kw):
        super().__init__(parent, **kw)

        self.font = loader.loadFont('./fonts/Genjyuu.ttf') # type: ignore

        j=0
        kyotulist= []
        for i in kyotu_name_list:
            kyotulist.append(DirectButton(parent=self,text_font= self.font, text=(i, "click!", "roll", "disabled"),
                                        text_scale=0.1, borderWidth=(0.01, 0.01),
                                        relief=2))
            j=j+1

        koyu_name_list= all_koyu_name_list[role]  # ロールを認識させて固有アクションを選択する
        j=0
        koyulist= []
        for i in koyu_name_list:
            koyulist.append(DirectButton(parent=self,text_font= self.font, text=(i, "click!", "roll", "disabled"),
                                        text_scale=0.1, borderWidth=(0.01, 0.01),
                                        relief=2))
            j=j+1

        j=0
        itemlist= []
        for i in item_name_list:
            itemlist.append(DirectButton(parent=self,text_font= self.font, text=(i, "click!", "roll", "disabled"),
                                        text_scale=0.1, borderWidth=(0.01, 0.01),
                                        relief=2))
            j=j+1

        self.leave_btn = DirectButton(parent=self,
                                        text="戻る",
                                        text_font=self.font,
                                        scale=.1,
                                        pos=(-1.0, 0, 0.85),
                                        command=on_leave)
        self.detamin= DirectButton(parent= self,
                                    text= "決定",
                                    text_font= self.font,
                                    scale= 0.1,
                                    pos= (1, 0, 0.85),
                                    command=on_leave)


        numItemsVisible = 4
        itemHeight = 0.11
        self.kyotu_action = DirectScrolledList(parent= self,
                                                text_font= self.font,
            
                                                decButton_pos=(0.35, 0, 0.53),
                                                decButton_text="Dec",
                                                decButton_text_scale=0.04,
                                                decButton_borderWidth=(0.005, 0.005),

                                                incButton_pos=(0.35, 0, -0.02),
                                                incButton_text="Inc",
                                                incButton_text_scale=0.04,
                                                incButton_borderWidth=(0.005, 0.005),

                                                frameSize=(0.0, 0.7, -0.05, 0.59),
                                                frameColor=(0,0,1,0.5),
                                                pos=(-0.75, 0, 0),
                                                items=kyotulist,
                                                numItemsVisible=numItemsVisible,
                                                forceHeight=itemHeight,
                                                itemFrame_frameSize=(-0.2, 0.2, -0.37, 0.11),
                                                itemFrame_pos=(0.35, 0, 0.4))


        self.koyu_action = DirectScrolledList(parent= self,
                                            text_font= self.font,decButton_pos=(0.35, 0, 0.53),
                                            decButton_text="Dec",
                                            decButton_text_scale=0.04,
                                            decButton_borderWidth=(0.005, 0.005),

                                            incButton_pos=(0.35, 0, -0.02),
                                            incButton_text="Inc",
                                            incButton_text_scale=0.04,
                                            incButton_borderWidth=(0.005, 0.005),

                                            frameSize=(0.0, 0.7, -0.05, 0.59),
                                            frameColor=(1,0,0,0.5),
                                            pos=(0, 0, 0),
                                            items=koyulist,
                                            numItemsVisible=numItemsVisible,
                                            forceHeight=itemHeight,
                                            itemFrame_frameSize=(-0.2, 0.2, -0.37, 0.11),
                                            itemFrame_pos=(0.35, 0, 0.4))



        self.item = DirectScrolledList(parent= self,
                                    text_font= self.font,
                                    decButton_pos=(0.35, 0, 0.53),
                                    decButton_text="Dec",
                                    decButton_text_scale=0.04,
                                    decButton_borderWidth=(0.005, 0.005),

                                    incButton_pos=(0.35, 0, -0.02),
                                    incButton_text="Inc",
                                    incButton_text_scale=0.04,
                                    incButton_borderWidth=(0.005, 0.005),

                                    frameSize=(0.0, 0.7, -0.05, 0.59),
                                    frameColor=(0,1,0,0.5),
                                    pos=(0.75, 0, 0),
                                    items=itemlist,
                                    numItemsVisible=numItemsVisible,
                                    forceHeight=itemHeight,
                                    itemFrame_frameSize=(-0.2, 0.2, -0.37, 0.11),
                                    itemFrame_pos=(0.35, 0, 0.4))

