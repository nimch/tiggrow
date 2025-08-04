from datetime import date, time
from enum import Enum
from typing import List, Optional
from uuid import UUID, uuid4

from sqlmodel import Column, Field, Relationship, SQLModel, String, Text


# Common base model for the Encounter resource.
# Defines shared fields used by both the database and form models.
class EncounterBase(SQLModel):
    encounter_date: date
    encounter_time: time
    invitation: str = Field(
        sa_column=Column(Text), min_length=10
    )  # Column(Text) affects PostgreSQL (not SQLite); min_length is enforced by Pydantic.
    venue: str = Field(
        sa_column=Column(String(100))
    )  # Column(String(100)) affects PostgreSQL (not SQLite).


# Database model for the Encounter resource.
# Inherits from EncounterBase and represents the actual table, including relationships.
class Encounter(EncounterBase, table=True):
    uuid: UUID = Field(default_factory=uuid4, primary_key=True)
    pets: List["Pet"] = Relationship(
        back_populates="encounter"
    )  # Defines ORM relationship: encounter.pets returns associated Pet objects.
    persons: List["Person"] = Relationship(
        back_populates="encounter"
    )  # Defines ORM relationship: encounter.persons returns associated Person objects.


# Form model for the Party resource.
# Used by FastAPI to validate and process incoming form data for Party operations.
class EncounterForm(EncounterBase):
    pass


# Define pets types
class PetType(Enum):
    DOG = "Dog"
    CAT = "Cat"
    OTHER = "Other"


# Common base model for the Pet resource.
# Contains shared fields used by both the database and form models.
class PetBase(SQLModel):
    pet_name: str = Field(sa_column=Column(String(100)))
    pet_type: PetType
    link: Optional[str]
    encounter_id: UUID = Field(
        default=None, foreign_key="encounter.uuid"
    )  # Defines a foreign key connecting the pet to a encounter at the database level.


# Database model for the Pet resource.
# Inherits from PetBase and represents the pet table, including its relationship to Encounter.
class Pet(PetBase, table=True):
    uuid: UUID = Field(default_factory=uuid4, primary_key=True)
    encounter: Encounter = Relationship(
        back_populates="pets"
    )  # Defines ORM relationship: gift.party returns the associated Party object.


# Form model for the Pet resource.
# Used for validating and processing incoming pet data via FastAPI.
class PetForm(PetBase):
    pass


# Common base model for the Person resource.
# Defines shared fields used by both the database and form models.
class PersonBase(SQLModel):
    name: str = Field(sa_column=Column(String(100)))
    attending: bool = False
    encounter_id: UUID = Field(
        default=None, foreign_key="encounter.uuid"
    )  # Defines a foreign key connecting the person to an encounter at the database level.


# Database model for the Person resource.
# Inherits from PersonBase and maps to the person table, including its relationship to Encounter.
class Person(PersonBase, table=True):
    uuid: UUID = Field(default_factory=uuid4, primary_key=True)
    encounter: Encounter = Relationship(
        back_populates="persons"
    )  # Establishes ORM relationship: person.encounter returns the associated Encounter object.


# Form model for the Person resource.
# Used by FastAPI for validating and processing incoming guest data.
class PersonForm(PersonBase):
    pass
