from pydantic import BaseModel
from datetime import datetime



class TipoMuestra(BaseModel):
    """Clase que representa tipo muestra"""
    id_tipo_muestra:int 
    descripcion_tipo_muestra:int


class Analisis(BaseModel):
    """Esta clase representa a analisis"""
    id_analisis: int
    nombre_analisis: str
    descripcion_analisis: str
    observaciones: str 
    id_determinacion:int
    id_tipo_muestra:int

class PedidoAnalisis(BaseModel):
    """Clase que representa el pedido de un analisis"""
    id_pedido_analisis:int
    fecha:datetime
    estado:str
    numero:int
    precio_cobrado:int
    id_paciente:int
    id_medico:int
    
class Paciente(BaseModel):
    """"Esta clase modela al paciente, que seria el interesado en realizarse el analisis"""
    id_paciente:int
    documento_paciente:str
    nombre_paciente:str
    apellido_paciente:str
    direccion_paciente:str
    telefono_paciente:str
    correo_paciente:str
    
class Medido(BaseModel):
    """Clase medico, que seria el que solicita el analisis para el paciente"""
    id_medico:int
    nombre_medico:str
    apellido_medico:str
    numero_registro:str
    

class PedidoAnalisisAnalisis(BaseModel):
    """Clase que representa la relacion muchos a muchos de Analisis con su Pedido"""
    id_pedido_analisis_analisis:int
    id_analisis:int
    id_resultado:int
    
    
class Resultado(BaseModel):
    """Clase donde va los resultados del pedido de analisis"""
    id_resultado:int 
    id_pedido_analisis:int 
    id_analisis:int
    id_resultado_determinacion_analisis:int
    
class ResultadoDeterminacionAnalisis(BaseModel):
    """Clase resultado de determinacion asociado a un analisis"""
    id_resultado_determinacion_analkisis:int
    resultado_valor:str
    id_determinacion:int
    id_analisis:int
    
    
    
class Determinaciones(BaseModel):
    """Esta clase representa la determinacion que pueda pertenecer a cada analisis,
    es importante recordar que puede haber determinaciones que compartan 2 analisis
    diferentes"""
    id_determinacion: int
    nombre_determinacion: str
    descripcion_determinacion: str
    limite_inferior: int
    limite_superior: int
    valor_referencia: str
    id_unidad_medida: int
    id_metodo: int


class AnalisisDeterminaciones(BaseModel):
    """Clase para las relaciones muchos a muchos entre analisis y determinaciones"""
    id_analisis_determinacion: int
    id_analisis: int
    id_determinacion: int
    

class UnidadMedida(BaseModel):
    """Clase para la unidad de medida de cada determinacion"""
    id_unidad_medida:int
    nombre_unidad:str
    abreviacion_unidad:str
    
    
class Metodo(BaseModel):
    """Clase para el metodo en que se realiza cada determinacion"""
    id_metodo:int
    nombre_metodo:str 


class EquiposLaboratorio(BaseModel):
    """Clase para equipos de laboratorio"""
    id_equipo_laboratorio:int 
    nombre_equipo:int 
    marca_equipo:int 
    id_tipo_conexion:int 


class TipoConexionEquipo(BaseModel):
    """Clase para tipo conexion"""
    id_tipo_conexion_equipo:int 
    descripcion_conexion:str 
    
