from . import baseDto

__all__ = [
    "InfoMessage",
]


class InfoMessage(baseDto.Base):
    msg: str = "Success"