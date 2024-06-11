import direct.directbase.DirectStart
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *

# Load font
font = loader.loadFont('./fonts/Genjyuu.ttf')

# Add button
b = DirectButton(text="ルームを作る", text_font=font,
                 scale=.2, pos=(0, 0, 0.5))
b2 = DirectButton(text="ルームに入る", text_font=font,
                 scale=.2, pos=(0, 0, -0.5))

# Run the tutorial
base.run()