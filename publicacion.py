from entidades.usuario import Usuario
from entidades.comentario import Comentario
from datetime import datetime

class Publicacion:

    def __init__(self, titulo: str, descripcion: str, fecha: datetime, usuario: Usuario, comentarios: list[Comentario]):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha = fecha
        self.usuario = usuario
        self.comentarios = comentarios