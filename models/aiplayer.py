from .actor import DistributedSmoothActor
from direct.showbase.ShowBase import ShowBase
from panda3d.core import KeyboardButton, VBase3, Vec3, Point3
from direct.distributed.ClientRepository import ClientRepository
from math import sin, cos, radians

# import our own repositories
from repos.client import GameClientRepository
from repos.client import DistributedSmoothActor
from panda3d.ai import AIWorld, AICharacter
from direct.showbase import ShowBaseGlobal
from direct.task.TaskManagerGlobal import taskMgr

class Player:
    heading_angular_velocity = 100
    pitch_angular_velocity = 50
    max_pitch_angle = 30
    speed = 1
    def __init__(self, cr:ClientRepository, base:ShowBase, room_id):
        self.cr = cr
        self.base=base
        self.ralph = DistributedSmoothActor(self.cr)
        self.ralph.setModel("sphere.bam")
        self.cr.createDistributedObject(
            distObj = self.ralph,
            zoneId = room_id)
        self.AIworld=AIWorld(ShowBaseGlobal.base.render)
        self.AIchar=AICharacter("seeker", self.ralph, 100, 0.05, 5)
        self.AIworld.addAiChar(self.AIchar)
        self.AIbehaviors=self.AIchar.getAiBehaviors()
        # self.base.cam.setScale(0.8)
        #self.ralph.b_setLocation(parentId=room_id, zoneId=room_id)
        self.position = Point3(0, 0, 0)
        # self.direction = VBase3(0, 0, 0)
        # self.velocity = Vec3(0, 0, 0)
        #  # キー操作を保存
        # self.key_map = {
        #     'w': 0,
        #     'a': 0,
        #     's': 0,
        #     'd': 0,
        # }

        # # ユーザー操作
        # self.base.accept('w', self.update_key_map, ["w", 1])
        # self.base.accept('a', self.update_key_map, ["a", 1])
        # self.base.accept('s', self.update_key_map, ["s", 1])
        # self.base.accept('d', self.update_key_map, ["d", 1])
        # self.base.accept('w-up', self.update_key_map, ["w", 0])
        # self.base.accept('a-up', self.update_key_map, ["a", 0])
        # self.base.accept('s-up', self.update_key_map, ["s", 0])
        # self.base.accept('d-up', self.update_key_map, ["d", 0])
        
    # def update_key_map(self, key_name, key_state):
    #     self.key_map[key_name] = key_state

    # def move(self, task):
    #     dt = globalClock.getDt()
    #     if self.base.mouseWatcherNode.hasMouse():
    #         mouse_pos = self.base.mouseWatcherNode.getMouse()
    #         x = mouse_pos.x
    #         #y = mouse_pos.y
    #         heading = self.direction.x
    #         #pitch = self.direction.y
    #         if x < -0.1 or 0.1 < x:
    #             heading -= x * Player.heading_angular_velocity * dt
    #         #if y < -0.1 or 0.1 < y:
    #         #    pitch += y * Player.pitch_angular_velocity * dt
    #         #if pitch < -Player.max_pitch_angle:
    #         #    pitch = -Player.max_pitch_angle
    #         #elif pitch > Player.max_pitch_angle:
    #         #    pitch = Player.max_pitch_angle
    #         #self.direction = VBase3(heading, pitch, 0)
    #         self.direction = VBase3(heading, 0, 0)
    #         self.base.cam.setH(self.direction.x)
    #         self.ralph.setH(self.direction.x)
    #         #self.base.cam.setP(self.direction.y)

    #     key_map = self.key_map

    #     if key_map['w'] or key_map['a'] or key_map['s'] or key_map['d']:
    #         heading = self.direction.x
    #         if key_map['w'] and key_map['a']:
    #             angle = 135
    #         elif key_map['a'] and key_map['s']:
    #             angle = 225
    #         elif key_map['s'] and key_map['d']:
    #             angle = 315
    #         elif key_map['d'] and key_map['w']:
    #             angle = 45
    #         elif key_map['w']:
    #             angle = 90
    #         elif key_map['a']:
    #             angle = 180
    #         elif key_map['s']:
    #             angle = 270
    #         else:  # key_map['d']
    #             angle = 0
    #         self.velocity = \
    #             Vec3(
    #                 cos(radians(angle + heading)),
    #                 sin(radians(angle + heading)),
    #                 0
    #             ) * Player.speed
    #     else:
    #         self.velocity = Vec3(0, 0, 0)
    #     self.position = self.position + self.velocity * dt
    #     self.base.cam.setPos(self.position)
    #     self.ralph.setPos(self.position)

    #     return task.cont
    def AIUpdate(self,task):
        self.AIworld.update()
        return task.cont
    def addSeekTarget(self, target):
        self.AIbehaviors.seek(target)
    def start(self):
        self.ralph.setPos(self.position)
        # taskMgr.add(self.move, "moveTask")
        taskMgr.add(self.AIUpdate, "AIUpdate")
        self.ralph.start()
    def delete(self):
        self.ralph.delete()
    @property
    def doId(self):
        return self.ralph.getDoId()
    @property
    def role(self):
        return self.ralph.role