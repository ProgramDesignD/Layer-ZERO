from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.gui.DirectGui import *
from panda3d.core import TextNode

kyotu_name_list= ["移動", "聞き込み"]
all_koyu_name_list= {"jikkohan":["盗む", "戦闘", "物理的破壊"],
                    "kyohan":["ハッキング(妨害)", "経路把握", "ピッキング"],
                    "naitusha":["偽の通報", "牢屋の開放"],
                    "kebin":["戦闘", "確保", "シャッター展開"],
                    "shain":["通報", "警備機能の追加"]}
item_name_list= ["けむりだま", "ドローン", "透明マント", "はしご"]

class CardChoice(DirectFrame):
    def __init__(self, role:str, parent=None, on_leave=None, **kw):
        super().__init__(parent, **kw)

        self.font = loader.loadFont('./fonts/Genjyuu.ttf') # type: ignore

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
        kyotulist= []
        for i in kyotu_name_list:
            kyotulist.append(DirectButton(parent=self,text_font= self.font, text=(i, "click!", "roll", "disabled"),
                                        text_scale=0.1, borderWidth=(0.01, 0.01),command=inc,
                                        relief=2))
            # self.btn_inc = DirectButton(
            #     parent=self,
            #     text=("+1"),
            #     command=inc,
            #     # pos=(0,0,0.65),
            #     scale=0.1)
            # self.btn_dec = DirectButton(
            #     parent=self,
            #     text=("-1"),
            #     command=dec,
            #     pos=(0,0,0.38),
            #     scale=0.1)
            j=j+1


        koyu_name_list= all_koyu_name_list[role]  # ロールを認識させて固有アクションを選択する
        j=0
        koyulist= []
        for i in koyu_name_list:
            koyulist.append(DirectButton(parent=self,text_font= self.font, text=(i, "click!", "roll", "disabled"),
                                        text_scale=0.1, borderWidth=(0.01, 0.01),command=inc,
                                        relief=2))
            j=j+1

        j=0
        itemlist= []
        for i in item_name_list:
            itemlist.append(DirectButton(parent=self,text_font= self.font, text=(i, "click!", "roll", "disabled"),
                                        text_scale=0.1, borderWidth=(0.01, 0.01),command=inc,
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
        



# 現在のデッキ枚数
        self.textObject = OnscreenText(
            parent=self,
            text="枚数 ",
            pos=(-0.05, -0.8),
            scale=0.08,
            fg=(1, 0.5, 0.5, 1),
            font=self.font,
            align=TextNode.ARight,
            mayChange=1
        )

        self.any_cards=0
        self.number = OnscreenText(
            parent=self,
            text=str(self.any_cards),
            pos=(0,-0.8),
            scale=0.15,
            fg=(1, 0.5, 0.5, 1),
            align=TextNode.ACenter
        )



class Countdown(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # カウントダウン時間を設定
        self.countdown_time = 60.0

        # 画面上にカウントダウンを表示するためのテキストノードを作成
        self.text_node = TextNode('countdown')
        self.text_node.setText(str(int(self.countdown_time)))
        self.text_node.setAlign(TextNode.ACenter)
        
        text_node_path = aspect2d.attachNewNode(self.text_node)
        text_node_path.setScale(0.2)
        text_node_path.setPos(-0.9, 1, 0.8)

        # カウントダウンを処理するタスクを追加
        self.taskMgr.add(self.update_countdown, "updateCountdownTask")

    def update_countdown(self, task):
        # 経過時間を計算
        dt = globalClock.getDt()
        self.countdown_time -= dt

        # カウントダウンが0以下になったら終了
        if self.countdown_time <= 0:
            self.text_node.setText("Time's Up!")
            return Task.done

        # 現在の残り時間をテキストノードに更新
        self.text_node.setText(str(int(self.countdown_time)))

        # タスクを継続
        return Task.cont

count=Countdown()
count.run()