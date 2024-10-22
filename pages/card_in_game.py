from tkinter import Scale
from direct.showbase.ShowBase import ShowBase
from direct.gui.DirectGui import DirectButton
from panda3d.core import TextNode

from random import choice
from makedeck import role_list,kyotu_name_list,all_koyu_name_list,item_name_list
import json

role:str ="jikkohan"
deck=[]
handcards= [1,1,1,1]

class card_in_game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.font=self.loader.loadFont('./fonts/Genjyuu.ttf')
        TextNode.setDefaultFont(self.font)

        with open("deck.json") as f:
            corrent_deck= json.load(f)

        # デッキの実体の作成、デッキの合計枚数の算出
            deck_sum=0
            for i in kyotu_name_list:
                deck[deck_sum:corrent_deck[role]["kyotu"][i]]= [i]*corrent_deck[role]["kyotu"][i]
                deck_sum+= corrent_deck[role]["kyotu"][i]
            for i in all_koyu_name_list[role]:
                deck[deck_sum:corrent_deck[role]["koyu"][i]]= [i]*corrent_deck[role]["koyu"][i]
                deck_sum+= corrent_deck[role]["koyu"][i]
            for i in item_name_list:
                deck[deck_sum:corrent_deck[role]["item"][i]]= [i]*corrent_deck[role]["item"][i]
                deck_sum+= corrent_deck[role]["item"][i]

        # 初期手札
        for i in range(4):
            self.draw(i)
        
        # # ボタンの作成
        self.card1 = DirectButton(text=(handcards[0], "使用", "説明でるといいよね"),  # ボタンのテキスト (4つの状態)
                                   scale=0.1,  # ボタンのサイズ
                                   pos=(-0.9, 0, -0.75),  # ボタンの位置
                                   command=lambda:self.usecard(0))  # ボタンがクリックされたときのコールバック
        self.card2 = DirectButton(text=(handcards[1], "使用", "説明でるといいよね"),
                                   scale=0.1,
                                   pos=(-0.3, 0, -0.75),
                                   command=lambda:self.usecard(1))
        self.card3 = DirectButton(text=(handcards[2], "使用", "説明でるといいよね"),
                                   scale= 0.1,
                                   pos=(0.3, 0, -0.75),
                                   command=lambda:self.usecard(2))
        self.card4 = DirectButton(text=(handcards[3], "使用", "説明でるといいよね"),
                                   scale=0.1,
                                   pos=(0.9, 0, -0.75),
                                   command=lambda:self.usecard(3))
        

    # ボタンがクリックされたときに呼び出される関数
    def usecard(self, card_index):
        self.draw(card_index)


    def draw(self, index):
        handcards[index]= choice(deck)
        self.card = DirectButton(text=(handcards[index], "使用", "説明でるといいよね"),
                                   scale=0.1,
                                   pos=(-0.9+index*0.6, 0, -0.75), # 式は座標を動的にコントロールするためのもの
                                   command=lambda:self.usecard(index))
        print(handcards)



app = card_in_game()
app.run()











