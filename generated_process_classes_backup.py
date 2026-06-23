from typing import List, Dict, Optional, Union
from pydantic import BaseModel, Field

class ProcessBase(BaseModel):
    """Base class for all process metadata schemas."""
    pass

# --- Base Classes for Categories ---

class CleaningProcess(ProcessBase):
    '''
    Category for processes involving surface cleaning and removal of contaminants.
    '''
    pass

class SurfaceTreatmentProcess(ProcessBase):
    '''
    Category for processes involving surface modification or treatment.
    '''
    pass

class HeatTreatmentProcess(ProcessBase):
    '''
    Category for processes involving thermal treatment.
    '''
    pass

class ThinFilmDepositionProcess(ProcessBase):
    '''
    Category for processes involving film growth on substrates.
    '''
    pass

class AlloyPreparationProcess(ProcessBase):
    '''
    Category for processes involving alloy fabrication.
    '''
    pass

class DealloyingProcess(ProcessBase):
    '''
    Category for processes involving selective dissolution to form porous structures.
    '''
    pass

class MechanicalProcessingProcess(ProcessBase):
    '''
    Category for processes involving mechanical deformation or shaping.
    '''
    pass

class PostProcessingProcess(ProcessBase):
    '''
    Category for processes involving post-fabrication steps.
    '''
    pass

class PrecursorFabricationProcess(ProcessBase):
    '''
    Category for processes involving precursor or slurry preparation.
    '''
    pass

class MechanicalAlloyingProcess(ProcessBase):
    '''
    Category for processes involving mechanical alloying.
    '''
    pass

class CastingProcess(ProcessBase):
    '''
    Category for processes involving casting and shaping.
    '''
    pass

class SurfaceFinishingProcess(ProcessBase):
    '''
    Category for processes involving surface finishing.
    '''
    pass

class ElectrodeAssemblyProcess(ProcessBase):
    '''
    Category for processes involving electrode or sensor assembly.
    '''
    pass

class ElectrochemicalCharacterizationProcess(ProcessBase):
    '''
    Category for processes involving electrochemical characterization.
    '''
    pass

class PatterningProcess(ProcessBase):
    '''
    Category for processes involving lithography and patterning.
    '''
    pass

class ThermalTreatmentProcess(ProcessBase):
    '''
    Category for processes involving general thermal treatment.
    '''
    pass

class SurfaceCoatingProcess(ProcessBase):
    '''
    Category for processes involving surface coating.
    '''
    pass

class FilmFabricationProcess(ProcessBase):
    '''
    Category for processes involving general film fabrication.
    '''
    pass

class RapidSolidificationProcess(ProcessBase):
    '''
    Category for processes involving rapid solidification.
    '''
    pass

class DispersionPreparationProcess(ProcessBase):
    '''
    Category for processes involving dispersion preparation.
    '''
    pass

class PrecursorPreparationProcess(ProcessBase):
    '''
    Category for processes involving precursor preparation.
    '''
    pass

class SensorAssemblyProcess(ProcessBase):
    '''
    Category for processes involving sensor assembly.
    '''
    pass

class SamplePreparationProcess(ProcessBase):
    '''
    Category for processes involving sample preparation.
    '''
    pass

class FabricationProcess(ProcessBase):
    '''
    Category for processes involving fabrication.
    '''
    pass

# --- Process Classes ---

