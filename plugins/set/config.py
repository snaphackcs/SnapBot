from pydantic import BaseModel, Extra


class Config(BaseModel, extra=Extra.ignore):
    subcommands = {
        "-n" : "name",
        "--name" : "name",
    }
