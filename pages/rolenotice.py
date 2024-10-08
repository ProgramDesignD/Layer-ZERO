from direct.gui.DirectGui import *
from direct.gui.OnscreenText import OnscreenText
from direct.task import Task
from panda3d.core import TextNode
try:from .cardchoice import CardChoice
except: from cardchoice import CardChoice
# from pages import cardchoice

class RoleNotice(DirectFrame):
    def __init__(self, parent=None, on_leave=None, **kw):
        super().__init__(parent, **kw)

        self.roles = {0:"実行犯", 1:"共犯", 2:"内通者", 3:"警備員", 4:"社員"}
        self.role_num = 0

        self.textObject = OnscreenText(
            parent=self,
            text="あなたのロールは",
            pos=(-0.9,0.8),
            scale=0.08,
            fg=(1,0.5,0.5,1),
            align=TextNode.ALeft,
            mayChange=1
        )

        self.roletext = OnscreenText(
            parent=self,
            text=self.roles[self.role_num],
            pos=(0,0),
            scale=0.14,
            fg=(1, 0.5, 0.5, 1),
            align=TextNode.ACenter,
            mayChange=1
        )

        self.textObject2 = OnscreenText(
            parent=self,
            text="です。",
            pos=(0.9,-0.8),
            scale=0.08,
            fg=(1,0.5,0.5,1),
            align=TextNode.ARight,
            mayChange=1
        )

    # def myFunction(task):
    #     print('auto change!')
    #     return Task.done
    
    # myTask = Task.TaskManager.doMethodLater(self, 2, myFunction, 'tickTask')



        # 一旦決定ボタンで遷移
        self.determinate_btn = DirectButton(parent=self,
                                      text="決定",
                                      scale=.1,
                                      pos=(-1.0, 0, 0.7),
                                      command= lambda: self.on_determinate(self.role_num))
    def on_determinate(self, role_num):
        self.hide()
        self.makedeck=CardChoice(parent=self.parent ,role_num=role_num)

if __name__ == "__main__":
    from direct.showbase.ShowBase import ShowBase
    base=ShowBase()
    RoleNotice()
    base.run()