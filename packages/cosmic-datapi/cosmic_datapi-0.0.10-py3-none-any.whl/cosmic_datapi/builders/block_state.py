from ..api import AbstractBuilder, BuiltData
from typing import Any


class BlockStateBuilder(AbstractBuilder):
    def __init__(self, mod: "Mod", name: str, block: "BlockBuilder"):
        super().__init__(mod)
        self._name = name
        self._block = block
        self._data = {
        #   "parameter":            None, # default value
            "modelName":            None,
            "isOpaque":             None, # true
            "isTransparent":        None, # false
            "stateGenerators":      None, # []
            "catalogHidden":        None, # false
            "lightAttenuation":     None, # 15
            "canRaycastForBreak":   None, # true
            "canRaycastForPlaceOn": None, # true
            "canRaycastForReplace": None, # false
            "walkThrough":          None, # false
            "lightLevelRed":        None, # 0
            "lightLevelGreen":      None, # 0
            "lightLevelBlue":       None, # 0
            "isFluid":              None, # false
            "rotXZ":                None, # n/a, this might only be used for slabs/stairs. I'm not sure yet
        }

    def set(self, option: str, value: Any) -> "BlockStateBuilder":
        self._data[option] = value
        return self

    def with_model(self, id: str) -> "BlockStateBuilder":
        return self.set("modelName", id)

    def with_state_generator(self, generator: str) -> "BlockStateBuilder":
        if self._data["stateGenerators"] is None:
            self._data["stateGenerators"] = []
        self._data["stateGenerators"].append(generator)
        return self

    def with_state_generators(self, generators: list[str]) -> "BlockStateBuilder":
        if self._data["stateGenerators"] is None:
            self._data["stateGenerators"] = []
        self._data["stateGenerators"].extend(generators)
        return self

    def with_slabs(self) -> "BlockStateBuilder":
        return self.with_state_generator("base:slabs_all")

    def with_stairs(self) -> "BlockStateBuilder":
        return self.with_state_generator("base:stairs_seamless_all")

    def with_light(self, r: int, g: int, b: int) -> "BlockStateBuilder":
        self.set("lightLevelRed", r)
        self.set("lightLevelGreen", g)
        self.set("lightLevelBlue", b)
        return self

    def with_light_attenuation(self, value: int) -> "BlockStateBuilder":
        return self.set("lightAttenuation", value)

    def with_block_events(self, id: str) -> "BlockStateBuilder":
        return self.set("blockEventsId", id)

    def with_no_catalog_entry(self) -> "BlockStateBuilder":
        return self.set("catalogHidden", True)

    def with_walk_through(self) -> "BlockStateBuilder":
        return self.set("walkThrough", True)

    def with_transparency(self) -> "BlockStateBuilder":
        return self.set("isTransparent", True)

    def not_opaque(self) -> "BlockStateBuilder":
        return self.set("isOpaque", False)

    def is_fluid(self) -> "BlockStateBuilder":
        return self.set("isFluid", True)

    def with_raycast_options(self, for_break: bool = True, for_place: bool = True, for_replace: bool = False) -> "BlockStateBuilder":
        self.set("canRaycastForBreak", for_break)
        self.set("canRaycastForPlaceOn", for_place)
        self.set("canRaycastForReplace", for_replace)
        return self

    def build(self) -> "BlockBuilder":
        data = {key: val for key, val in self._data.items() if val is not None}
        if "modelName" not in data:
            print(f"error: block state {self._mod.namespace}:{self._block._name}[{self._name}] has no model.")
        self._block._data["blockStates"][self._name] = data
        return self._block
