from pydantic import BaseModel


class TodoBase(BaseModel):
    title : str
    description : str