# cluster_0
class MechanicalCleaning(CleaningProcess):
    '''
    Physical removal of surface contaminants or oxides using non-electrochemical mechanical means.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Physical removal of surface contaminants or oxides using non-electrochemical mechanical means.",
        json_schema_extra={"synonyms": ["Abrasive Cleaning", "Oxide Removal (Mechanical)"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    input_state: str | None = Field(
        None,
        description="Description of the physical state of the sample before the cleaning step is initiated.",
        json_schema_extra={"example_values": ["oxide covered"], "required": "optional"},
    )
    cleaning_method: str | None = Field(
        None,
        description="The specific physical mechanism used to perform the cleaning or removal of material.",
        json_schema_extra={"example_values": ["Mechanical"], "required": "optional"},
    )

class ElectrochemicalCleaning(CleaningProcess):
    '''
    Removal of oxides or contaminants from the sample surface via cycling the electrochemical potential.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Removal of oxides or contaminants from the sample surface via cycling the electrochemical potential.",
        json_schema_extra={"synonyms": ["Electrolytic Cleaning", "Potential Cycling Cleaning", "Electrochemical Oxide Removal"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    number_of_cycles: str | None = Field(
        None,
        description="The number of potential cycles executed during the electrochemical cleaning procedure.",
        json_schema_extra={"example_values": ["3", "5"], "required": "optional"},
    )
    potential_range: str | None = Field(
        None,
        description="The voltage window applied during the electrochemical cleaning cycles.",
        json_schema_extra={"example_values": ["-0.5 V to 0.5 V"], "required": "optional"},
    )
    scan_rate: str | None = Field(
        None,
        description="The speed of the potential sweep during the electrochemical process.",
        json_schema_extra={"example_values": ["10 mV/s"], "required": "optional"},
    )
    scan_rate_unit: str | None = Field(
        None,
        description="The unit of measurement for the scan rate parameter.",
        json_schema_extra={"example_values": ["V/s", "mV/s"], "required": "optional"},
    )

# cluster_1
class Sputtering(ThinFilmDepositionProcess):
    '''
    Physical vapor deposition process where material is sputtered from a target onto a substrate using plasma or inert gas bombardment.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Physical vapor deposition process where material is sputtered from a target onto a substrate using plasma or inert gas bombardment.",
        json_schema_extra={"synonyms": ["Magnetron Sputtering", "Physical Vapor Deposition", "PVD", "Ion Beam Sputtering"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    deposition_method: str | None = Field(
        None,
        description="The specific physical technique used for material deposition.",
        json_schema_extra={"example_values": ["magnetron co-sputtering", "sequential sputtering", "magnetron sputtering system"], "required": "usually_required"},
    )
    deposited_material: str | None = Field(
        None,
        description="The elemental or alloy composition of the deposited film.",
        json_schema_extra={"example_values": ["Ta", "Pd", "Au", "Ag", "Au-Ag", "PdNi"], "required": "usually_required"},
    )
    film_thickness: str | None = Field(
        None,
        description="The thickness of the deposited metal layer.",
        json_schema_extra={"example_values": ["18/22/25 at % Pd", "100 nm", "variable"], "required": "optional"},
    )
    substrate: str | None = Field(
        None,
        description="The material type and orientation of the substrate used.",
        json_schema_extra={"example_values": ["Si", "polyimide", "nanoporous bulk materials"], "required": "usually_required"},
    )
    vacuum_pressure: str | None = Field(
        None,
        description="The base vacuum pressure of the sputtering chamber.",
        json_schema_extra={"example_values": ["base pressure", "low vacuum"], "required": "optional"},
    )
    temperature: str | None = Field(
        None,
        description="The temperature condition during deposition.",
        json_schema_extra={"example_values": ["room temperature", "heated"], "required": "optional"},
    )
    equipment: str | None = Field(
        None,
        description="The equipment used to perform the deposition.",
        json_schema_extra={"example_values": ["Sputtering system", "Magnetron sputtering system"], "required": "optional"},
    )
    plasma_gas: str | None = Field(
        None,
        description="The gas used to generate the plasma for sputtering.",
        json_schema_extra={"example_values": ["Ar", "Argon"], "required": "optional"},
    )
    biasing_power: str | None = Field(
        None,
        description="The RF power or biasing applied during sputtering.",
        json_schema_extra={"example_values": ["RF power", "50 W"], "required": "optional"},
    )
    target_purity: str | None = Field(
        None,
        description="The purity level of the sputtering targets.",
        json_schema_extra={"example_values": ["99.99%"], "required": "optional"},
    )

class AtomicLayerDeposition(ThinFilmDepositionProcess):
    '''
    Cyclic vapor deposition technique that forms a thin film layer by layer through self-limiting surface reactions.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Cyclic vapor deposition technique that forms a thin film layer by layer through self-limiting surface reactions.",
        json_schema_extra={"synonyms": ["ALD", "Chemical Vapor Deposition (specific)"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    deposition_method: str | None = Field(
        None,
        description="The technique used for film growth (e.g., ALD, CVD).",
        json_schema_extra={"example_values": ["atomic layer deposition", "self-limiting surface reactions"], "required": "usually_required"},
    )
    film_thickness: str | None = Field(
        None,
        description="Thickness of the film grown via ALD.",
        json_schema_extra={"example_values": ["10 nm", "variable"], "required": "optional"},
    )
    substrate: str | None = Field(
        None,
        description="The material of the substrate for ALD.",
        json_schema_extra={"example_values": ["nanoporous bulk materials", "CAs"], "required": "usually_required"},
    )
    cycles: str | None = Field(
        None,
        description="The number of deposition cycles performed in ALD.",
        json_schema_extra={"example_values": ["100 cycles", "50 cycles"], "required": "optional"},
    )
    reactor_type: str | None = Field(
        None,
        description="The type of reactor used for ALD.",
        json_schema_extra={"example_values": ["continuous flow reactor", "batch reactor"], "required": "optional"},
    )
    cleaning_steps: str | None = Field(
        None,
        description="Cleaning or purge steps between ALD cycles.",
        json_schema_extra={"example_values": ["eliminated due to volatile co-products", "oxidation pulse"], "required": "optional"},
    )

# cluster_2
class Annealing(HeatTreatmentProcess):
    '''
    Thermal treatment applied to dealloyed or porous metal samples to modify microstructure, induce coarsening, or recover the sample structure.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Thermal treatment applied to dealloyed or porous metal samples to modify microstructure, induce coarsening, or recover the sample structure.",
        json_schema_extra={"synonyms": ["Thermal annealing", "Heat treatment", "Coarsening Annealing"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    temperature: str | None = Field(
        None,
        description="Temperature setpoint or range for the thermal treatment.",
        json_schema_extra={"example_values": ["773 K", "Range of annealing temperatures"], "required": "usually_required"},
    )
    temperature_unit: str | None = Field(
        None,
        description="Unit of temperature used for the process parameter.",
        json_schema_extra={"example_values": ["\u00b0C", "K"], "required": "optional"},
    )
    atmosphere: str | None = Field(
        None,
        description="Atmosphere or gas environment during the thermal treatment.",
        json_schema_extra={"example_values": ["Argon", "Vacuum", "Air", "Ar"], "required": "usually_required"},
    )
    duration: str | None = Field(
        None,
        description="Time duration for which the thermal treatment is applied.",
        json_schema_extra={"example_values": ["varying", "overnight"], "required": "optional"},
    )
    equipment: str | None = Field(
        None,
        description="Equipment used to perform the thermal treatment.",
        json_schema_extra={"example_values": ["Furnace"], "required": "optional"},
    )
    purpose: str | None = Field(
        None,
        description="Intended outcome of the thermal treatment.",
        json_schema_extra={"example_values": ["feature size control", "coarsening", "recovery", "modify microstructure"], "required": "optional"},
    )
    input_state: str | None = Field(
        None,
        description="State of the sample before the thermal treatment.",
        json_schema_extra={"example_values": ["as-fabricated", "dealloyed sample"], "required": "optional"},
    )
    output_state: str | None = Field(
        None,
        description="State of the sample after the thermal treatment.",
        json_schema_extra={"example_values": ["coarsened"], "required": "optional"},
    )
    heating_rate: str | None = Field(
        None,
        description="Rate at which the temperature is increased.",
        json_schema_extra={"example_values": ["not specified"], "required": "optional"},
    )
    cooling_method: str | None = Field(
        None,
        description="Method used to cool the sample after heating.",
        json_schema_extra={"example_values": ["not specified"], "required": "optional"},
    )
    container: str | None = Field(
        None,
        description="Material of the container inside the furnace.",
        json_schema_extra={"example_values": ["not specified"], "required": "optional"},
    )

class MeltSpinning(AlloyPreparationProcess):
    '''
    Physical process to solidify molten alloy into thin ribbon strips, typically used to prepare precursor material for subsequent nanoporous fabrication.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Physical process to solidify molten alloy into thin ribbon strips, typically used to prepare precursor material for subsequent nanoporous fabrication.",
        json_schema_extra={"synonyms": ["Alloy preparation", "Ribbons preparation"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    alloy_composition: str | None = Field(
        None,
        description="Chemical composition of the alloy being spun.",
        json_schema_extra={"example_values": ["Al80Pd20"], "required": "usually_required"},
    )
    output_geometry: str | None = Field(
        None,
        description="Geometric form of the material produced by the spinning process.",
        json_schema_extra={"example_values": ["ribbons"], "required": "usually_required"},
    )
    equipment: str | None = Field(
        None,
        description="Equipment used for the spinning process.",
        json_schema_extra={"example_values": ["not specified"], "required": "optional"},
    )

# cluster_3
class SampleCleaning(FabricationProcess):
    '''
    Removal of residual electrolytes, acids, organic contaminants, or oxides from the sample surface using a liquid medium, typically performed after dealloying or prior to deposition.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Removal of residual electrolytes, acids, organic contaminants, or oxides from the sample surface using a liquid medium, typically performed after dealloying or prior to deposition.",
        json_schema_extra={"synonyms": ["Rinsing", "Substrate Cleaning", "Washing", "Soaking", "Ethanol Cleaning"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    cleaning_medium: str | None = Field(
        None,
        description="Liquid medium used for cleaning, rinsing, or soaking the sample.",
        json_schema_extra={"example_values": ["DI water", "ethanol", "ultrapure water", "distilled water"], "required": "usually_required"},
    )
    duration: str | None = Field(
        None,
        description="Time duration of the cleaning/rinsing step.",
        json_schema_extra={"example_values": ["10 min", "overnight", "extended period"], "required": "optional"},
    )
    cleaning_method: str | None = Field(
        None,
        description="Methodology used for cleaning (e.g., boiling, frequency of rinsing).",
        json_schema_extra={"example_values": ["boiling", "ultrasound", "ambient", "room temperature"], "required": "optional"},
    )
    sample_state: str | None = Field(
        None,
        description="State of the sample before and after the cleaning process.",
        json_schema_extra={"example_values": ["as-dealloyed", "cleaned", "prior to testing"], "required": "optional"},
    )

class SampleDrying(PostProcessingProcess):
    '''
    Removal of residual liquid solvent from the sample surface using air flow, vacuum, or inert gas atmosphere after rinsing or cleaning.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Removal of residual liquid solvent from the sample surface using air flow, vacuum, or inert gas atmosphere after rinsing or cleaning.",
        json_schema_extra={"synonyms": ["Air Drying", "Vacuum Drying", "Dehydration"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    drying_atmosphere: str | None = Field(
        None,
        description="Environment used to dry the sample (air, gas, or pressure).",
        json_schema_extra={"example_values": ["air", "argon", "vacuum"], "required": "optional"},
    )
    duration: str | None = Field(
        None,
        description="Duration of the drying process.",
        json_schema_extra={"example_values": ["variable"], "required": "optional"},
    )
    drying_temperature: str | None = Field(
        None,
        description="Temperature applied during drying.",
        json_schema_extra={"example_values": ["room temperature", "heat treatment"], "required": "optional"},
    )
    drying_equipment: str | None = Field(
        None,
        description="Equipment used for drying.",
        json_schema_extra={"example_values": ["vacuum chamber", "oven"], "required": "optional"},
    )

# cluster_4
class Homogenization(HeatTreatmentProcess):
    '''
    Thermal treatment applied at high temperature for an extended duration to ensure uniform alloy composition and prevent undesirable phase segregation.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Thermal treatment applied at high temperature for an extended duration to ensure uniform alloy composition and prevent undesirable phase segregation.",
        json_schema_extra={"synonyms": ["Homogenization Annealing", "Homogenization", "Alloy Homogenization"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    temperature: str | None = Field(
        None,
        description="Applied temperature during the thermal treatment.",
        json_schema_extra={"example_values": ["1223 Kelvin", "850", "800 degrees Celsius"], "required": "required"},
    )
    duration: str | None = Field(
        None,
        description="Time length of the heat treatment step.",
        json_schema_extra={"example_values": ["100", "1 hour", "70 hours"], "required": "optional"},
    )
    atmosphere: str | None = Field(
        None,
        description="Environment or gas composition during heat treatment.",
        json_schema_extra={"example_values": ["Quartz sealed environment", "Ambient", "null"], "required": "optional"},
    )
    sealing_material: str | None = Field(
        None,
        description="Material used to seal the sample during processing (furnace sealed).",
        json_schema_extra={"example_values": ["Material used to seal the sample"], "required": "optional"},
    )
    input_state: str | None = Field(
        None,
        description="Material condition prior to the homogenization step.",
        json_schema_extra={"example_values": ["State of the material before treatment"], "required": "optional"},
    )
    output_state: str | None = Field(
        None,
        description="Material condition after the homogenization step.",
        json_schema_extra={"example_values": ["State of the material after treatment"], "required": "optional"},
    )

class WaterQuenching(HeatTreatmentProcess):
    '''
    Rapid cooling of a material, typically using water, immediately following heat treatment to lock in microstructure properties.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Rapid cooling of a material, typically using water, immediately following heat treatment to lock in microstructure properties.",
        json_schema_extra={"synonyms": ["Quenching", "Water Quench"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    quenching_medium: str | None = Field(
        None,
        description="Liquid medium used for the quenching step.",
        json_schema_extra={"example_values": ["Water"], "required": "optional"},
    )
    temperature: str | None = Field(
        None,
        description="Temperature prior to quenching (inferred).",
        json_schema_extra={"example_values": ["Treatment temperature"], "required": "optional"},
    )
    duration: str | None = Field(
        None,
        description="Duration of the quenching process.",
        json_schema_extra={"example_values": ["Duration of the process"], "required": "optional"},
    )
    atmosphere: str | None = Field(
        None,
        description="Environment during the quenching process.",
        json_schema_extra={"example_values": ["Ambient"], "required": "optional"},
    )

# cluster_5
class ElectrochemicalDealloying(DealloyingProcess):
    '''
    Selective dissolution of a less noble phase from an alloy under potentiostatic or galvanostatic potential control in an electrolyte solution to form a nanoporous structure.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Selective dissolution of a less noble phase from an alloy under potentiostatic or galvanostatic potential control in an electrolyte solution to form a nanoporous structure.",
        json_schema_extra={"synonyms": ["Electrochemical Etching", "Anodic Dealloying", "Potential Controlled Dealloying"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    electrolyte_formula: str | None = Field(
        None,
        description="Chemical formula of the solution used during the dealloying process.",
        json_schema_extra={"example_values": ["HClO4", "HNO3", "HCl", "NaOH"], "required": "usually_required"},
    )
    electrolyte_concentration: str | None = Field(
        None,
        description="Concentration of the electrolyte solution.",
        json_schema_extra={"example_values": ["1 M", "70%", "concentrated", "diluted"], "required": "usually_required"},
    )
    electrolyte_type: str | None = Field(
        None,
        description="General type of electrolyte environment.",
        json_schema_extra={"example_values": ["aqueous", "alkaline", "acidic", "NaOH"], "required": "optional"},
    )
    potential: str | None = Field(
        None,
        description="Applied potential range or value during electrochemical dealloying.",
        json_schema_extra={"example_values": ["1.0 V", "650 mV", "0.8 V"], "required": "optional"},
    )
    duration: str | None = Field(
        None,
        description="Total time or time at specific potential for the dealloying step.",
        json_schema_extra={"example_values": ["17 h", "overnight", "10 min"], "required": "optional"},
    )
    temperature: str | None = Field(
        None,
        description="Temperature at which the dealloying process is performed.",
        json_schema_extra={"example_values": ["330 K", "room temperature", "60 C"], "required": "optional"},
    )
    control_mode: str | None = Field(
        None,
        description="The control mode applied to the electrochemical or corrosion process.",
        json_schema_extra={"example_values": ["potentiostatic", "galvanostatic", "free corrosion"], "required": "optional"},
    )
    reference_electrode: str | None = Field(
        None,
        description="Type or model of reference electrode used in the cell.",
        json_schema_extra={"example_values": ["Ag/AgCl", "SCE", "null"], "required": "optional"},
    )
    counter_electrode: str | None = Field(
        None,
        description="Material and type of counter electrode in the electrochemical cell.",
        json_schema_extra={"example_values": ["Platinum wire", "Silver wire", "Pt"], "required": "optional"},
    )

class ChemicalDealloying(DealloyingProcess):
    '''
    Selective dissolution of a less noble phase from an alloy under open-circuit or free corrosion conditions in a corrosive electrolyte solution without applied potential control.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Selective dissolution of a less noble phase from an alloy under open-circuit or free corrosion conditions in a corrosive electrolyte solution without applied potential control.",
        json_schema_extra={"synonyms": ["Free Corrosion Dealloying", "Chemical Etching", "Acid Dealloying"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    electrolyte_formula: str | None = Field(
        None,
        description="Chemical formula of the solution used during the dealloying process.",
        json_schema_extra={"example_values": ["HCl", "HNO3", "NaOH", "H2SO4"], "required": "usually_required"},
    )
    electrolyte_concentration: str | None = Field(
        None,
        description="Concentration of the electrolyte solution.",
        json_schema_extra={"example_values": ["concentrated", "diluted", "25%", "1 M"], "required": "usually_required"},
    )
    duration: str | None = Field(
        None,
        description="Total time or time criterion for the dealloying process.",
        json_schema_extra={"example_values": ["overnight", "10 min", "until stopping condition"], "required": "optional"},
    )
    temperature: str | None = Field(
        None,
        description="Temperature at which the dealloying process is performed.",
        json_schema_extra={"example_values": ["room temperature", "60 C"], "required": "optional"},
    )
    surfactant: str | None = Field(
        None,
        description="Surfactants added to the electrolyte to prevent pore clogging.",
        json_schema_extra={"example_values": ["CTAB", "none"], "required": "optional"},
    )
    ultrasonic_agitation: str | None = Field(
        None,
        description="Whether ultrasonic agitation was applied during the process.",
        json_schema_extra={"example_values": ["yes", "no"], "required": "optional"},
    )

# cluster_6
class Cutting(MechanicalProcessingProcess):
    '''
    Mechanical process to separate or shape a material into smaller pieces or specific geometries.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Mechanical process to separate or shape a material into smaller pieces or specific geometries.",
        json_schema_extra={"synonyms": ["Sample Cutting", "Wire Cutting", "Slicing", "Shaping"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    cut_dimensions: str | None = Field(
        None,
        description="The resulting geometry or dimensions of the sample after the cutting step.",
        json_schema_extra={"example_values": ["1 x 1 x 2 mm3", "Plates", "Disk", "Cuboids", "~4 mm"], "required": "usually_required"},
    )
    input_material: str | None = Field(
        None,
        description="The chemical composition or material identity of the sample being cut.",
        json_schema_extra={"example_values": ["AuâAg alloy", "precursor bulk alloy", "rolled alloy"], "required": "optional"},
    )
    sample_state: str | None = Field(
        None,
        description="The physical state of the sample before cutting (e.g., bulk ingot, pellets, or nanoporous film).",
        json_schema_extra={"example_values": ["Homogenized ingot", "Bulk alloy pellets", "Nanoporous samples", "Rolled alloy"], "required": "optional"},
    )
    tool: str | None = Field(
        None,
        description="The equipment or tool used to perform the cutting operation.",
        json_schema_extra={"example_values": ["Diamond wire saw", "Electric discharge machining", "Grinding tool"], "required": "optional"},
    )
    target_surface: str | None = Field(
        None,
        description="The desired surface quality of the cut sample.",
        json_schema_extra={"example_values": ["smooth surface finish"], "required": "optional"},
    )
    cut_quantity: str | None = Field(
        None,
        description="The quantity or number of pieces resulting from the cutting step.",
        json_schema_extra={"example_values": ["multiple"], "required": "optional"},
    )

# cluster_7
class MechanicalShaping(MechanicalProcessingProcess):
    '''
    Mechanical reduction of bulk alloy into specific sample geometries (e.g., cylindrical wires) via techniques such as wire drawing, cutting, or sectioning.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Mechanical reduction of bulk alloy into specific sample geometries (e.g., cylindrical wires) via techniques such as wire drawing, cutting, or sectioning.",
        json_schema_extra={"synonyms": ["Mechanical Processing", "Wire Drawing", "Machining", "Sample Forming", "Sample Preparation"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    sample_dimensions: str | None = Field(
        None,
        description="Target dimensions of the processed sample (diameter, length).",
        json_schema_extra={"example_values": ["mm-size"], "required": "optional"},
    )
    sample_geometry: str | None = Field(
        None,
        description="Shape of the sample after shaping.",
        json_schema_extra={"example_values": ["cylindrical"], "required": "optional"},
    )
    tool: str | None = Field(
        None,
        description="Type of mechanical tool used for the shaping operation.",
        json_schema_extra={"example_values": ["mechanical tool"], "required": "optional"},
    )
    method: str | None = Field(
        None,
        description="Specific mechanical method used for shaping (drawing, cutting, sectioning).",
        json_schema_extra={"example_values": ["wire drawing", "cutting", "sectioning"], "required": "optional"},
    )

# cluster_8
class Ultramicrotomy(MechanicalProcessingProcess):
    '''
    Process of cutting samples into ultra-thin slices for transmission electron microscopy (TEM) analysis using an ultramicrotome.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Process of cutting samples into ultra-thin slices for transmission electron microscopy (TEM) analysis using an ultramicrotome.",
        json_schema_extra={"synonyms": ["Thin Sectioning", "Sample Cutting for TEM", "Ultramicrotomy"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    equipment: str | None = Field(
        None,
        description="The specific instrument or tool used to perform the cutting operation.",
        json_schema_extra={"example_values": [], "required": "usually_required"},
    )
    slice_thickness: str | None = Field(
        None,
        description="The nominal thickness of the individual specimen slices produced.",
        json_schema_extra={"example_values": [], "required": "optional"},
    )
    cutting_speed: str | None = Field(
        None,
        description="The speed at which the ultramicrotome knife cuts through the sample.",
        json_schema_extra={"example_values": [], "required": "optional"},
    )
    cutting_speed_unit: str | None = Field(
        None,
        description="The unit of measurement used to specify the cutting speed.",
        json_schema_extra={"example_values": [], "required": "optional"},
    )

# cluster_9
class FreeCorrosionDealloying(DealloyingProcess):
    '''
    Dealloying process performed under open-circuit conditions without applied electrochemical potential, relying on spontaneous corrosion in electrolyte.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Dealloying process performed under open-circuit conditions without applied electrochemical potential, relying on spontaneous corrosion in electrolyte.",
        json_schema_extra={"synonyms": ["Free corrosion", "Immersion dealloying", "OCP dealloying", "Spontaneous dealloying"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    electrolyte_concentration: str | None = Field(
        None,
        description="Chemical formula and concentration of the electrolyte used during immersion.",
        json_schema_extra={"example_values": ["DI water", "concentrated nitric acid"], "required": "usually_required"},
    )
    duration: str | None = Field(
        None,
        description="Time for which the dealloying step is performed.",
        json_schema_extra={"example_values": ["10 min", "overnight"], "required": "usually_required"},
    )
    temperature: str | None = Field(
        None,
        description="Process temperature for the immersion step.",
        json_schema_extra={"example_values": ["room temperature"], "required": "optional"},
    )

class PotentiostaticDealloying(DealloyingProcess):
    '''
    Dealloying process performed under a controlled applied potential (potentiostatic or holding step) to selectively remove specific alloy elements.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Dealloying process performed under a controlled applied potential (potentiostatic or holding step) to selectively remove specific alloy elements.",
        json_schema_extra={"synonyms": ["Controlled potential dealloying", "Holding potential dealloying", "Potentiostatic removal", "Route B dealloying"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    potential: str | None = Field(
        None,
        description="Applied electrochemical potential during the dealloying step.",
        json_schema_extra={"example_values": ["-0.5 V"], "required": "usually_required"},
    )
    reference_electrode: str | None = Field(
        None,
        description="Reference electrode used for potential control.",
        json_schema_extra={"example_values": ["Ag/AgCl"], "required": "optional"},
    )
    electrolyte_concentration: str | None = Field(
        None,
        description="Electrolyte composition and concentration used during the process.",
        json_schema_extra={"example_values": ["concentrated nitric acid"], "required": "usually_required"},
    )
    duration: str | None = Field(
        None,
        description="Duration of the holding or dealloying step.",
        json_schema_extra={"example_values": ["10 min"], "required": "usually_required"},
    )

# cluster_10
class MasterAlloyPreparation(AlloyPreparationProcess):
    '''
    Process involving the melting of constituent elemental materials to form a homogeneous master alloy ingot, typically used as a precursor for nanoporous metal fabrication.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Process involving the melting of constituent elemental materials to form a homogeneous master alloy ingot, typically used as a precursor for nanoporous metal fabrication.",
        json_schema_extra={"synonyms": ["Alloy Synthesis", "Alloy Preparation", "Melting"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    input_material: str | None = Field(
        None,
        description="List of elemental materials used to form the alloy.",
        json_schema_extra={"example_values": ["Al, Au", "Au, Ag", "Cu and Pd", "Ni, Pd"], "required": "required"},
    )
    alloy_composition: str | None = Field(
        None,
        description="Composition or atomic ratio of the resulting alloy.",
        json_schema_extra={"example_values": ["Ni-Pd", "Ag75Au25", "Atomic ratio"], "required": "optional"},
    )
    input_material_purity: str | None = Field(
        None,
        description="Purity level of the input elemental materials.",
        json_schema_extra={"example_values": ["High purity", "Pure", "99.99%"], "required": "optional"},
    )
    equipment: str | None = Field(
        None,
        description="Melting equipment used for the synthesis.",
        json_schema_extra={"example_values": ["Arc melter", "Induction furnace", "Electron beam"], "required": "required"},
    )
    crucible_material: str | None = Field(
        None,
        description="Material used for the container holding the melt.",
        json_schema_extra={"example_values": ["Quartz", "Crucible"], "required": "optional"},
    )
    atmosphere: str | None = Field(
        None,
        description="Gas atmosphere used during the melting process.",
        json_schema_extra={"example_values": ["Inert", "Argon"], "required": "optional"},
    )
    temperature: str | None = Field(
        None,
        description="Operating temperature of the melting process.",
        json_schema_extra={"example_values": ["Melting temperature"], "required": "optional"},
    )
    duration: str | None = Field(
        None,
        description="Duration of the melting process.",
        json_schema_extra={"example_values": ["Melting duration", "overnight"], "required": "optional"},
    )
    input_state: str | None = Field(
        None,
        description="Physical state of the input materials before melting.",
        json_schema_extra={"example_values": ["Constituents in elemental form", "Wires"], "required": "optional"},
    )
    output_state: str | None = Field(
        None,
        description="Physical state of the material after the process.",
        json_schema_extra={"example_values": ["Master alloy ingot", "Homogeneous master alloy"], "required": "optional"},
    )

# cluster_11
class ElectrochemicalPolymerization(SurfaceCoatingProcess):
    '''
    Growth of conductive polymer films on a substrate surface via electrochemical oxidation or reduction of monomer species, typically utilizing cyclic potential control.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Growth of conductive polymer films on a substrate surface via electrochemical oxidation or reduction of monomer species, typically utilizing cyclic potential control.",
        json_schema_extra={"synonyms": ["Electrochemical Deposition", "E-Polymerization", "Polymer Electrodeposition"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    monomer: str | None = Field(
        None,
        description="The organic molecule that serves as the precursor for the polymer film deposition.",
        json_schema_extra={"example_values": ["polypyrrole"], "required": "optional"},
    )
    electrolyte: str | None = Field(
        None,
        description="The conductive medium (solution) containing ions that facilitate electrochemical reactions.",
        json_schema_extra={"example_values": ["N/A"], "required": "optional"},
    )
    potential_range: str | None = Field(
        None,
        description="The voltage window or limits applied to the electrode during polymerization.",
        json_schema_extra={"example_values": ["N/A"], "required": "optional"},
    )
    control_mode: str | None = Field(
        None,
        description="The mode of electrical control used (e.g., potentiodynamic, galvanostatic).",
        json_schema_extra={"example_values": ["N/A"], "required": "optional"},
    )
    number_of_cycles: str | None = Field(
        None,
        description="The count of potential sweep cycles performed during the deposition process.",
        json_schema_extra={"example_values": ["N/A"], "required": "optional"},
    )
    duration: str | None = Field(
        None,
        description="The total time allocated for the polymerization process.",
        json_schema_extra={"example_values": ["N/A"], "required": "optional"},
    )
    output_thickness: str | None = Field(
        None,
        description="The target or measured thickness of the polymer layer after deposition.",
        json_schema_extra={"example_values": ["N/A"], "required": "optional"},
    )

# cluster_12
class ElectrolytePreparation(PrecursorPreparationProcess):
    '''
    The process of mixing acids, solvents, and additives to formulate the electrolyte solution required for dealloying.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="The process of mixing acids, solvents, and additives to formulate the electrolyte solution required for dealloying.",
        json_schema_extra={"synonyms": ["Electrolyte Solution Preparation", "Making Electrolyte", "Mixing Electrolyte"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    chemical_composition: str | None = Field(
        None,
        description="The chemical formula of the primary electrolyte or base chemical used.",
        json_schema_extra={"example_values": ["HNO3 and H2O", "HNO 3", "sulfuric acid"], "required": "usually_required"},
    )
    additives: str | None = Field(
        None,
        description="List of additional chemicals or surfactants mixed into the electrolyte.",
        json_schema_extra={"example_values": ["First chemical added", "Second chemical added", "List of surfactants used"], "required": "optional"},
    )
    concentration: str | None = Field(
        None,
        description="The concentration level of the electrolyte or stock solution used.",
        json_schema_extra={"example_values": ["70% stock solution"], "required": "usually_required"},
    )
    volume: str | None = Field(
        None,
        description="The volume of the electrolyte solution or chemical added.",
        json_schema_extra={"example_values": ["30 ml (HNO3) + 60 ml (H2O)", "Volume of base chemical"], "required": "usually_required"},
    )
    step: str | None = Field(
        None,
        description="Identifier indicating the sequence or stage within the preparation workflow.",
        json_schema_extra={"example_values": ["Step 1", "Step 2"], "required": "optional"},
    )

# cluster_13
class Rolling(MechanicalProcessingProcess):
    '''
    Mechanical deformation of bulk alloy material (ingots, droplets) using rollers to reduce thickness and shape into sheets, typically performed at room temperature or elevated temperatures.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Mechanical deformation of bulk alloy material (ingots, droplets) using rollers to reduce thickness and shape into sheets, typically performed at room temperature or elevated temperatures.",
        json_schema_extra={"synonyms": ["Cold rolling", "Cold Working"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    target_thickness: str | None = Field(
        None,
        description="Target or resulting thickness of the material after the rolling process.",
        json_schema_extra={"example_values": ["50 um"], "required": "optional"},
    )
    thickness_unit: str | None = Field(
        None,
        description="Unit of measurement for the sample thickness.",
        json_schema_extra={"example_values": ["um", "mm"], "required": "optional"},
    )
    equipment: str | None = Field(
        None,
        description="Equipment used for the rolling process.",
        json_schema_extra={"example_values": ["rolling mill"], "required": "optional"},
    )
    geometry: str | None = Field(
        None,
        description="Geometry of the output specimen.",
        json_schema_extra={"example_values": ["sheet"], "required": "optional"},
    )
    material_state: str | None = Field(
        None,
        description="State of the material before or during the process.",
        json_schema_extra={"example_values": ["homogenized alloy ingot"], "required": "optional"},
    )
    process_steps: str | None = Field(
        None,
        description="Number of rolling steps performed.",
        json_schema_extra={"example_values": ["2", "multiple"], "required": "optional"},
    )
    frequency: str | None = Field(
        None,
        description="Frequency or pattern of the deformation process.",
        json_schema_extra={"example_values": ["intermittent"], "required": "optional"},
    )

class Pressing(MechanicalProcessingProcess):
    '''
    Mechanical deformation of bulk alloy material using compressive pressure (pressing) to reduce thickness and shape the ingot into sheets.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Mechanical deformation of bulk alloy material using compressive pressure (pressing) to reduce thickness and shape the ingot into sheets.",
        json_schema_extra={"synonyms": [], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    target_thickness: str | None = Field(
        None,
        description="Target or resulting thickness of the material after the pressing process.",
        json_schema_extra={"example_values": ["50 um"], "required": "optional"},
    )
    equipment: str | None = Field(
        None,
        description="Equipment used for the pressing process.",
        json_schema_extra={"example_values": ["press"], "required": "optional"},
    )
    geometry: str | None = Field(
        None,
        description="Geometry of the output specimen.",
        json_schema_extra={"example_values": ["sheet"], "required": "optional"},
    )

# cluster_14
class AcidTreatment(ChemicaltreatmentProcess):
    '''
    Chemical immersion or treatment using acids to modify nanoporous metal surface or pore structure.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Chemical immersion or treatment using acids to modify nanoporous metal surface or pore structure.",
        json_schema_extra={"synonyms": ["Acid immersion treatment", "Acid etching"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    medium: str | None = Field(
        None,
        description="The chemical liquid used for the treatment.",
        json_schema_extra={"example_values": ["Acid solution"], "required": "usually_required"},
    )
    medium_concentration: str | None = Field(
        None,
        description="Concentration level of the chemical medium.",
        json_schema_extra={"example_values": ["Concentration of the acid"], "required": "optional"},
    )
    volume: str | None = Field(
        None,
        description="Volume of the liquid medium.",
        json_schema_extra={"example_values": ["Volume of the solution"], "required": "optional"},
    )
    duration: str | None = Field(
        None,
        description="Time length of the acid treatment.",
        json_schema_extra={"example_values": ["Treatment duration"], "required": "optional"},
    )
    temperature: str | None = Field(
        None,
        description="Temperature at which the acid treatment is performed.",
        json_schema_extra={"example_values": ["Treatment temperature"], "required": "optional"},
    )

class ThermalTreatment(HeatTreatmentProcess):
    '''
    Application of heat to nanoporous metals to modify pore structure, texture, or mechanical properties.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Application of heat to nanoporous metals to modify pore structure, texture, or mechanical properties.",
        json_schema_extra={"synonyms": ["Annealing", "Heat treatment"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    duration: str | None = Field(
        None,
        description="Time length of the thermal process.",
        json_schema_extra={"example_values": ["Duration of the treatment"], "required": "optional"},
    )
    temperature: str | None = Field(
        None,
        description="Target temperature of the thermal process.",
        json_schema_extra={"example_values": ["Treatment temperature", "Treatment temperatures"], "required": "optional"},
    )
    atmosphere: str | None = Field(
        None,
        description="Ambient gas environment during thermal treatment.",
        json_schema_extra={"example_values": ["Gas atmosphere during treatment"], "required": "optional"},
    )

# cluster_15
class EpoxyImpregnation(PostProcessingProcess):
    '''
    Vacuum impregnation of samples with epoxy resin, typically for TEM preparation or encapsulation.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Vacuum impregnation of samples with epoxy resin, typically for TEM preparation or encapsulation.",
        json_schema_extra={"synonyms": ["Epoxy Resin Impregnation", "Vacuum Impregnation", "Resin Encapsulation", "Epoxy Coating"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    medium: str | None = Field(
        None,
        description="Liquid or resin substance used for impregnation or filling the sample pores.",
        json_schema_extra={"example_values": ["Epoxy resin"], "required": "usually_required"},
    )
    temperature: str | None = Field(
        None,
        description="Thermal condition applied during impregnation or subsequent curing.",
        json_schema_extra={"example_values": ["Curing temperature"], "required": "optional"},
    )
    temperature_unit: str | None = Field(
        None,
        description="Standard unit used to measure the temperature parameter.",
        json_schema_extra={"example_values": ["Celsius", "Kelvin"], "required": "optional"},
    )
    duration: str | None = Field(
        None,
        description="Time period for which the impregnation or curing process is performed.",
        json_schema_extra={"example_values": ["Curing duration"], "required": "optional"},
    )
    duration_unit: str | None = Field(
        None,
        description="Standard unit used to measure the duration parameter.",
        json_schema_extra={"example_values": ["Minutes", "Hours"], "required": "optional"},
    )

# cluster_16
class SlurryPreparation(PrecursorFabricationProcess):
    '''
    Mixing of metal powder and binder to form a homogeneous slurry for coating.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Mixing of metal powder and binder to form a homogeneous slurry for coating.",
        json_schema_extra={"synonyms": ["Slurry Formulation", "Powder Slurry Mixing", "Precursor Slurry Preparation"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    binder_type: str | None = Field(
        None,
        description="Type of binder used in the slurry mixture.",
        json_schema_extra={"example_values": ["water-soluble binder"], "required": "required"},
    )
    powder_material: str | None = Field(
        None,
        description="Type of metal powder used in the slurry.",
        json_schema_extra={"example_values": ["metal powder"], "required": "required"},
    )

class Sintering(PrecursorFabricationProcess):
    '''
    Thermal treatment of a precursor slurry-coated substrate to form a porous structure.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Thermal treatment of a precursor slurry-coated substrate to form a porous structure.",
        json_schema_extra={"synonyms": ["Thermal Sintering", "Heat Treatment", "Calcination"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    sintering_temperature: str | None = Field(
        None,
        description="Temperature used for the sintering step.",
        json_schema_extra={"example_values": ["N/A"], "required": "optional"},
    )
    sintering_duration: str | None = Field(
        None,
        description="Duration of the sintering process.",
        json_schema_extra={"example_values": ["N/A"], "required": "optional"},
    )
    substrate: str | None = Field(
        None,
        description="Material of the substrate used for sintering.",
        json_schema_extra={"example_values": ["paper sheet"], "required": "required"},
    )

# cluster_17
class ElectrochemicalActivation(DealloyingProcess):
    '''
    Reduction of the sample surface oxides via cyclic voltammetry to achieve metallic behavior before hydrogen loading experiments.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Reduction of the sample surface oxides via cyclic voltammetry to achieve metallic behavior before hydrogen loading experiments.",
        json_schema_extra={"synonyms": ["Surface Oxide Reduction", "Cyclic Voltammetry Activation", "Surface Cleaning"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    ElectrolyteConcentration: str | None = Field(
        None,
        description="Concentration of the electrolyte used for activation.",
        json_schema_extra={"example_values": [], "required": "usually_required"},
    )
    ElectrolyteFormula: str | None = Field(
        None,
        description="Chemical formula of the electrolyte used for activation.",
        json_schema_extra={"example_values": [], "required": "optional"},
    )
    ReferenceElectrode: str | None = Field(
        None,
        description="Reference electrode used during activation.",
        json_schema_extra={"example_values": [], "required": "usually_required"},
    )
    CounterElectrode: str | None = Field(
        None,
        description="Counter electrode used during activation.",
        json_schema_extra={"example_values": [], "required": "usually_required"},
    )
    Temperature: str | None = Field(
        None,
        description="Temperature of the activation process.",
        json_schema_extra={"example_values": [], "required": "optional"},
    )
    PotentialRange: str | None = Field(
        None,
        description="Potential range used for cyclic voltammetry.",
        json_schema_extra={"example_values": [], "required": "optional"},
    )
    ScanRate: str | None = Field(
        None,
        description="Scan rate of the cyclic voltammetry.",
        json_schema_extra={"example_values": [], "required": "optional"},
    )
    Duration: str | None = Field(
        None,
        description="Duration of the activation process.",
        json_schema_extra={"example_values": [], "required": "optional"},
    )

# cluster_18
class BlowCasting(CastingProcess):
    '''
    A shaping technique where a precursor alloy is formed into a rod using gas pressure.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="A shaping technique where a precursor alloy is formed into a rod using gas pressure.",
        json_schema_extra={"synonyms": ["blow-casting", "gas-pressure casting"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    technique: str | None = Field(
        None,
        description="The specific method used for the casting process.",
        json_schema_extra={"example_values": ["Blow casting"], "required": "optional"},
    )
    output_geometry: str | None = Field(
        None,
        description="The geometric shape of the formed precursor material.",
        json_schema_extra={"example_values": ["rod"], "required": "optional"},
    )

# cluster_19
class Polishing(MechanicalprocessingProcess):
    '''
    Mechanical abrasion of a sample surface to remove material, smooth defects, or prepare a specific surface finish using abrasive materials (e.g., diamond paste, SiC paper, abrasive pastes).
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Mechanical abrasion of a sample surface to remove material, smooth defects, or prepare a specific surface finish using abrasive materials (e.g., diamond paste, SiC paper, abrasive pastes).",
        json_schema_extra={"synonyms": ["Surface Polishing", "Mechanical Polishing", "Abrasion Polishing", "Surface Finishing"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    abrasive_material: str | None = Field(
        None,
        description="The physical abrasive substance (e.g., paste, powder, paper) used to remove material from the surface.",
        json_schema_extra={"example_values": ["abrasive pastes", "powders", "SiC paper", "diamond finish"], "required": "usually_required"},
    )
    abrasive_particle_size: str | None = Field(
        None,
        description="The particle size or grit size of the abrasive material used for polishing.",
        json_schema_extra={"example_values": ["1 \u03bcm", "micrometers", "grit sizes"], "required": "optional"},
    )
    target_surface_finish: str | None = Field(
        None,
        description="The desired surface quality or geometry achieved after the polishing step.",
        json_schema_extra={"example_values": ["specific diamond finish", "smoothness", "planar surfaces"], "required": "optional"},
    )
    workpiece_state: str | None = Field(
        None,
        description="The initial state or geometry of the sample before polishing (e.g., cut, disk).",
        json_schema_extra={"example_values": ["Cut sample"], "required": "optional"},
    )
    substrate_material: str | None = Field(
        None,
        description="The material type of the sample being polished (e.g., electrode, sample disks).",
        json_schema_extra={"example_values": ["electrode surface"], "required": "optional"},
    )
    polishing_location: str | None = Field(
        None,
        description="Which specific side or region of the sample was polished.",
        json_schema_extra={"example_values": ["one side"], "required": "optional"},
    )
    electrode_geometry: str | None = Field(
        None,
        description="Geometric dimensions of the sample (e.g., electrode diameter), often relevant for porous metal electrodes.",
        json_schema_extra={"example_values": ["diameter"], "required": "optional"},
    )

# cluster_20
class ThermalCoarsening(HeatTreatmentProcess):
    '''
    Application of heat to nanoporous structures to induce structural evolution, specifically coarsening of ligaments, thickening of ligaments, pore elimination, and adjustment of pore size/ligament dimensions.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Application of heat to nanoporous structures to induce structural evolution, specifically coarsening of ligaments, thickening of ligaments, pore elimination, and adjustment of pore size/ligament dimensions.",
        json_schema_extra={"synonyms": ["Annealing", "Thermal Annealing", "Heat Treatment", "Thermal Treatment"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    Temperature: str | None = Field(
        None,
        description="The temperature at which the heat treatment is applied.",
        json_schema_extra={"example_values": ["elevated temperatures", "Annealing temperature"], "required": "usually_required"},
    )
    Duration: str | None = Field(
        None,
        description="The time length for which the heat treatment is applied.",
        json_schema_extra={"example_values": ["duration of annealing", "overnight"], "required": "optional"},
    )
    Atmosphere: str | None = Field(
        None,
        description="The gas environment during the thermal treatment (e.g., vacuum, inert gas, hydrogen).",
        json_schema_extra={"example_values": ["ambient atmosphere", "reductive"], "required": "optional"},
    )
    Equipment: str | None = Field(
        None,
        description="The equipment used to perform the heating treatment.",
        json_schema_extra={"example_values": ["Furnace"], "required": "optional"},
    )
    InputMaterial: str | None = Field(
        None,
        description="The chemical composition of the sample before heat treatment.",
        json_schema_extra={"example_values": ["NPG", "NPG-Pt"], "required": "optional"},
    )
    TargetLigamentSize: str | None = Field(
        None,
        description="The desired ligament size after the coarsening process.",
        json_schema_extra={"example_values": ["approximate"], "required": "optional"},
    )
    CoarseningMechanism: str | None = Field(
        None,
        description="The dominant mechanism driving the microstructural change during heating.",
        json_schema_extra={"example_values": ["coalescence", "Ostwald ripening"], "required": "optional"},
    )
    SampleRelativeDensity: str | None = Field(
        None,
        description="The relative density of the sample during the treatment.",
        json_schema_extra={"example_values": ["Relative density"], "required": "optional"},
    )
    InputSampleState: str | None = Field(
        None,
        description="The condition of the sample before the heat treatment step.",
        json_schema_extra={"example_values": ["State of sample"], "required": "optional"},
    )
    OutputSampleState: str | None = Field(
        None,
        description="The condition of the sample after the heat treatment step.",
        json_schema_extra={"example_values": ["State after annealing"], "required": "optional"},
    )
    DensificationState: str | None = Field(
        None,
        description="The stage of densification achieved during or after coarsening.",
        json_schema_extra={"example_values": ["initial", "complete"], "required": "optional"},
    )

# cluster_21
class MeltSpinning2(RapidSolidificationProcess):
    '''
    Rapid solidification of a molten alloy onto a moving substrate (roller) to produce thin metallic ribbons or films, often in a controlled atmosphere.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Rapid solidification of a molten alloy onto a moving substrate (roller) to produce thin metallic ribbons or films, often in a controlled atmosphere.",
        json_schema_extra={"synonyms": ["Melt Spinning", "Melt-spinning", "Melt spinning", "Solidification", "Rapid Solidification"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    Equipment: str | None = Field(
        None,
        description="The apparatus or machine used to perform the melt spinning process.",
        json_schema_extra={"example_values": ["Spinner", "Copper roller apparatus"], "required": "optional"},
    )
    Atmosphere: str | None = Field(
        None,
        description="The gaseous environment maintained during the spinning process to prevent oxidation.",
        json_schema_extra={"example_values": ["Argon atmosphere", "Controlled atmosphere"], "required": "optional"},
    )
    RollerDiameter: str | None = Field(
        None,
        description="The physical diameter of the rotating roller used for solidification.",
        json_schema_extra={"example_values": ["1 inch", "25 mm", "10 cm"], "required": "optional"},
    )
    SpinningSpeed: str | None = Field(
        None,
        description="The rotational speed of the roller during the spinning process.",
        json_schema_extra={"example_values": ["10 m/s", "50 m/min"], "required": "optional"},
    )
    HeatingMethod: str | None = Field(
        None,
        description="The method used to melt the ingot before spinning.",
        json_schema_extra={"example_values": ["Induction heating"], "required": "optional"},
    )
    TubeMaterial: str | None = Field(
        None,
        description="Material of the tube or chamber used for the melting/spinning process.",
        json_schema_extra={"example_values": ["Copper", "Quartz"], "required": "optional"},
    )
    RollerMaterial: str | None = Field(
        None,
        description="Material used to manufacture the spinning roller.",
        json_schema_extra={"example_values": ["Copper"], "required": "optional"},
    )
    InputMaterial: str | None = Field(
        None,
        description="The raw material form fed into the spinning apparatus.",
        json_schema_extra={"example_values": ["Ingots", "Pre-alloyed ingots"], "required": "optional"},
    )
    InputState: str | None = Field(
        None,
        description="The physical state of the material before solidification onto the roller.",
        json_schema_extra={"example_values": ["Molten"], "required": "optional"},
    )
    AlloyComposition: str | None = Field(
        None,
        description="Chemical composition of the alloy processed during spinning.",
        json_schema_extra={"example_values": ["50 at.% Ni", "Fe75B20P5"], "required": "optional"},
    )
    OutputGeometry: str | None = Field(
        None,
        description="The geometric form or dimensions of the product resulting from the process.",
        json_schema_extra={"example_values": ["Ribbon", "Thin ribbons"], "required": "optional"},
    )

# cluster_22
class SurfaceGrinding(SurfaceFinishingProcess):
    '''
    Abrasive grinding process intended for smoothing, polishing, or finishing the surface of a solid sample.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Abrasive grinding process intended for smoothing, polishing, or finishing the surface of a solid sample.",
        json_schema_extra={"synonyms": ["Abrasive grinding", "Surface finishing grinding"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    abrasive_material: str | None = Field(
        None,
        description="Material used for the abrasive grinding tool or wheel.",
        json_schema_extra={"example_values": [], "required": "optional"},
    )

class MechanicalSizeReduction(MechanicalprocessingProcess):
    '''
    Grinding or milling process intended to reduce material to fine powder or particles for downstream processing.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Grinding or milling process intended to reduce material to fine powder or particles for downstream processing.",
        json_schema_extra={"synonyms": ["Powder Grinding", "Milling"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    material_state: str | None = Field(
        None,
        description="Description of the physical state of the material (e.g., powder, solid block) during the process.",
        json_schema_extra={"example_values": [], "required": "optional"},
    )

# cluster_23
class Cutting2(MechanicalProcessingProcess):
    '''
    Mechanical process to separate bulk master alloy into specific sample platelet shapes for subsequent experiments.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Mechanical process to separate bulk master alloy into specific sample platelet shapes for subsequent experiments.",
        json_schema_extra={"synonyms": ["Platelet Preparation", "Sample Cutting"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    sample_shape: str | None = Field(
        None,
        description="Shape of the cut samples.",
        json_schema_extra={"example_values": [], "required": "optional"},
    )

# cluster_24
class Mounting(SamplePreparationProcess):
    '''
    Transferring or placing a prepared sample slice onto a support grid (e.g., TEM grid) for subsequent analysis such as TEM imaging.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Transferring or placing a prepared sample slice onto a support grid (e.g., TEM grid) for subsequent analysis such as TEM imaging.",
        json_schema_extra={"synonyms": ["Sample Mounting", "Grid Loading", "Sample Transfer to Grid"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    grid_type: str | None = Field(
        None,
        description="Material or pattern type of the support grid used to hold the sample.",
        json_schema_extra={"example_values": ["copper", "gold", "lacey carbon"], "required": "optional"},
    )
    grid_mesh: str | None = Field(
        None,
        description="Mesh size or density of the support grid, indicating pore size or wire density.",
        json_schema_extra={"example_values": ["200 mesh", "400 mesh", "100 mesh"], "required": "optional"},
    )

# cluster_25
class SpinCoating(ThinFilmDepositionProcess):
    '''
    Uniform spreading of a liquid coating solution onto a substrate using a spin coater to form a thin film.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Uniform spreading of a liquid coating solution onto a substrate using a spin coater to form a thin film.",
        json_schema_extra={"synonyms": [], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    medium: str | None = Field(
        None,
        description="The liquid solution or solvent used in the coating process, including its chemical composition if specified.",
        json_schema_extra={"example_values": ["coating solution", "solvent"], "required": "usually_required"},
    )
    substrate: str | None = Field(
        None,
        description="The material of the substrate being coated.",
        json_schema_extra={"example_values": ["substrate material"], "required": "usually_required"},
    )
    output_state: str | None = Field(
        None,
        description="The state or morphology of the substrate after the coating process.",
        json_schema_extra={"example_values": ["thin film"], "required": "optional"},
    )

# cluster_26
class ElectrochemicalReduction(PostDealloyingTreatmentProcess):
    '''
    Post-dealloying electrochemical treatment involving potential cycling to control or refine nanoporous ligament diameter.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Post-dealloying electrochemical treatment involving potential cycling to control or refine nanoporous ligament diameter.",
        json_schema_extra={"synonyms": ["Potential Cycling", "Ligament Size Tuning"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    electrolyte_formula: str | None = Field(
        None,
        description="Chemical formula of the electrolyte used in the electrochemical cell.",
        json_schema_extra={"example_values": [], "required": "optional"},
    )
    electrolyte_concentration: str | None = Field(
        None,
        description="Concentration of the electrolyte used.",
        json_schema_extra={"example_values": [], "required": "optional"},
    )
    potential_range_min: str | None = Field(
        None,
        description="Minimum potential applied during the potential cycling.",
        json_schema_extra={"example_values": [], "required": "optional"},
    )
    potential_range_max: str | None = Field(
        None,
        description="Maximum potential applied during the potential cycling.",
        json_schema_extra={"example_values": [], "required": "optional"},
    )
    cycles: str | None = Field(
        None,
        description="Number of potential cycles performed.",
        json_schema_extra={"example_values": [], "required": "optional"},
    )
    scan_rate: str | None = Field(
        None,
        description="Scan rate of the potential cycling.",
        json_schema_extra={"example_values": [], "required": "optional"},
    )
    potentiostat_model: str | None = Field(
        None,
        description="Model of the potentiostat instrument used.",
        json_schema_extra={"example_values": [], "required": "optional"},
    )
    potentiostat_manufacturer: str | None = Field(
        None,
        description="Manufacturer of the potentiostat instrument.",
        json_schema_extra={"example_values": [], "required": "optional"},
    )
    reference_electrode: str | None = Field(
        None,
        description="Reference electrode used in the electrochemical setup.",
        json_schema_extra={"example_values": [], "required": "optional"},
    )
    counter_electrode: str | None = Field(
        None,
        description="Counter electrode used in the electrochemical setup.",
        json_schema_extra={"example_values": [], "required": "optional"},
    )
    electrolyte_purity: str | None = Field(
        None,
        description="Purity level of the electrolyte used.",
        json_schema_extra={"example_values": [], "required": "optional"},
    )
    electrolyte_supplier: str | None = Field(
        None,
        description="Supplier of the electrolyte used.",
        json_schema_extra={"example_values": [], "required": "optional"},
    )
    output_ligament_diameter: str | None = Field(
        None,
        description="Resulting mean ligament diameter of the nanoporous structure.",
        json_schema_extra={"example_values": [], "required": "optional"},
    )

# cluster_27
class HydrogenTreatment(PostProcessingProcess):
    '''
    Exposure of the material to hydrogen to modify hydride content or test material response.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Exposure of the material to hydrogen to modify hydride content or test material response.",
        json_schema_extra={"synonyms": ["Hydrogen Exposure", "Hydrogen Charging", "Hydrogen Saturation"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    atmosphere_composition: str | None = Field(
        None,
        description="The specific composition of the gaseous environment, particularly hydrogen concentration.",
        json_schema_extra={"example_values": ["Hydrogen atmosphere", "Hydrogen content in the atmosphere"], "required": "usually_required"},
    )
    exposure_sequence: str | None = Field(
        None,
        description="The temporal variation or order of exposure parameters.",
        json_schema_extra={"example_values": ["Cyclic exposure"], "required": "optional"},
    )

# cluster_28
class Lithography(PatterningProcess):
    '''
    Fabrication technique using an electron beam or other means to pattern the substrate or resist to create specific shapes.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Fabrication technique using an electron beam or other means to pattern the substrate or resist to create specific shapes.",
        json_schema_extra={"synonyms": ["Patterning", "E-beam Patterning", "Electron Beam Lithography"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    tool: str | None = Field(
        None,
        description="The lithography technique or equipment used to perform the patterning.",
        json_schema_extra={"example_values": ["electron beam"], "required": "usually_required"},
    )
    specimen_shape: str | None = Field(
        None,
        description="The geometric shape of the fabricated specimen after patterning.",
        json_schema_extra={"example_values": ["dog-bone"], "required": "optional"},
    )
    specimen_gauge_length: str | None = Field(
        None,
        description="The gauge length of the specimen.",
        json_schema_extra={"example_values": [], "required": "optional"},
    )
    specimen_gauge_length_unit: str | None = Field(
        None,
        description="The unit of measurement for the gauge length.",
        json_schema_extra={"example_values": [], "required": "optional"},
    )
    specimen_width: str | None = Field(
        None,
        description="The width of the specimen.",
        json_schema_extra={"example_values": [], "required": "optional"},
    )
    specimen_width_unit: str | None = Field(
        None,
        description="The unit of measurement for the width.",
        json_schema_extra={"example_values": [], "required": "optional"},
    )

# cluster_29
class ElectricalContacting(SensorAssemblyProcess):
    '''
    Application of conductive materials, such as silver paint or epoxy, to establish electrical connections between components.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Application of conductive materials, such as silver paint or epoxy, to establish electrical connections between components.",
        json_schema_extra={"synonyms": ["Conductive Glue Application", "Contact Application", "Paint Contacting"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    contacting_agent: str | None = Field(
        None,
        description="Material used to facilitate electrical contact between components, typically conductive.",
        json_schema_extra={"example_values": ["silver paint"], "required": "optional"},
    )
    manufacturer: str | None = Field(
        None,
        description="Entity that manufactured or supplied the contacting agent.",
        json_schema_extra={"example_values": [], "required": "optional"},
    )

# cluster_30
class SparkPlasmaSintering(SinteringProcess):
    '''
    Thermal processing of powdered materials into a dense bulk precursor alloy using electric current pulses within a dielectric environment.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Thermal processing of powdered materials into a dense bulk precursor alloy using electric current pulses within a dielectric environment.",
        json_schema_extra={"synonyms": ["spark plasma sintering", "SPS", "spark plasma sintering process"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    heating_rate: str | None = Field(
        None,
        description="The rate at which the temperature is increased during the sintering process.",
        json_schema_extra={"example_values": ["10 K/min"], "required": "optional"},
    )
    heating_rate_unit: str | None = Field(
        None,
        description="The unit of measurement for the heating rate.",
        json_schema_extra={"example_values": ["K/min", "K/h"], "required": "optional"},
    )
    sintering_temperature: str | None = Field(
        None,
        description="The target or maximum temperature maintained during sintering.",
        json_schema_extra={"example_values": ["1050 C"], "required": "optional"},
    )
    temperature_unit: str | None = Field(
        None,
        description="The unit of measurement for temperature.",
        json_schema_extra={"example_values": ["C", "K"], "required": "optional"},
    )
    sintering_pressure: str | None = Field(
        None,
        description="The applied pressure during the spark plasma sintering process.",
        json_schema_extra={"example_values": ["50 MPa"], "required": "optional"},
    )
    pressure_unit: str | None = Field(
        None,
        description="The unit of measurement for the applied pressure.",
        json_schema_extra={"example_values": ["MPa", "bar"], "required": "optional"},
    )
    holding_time: str | None = Field(
        None,
        description="The duration maintained at the target sintering temperature.",
        json_schema_extra={"example_values": ["10 min"], "required": "optional"},
    )
    time_unit: str | None = Field(
        None,
        description="The unit of measurement for the holding time.",
        json_schema_extra={"example_values": ["min", "h"], "required": "optional"},
    )
    input_state: str | None = Field(
        None,
        description="The state of the material before the sintering process begins.",
        json_schema_extra={"example_values": ["milled alloy powder", "powder"], "required": "optional"},
    )
    output_state: str | None = Field(
        None,
        description="The state of the material after the sintering process.",
        json_schema_extra={"example_values": ["dense bulk precursor alloy"], "required": "optional"},
    )

# cluster_31
class Encapsulation(SensorAssemblyProcess):
    '''
    Sealing a device or sensor inside a protective or functional chamber to form an enclosed unit.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Sealing a device or sensor inside a protective or functional chamber to form an enclosed unit.",
        json_schema_extra={"synonyms": ["Sealing", "Packaging", "Enclosure", "Chamber Sealing"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    chamber_material: str | None = Field(
        None,
        description="Material used to construct the enclosing chamber of the sensor.",
        json_schema_extra={"example_values": ["glass"], "required": "optional"},
    )
    chamber_features: str | None = Field(
        None,
        description="Specific functional features or components present in the chamber.",
        json_schema_extra={"example_values": ["gas inlet", "gas outlet"], "required": "optional"},
    )

# cluster_32
class BallMilling(MechanicalalloyingProcess):
    '''
    Mechanical process involving high-energy impact of milling media on powder materials to synthesize alloys or nanomaterials.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Mechanical process involving high-energy impact of milling media on powder materials to synthesize alloys or nanomaterials.",
        json_schema_extra={"synonyms": ["Mechanical alloying", "Powder milling", "High energy milling"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    material: str | None = Field(
        None,
        description="Powder materials used in the milling process.",
        json_schema_extra={"example_values": ["Al", "Pd"], "required": "usually_required"},
    )
    material_purity: str | None = Field(
        None,
        description="Purity level of the powder materials used.",
        json_schema_extra={"example_values": ["99.9%", "99%"], "required": "optional"},
    )
    material_size: str | None = Field(
        None,
        description="Particle size of the powder materials before milling.",
        json_schema_extra={"example_values": ["micron range", "fine"], "required": "optional"},
    )
    composition: str | None = Field(
        None,
        description="Final or target alloy composition.",
        json_schema_extra={"example_values": ["Al-Pd"], "required": "optional"},
    )
    atmosphere: str | None = Field(
        None,
        description="Atmospheric condition during the milling process.",
        json_schema_extra={"example_values": ["vacuum"], "required": "optional"},
    )
    mass_ratio: str | None = Field(
        None,
        description="Ratio of ball mass to powder mass.",
        json_schema_extra={"example_values": ["variable"], "required": "optional"},
    )
    rotational_speed: str | None = Field(
        None,
        description="Rotational speed of the milling balls.",
        json_schema_extra={"example_values": ["variable"], "required": "optional"},
    )
    duration: str | None = Field(
        None,
        description="Total time duration of the milling process.",
        json_schema_extra={"example_values": ["variable"], "required": "optional"},
    )
    duration_unit: str | None = Field(
        None,
        description="Unit of time for the milling duration.",
        json_schema_extra={"example_values": ["min", "h"], "required": "optional"},
    )

# cluster_33
class BallMilling2(MechanicalsizereductionProcess):
    '''
    Mechanical process utilizing high-energy impact using a planetary mill to alloy materials or reduce particle size, typically converting solid samples into powder form.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Mechanical process utilizing high-energy impact using a planetary mill to alloy materials or reduce particle size, typically converting solid samples into powder form.",
        json_schema_extra={"synonyms": ["Mechanical alloying", "Grinding", "Planetary Milling"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    equipment: str | None = Field(
        None,
        description="Name and model of the mill used for processing.",
        json_schema_extra={"example_values": [], "required": "usually_optional"},
    )
    ball_to_sample_ratio: str | None = Field(
        None,
        description="Weight ratio of balls to sample during the milling process.",
        json_schema_extra={"example_values": [], "required": "usually_optional"},
    )
    atmosphere: str | None = Field(
        None,
        description="Atmosphere maintained inside the mill chamber during processing.",
        json_schema_extra={"example_values": [], "required": "usually_optional"},
    )
    disk_speed: str | None = Field(
        None,
        description="Rotational speed of the main disk in the planetary mill.",
        json_schema_extra={"example_values": [], "required": "usually_optional"},
    )
    disk_speed_unit: str | None = Field(
        None,
        description="Unit of measurement for disk speed (e.g., rpm).",
        json_schema_extra={"example_values": [], "required": "usually_optional"},
    )
    duration: str | None = Field(
        None,
        description="Total duration of the milling process.",
        json_schema_extra={"example_values": [], "required": "usually_optional"},
    )
    duration_unit: str | None = Field(
        None,
        description="Unit of measurement for duration (e.g., hours, minutes).",
        json_schema_extra={"example_values": [], "required": "usually_optional"},
    )
    duty_cycle_interval: str | None = Field(
        None,
        description="Time interval between milling cycles and pauses.",
        json_schema_extra={"example_values": [], "required": "usually_optional"},
    )
    duty_cycle_pause: str | None = Field(
        None,
        description="Pause duration between milling intervals.",
        json_schema_extra={"example_values": [], "required": "usually_optional"},
    )

# cluster_34
class ElectrochemicalCharging(DealloyingProcess):
    '''
    Application of a controlled potential to the nanoporous metal surface within an electrochemical cell, typically to tune electrical resistance or induce specific surface states.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Application of a controlled potential to the nanoporous metal surface within an electrochemical cell, typically to tune electrical resistance or induce specific surface states.",
        json_schema_extra={"synonyms": ["Electrolyte Charging", "Potential Application"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    electrolyte: str | None = Field(
        None,
        description="Electrolyte used for charging",
        json_schema_extra={"example_values": [], "required": "optional"},
    )
    electrolyte_concentration: str | None = Field(
        None,
        description="Concentration of the electrolyte",
        json_schema_extra={"example_values": [], "required": "optional"},
    )
    potentiostat_model: str | None = Field(
        None,
        description="Model of the potentiostat used",
        json_schema_extra={"example_values": [], "required": "optional"},
    )
    potential_range: str | None = Field(
        None,
        description="Voltage range applied during charging",
        json_schema_extra={"example_values": [], "required": "optional"},
    )
    voltage_step: str | None = Field(
        None,
        description="Step size for voltage increment",
        json_schema_extra={"example_values": [], "required": "optional"},
    )
    voltage_step_unit: str | None = Field(
        None,
        description="Unit of voltage step",
        json_schema_extra={"example_values": [], "required": "optional"},
    )
    time_interval: str | None = Field(
        None,
        description="Time interval between voltage steps",
        json_schema_extra={"example_values": [], "required": "optional"},
    )
    regime: str | None = Field(
        None,
        description="Regime of charging (e.g., double layer, chemisorption)",
        json_schema_extra={"example_values": [], "required": "optional"},
    )
    reference_electrode: str | None = Field(
        None,
        description="Reference electrode used during charging",
        json_schema_extra={"example_values": [], "required": "optional"},
    )
    counter_electrode: str | None = Field(
        None,
        description="Counter electrode used during charging",
        json_schema_extra={"example_values": [], "required": "optional"},
    )
    measurement_method: str | None = Field(
        None,
        description="Method used for charging (e.g., chronoamperometric)",
        json_schema_extra={"example_values": [], "required": "optional"},
    )

# cluster_35
class Cyclovoltammetry(ElectrochemicalCharacterizationProcess):
    '''
    Electrochemical scanning technique used to determine potential ranges, monitor resistance, or analyze redox behavior in a system.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Electrochemical scanning technique used to determine potential ranges, monitor resistance, or analyze redox behavior in a system.",
        json_schema_extra={"synonyms": ["Cyclic Voltammetry", "CV", "Electrochemical Scanning"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    scan_rate: str | None = Field(
        None,
        description="The velocity at which the potential is swept during the cyclovoltammetric cycle.",
        json_schema_extra={"example_values": [], "required": "usually_required"},
    )
    scan_rate_unit: str | None = Field(
        None,
        description="The unit of measurement for the scan rate (e.g., V/s, mV/s).",
        json_schema_extra={"example_values": [], "required": "optional"},
    )
    purpose: str | None = Field(
        None,
        description="The specific objective of the scanning process, such as determining potential ranges or monitoring resistance.",
        json_schema_extra={"example_values": [], "required": "optional"},
    )
    reference_electrode: str | None = Field(
        None,
        description="The reference electrode used to maintain a stable potential reference during the electrochemical scanning.",
        json_schema_extra={"example_values": [], "required": "usually_required"},
    )

# cluster_36
class InkCoating(ElectrodeAssemblyProcess):
    '''
    Application of a liquid catalyst ink drop onto a polished substrate to form a functional electrocatalytic electrode.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Application of a liquid catalyst ink drop onto a polished substrate to form a functional electrocatalytic electrode.",
        json_schema_extra={"synonyms": ["Coating", "Drop Coating", "Ink Deposition", "Catalyst Application"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    ink_volume: str | None = Field(
        None,
        description="Volume of the catalyst ink applied to the substrate.",
        json_schema_extra={"example_values": ["<value>"], "required": "optional"},
    )
    ink_volume_unit: str | None = Field(
        None,
        description="Unit of measurement for the ink volume.",
        json_schema_extra={"example_values": ["<unit>"], "required": "optional"},
    )
    substrate_material: str | None = Field(
        None,
        description="Material composition of the electrode substrate.",
        json_schema_extra={"example_values": ["<material>"], "required": "optional"},
    )
    substrate_diameter: str | None = Field(
        None,
        description="Diameter of the substrate used for the electrode.",
        json_schema_extra={"example_values": ["<value>"], "required": "optional"},
    )
    substrate_diameter_unit: str | None = Field(
        None,
        description="Unit of measurement for the substrate diameter.",
        json_schema_extra={"example_values": ["<unit>"], "required": "optional"},
    )

# cluster_37
class Mixing(DispersionPreparationProcess):
    '''
    Combining solid powders, solvents, and binders to form a homogeneous suspension or slurry suitable for subsequent fabrication steps.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Combining solid powders, solvents, and binders to form a homogeneous suspension or slurry suitable for subsequent fabrication steps.",
        json_schema_extra={"synonyms": ["Slurry Preparation", "Ink Preparation", "Homogenization", "Suspension Mixing"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    solvent_volume: str | None = Field(
        None,
        description="Volume of solvent (e.g., isopropanol) added to the mixture.",
        json_schema_extra={"example_values": ["10 mL"], "required": "usually_required"},
    )
    solvent_volume_unit: str | None = Field(
        None,
        description="Unit of measurement for the solvent volume.",
        json_schema_extra={"example_values": ["mL"], "required": "optional"},
    )
    binder_volume: str | None = Field(
        None,
        description="Volume of binder solution (e.g., Nafion) added to the mixture.",
        json_schema_extra={"example_values": ["2 mL"], "required": "usually_required"},
    )
    binder_concentration: str | None = Field(
        None,
        description="Concentration of the binder solution used in the dispersion.",
        json_schema_extra={"example_values": ["5 wt%"], "required": "optional"},
    )
    mixing_equipment: str | None = Field(
        None,
        description="Equipment used to perform the mixing or homogenization step.",
        json_schema_extra={"example_values": ["magnetic stirrer"], "required": "optional"},
    )

# cluster_38
class Flattening(SurfaceTreatmentProcess):
    '''
    Mechanical process applying pressure or force with a smooth surface to flatten and planarize a coated layer or specimen.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Mechanical process applying pressure or force with a smooth surface to flatten and planarize a coated layer or specimen.",
        json_schema_extra={"synonyms": ["Planarizing", "Pressing", "Smoothing"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    tool: str | None = Field(
        None,
        description="The tool or surface used for flattening.",
        json_schema_extra={"example_values": [], "required": "optional"},
    )
    output_thickness: str | None = Field(
        None,
        description="Target thickness achieved after flattening.",
        json_schema_extra={"example_values": [], "required": "optional"},
    )
    thickness_unit: str | None = Field(
        None,
        description="Unit of the output thickness.",
        json_schema_extra={"example_values": [], "required": "optional"},
    )

# cluster_39
class SurfaceExposure(PostProcessingProcess):
    '''
    Process of exposing the sample surface to specific gases to modify surface chemistry or induce strain.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Process of exposing the sample surface to specific gases to modify surface chemistry or induce strain.",
        json_schema_extra={"synonyms": ["Gas Exposure"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    gas_type: str | None = Field(
        None,
        description="Type of gas used for exposure to modify surface chemistry or induce strain.",
        json_schema_extra={"example_values": ["Ozone", "Carbon Monoxide", "O2", "Pure CO"], "required": "usually_required"},
    )
    concentration: str | None = Field(
        None,
        description="Concentration of the gas used during the exposure process.",
        json_schema_extra={"example_values": ["~7 vol % O3"], "required": "optional"},
    )
    atmosphere: str | None = Field(
        None,
        description="The surrounding atmospheric environment during the exposure step.",
        json_schema_extra={"example_values": ["O2", "Pure CO"], "required": "optional"},
    )
    purpose: str | None = Field(
        None,
        description="The intended outcome or function of the gas exposure (e.g., surface modification, actuation).",
        json_schema_extra={"example_values": ["surface engineering", "actuation", "cleaning"], "required": "optional"},
    )

# cluster_40
class ProtectiveCoatingApplication(FabricationProcess):
    '''
    Application of a protective layer (e.g., lacquer) on the borders or surface of a sample to secure it during subsequent processing or handling.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Application of a protective layer (e.g., lacquer) on the borders or surface of a sample to secure it during subsequent processing or handling.",
        json_schema_extra={"synonyms": ["Protective coating", "Sample sealing", "Border coating"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    coating_material: str | None = Field(
        None,
        description="The specific material used to form the protective coating.",
        json_schema_extra={"example_values": ["lacquer"], "required": "optional"},
    )
    coating_location: str | None = Field(
        None,
        description="The specific region or surface area of the sample where the coating is applied.",
        json_schema_extra={"example_values": ["borders"], "required": "optional"},
    )
    coating_purpose: str | None = Field(
        None,
        description="The functional reason or outcome intended by applying the protective coating.",
        json_schema_extra={"example_values": ["secure them during processing"], "required": "optional"},
    )

# cluster_41
class PotentialCycling(HeatTreatmentProcess):
    '''
    Electrochemical technique involving repeated potential sweeps to stabilize nanoporous samples or modify surface states prior to actuation measurements.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Electrochemical technique involving repeated potential sweeps to stabilize nanoporous samples or modify surface states prior to actuation measurements.",
        json_schema_extra={"synonyms": ["Electrochemical Cycling", "Cycling Treatment", "Activation Cycling"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    cycle_count: str | None = Field(
        None,
        description="Number of potential cycles performed during the electrochemical treatment.",
        json_schema_extra={"example_values": [], "required": "usually_required"},
    )
    potential_range: str | None = Field(
        None,
        description="Range of potential applied during the cycling process.",
        json_schema_extra={"example_values": [], "required": "usually_required"},
    )
    reference_electrode: str | None = Field(
        None,
        description="Type of reference electrode used to control the potential.",
        json_schema_extra={"example_values": [], "required": "usually_required"},
    )
    scan_rate: str | None = Field(
        None,
        description="Rate at which the potential is swept during cycling.",
        json_schema_extra={"example_values": [], "required": "usually_required"},
    )
    scan_rate_unit: str | None = Field(
        None,
        description="Unit of measurement for the scan rate (e.g., V/s, V/min).",
        json_schema_extra={"example_values": [], "required": "optional"},
    )
    electrolyte: str | None = Field(
        None,
        description="Electrolyte solution used during the electrochemical cycling process.",
        json_schema_extra={"example_values": [], "required": "usually_required"},
    )
    electrolyte_concentration: str | None = Field(
        None,
        description="Concentration of the electrolyte solution used.",
        json_schema_extra={"example_values": [], "required": "optional"},
    )

# cluster_42
class FilmDeposition(FilmFabricationProcess):
    '''
    Deposition of material onto a substrate to form a thin film layer.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Deposition of material onto a substrate to form a thin film layer.",
        json_schema_extra={"synonyms": ["Deposition", "Film Fabrication"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    substrate_material: str | None = Field(
        None,
        description="Material of the substrate wafer onto which the film is deposited.",
        json_schema_extra={"example_values": ["Si wafer"], "required": "usually_required"},
    )
    substrate_thickness: str | None = Field(
        None,
        description="Thickness of the substrate or barrier layer on the wafer.",
        json_schema_extra={"example_values": ["Unknown"], "required": "optional"},
    )
    deposited_material: str | None = Field(
        None,
        description="Material that is deposited onto the substrate.",
        json_schema_extra={"example_values": ["AuCu alloy"], "required": "usually_required"},
    )
    deposited_composition: str | None = Field(
        None,
        description="Atomic percentage composition of the deposited layer.",
        json_schema_extra={"example_values": ["Atomic percentage"], "required": "optional"},
    )
    tool: str | None = Field(
        None,
        description="Equipment used for the deposition process.",
        json_schema_extra={"example_values": ["Unknown"], "required": "usually_required"},
    )

class Annealing2(HeatTreatmentProcess):
    '''
    Heat treatment applied to a material to achieve specific microstructural changes such as mixing or crystallization.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Heat treatment applied to a material to achieve specific microstructural changes such as mixing or crystallization.",
        json_schema_extra={"synonyms": ["Heat treatment"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    temperature: str | None = Field(
        None,
        description="Temperature at which the annealing heat treatment is performed.",
        json_schema_extra={"example_values": ["Unknown"], "required": "usually_required"},
    )
    duration: str | None = Field(
        None,
        description="Duration for which the annealing step is performed.",
        json_schema_extra={"example_values": ["Unknown"], "required": "optional"},
    )
    input_state: str | None = Field(
        None,
        description="Material state before the annealing step.",
        json_schema_extra={"example_values": ["as-deposited alloy film"], "required": "optional"},
    )
    output_state: str | None = Field(
        None,
        description="Material state after the annealing step.",
        json_schema_extra={"example_values": ["mixed alloy film"], "required": "optional"},
    )
    atmosphere: str | None = Field(
        None,
        description="Processing atmosphere during heat treatment.",
        json_schema_extra={"example_values": ["Unknown"], "required": "optional"},
    )

# cluster_43
class Mounting2(SensorAssemblyProcess):
    '''
    Securing a sample or ribbon onto a substrate to establish mechanical stability or electrical connectivity for subsequent measurements.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Securing a sample or ribbon onto a substrate to establish mechanical stability or electrical connectivity for subsequent measurements.",
        json_schema_extra={"synonyms": ["Sample Attachment", "Fixing", "Mounting the sample"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    substrate: str | None = Field(
        None,
        description="The material or surface onto which the sample is mounted.",
        json_schema_extra={"example_values": ["glass slide"], "required": "optional"},
    )
    contact_wires: str | None = Field(
        None,
        description="Conducting wires used for electrical connection to the mounted sample.",
        json_schema_extra={"example_values": ["conducting wires"], "required": "optional"},
    )

# cluster_44
class HeatTreatment2(ThermalTreatmentProcess):
    '''
    Process involving controlled heating of a sample to relieve internal stresses without altering its microstructure significantly, typically prior to nanoporous metal fabrication or as a stabilization step.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Process involving controlled heating of a sample to relieve internal stresses without altering its microstructure significantly, typically prior to nanoporous metal fabrication or as a stabilization step.",
        json_schema_extra={"synonyms": ["Thermal stress relief", "Stress relief treatment"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    temperature: str | None = Field(
        None,
        description="The specific heat treatment temperature applied to the sample.",
        json_schema_extra={"example_values": [], "required": "optional"},
    )
    temperature_unit: str | None = Field(
        None,
        description="The unit of measurement for the heat treatment temperature (e.g., \u00b0C, \u00b0F).",
        json_schema_extra={"example_values": [], "required": "optional"},
    )
    duration: str | None = Field(
        None,
        description="The length of time the heat treatment is maintained.",
        json_schema_extra={"example_values": [], "required": "optional"},
    )
    duration_unit: str | None = Field(
        None,
        description="The unit of measurement for the heat treatment duration (e.g., min, h).",
        json_schema_extra={"example_values": [], "required": "optional"},
    )

# cluster_45
class Stabilization(PostProcessingProcess):
    '''
    A post-processing step involving immersion of nanoporous metal samples in a liquid medium (e.g., water) to form a passivating oxide layer and prevent oxidation or combustion of the porous structure.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="A post-processing step involving immersion of nanoporous metal samples in a liquid medium (e.g., water) to form a passivating oxide layer and prevent oxidation or combustion of the porous structure.",
        json_schema_extra={"synonyms": ["Passivation", "Oxidation Prevention", "Water Stabilization"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    immersion_medium: str | None = Field(
        None,
        description="Liquid used for immersion to facilitate stabilization or passivation of the nanoporous structure.",
        json_schema_extra={"example_values": ["distilled water"], "required": "usually_required"},
    )
    duration: str | None = Field(
        None,
        description="Time duration of the immersion stabilization step.",
        json_schema_extra={"example_values": ["variable"], "required": "optional"},
    )
    purpose: str | None = Field(
        None,
        description="The intended outcome or reason for performing the stabilization step.",
        json_schema_extra={"example_values": ["prevent oxidation or combustion"], "required": "optional"},
    )

# cluster_46
class ThermalCycling(HeatTreatmentProcess):
    '''
    Cyclic thermal treatment applied to specimens, typically to induce structural changes such as coarsening or study stress evolution.
    '''
    preferred_name: str | None = Field(
        description="Preferred human readable name for the process.",
        json_schema_extra={"source": "preferred_name"},
    )
    parent_process_name: str | None = Field(
        description="Parent category process name.",
        json_schema_extra={"source": "parent_process_name"},
    )
    definition: str = Field(
        description="Cyclic thermal treatment applied to specimens, typically to induce structural changes such as coarsening or study stress evolution.",
        json_schema_extra={"synonyms": ["Cyclic thermal treatment", "Thermal Cycles"], "source": "definition"},
    )
    process_identifier: str | None = Field(
        default=None,
        description="Process identifier or reference.",
    )
    temperature: str | None = Field(
        None,
        description="Temperature of the thermal cycling.",
        json_schema_extra={"example_values": [], "required": "usually_required"},
    )
    cycle_range: str | None = Field(
        None,
        description="Range of temperatures involved in the cycle.",
        json_schema_extra={"example_values": [], "required": "optional"},
    )

# List of defined process class names
PROCESS_CLASS_NAMES = [
    "MechanicalCleaning", "ElectrochemicalCleaning", "Sputtering", "AtomicLayerDeposition",
    "Annealing", "MeltSpinning", "SampleCleaning", "SampleDrying", "Homogenization",
    "WaterQuenching", "ElectrochemicalDealloying", "ChemicalDealloying", "Cutting",
    "MechanicalShaping", "Ultramicrotomy", "FreeCorrosionDealloying", "PotentiostaticDealloying",
    "MasterAlloyPreparation", "ElectrochemicalPolymerization", "ElectrolytePreparation",
    "Rolling", "Pressing", "AcidTreatment", "ThermalTreatment", "EpoxyImpregnation",
    "SlurryPreparation", "Sintering", "ElectrochemicalActivation", "BlowCasting", "Polishing",
    "ThermalCoarsening", "MeltSpinning2", "SurfaceGrinding", "MechanicalSizeReduction",
    "Cutting2", "Mounting", "SpinCoating", "ElectrochemicalReduction", "HydrogenTreatment",
    "Lithography", "ElectricalContacting", "SparkPlasmaSintering", "Encapsulation", "BallMilling",
    "BallMilling2", "ElectrochemicalCharging", "Cyclovoltammetry", "InkCoating", "Mixing",
    "Flattening", "SurfaceExposure", "ProtectiveCoatingApplication", "PotentialCycling",
    "FilmDeposition", "Annealing2", "Mounting2", "HeatTreatment2", "Stabilization", "ThermalCycling"
]

# List of duplicate process identifiers (Process names that appeared in multiple clusters with different attributes)
# This is a manual list based on the analysis of the JSON data structure provided in the prompt.
PROCESS_DUPLICATES = [
    ("Annealing", ["cluster_0", "cluster_42"]),
    ("Melt Spinning", ["cluster_2", "cluster_21"]),
    ("Cutting", ["cluster_6", "cluster_23"]),
    ("Electrochemical Dealloying", ["cluster_5", "cluster_12"]),
    ("Rolling", ["cluster_13"]),
    ("Thermal Treatment", ["cluster_14", "cluster_46"]),
]

# List of all process classes
PROCESS_CLASSES = PROCESS_CLASS_NAMES

PROCESS_CLASS_NAMES