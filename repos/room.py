from typing import Dict
from direct.distributed.DistributedObject import DistributedObject
from direct.showbase import ShowBaseGlobal
from models.player import Player

class RoomModel:    
    def __init__(self, id, name, max_player, is_visible):
        self.id=id
        self.name=name
        self.max_player=max_player
        self.is_visible=is_visible

class Room(DistributedObject):
    rooms:Dict[int, "Room"]={}
    def __init__(self, cr, room:RoomModel=None): # type: ignore
        super().__init__(cr)
        self.roomModel=room
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
    def disable(self) -> None:
        return super().disable()
    def delete(self):
        Room.rooms.pop(self.getDoId(), None)
        ShowBaseGlobal.base.messenger.send("room_deleted", [self])
        return super().delete()
    def joinPlayer(self, player_id:Player):
        pass
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