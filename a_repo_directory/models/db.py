from dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str
    age: int


@dataclass
class Pet:
    owner: User
    name: str
    age: int
