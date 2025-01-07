from direct.gui.DirectGui import *
from direct.gui.OnscreenText import OnscreenText
from direct.task import Task
from panda3d.core import TextNode
from .cardchoice import CardChoice
from direct.showbase import ShowBaseGlobal

class RoleNotice(DirectFrame):
    roles = {0:"実行犯", 1:"共犯", 2:"内通者", 3:"警備員", 4:"社員"}
    def __init__(self, parent=None, on_leave=None, roleName="", **kw):
        super().__init__(parent, **kw)
        self.role_num = 0

        self.textObject = OnscreenText(
            parent=self,
            text="あなたのロールは",
            pos=(-0.9,0.8),
            scale=0.08,
            fg=(1,0.5,0.5,1),
            align=TextNode.ALeft,
            mayChange=True
        )

        self.roletext = OnscreenText(
            parent=self,
            text=ShowBaseGlobal.base.player.role, # type: ignore
            pos=(0,0),
            scale=0.14,
            fg=(1, 0.5, 0.5, 1),
            align=TextNode.ACenter,
            mayChange=True
        )

        self.textObject2 = OnscreenText(
            parent=self,
            text="です。",
            pos=(0.9,-0.8),
            scale=0.08,
            fg=(1,0.5,0.5,1),
            align=TextNode.ARight,
            mayChange=True
        )
    
        ShowBaseGlobal.base.taskMgr.doMethodLater(2, self.on_two_seconds_later, 'tickTask')

    def on_two_seconds_later(self, task):
        self.hide()
        self.makedeck=CardChoice(parent=self.parent ,role_num=self.role_num, command=self.on_cardchoice_done)
        return task.done
    
    def on_cardchoice_done(self):
        self.makedeck.hide()
        ShowBaseGlobal.base.player.start() # type: ignore