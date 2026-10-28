from fastapi import APIRouter, HTTPException, status

from app.schemas import Tarea, TareaCrear
from app.service import TareaService

router = APIRouter(prefix="/tareas", tags=["tareas"])
servicio = TareaService()


@router.get("")
async def listar_tareas() -> list[Tarea]:
    return servicio.listar()


@router.post("", status_code=status.HTTP_201_CREATED)
async def crear_tarea(datos: TareaCrear) -> Tarea:
    return servicio.crear(datos)


@router.get("/{tarea_id}")
async def obtener_tarea(tarea_id: int) -> Tarea:
    tarea = servicio.obtener(tarea_id)
    if tarea is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarea no encontrada",
        )
    return tarea
