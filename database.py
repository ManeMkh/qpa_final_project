from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class DNA(Base):
    __tablename__ = "dna_bases"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    rna_id = Column(Integer, ForeignKey("rna_bases.id"))
    rna = relationship("RNA", back_populates="dna_bases", uselist=False)


class RNA(Base):
    __tablename__ = "rna_bases"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    dna_id = Column(Integer, ForeignKey("dna_bases.id"))
    dna = relationship("DNA", back_populates="rna_bases")

    amino_acids_id = Column(Integer, ForeignKey("amino_acids.id"))
    amino_acids = relationship("AminoAcids", back_populates="amino_acids", uselist=False)


class AminoAcids(Base):
    __tablename__ = "amino_acids"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    rna_id = Column(Integer, ForeignKey("rna_bases.id"))
    rna = relationship("RNA", back_populates="amino_acids")
    





