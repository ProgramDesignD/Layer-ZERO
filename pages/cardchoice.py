from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.gui.DirectGui import *
from panda3d.core import TextNode
from direct.showbase import ShowBaseGlobal
import warnings
import json
from .makedeck import role_list,kyotu_name_list,all_koyu_name_list,item_name_list

warnings.simplefilter('ignore')


# デッキの初期化
decks={}
temp=[]
for i in role_list: #each role's
    kyotu={}
    koyu={}
    item={}
    for j in kyotu_name_list:
        kyotu[j]= 0

    for j in all_koyu_name_list[i]:
        koyu[j]= 0

    for j in item_name_list:
        item[j]= 0

    decks[i]= {"kyotu":kyotu, "koyu":koyu, "item":item}

with open('deck.json', encoding='utf-8') as file:
    try:
        d = json.load(file)
    except:
        with open('deck.json', 'wt', encoding='utf-8') as f:
            json.dump(decks, f, indent=2, ensure_ascii=False)

with open('deck.json',encoding='utf-8') as f:
    d_update = json.load(f)



class CardChoice(DirectFrame):
    def __init__(self, role_num:int, parent=None, command=None, **kw):
        super().__init__(parent, **kw)

        role= role_list[role_num]

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
            kyotulist.append(DirectOptionMenu(parent=self, items=contents, scale=0.1, command=lambda arg: change_contents(arg, "kyotu"),
                                                highlightColor=(0.65, 0.65, 0.65, 1), initialitem=corrent_deck[role]["kyotu"][i]))
            contents=[]


        koyu_name_list= all_koyu_name_list[role]  # ロールを認識させて固有アクションを選ぶ
        j=0
        contents=[]
        koyulist= []
        for i in koyu_name_list:
            for j in range(21):
                contents.append(i+str(j))
            koyulist.append(DirectOptionMenu(parent=self,items=contents, scale=0.1, command=lambda arg: change_contents(arg, "koyu"),
                                                highlightColor=(0.65, 0.65, 0.65, 1), initialitem=corrent_deck[role]["koyu"][i]))
            contents=[]
        
        
        j=0
        contents=[]
        itemlist= []
        for i in item_name_list:
            for j in range(21):
                contents.append(i+str(j))
            itemlist.append(DirectOptionMenu(parent=self, items=contents, scale=0.1, command=lambda arg: change_contents(arg, "item"), 
                                                highlightColor=(0.65, 0.65, 0.65, 1), initialitem=corrent_deck[role]["item"][i]))
            contents=[]




# デフォルト機能
        self.leave_btn = DirectButton(parent=self,
                                        text="決定",
                                        scale=.1,
                                        pos=(-1.0, 0, 0.85),
                                        command=command)


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


# カウントダウンは全ユーザで同期するので、サーバ側で処理する？
# class Countdown(ShowBase):
#     def __init__(self):
#         ShowBase.__init__(self)

#         # カウントダウン時間を設定
#         self.countdown_time = 60.0

#         # 画面上にカウントダウンを表示するためのテキストノードを作成
#         self.text_node = TextNode('countdown')
#         self.text_node.setText(str(int(self.countdown_time)))
#         self.text_node.setAlign(TextNode.ACenter)
        
#         text_node_path = ShowBaseGlobal.aspect2d.attachNewNode(self.text_node)
#         text_node_path.setScale(0.2)
#         text_node_path.setPos(-0.9, 1, 0.8)

#         # カウントダウンを処理するタスクを追加
#         self.taskMgr.add(self.update_countdown, "updateCountdownTask")

#     def update_countdown(self, task):
#         # 経過時間を計算
#         dt = ShowBaseGlobal.globalClock.getDt()
#         self.countdown_time -= dt

#         # カウントダウンが0以下になったら終了
#         if self.countdown_time <= 0:
#             self.text_node.setText("Time's Up!")
#             return Task.done

#         # 現在の残り時間をテキストノードに更新
#         self.text_node.setText(str(int(self.countdown_time)))

#         # タスクを継続
#         return Task.cont

# count=Countdown()
# count.run()


