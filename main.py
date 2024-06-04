from direct.showbase.ShowBase import ShowBase

class ZeroLayer(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

app = ZeroLayer()
app.run()