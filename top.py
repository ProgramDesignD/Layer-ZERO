import direct.directbase.DirectStart
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *

from panda3d.core import TextNode

# Add some text
bk_text = "Layer-ZERO"
textObject = OnscreenText(text=bk_text, pos=(0,0), scale=0.2,
                          fg=(1, 0.5, 0.5, 1), align=TextNode.ACenter)

# Add button
b = DirectButton(text="START",
                 scale=.1, pos=(0, 0, -0.5))
b2 = DirectButton(text="Icon",
                 scale=.1, pos=(1.0, 0, 0.8))

# Run the tutorial
base.run()