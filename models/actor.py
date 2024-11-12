from direct.distributed.DistributedSmoothNode import DistributedSmoothNode
from direct.showbase import ShowBaseGlobal

from direct.actor.Actor import Actor

class DistributedSmoothActor(DistributedSmoothNode, Actor):
    def __init__(self, cr):
        Actor.__init__(self)
        DistributedSmoothNode.__init__(self, cr)
        self.setCacheable(1)
        self.setScale(0.1)
        self.ModelName=""
    def setModel(self, modelName:str):
        Actor.loadModel(self, "models/"+modelName)
        self.ModelName=modelName
    def getModel(self):
        return self.ModelName
    def generate(self):
        DistributedSmoothNode.generate(self)
        self.activateSmoothing(True, False)
        self.startSmooth()

    def announceGenerate(self):
        DistributedSmoothNode.announceGenerate(self)
        self.reparentTo(ShowBaseGlobal.base.render)

    def disable(self):
        # remove all anims, on all parts and all lods
        self.stopSmooth()
        if (not self.isEmpty()):
            Actor.unloadAnims(self, None, None, None)
        DistributedSmoothNode.disable(self)

    def delete(self):
        try:
            self.DistributedActor_deleted
        except:
            self.DistributedActor_deleted = 1
            DistributedSmoothNode.delete(self)
            Actor.delete(self)

    def start(self):
        # Let the DistributedSmoothNode take care of broadcasting the
        # position updates several times a second.
        self.startPosHprBroadcast()

    def loop(self, animName):
        self.sendUpdate("loop", [animName])
        return Actor.loop(self, animName)

    def pose(self, animName, frame):
        self.sendUpdate("pose", [animName, frame])
        return Actor.pose(self, animName, frame)