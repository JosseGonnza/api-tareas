from pydantic import BaseModel, Field


class TareaCrear(BaseModel):
    titulo: str = Field(min_length=1, max_length=100)
    descripcion: str | None = Field(default=None, max_length=500)
    completada: bool = False


class Tarea(TareaCrear):
    id: int
