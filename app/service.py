from app.schemas import Tarea, TareaCrear


class TareaService:
    def __init__(self):
        self._tareas: dict[int, Tarea] = {}
        self._siguiente_id = 1

    def listar(self) -> list[Tarea]:
        return list(self._tareas.values())

    def obtener(self, tarea_id: int) -> Tarea | None:
        return self._tareas.get(tarea_id)

    def crear(self, datos: TareaCrear) -> Tarea:
        tarea = Tarea(id=self._siguiente_id, **datos.model_dump())
        self._tareas[tarea.id] = tarea
        self._siguiente_id += 1
        return tarea
