from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import json
import os
from datetime import datetime

app = FastAPI(
    title="API Gestión de Tareas"
)

# =========================
# RUTA DEL ARCHIVO JSON
# =========================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FILE_NAME = os.path.join(BASE_DIR, "tasks.json")


# =========================
# MODELOS
# =========================

class Task(BaseModel):
    titulo: str
    descripcion: str
    completado: bool = False


class TaskResponse(Task):
    id: int
    fecha_creacion: str


# =========================
# FUNCIONES AUXILIARES
# =========================

def load_tasks():

    if not os.path.exists(FILE_NAME):

        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump([], file)

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        return json.load(file)


def save_tasks(tasks):

    with open(FILE_NAME, "w", encoding="utf-8") as file:

        json.dump(
            tasks,
            file,
            indent=4,
            ensure_ascii=False
        )


# =========================
# RUTA PRINCIPAL
# =========================

@app.get("/")
def home():

    return {
        "mensaje": "API de Gestión de Tareas"
    }


# =========================
# OBTENER TODAS LAS TAREAS
# =========================

@app.get("/api/tasks", response_model=List[TaskResponse])
def get_tasks():

    return load_tasks()


# =========================
# OBTENER UNA TAREA
# =========================

@app.get("/api/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):

    tasks = load_tasks()

    for task in tasks:

        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail="Tarea no encontrada"
    )


# =========================
# CREAR TAREA
# =========================

@app.post("/api/tasks", response_model=TaskResponse)
def create_task(task: Task):

    tasks = load_tasks()

    # Generar ID único
    new_id = 1

    if tasks:
        new_id = max(task["id"] for task in tasks) + 1

    new_task = {
        "id": new_id,
        "titulo": task.titulo,
        "descripcion": task.descripcion,
        "completado": task.completado,
        "fecha_creacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    tasks.append(new_task)

    save_tasks(tasks)

    return new_task


# =========================
# ACTUALIZAR TAREA
# =========================

@app.put("/api/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, updated_task: Task):

    tasks = load_tasks()

    for task in tasks:

        if task["id"] == task_id:

            task["titulo"] = updated_task.titulo
            task["descripcion"] = updated_task.descripcion
            task["completado"] = updated_task.completado

            save_tasks(tasks)

            return task

    raise HTTPException(
        status_code=404,
        detail="Tarea no encontrada"
    )


# =========================
# ELIMINAR TAREA
# =========================

@app.delete("/api/tasks/{task_id}")
def delete_task(task_id: int):

    tasks = load_tasks()

    for task in tasks:

        if task["id"] == task_id:

            tasks.remove(task)

            save_tasks(tasks)

            return {
                "mensaje": "Tarea eliminada correctamente"
            }

    raise HTTPException(
        status_code=404,
        detail="Tarea no encontrada"
    )