from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


class AnalisisRepository(Base):
    __tablename__ = 'analisis'

    id_analisis = Column(Integer, primary_key=True, index=True)
    nombre_analisis = Column(String, index=True)
    descripcion_analisis = Column(String)
    id_tipo_muestra = Column(Integer, ForeignKey('tipo_muestra.id'))
    tipo_muestra = relationship('TipoMuestra', back_populates='tipo_muestra')


class TipoMuestra(Base):
    __tablename__ = 'tipo_muestra'

    id_tipo_muestra = Column(Integer, primary_key=True)
    descripcion_tipo_muestra = Column(String)