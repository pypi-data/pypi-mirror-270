from pringles.models import Port
from pringles.utils import VirtualTime
from typing import Union, List


class Event:
    """Event is the representation of external influence into the model.
    An event is composed of:

    * event time
    * target port, belonging to the top model
    * value

    """
    def __init__(self,
                 time: VirtualTime,
                 port: Port,
                 value: Union[float, List[float]]):
        self.time = time
        self.target_port = port
        self.value = value

    def serialize(self) -> str:
        """Serialize the :class:`Event` into a CD++ consumable string."""
        return f"{str(self.time)} {self.target_port.name} {self._serialize_value()};"

    def _serialize_value(self) -> str:
        if type(self.value) == float or type(self.value) == int: 
            return str(self.value)
        else:
            return f"[{','.join(map(str, self.value))}]"