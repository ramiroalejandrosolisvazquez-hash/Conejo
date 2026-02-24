from entidades.usuario import Usuario
from datetime import datetime

class Comentario:

    def __init__ (self, contenido:str, likes: int, dislikes: int, usuario: Usuario, fecha: datetime):
        self.contenido = contenido
        self.like = likes
        self.dislikes = dislikes
        self.usuario = usuario
        self.fecha = fecha