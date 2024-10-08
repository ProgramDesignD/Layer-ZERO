from direct.gui.DirectGui import *
import json
import warnings

warnings.simplefilter('ignore')

role_list= ["jikkohan", "kyohan", "naitusha", "kebin", "shain"]
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

with open('deck.json', encoding='utf-8') as file:
    try:
        d = json.load(file)
    except:
        with open('deck.json', 'wt', encoding='utf-8') as f:
            json.dump(decks, f, indent=2, ensure_ascii=False)

with open('deck.json',encoding='utf-8') as f:
    d_update = json.load(f)



class MakeDeck(DirectFrame):
    def __init__(self, role:str, parent=None, on_leave=None, **kw):
        super().__init__(parent, **kw)

        def change_contents(arg, action_kind):
            card_sum={}
            card_contents=""
            for i in range(len(arg)):
                if(arg[i] >= str(0) and arg[i] <= str(9)):
                    card_sum= int(arg[i:])
                    break
                else:
                    card_contents= card_contents+arg[i]
            with open('deck.json') as f:
                deck_update = json.load(f)
                deck_update[role][action_kind][card_contents]= card_sum
            with open('deck.json', 'wt', encoding='utf-8') as x:
                json.dump(deck_update, x, indent=2, ensure_ascii=False)



# 各アクション種別ごとの中身
        # すでにデッキ作成済みの場合、その枚数を読み込む
        with open("deck.json") as f:
            corrent_deck= json.load(f)

        j=0
        contents=[]
        kyotulist= []
        for i in kyotu_name_list:
            for j in range(21):
                contents.append(i+str(j))
            kyotulist.append(DirectOptionMenu(parent=self, items=contents, scale=0.1, command=lambda arg: change_contents(arg, 0),
                                                highlightColor=(0.65, 0.65, 0.65, 1), initialitem=corrent_deck[role][0].get(i)))
            contents=[]


        koyu_name_list= all_koyu_name_list[role]  # ロールを認識させて固有アクションを選ぶ
        j=0
        contents=[]
        koyulist= []
        for i in koyu_name_list:
            for j in range(21):
                contents.append(i+str(j))
            koyulist.append(DirectOptionMenu(parent=self,items=contents, scale=0.1, command=lambda arg: change_contents(arg, 1),
                                                highlightColor=(0.65, 0.65, 0.65, 1), initialitem=corrent_deck[role][1].get(i)))
            contents=[]
        
        
        j=0
        contents=[]
        itemlist= []
        for i in item_name_list:
            for j in range(21):
                contents.append(i+str(j))
            itemlist.append(DirectOptionMenu(parent=self, items=contents, scale=0.1, command=lambda arg: change_contents(arg, 2), 
                                                highlightColor=(0.65, 0.65, 0.65, 1), initialitem=corrent_deck[role][2].get(i)))
            contents=[]



# デフォルト機能
        self.leave_btn = DirectButton(parent=self,
                                        text="戻る",
                                        scale=.1,
                                        pos=(-1.0, 0, 0.85),
                                        command=on_leave)
        # self.detamin= DirectButton(parent= self,
        #                             text= "決定",
        #                             text_font= self.font,
        #                             scale= 0.1,
        #                             pos= (1, 0, 0.85),
        #                             command=on_leave)
        
        

# 枠
        numItemsVisible = 4
        itemHeight = 0.11
        self.kyotu_action = DirectScrolledList(parent= self,            
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
                                                pos=(-1.2, 0, 0.2),
                                                items=kyotulist,
                                                numItemsVisible=numItemsVisible,
                                                forceHeight=itemHeight,
                                                itemFrame_frameSize=(-0.3, 0.3, -0.37, 0.11),
                                                itemFrame_pos=(0.35, 0, 0.4))


        self.koyu_action = DirectScrolledList(parent= self,
                                            decButton_pos=(0.35, 0, 0.53),
                                            decButton_text="Dec",
                                            decButton_text_scale=0.04,
                                            decButton_borderWidth=(0.005, 0.005),

                                            incButton_pos=(0.35, 0, -0.02),
                                            incButton_text="Inc",
                                            incButton_text_scale=0.04,
                                            incButton_borderWidth=(0.005, 0.005),

                                            frameSize=(0.0, 0.7, -0.05, 0.59),
                                            frameColor=(1,0,0,0.5),
                                            pos=(-0.35, 0, -0.7),
                                            items=koyulist,
                                            numItemsVisible=numItemsVisible,
                                            forceHeight=itemHeight,
                                            itemFrame_frameSize=(-0.3, 0.3, -0.37, 0.11),
                                            itemFrame_pos=(0.35, 0, 0.4))



        self.item = DirectScrolledList(parent= self,
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
                                    pos=(0.5, 0, 0.2),
                                    items=itemlist,
                                    numItemsVisible=numItemsVisible,
                                    forceHeight=itemHeight,
                                    itemFrame_frameSize=(-0.3, 0.3, -0.37, 0.11),
                                    itemFrame_pos=(0.35, 0, 0.4))