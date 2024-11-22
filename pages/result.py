from direct.gui.DirectGui import *
from panda3d.core import TextNode

class Result(DirectFrame):
    def __init__(self, role: str, result: str, items: list, parent=None, on_leave=None, **kw):  # resultをゲームから受け取る
        super().__init__(parent=parent, **kw)

        # 勝ち負けの表示
        if result == "win":
            result_text = "勝利！"
        else:
            result_text = "敗北..."

        self.result_label = DirectLabel(
            parent=self,
            scale=0.2,
            pos=(0, 0, 0.5),
            text_align=TextNode.A_center
        )

        # 獲得アイテムの表示        
        items_text1 = "獲得アイテム "
        items_text2 =  ""+ "\n ".join(items)
        self.items_label1 = DirectLabel(
            parent=self,
            text=items_text1,
            scale=0.1,
            pos=(0, 0, 0.3),
            text_align=TextNode.A_center
        )
        self.items_label2 = DirectLabel(
            parent=self,
            text=items_text2,
            scale=0.1,
            pos=(0, 0, 0.2),
            text_align=TextNode.A_center
        )

        # 戻るボタン
        self.leave_btn = DirectButton(
            parent=self,
            text="戻る",
            scale=0.1,
            pos=(0, 0, -0.8),
            command=on_leave
        )