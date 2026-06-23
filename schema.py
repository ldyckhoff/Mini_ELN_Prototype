# schema.py
from pydantic import BaseModel, Field
from typing import List, Dict, Union

class ProcessStep(BaseModel):
    name: str
    # additional_parameters: Dict[str, str]|None = {}

class Annealing(ProcessStep):
    temperature_c: float
    duration_min: float

class Dealloying(ProcessStep):
    temperature_c: float
    duration_min: float
    electrolyte: str
    voltage: float

class Sample(BaseModel):
    name: str
    material: str

class Experiment(BaseModel):
    name: str
    samples: List[Sample] = []
    process_steps: List[ProcessStep] = []
