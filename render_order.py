from enum import auto, Enum

class RenderOrder(Enum):
    CORPSE = auto() #assigns incrementing integer values automatically (corpse lowest priority)
    ITEM = auto()
    ACTOR = auto()