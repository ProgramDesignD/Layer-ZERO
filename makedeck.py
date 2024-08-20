from click import command
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from panda3d.core import TextNode
import json

role_list= {"jikkohan", "kyohan", "naitusha", "kebin", "shain"}
kyotu_name_list= ["移動", "聞き込み"]
all_koyu_name_list= {"jikkohan":["盗む", "戦闘", "物理的破壊"],
                    "kyohan":["ハッキング(妨害)", "経路把握", "ピッキング"],
                    "naitusha":["偽の通報", "牢屋の開放"],
                    "kebin":["戦闘", "確保", "シャッター展開"],
                    "shain":["通報", "警備機能の追加"]}
item_name_list= ["けむりだま", "ドローン", "透明マント", "はしご"]

decks={}

for i in role_list: #each role's
    kyotu={}
    koyu={}
    item={}
    any={}
    for j in kyotu_name_list:
        any[j]= 0
    kyotu["kyotu"]= any
    any={}

    for j in all_koyu_name_list[i]:
        any[j]= 0
    koyu= {"koyu":any}
    any={}

    for j in item_name_list:
        any[j]= 0
    item= {"item":any}
    any={}
    decks[i]= [kyotu, koyu, item]

with open('tmp.json', 'wt') as f:

    json.dump(decks, f, indent=2)




class MakeDeck(DirectFrame):
    def __init__(self, role:str, parent=None, on_leave=None, **kw):
        super().__init__(parent, **kw)

        self.font = loader.loadFont('./fonts/Genjyuu.ttf') # type: ignore

        def effect_card_sum(arg):
            corrent_card_sum=0
            for i in range(len(arg)):
                if(arg[i] >= str(0) and arg[i] <= str(9)):
                    corrent_card_sum = corrent_card_sum+int(arg[i:])
                    textObject.setText(str(corrent_card_sum))

# カード枚数の増加減少
        def inc():
            global any_cards
            any_cards_max = 40
            if self.any_cards >= any_cards_max:
                return
            self.any_cards = self.any_cards+1
            self.number.setText(str(self.any_cards))
        def dec():
            global any_cards
            any_cards_min = 0
            if self.any_cards <= any_cards_min:
                return
            self.any_cards = self.any_cards-1
            self.number.setText(str(self.any_cards))

# 各アクション種別ごとの中身
        j=0
        contents=[]
        kyotulist= []
        for i in kyotu_name_list:
            for j in range(21):
                contents.append(i+str(j))
            kyotulist.append(DirectOptionMenu(parent=self, text_font= self.font,items=contents, scale=0.1,text="option",command=effect_card_sum,
                                                highlightColor=(0.65, 0.65, 0.65, 1)))
            contents=[]


        koyu_name_list= all_koyu_name_list[role]  # ロールを認識させて固有アクションを選択する
        j=0
        contents=[]
        koyulist= []
        for i in koyu_name_list:
            for j in range(21):
                contents.append(i+str(j))
            koyulist.append(DirectOptionMenu(parent=self, text_font= self.font,items=contents, scale=0.1,text="option",command=effect_card_sum,
                                                highlightColor=(0.65, 0.65, 0.65, 1)))
            contents=[]
        
        
        j=0
        contents=[]
        itemlist= []
        for i in item_name_list:
            for j in range(21):
                contents.append(i+str(j))
            itemlist.append(DirectOptionMenu(parent=self, text_font= self.font,items=contents, scale=0.1,text="option",command=effect_card_sum,
                                                highlightColor=(0.65, 0.65, 0.65, 1)))
            contents=[]




# デフォルト機能
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
        
        

# 枠
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
                                                pos=(-1.2, 0, 0),
                                                items=kyotulist,
                                                numItemsVisible=numItemsVisible,
                                                forceHeight=itemHeight,
                                                itemFrame_frameSize=(-0.3, 0.3, -0.37, 0.11),
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
                                            pos=(-0.35, 0, 0),
                                            items=koyulist,
                                            numItemsVisible=numItemsVisible,
                                            forceHeight=itemHeight,
                                            itemFrame_frameSize=(-0.3, 0.3, -0.37, 0.11),
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
                                    pos=(0.5, 0, 0),
                                    items=itemlist,
                                    numItemsVisible=numItemsVisible,
                                    forceHeight=itemHeight,
                                    itemFrame_frameSize=(-0.3, 0.3, -0.37, 0.11),
                                    itemFrame_pos=(0.35, 0, 0.4))

        # Add some text
        output = ""
        textObject = OnscreenText(text=output, pos=(0.95, -0.95), scale=0.07,
                                fg=(1, 0.5, 0.5, 1), align=TextNode.ACenter,
                                mayChange=1)