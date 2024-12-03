from typing import Dict
from direct.distributed.DistributedObject import DistributedObject
from direct.showbase import ShowBaseGlobal
from models.actor import DistributedSmoothActor

class RoomModel:    
    def __init__(self, id, name, max_player, is_visible):
        self.id=id
        self.name=name
        self.max_player=max_player
        self.is_visible=is_visible

class Room(DistributedObject):
    rooms:Dict[int, "Room"]={}
    players:Dict[int,"DistributedSmoothActor"]
    def __init__(self, cr, room:RoomModel=None): # type: ignore
        super().__init__(cr)
        self.roomModel=room
        self.players={}
    def setRoomModel(self, room):
        self.roomModel=RoomModel(*room)
        self.roomModel.id=self.getDoId()
    def getRoomModel(self):
        return self.roomModel
    def generate(self):
        doid=self.getDoId()
        if self.roomModel is not None: self.roomModel.id=doid
        Room.rooms[doid]=self
        return super().generate()
    def announceGenerate(self) -> None:
        ShowBaseGlobal.base.messenger.send("room_generated", [self])
        return super().announceGenerate()
    def delete(self):
        Room.rooms.pop(self.getDoId(), None)
        ShowBaseGlobal.base.messenger.send("room_deleted", [self])
        return super().delete()
    def onPlayerUpdate(self, player_id:int):
        player:DistributedSmoothActor|None=self.cr.getDo(player_id) # type: ignore
        if player is not None:
            self.players[player_id]=player
            ShowBaseGlobal.base.messenger.send("player_update", [self])
    def handleChildArriveZone(self, childObj, zoneId) -> None:
        print(childObj, zoneId)
        return super().handleChildArriveZone(childObj, zoneId)
    @property
    def id(self):
        return self.roomModel.id
    @property
    def name(self):
        return self.roomModel.name
    @property
    def max_player(self):
        return self.roomModel.max_player
    @property
    def is_visible(self):
        return bool(self.roomModel.is_visible)