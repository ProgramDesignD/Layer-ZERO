from .actor import DistributedSmoothActor
from direct.showbase.ShowBase import ShowBase
from panda3d.core import KeyboardButton, NodePath, PandaNode
from direct.distributed.ClientRepository import ClientRepository

# import our own repositories
from repos.client import GameClientRepository
from repos.client import DistributedSmoothActor
from direct.task.TaskManagerGlobal import taskMgr

class Avatar:
    def __init__(self, cr:ClientRepository, base:ShowBase):
        self.cr = cr
        self.base=base
        self.ralph = DistributedSmoothActor(self.cr, "models/sphere.bam")
        self.cr.createDistributedObject(
            distObj = self.ralph,
            zoneId = 2)

        # Create a floater object, which floats 2 units above ralph.  We
        # use this as a target for the camera to look at.

        self.floater = NodePath(PandaNode("floater"))
        self.floater.reparentTo(self.ralph)
        self.floater.setZ(2.0)

        # We will use this for checking if keyboard keys are pressed
        self.isDown = self.base.mouseWatcherNode.isButtonDown

        taskMgr.add(self.move, "moveTask")

        # Set up the camera
        self.base.camera.setPos(self.ralph.getX(), self.ralph.getY() + 10, 2)

        # start the avatar
        self.ralph.start()

    # Accepts arrow keys to move either the player or the menu cursor,
    # Also deals with grid checking and collision detection
    def move(self, task):
        # Get the time that elapsed since last frame.  We multiply this with
        # the desired speed in order to find out with which distance to move
        # in order to achieve that desired speed.
        dt = self.base.clock.dt

        # If the camera-left key is pressed, move camera left.
        # If the camera-right key is pressed, move camera right.

        # if self.isDown(KeyboardButton.asciiKey(b"j")):
        #     self.base.camera.setX(self.base.camera, -20 * dt)
        # if self.isDown(KeyboardButton.asciiKey(b"k")):
        #     self.base.camera.setX(self.base.camera, +20 * dt)

        # If a move-key is pressed, move ralph in the specified direction.

        if self.isDown(KeyboardButton.asciiKey(b"a")):
            self.ralph.setH(self.ralph.getH() + 300 * dt)
        if self.isDown(KeyboardButton.asciiKey(b"d")):
            self.ralph.setH(self.ralph.getH() - 300 * dt)
        if self.isDown(KeyboardButton.asciiKey(b"w")):
            self.ralph.setY(self.ralph, -20 * dt)
        if self.isDown(KeyboardButton.asciiKey(b"s")):
            self.ralph.setY(self.ralph, +10 * dt)

        # update distributed position and rotation
        #self.ralph.setDistPos(self.ralph.getX(), self.ralph.getY(), self.ralph.getZ())
        #self.ralph.setDistHpr(self.ralph.getH(), self.ralph.getP(), self.ralph.getR())

        # If ralph is moving, loop the run animation.
        # If he is standing still, stop the animation.
        # currentAnim = self.ralph.getCurrentAnim()

        # if self.isDown(KeyboardButton.asciiKey(b"w")):
        #     if currentAnim != "run":
        #         self.ralph.loop("run")
        # elif self.isDown(KeyboardButton.asciiKey(b"s")):
        #     # Play the walk animation backwards.
        #     if currentAnim != "walk":
        #         self.ralph.loop("walk")
        #     self.ralph.setPlayRate(-1.0, "walk")
        # elif self.isDown(KeyboardButton.asciiKey(b"a")) or self.isDown(KeyboardButton.asciiKey(b"d")):
        #     if currentAnim != "walk":
        #         self.ralph.loop("walk")
        #     self.ralph.setPlayRate(1.0, "walk")
        # else:
        #     if currentAnim is not None:
        #         self.ralph.stop()
        #         self.ralph.pose("walk", 5)
        #         self.isMoving = False

        # If the camera is too far from ralph, move it closer.
        # If the camera is too close to ralph, move it farther.

        camvec = self.ralph.getPos() - self.base.camera.getPos()
        camvec.setZ(0)
        camdist = camvec.length()
        camvec.normalize()
        print("\r", camdist, end="")
        # if camdist > 10.0:
        #     self.base.camera.setPos(self.base.camera.getPos() + camvec * (camdist - 10))
        #     camdist = 10.0
        # if camdist < 5.0:
        self.base.camera.setPos(self.base.camera.getPos() - camvec * camdist)
        #camdist = 5.0

        # The camera should look in ralph's direction,
        # but it should also try to stay horizontal, so look at
        # a floater which hovers above ralph's head.
        self.base.camera.lookAt(self.floater)

        return task.cont