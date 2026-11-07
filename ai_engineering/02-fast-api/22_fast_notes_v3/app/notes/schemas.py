from pydantic import BaseModel, ConfigDict


# Note Base Model
class NoteBase(BaseModel):
    title: str
    content: str

# Note Create Model
class NoteCreate(NoteBase):
    pass

# Note Response Model
class NoteResponse(NoteBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


# Note Partial Update Model
class NotePartialUpdate(BaseModel):
    title: str | None = None
    content: str | None = None

# Note Update Model
class NoteUpdate(NoteBase):
    pass

# Note Delete Response Model
class NoteDeleteResponse(BaseModel):
    message: str
