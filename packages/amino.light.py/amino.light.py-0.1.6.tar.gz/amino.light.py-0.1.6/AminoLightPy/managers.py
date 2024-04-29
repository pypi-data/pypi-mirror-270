from typing import Union
from . import SubClient, Client

class Typing():
    def __init__(self, context: Union[Client, SubClient]) -> None:
        self.profile = context.profile