from pydantic import BaseModel, Field
from typing import List, Optional, Union

class Cleaning(BaseModel):
    pass

class SurfaceTreatment(BaseModel):
    pass

class ThinFilmDeposition(BaseModel):
    pass

class HeatTreatment(BaseModel):
    pass

class Dealloying(BaseModel):
    pass

class ElectrodeAssembly(BaseModel):
    pass

class MechanicalProcessing(BaseModel):
    pass

class MechanicalShaping(BaseModel):
    pass

class AlloyPreparation(BaseModel):
    pass

class SurfaceCoating(BaseModel):
    pass

class PrecursorPreparation(BaseModel):
    pass

class Coating(BaseModel):
    pass

class Patterning(BaseModel):
    pass

class SensorAssembly(BaseModel):
    pass

class Sintering(BaseModel):
    pass

class SamplePreparation(BaseModel):
    pass

class PostProcessing(BaseModel):
    pass

class ElectrochemicalConditioning(BaseModel):
    pass

class FilmFabrication(BaseModel):
    pass

class ThermalTreatment(BaseModel):
    pass

class ChemicalTreatment(BaseModel):
    pass

class MechanicalSurfaceCleaning(Cleaning):
    '''
    Removal of surface contaminants, such as oxide scales, using physical or mechanical force.
    Synonyms: mechanical cleaning, physical surface cleaning
    '''
    process_identifier: str | None = Field("mechanical_surface_cleaning", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Mechanical Surface Cleaning", description="Human readable process name from the source schema.")
    input_state: str | None = Field(None, description="The state or condition of the sample surface before the cleaning process.", json_schema_extra={"source_attribute_names": ["input_state"], "example_values": ["oxide covered"], "required": "usually_required", "confidence": "high"})
    cleaning_method: str | None = Field(None, description="The specific mechanical technique used to remove the surface layer.", json_schema_extra={"source_attribute_names": ["cleaning_method"], "example_values": [], "required": "usually_required", "confidence": "high"})

class ElectrochemicalSurfaceCleaning(SurfaceTreatment):
    '''
    Removal of surface contaminants or oxides by applying an electrical potential or cycling potentials in an electrolyte.
    Synonyms: electrochemical cleaning, potential cycling cleaning
    '''
    process_identifier: str | None = Field("electrochemical_surface_cleaning", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Electrochemical Surface Cleaning", description="Human readable process name from the source schema.")
    number_of_cycles: int | None = Field(None, description="The number of times the potential is cycled to clean the surface.", json_schema_extra={"source_attribute_names": ["number_of_cycles"], "example_values": [], "required": "usually_required", "confidence": "high"})
    potential_range: str | None = Field(None, description="The voltage range over which the potential is cycled.", json_schema_extra={"source_attribute_names": ["potential_range"], "example_values": [], "required": "usually_required", "confidence": "high"})
    scan_rate: float | str | None = Field(None, description="The speed at which the potential is varied during the cleaning cycle.", json_schema_extra={"source_attribute_names": ["scan_rate"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    scan_rate_units: str | None = Field(None, description="The unit of measurement for the scan rate.", json_schema_extra={"source_attribute_names": ["scan_rate_unit"], "example_values": [], "required": "usually_required", "confidence": "high", "unit_for": "scan_rate"})

class Sputtering(ThinFilmDeposition):
    '''
    A physical vapor deposition process where atoms are ejected from a target material due to bombardment by energetic particles and deposited onto a substrate to form a thin film.
    Synonyms: magnetron sputtering, co-sputtering, PVD sputtering
    '''
    process_identifier: str | None = Field("sputtering", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Sputtering", description="Human readable process name from the source schema.")
    target_material: str | None = Field(None, description="The material of the sputtering target used to provide the atoms for deposition.", json_schema_extra={"source_attribute_names": ["layer_material", "target_materials", "deposited_material", "deposited_material_list"], "example_values": ["Ta", "Pd", "Au", "Au-Ag"], "required": "usually_required", "confidence": "high"})
    substrate_material: str | None = Field(None, description="The material and type of the substrate onto which the film is deposited.", json_schema_extra={"source_attribute_names": ["substrate_type", "substrate_material", "substrate"], "example_values": ["Si", "polyimide", "silicon wafers"], "required": "usually_required", "confidence": "high"})
    film_thickness: float | str | None = Field(None, description="The thickness of the deposited layer or film.", json_schema_extra={"source_attribute_names": ["layer_thickness", "film_thickness", "thickness", "interlayer_thickness"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    film_thickness_units: str | None = Field(None, description="Units for film_thickness.", json_schema_extra={"unit_for": "film_thickness"})
    chamber_pressure: float | str | None = Field(None, description="The vacuum pressure level within the sputtering chamber.", json_schema_extra={"source_attribute_names": ["vacuum_level", "vacuum_pressure", "base_pressure"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    chamber_pressure_units: str | None = Field(None, description="Units for chamber_pressure.", json_schema_extra={"unit_for": "chamber_pressure"})
    deposition_temperature: float | str | None = Field(None, description="The temperature of the substrate or chamber during the deposition process.", json_schema_extra={"source_attribute_names": ["temperature", "deposition_temperature"], "example_values": [], "required": "optional", "confidence": "medium", "value_type": "quantity"})
    deposition_temperature_units: str | None = Field(None, description="Units for deposition_temperature.", json_schema_extra={"unit_for": "deposition_temperature"})
    plasma_gas: str | None = Field(None, description="The gas used to create the plasma for sputtering.", json_schema_extra={"source_attribute_names": ["plasma_gas"], "example_values": ["Ar"], "required": "optional", "confidence": "medium"})
    biasing_power: float | str | None = Field(None, description="The RF or DC power applied as a bias during deposition.", json_schema_extra={"source_attribute_names": ["biasing_power"], "example_values": [], "required": "optional", "confidence": "medium", "value_type": "quantity"})
    biasing_power_units: str | None = Field(None, description="Units for biasing_power.", json_schema_extra={"unit_for": "biasing_power"})
    deposition_method: str | None = Field(None, description="The specific mode of sputtering (e.g., co-sputtering for alloys, sequential for multilayers).", json_schema_extra={"source_attribute_names": ["deposition_method"], "example_values": ["sequential", "co-sputtering"], "required": "optional", "confidence": "medium"})

class AtomicLayerDeposition(ThinFilmDeposition):
    '''
    A vapor phase deposition technique that uses sequential, self-limiting surface reactions to deposit ultra-thin films with atomic-level thickness control.
    Synonyms: ALD
    '''
    process_identifier: str | None = Field("atomic_layer_deposition", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Atomic Layer Deposition", description="Human readable process name from the source schema.")
    number_of_cycles: int | None = Field(None, description="The number of ALD cycles performed to achieve the desired film thickness.", json_schema_extra={"source_attribute_names": ["cycles"], "example_values": [], "required": "usually_required", "confidence": "high"})
    reactor_type: str | None = Field(None, description="The type of chemical reactor used for the ALD process.", json_schema_extra={"source_attribute_names": ["reactor_type"], "example_values": ["continuous flow reactor"], "required": "optional", "confidence": "high"})
    substrate: str | None = Field(None, description="The material or structure upon which the ALD layers are deposited.", json_schema_extra={"source_attribute_names": ["substrate"], "example_values": ["nanoporous bulk materials"], "required": "usually_required", "confidence": "high"})
    deposition_method: str | None = Field(None, description="Description of the chemical reaction mechanism used.", json_schema_extra={"source_attribute_names": ["deposition_method"], "example_values": ["sequential, self-limiting surface reactions"], "required": "optional", "confidence": "medium"})

class Annealing(HeatTreatment):
    '''
    Heat treatment of a material at elevated temperatures for a specific duration and atmosphere to modify its microstructure, such as inducing coarsening, recovery, or modifying pore size.
    Synonyms: thermal annealing, coarsening annealing, heat treatment
    '''
    process_identifier: str | None = Field("annealing", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Annealing", description="Human readable process name from the source schema.")
    temperature: float | str | None = Field(None, description="The temperature at which the annealing is performed.", json_schema_extra={"source_attribute_names": ["temperature", "temperature_range_min", "temperature_range_max", "temperature_min", "temperature_max"], "example_values": ["773 K"], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    temperature_units: str | None = Field(None, description="Units for temperature.", json_schema_extra={"unit_for": "temperature"})
    duration: float | str | None = Field(None, description="The length of time the material is held at the annealing temperature.", json_schema_extra={"source_attribute_names": ["duration"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    duration_units: str | None = Field(None, description="Units for duration.", json_schema_extra={"unit_for": "duration"})
    atmosphere: str | None = Field(None, description="The gas environment or vacuum condition maintained during the heat treatment.", json_schema_extra={"source_attribute_names": ["atmosphere"], "example_values": ["Argon", "air", "inert gas", "Vacuum"], "required": "usually_required", "confidence": "high"})
    equipment: str | None = Field(None, description="The apparatus or furnace used to perform the annealing.", json_schema_extra={"source_attribute_names": ["equipment"], "example_values": ["Furnace"], "required": "optional", "confidence": "medium"})
    gas_flow_rate: float | str | None = Field(None, description="The rate at which the protective or reactive gas is flowed over the sample.", json_schema_extra={"source_attribute_names": ["flow_speed", "gas_flow_rate"], "example_values": [], "required": "context_dependent", "confidence": "medium", "value_type": "quantity"})
    gas_flow_rate_units: str | None = Field(None, description="Units for gas_flow_rate.", json_schema_extra={"unit_for": "gas_flow_rate"})
    heating_rate: float | str | None = Field(None, description="The speed at which the temperature is increased to reach the annealing target.", json_schema_extra={"source_attribute_names": ["heating_rate"], "example_values": [], "required": "context_dependent", "confidence": "medium", "value_type": "quantity"})
    heating_rate_units: str | None = Field(None, description="Units for heating_rate.", json_schema_extra={"unit_for": "heating_rate"})
    cooling_method: str | None = Field(None, description="The method used to cool the sample after the annealing duration.", json_schema_extra={"source_attribute_names": ["cooling_method"], "example_values": [], "required": "context_dependent", "confidence": "medium"})
    input_state: str | None = Field(None, description="The state or condition of the sample before the annealing process.", json_schema_extra={"source_attribute_names": ["input_state"], "example_values": [], "required": "optional", "confidence": "medium"})
    output_state: str | None = Field(None, description="The state or condition of the sample after the annealing process.", json_schema_extra={"source_attribute_names": ["output_state"], "example_values": [], "required": "optional", "confidence": "medium"})
    container: str | None = Field(None, description="The material or type of container used to hold the sample inside the furnace.", json_schema_extra={"source_attribute_names": ["container"], "example_values": [], "required": "optional", "confidence": "medium"})

class Rinsing(Cleaning):
    '''
    The process of washing a sample with a liquid medium to remove residual chemicals, electrolytes, or contaminants from the surface or structure.
    Synonyms: Washing, Cleaning (liquid), Soaking
    '''
    process_identifier: str | None = Field("Rinsing", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Rinsing", description="Human readable process name from the source schema.")
    rinsing_medium: str | None = Field(None, description="The liquid solvent used to rinse the sample.", json_schema_extra={"source_attribute_names": ["rinsing_medium", "medium", "cleaning_medium"], "example_values": ["distilled water", "ethanol", "ultrapure water"], "required": "usually_required", "confidence": "high"})
    duration: float | str | None = Field(None, description="The length of time the sample is rinsed or soaked.", json_schema_extra={"source_attribute_names": ["duration"], "example_values": [], "required": "optional", "confidence": "high", "value_type": "quantity"})
    duration_units: str | None = Field(None, description="Units for duration.", json_schema_extra={"source_attribute_names": ["duration_unit"], "example_values": [], "required": "optional", "confidence": "high", "unit_for": "duration"})
    medium_concentration: str | None = Field(None, description="The concentration of the rinsing agent in the medium.", json_schema_extra={"source_attribute_names": ["rinsing_medium_concentration"], "example_values": [], "required": "context_dependent", "confidence": "medium"})
    input_state: str | None = Field(None, description="The state of the sample before the rinsing process.", json_schema_extra={"source_attribute_names": ["input_state"], "example_values": ["as-dealloyed"], "required": "optional", "confidence": "medium"})
    output_state: str | None = Field(None, description="The state of the sample after the rinsing process.", json_schema_extra={"source_attribute_names": ["output_state"], "example_values": [], "required": "optional", "confidence": "medium"})
    temperature: float | str | None = Field(None, description="The temperature of the rinsing medium.", json_schema_extra={"source_attribute_names": ["temperature"], "example_values": ["boiling"], "required": "context_dependent", "confidence": "medium", "value_type": "quantity"})
    temperature_units: str | None = Field(None, description="Units for temperature.", json_schema_extra={"unit_for": "temperature"})

class Drying(BaseModel):
    '''
    The process of removing a liquid medium from a sample, typically via evaporation, air flow, or vacuum.
    Synonyms: Air Drying, Vacuum Drying
    '''
    process_identifier: str | None = Field("Drying", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Drying", description="Human readable process name from the source schema.")
    drying_atmosphere: str | None = Field(None, description="The gas or environment used to facilitate drying.", json_schema_extra={"source_attribute_names": ["drying_medium", "atmosphere"], "example_values": ["ambient air", "vacuum", "Argon"], "required": "usually_required", "confidence": "high"})
    duration: float | str | None = Field(None, description="The length of time the sample is dried.", json_schema_extra={"source_attribute_names": ["duration"], "example_values": [], "required": "optional", "confidence": "high", "value_type": "quantity"})
    duration_units: str | None = Field(None, description="Units for duration.", json_schema_extra={"unit_for": "duration"})
    temperature: float | str | None = Field(None, description="The temperature during the drying process.", json_schema_extra={"source_attribute_names": ["temperature"], "example_values": ["room temperature"], "required": "optional", "confidence": "high", "value_type": "quantity"})
    temperature_units: str | None = Field(None, description="Units for temperature.", json_schema_extra={"unit_for": "temperature"})
    equipment: str | None = Field(None, description="The device used to perform drying (e.g., vacuum oven).", json_schema_extra={"source_attribute_names": ["equipment"], "example_values": [], "required": "context_dependent", "confidence": "high"})
    output_state: str | None = Field(None, description="The state of the sample after drying.", json_schema_extra={"source_attribute_names": ["output_state"], "example_values": [], "required": "optional", "confidence": "medium"})

class Quenching(HeatTreatment):
    '''
    The process of rapidly cooling a material, typically from an elevated temperature, to preserve a specific microstructure or phase.
    Synonyms: water quenching, rapid cooling
    '''
    process_identifier: str | None = Field("quenching", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Quenching", description="Human readable process name from the source schema.")
    quenching_medium: str | None = Field(None, description="The medium used to rapidly cool the material.", json_schema_extra={"source_attribute_names": ["quenching_medium"], "example_values": ["water"], "required": "usually_required", "confidence": "high"})

class ElectrochemicalDealloying(Dealloying):
    '''
    The selective dissolution of a less noble component from an alloy using an external electric potential or current to control the leaching process and create a nanoporous structure.
    Synonyms: electrochemical etching, potentiostatic dealloying, galvanostatic dealloying, pulse electrochemical dealloying
    '''
    process_identifier: str | None = Field("Electrochemical Dealloying", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Electrochemical Dealloying", description="Human readable process name from the source schema.")
    potential: float | str | None = Field(None, description="The applied electrochemical potential or voltage range used to drive the dissolution.", json_schema_extra={"source_attribute_names": ["potential", "voltage", "dealloying_potentials", "potential_range", "potential_range_min", "potential_range_max"], "example_values": ["650 mV", "1.0 V"], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    potential_units: str | None = Field(None, description="Units for potential.", json_schema_extra={"unit_for": "potential"})
    control_mode: str | None = Field(None, description="The mode of electrochemical control (e.g., constant potential or constant current).", json_schema_extra={"source_attribute_names": ["control_mode", "control_type"], "example_values": ["Potentiostatic", "galvanostatic"], "required": "usually_required", "confidence": "high"})
    reference_electrode: str | None = Field(None, description="The electrode used as a stable reference to measure and control the applied potential.", json_schema_extra={"source_attribute_names": ["reference_electrode", "potential_reference", "reference_electrode_model"], "example_values": ["Ag/AgCl"], "required": "usually_required", "confidence": "high"})
    counter_electrode: str | None = Field(None, description="The electrode that completes the electrical circuit in the electrochemical cell.", json_schema_extra={"source_attribute_names": ["counter_electrode", "counter_electrode_material"], "example_values": ["platinum wire", "Silver wire"], "required": "usually_required", "confidence": "high"})
    working_electrode: str | None = Field(None, description="The electrode consisting of the alloy sample being dealloyed.", json_schema_extra={"source_attribute_names": ["working_electrode", "work_electrode"], "example_values": ["alloy sheet"], "required": "optional", "confidence": "medium"})
    electrolyte_formula: str | None = Field(None, description="The chemical composition of the electrolyte solution.", json_schema_extra={"source_attribute_names": ["electrolyte_formula", "electrolyte"], "example_values": ["HClO4", "HNO3"], "required": "usually_required", "confidence": "high"})
    electrolyte_concentration: str | None = Field(None, description="The concentration of the electrolyte used.", json_schema_extra={"source_attribute_names": ["electrolyte_concentration", "concentration"], "example_values": ["1 M", "70% stock"], "required": "usually_required", "confidence": "high"})
    duration: float | str | None = Field(None, description="The total time the sample is subjected to the electrochemical process.", json_schema_extra={"source_attribute_names": ["duration", "duration_0.8V", "duration_1.3V"], "example_values": ["17 h"], "required": "usually_required", "confidence": "medium", "value_type": "quantity"})
    duration_units: str | None = Field(None, description="Units for duration.", json_schema_extra={"unit_for": "duration"})
    current_threshold: float | str | None = Field(None, description="The electrical current value used as a criterion to stop the process.", json_schema_extra={"source_attribute_names": ["current_threshold", "dissolution_current"], "example_values": [], "required": "context_dependent", "confidence": "medium", "value_type": "quantity"})
    current_threshold_units: str | None = Field(None, description="Units for current_threshold.", json_schema_extra={"unit_for": "current_threshold"})
    pulse_on_time: float | str | None = Field(None, description="The duration of the 'on' cycle in pulse electrochemical dealloying.", json_schema_extra={"source_attribute_names": ["pulse_on_time"], "example_values": [], "required": "context_dependent", "confidence": "high", "value_type": "quantity"})
    pulse_on_time_units: str | None = Field(None, description="Units for pulse_on_time.", json_schema_extra={"unit_for": "pulse_on_time"})
    pulse_off_time: float | str | None = Field(None, description="The duration of the 'off' cycle in pulse electrochemical dealloying.", json_schema_extra={"source_attribute_names": ["pulse_off_time"], "example_values": [], "required": "context_dependent", "confidence": "high", "value_type": "quantity"})
    pulse_off_time_units: str | None = Field(None, description="Units for pulse_off_time.", json_schema_extra={"unit_for": "pulse_off_time"})

class ChemicalDealloying(Dealloying):
    '''
    The selective dissolution of a less noble component from an alloy using a chemical solution (typically acid or base) under free corrosion conditions without an external electrical drive.
    Synonyms: chemical etching, selective leaching, free corrosion dealloying
    '''
    process_identifier: str | None = Field("Chemical Dealloying", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Chemical Dealloying", description="Human readable process name from the source schema.")
    electrolyte_formula: str | None = Field(None, description="The chemical composition of the etching solution.", json_schema_extra={"source_attribute_names": ["electrolyte_formula", "electrolyte"], "example_values": ["nitric acid", "HCl"], "required": "usually_required", "confidence": "high"})
    electrolyte_concentration: str | None = Field(None, description="The concentration of the electrolyte solution.", json_schema_extra={"source_attribute_names": ["electrolyte_concentration", "concentration"], "example_values": ["concentrated"], "required": "usually_required", "confidence": "high"})
    duration: float | str | None = Field(None, description="The length of time the alloy is immersed in the chemical solution.", json_schema_extra={"source_attribute_names": ["duration"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    duration_units: str | None = Field(None, description="Units for duration.", json_schema_extra={"unit_for": "duration"})
    temperature: float | str | None = Field(None, description="The temperature at which the chemical dealloying is performed.", json_schema_extra={"source_attribute_names": ["temperature"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    temperature_units: str | None = Field(None, description="Units for temperature.", json_schema_extra={"unit_for": "temperature"})
    input_state: str | None = Field(None, description="The state or composition of the material before the dealloying process.", json_schema_extra={"source_attribute_names": ["input_state", "input_material"], "example_values": ["as-deposited film"], "required": "optional", "confidence": "medium"})
    output_state: str | None = Field(None, description="The resulting state or morphology of the material after dealloying.", json_schema_extra={"source_attribute_names": ["output_state", "output_material"], "example_values": ["np-Au film"], "required": "optional", "confidence": "medium"})
    surfactant: str | None = Field(None, description="Chemical additives used to modify the surface tension or stability of the process.", json_schema_extra={"source_attribute_names": ["surfactant", "surfactants"], "example_values": ["CTAB"], "required": "optional", "confidence": "medium"})

class Cutting(MechanicalProcessing):
    '''
    The process of dividing a material or sample into smaller pieces, slices, or specific geometries using mechanical or electrical means.
    Synonyms: sample cutting, sectioning, slicing, dividing
    '''
    process_identifier: str | None = Field("cutting", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Cutting", description="Human readable process name from the source schema.")
    output_geometry: str | None = Field(None, description="The resulting shape or geometric form of the sample after cutting.", json_schema_extra={"source_attribute_names": ["output_geometry", "sample_geometry", "shape"], "example_values": ["cuboids", "plates", "disks", "slices"], "required": "usually_required", "confidence": "high"})
    output_dimensions: float | str | None = Field(None, description="The specific measurements (length, width, thickness, diameter) of the cut sample.", json_schema_extra={"source_attribute_names": ["cut_dimensions", "cut_size", "output_width", "output_length", "output_thickness", "output_dimensions", "sample_diameter", "sample_thickness", "sample_dimensions", "size"], "example_values": ["1 x 1 x 2 mm3", "~4 mm"], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    output_dimensions_units: str | None = Field(None, description="Units for output_dimensions.", json_schema_extra={"unit_for": "output_dimensions"})
    cutting_tool: str | None = Field(None, description="The instrument or equipment used to perform the cutting operation.", json_schema_extra={"source_attribute_names": ["tool", "tool_name"], "example_values": ["electric discharge machining", "diamond wire saw"], "required": "optional", "confidence": "high"})
    input_material: str | None = Field(None, description="The material being processed.", json_schema_extra={"source_attribute_names": ["input_material", "material"], "example_values": ["Au-Ag alloy"], "required": "optional", "confidence": "medium"})
    input_state: str | None = Field(None, description="The physical state or form of the material before the cutting process (e.g., rolled, annealed, bulk).", json_schema_extra={"source_attribute_names": ["input_state", "sample_form"], "example_values": ["Homogenized ingot", "Bulk alloy pellets"], "required": "optional", "confidence": "medium"})

class WireDrawing(MechanicalShaping):
    '''
    A mechanical process of reducing the cross-section of a rod or wire by pulling it through a shaped die to achieve a desired cylindrical geometry.
    Synonyms: wire drawing, drawing
    '''
    process_identifier: str | None = Field("Wire Drawing", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Wire Drawing", description="Human readable process name from the source schema.")
    sample_diameter: float | str | None = Field(None, description="The final diameter of the drawn wire/sample.", json_schema_extra={"source_attribute_names": ["sample_diameter"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    sample_diameter_units: str | None = Field(None, description="Units for sample_diameter.", json_schema_extra={"unit_for": "sample_diameter"})
    sample_length: float | str | None = Field(None, description="The final length of the drawn wire/sample.", json_schema_extra={"source_attribute_names": ["sample_length"], "example_values": [], "required": "optional", "confidence": "high", "value_type": "quantity"})
    sample_length_units: str | None = Field(None, description="Units for sample_length.", json_schema_extra={"unit_for": "sample_length"})
    output_geometry: str | None = Field(None, description="The geometric shape of the sample after the drawing process.", json_schema_extra={"source_attribute_names": ["output_geometry"], "example_values": ["cylindrical form"], "required": "usually_required", "confidence": "high"})
    tool: str | None = Field(None, description="The tool (e.g., die) used to perform the drawing operation.", json_schema_extra={"source_attribute_names": ["tool_type", "tool"], "example_values": [], "required": "usually_required", "confidence": "high"})
    target_dimensions: str | None = Field(None, description="The specified dimensions for the processed sample.", json_schema_extra={"source_attribute_names": ["target_dimensions"], "example_values": [], "required": "optional", "confidence": "medium"})

class Ultramicrotomy(BaseModel):
    '''
    The process of cutting extremely thin sections of a sample, typically for transmission electron microscopy (TEM), using an ultramicrotome.
    Synonyms: ultra-microtomy, ultrathin sectioning
    '''
    process_identifier: str | None = Field("ultramicrotomy", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Ultramicrotomy", description="Human readable process name from the source schema.")
    equipment: str | None = Field(None, description="The specific ultramicrotome instrument used for sectioning.", json_schema_extra={"source_attribute_names": ["equipment"], "example_values": [], "required": "usually_required", "confidence": "high"})
    section_thickness: float | str | None = Field(None, description="The thickness of the resulting sample slices.", json_schema_extra={"source_attribute_names": ["thickness"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    section_thickness_units: str | None = Field(None, description="Units for section_thickness.", json_schema_extra={"unit_for": "section_thickness"})
    cutting_speed: float | str | None = Field(None, description="The speed at which the knife cuts through the sample.", json_schema_extra={"source_attribute_names": ["cutting_speed"], "example_values": [], "required": "optional", "confidence": "high", "value_type": "quantity"})
    cutting_speed_units: str | None = Field(None, description="The unit of measurement for the cutting speed.", json_schema_extra={"source_attribute_names": ["cutting_speed_unit"], "example_values": [], "required": "optional", "confidence": "high", "unit_for": "cutting_speed"})

class FreeCorrosionDealloying(Dealloying):
    '''
    Removal of a selective component from an alloy through immersion in an electrolyte without the application of an external electrical potential.
    Synonyms: chemical dealloying, spontaneous dealloying, free corrosion
    '''
    process_identifier: str | None = Field("free_corrosion_dealloying", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Free Corrosion Dealloying", description="Human readable process name from the source schema.")
    electrolyte_formula: str | None = Field(None, description="The chemical composition or formula of the electrolyte used for immersion.", json_schema_extra={"source_attribute_names": ["electrolyte_formula", "electrolyte"], "example_values": ["concentrated nitric acid"], "required": "usually_required", "confidence": "high"})
    electrolyte_concentration: str | None = Field(None, description="The concentration of the electrolyte solution.", json_schema_extra={"source_attribute_names": ["electrolyte_concentration", "concentration", "electrolyte"], "example_values": [], "required": "usually_required", "confidence": "high"})
    electrolyte_concentration_unit: str | None = Field(None, description="The unit used to measure the electrolyte concentration.", json_schema_extra={"source_attribute_names": ["electrolyte_concentration_unit"], "example_values": [], "required": "optional", "confidence": "high"})
    duration: float | str | None = Field(None, description="The length of time the sample was immersed in the electrolyte.", json_schema_extra={"source_attribute_names": ["duration"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    duration_units: str | None = Field(None, description="The unit of time for the immersion duration.", json_schema_extra={"source_attribute_names": ["duration_unit"], "example_values": [], "required": "optional", "confidence": "high", "unit_for": "duration"})
    temperature: float | str | None = Field(None, description="The temperature at which the immersion process was conducted.", json_schema_extra={"source_attribute_names": ["temperature"], "example_values": [], "required": "optional", "confidence": "medium", "value_type": "quantity"})
    temperature_units: str | None = Field(None, description="The unit of temperature.", json_schema_extra={"source_attribute_names": ["temperature_unit"], "example_values": [], "required": "optional", "confidence": "high", "unit_for": "temperature"})

class AlloyMelting(AlloyPreparation):
    '''
    The process of heating elemental materials above their melting points to create a homogeneous metallic alloy, typically resulting in an ingot. This operation may employ different heating methods such as arc, induction, or electron beam melting.
    Synonyms: arc melting, induction melting, electron beam melting, alloy synthesis via melting, master alloy preparation
    '''
    process_identifier: str | None = Field("alloy_melting", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Alloy Melting", description="Human readable process name from the source schema.")
    input_materials: List[str] | None = Field(None, description="The elemental materials or precursor materials used to create the alloy.", json_schema_extra={"source_attribute_names": ["input_materials", "input_material", "input_material_list", "material", "material_composition"], "example_values": ["Al", "Au", "Ag", "Pd", "Co", "Cu"], "required": "usually_required", "confidence": "high"})
    input_material_purity: str | None = Field(None, description="The purity level of the starting elemental materials.", json_schema_extra={"source_attribute_names": ["input_material_purity", "material_purity", "input_purity_al", "input_purity_pure_palladium", "input_purity_1", "input_purity_2", "wire_purity"], "example_values": [], "required": "usually_required", "confidence": "high"})
    melting_equipment: str | None = Field(None, description="The instrument or furnace used to provide the heat for melting.", json_schema_extra={"source_attribute_names": ["equipment", "equipment_type"], "example_values": ["arc melter", "high-frequency induction heating", "electron beam melting equipment"], "required": "usually_required", "confidence": "high"})
    atmosphere: str | None = Field(None, description="The gas environment maintained during the melting process to prevent oxidation or contamination.", json_schema_extra={"source_attribute_names": ["atmosphere"], "example_values": ["inert atmosphere", "argon"], "required": "usually_required", "confidence": "high"})
    crucible_material: str | None = Field(None, description="The material of the container (crucible) used to hold the materials during melting.", json_schema_extra={"source_attribute_names": ["crucible_material", "vessel", "container_material"], "example_values": ["quartz"], "required": "context_dependent", "confidence": "high"})
    melting_temperature: float | str | None = Field(None, description="The temperature at which the materials were melted.", json_schema_extra={"source_attribute_names": ["temperature"], "example_values": [], "required": "optional", "confidence": "medium", "value_type": "quantity"})
    melting_temperature_units: str | None = Field(None, description="Units for melting_temperature.", json_schema_extra={"unit_for": "melting_temperature"})
    melting_duration: float | str | None = Field(None, description="The amount of time the materials were held at melting temperature.", json_schema_extra={"source_attribute_names": ["duration"], "example_values": [], "required": "optional", "confidence": "medium", "value_type": "quantity"})
    melting_duration_units: str | None = Field(None, description="Units for melting_duration.", json_schema_extra={"unit_for": "melting_duration"})
    output_form: str | None = Field(None, description="The final physical form of the synthesized alloy (e.g., ingot).", json_schema_extra={"source_attribute_names": ["output_state"], "example_values": ["master alloy ingot", "precursor alloy"], "required": "optional", "confidence": "medium"})

class ElectrochemicalPolymerization(SurfaceCoating):
    '''
    The process of using an electric current to induce the polymerization of a monomer onto a conductive substrate, creating a polymer layer.
    Synonyms: electropolymerization, electrochemical growth of polymers
    '''
    process_identifier: str | None = Field("electrochemical_polymerization", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Electrochemical Polymerization", description="Human readable process name from the source schema.")
    control_mode: str | None = Field(None, description="The electrical control mode (e.g., potentiostatic, galvanostatic, or potentiodynamic) used for polymerization.", json_schema_extra={"source_attribute_names": ["control_mode"], "example_values": [], "required": "usually_required", "confidence": "high"})
    potential_range: str | None = Field(None, description="The range of electrical potentials applied during the polymerization process.", json_schema_extra={"source_attribute_names": ["potential_range"], "example_values": [], "required": "usually_required", "confidence": "high"})
    number_of_cycles: int | None = Field(None, description="The number of potential cycles performed, typically in the case of cyclic voltammetry polymerization.", json_schema_extra={"source_attribute_names": ["number_of_cycles"], "example_values": [], "required": "context_dependent", "confidence": "high"})
    duration: float | str | None = Field(None, description="The total time elapsed during the polymerization process.", json_schema_extra={"source_attribute_names": ["duration"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    duration_units: str | None = Field(None, description="Units for duration.", json_schema_extra={"unit_for": "duration"})
    output_thickness: float | str | None = Field(None, description="The target or resulting thickness of the polymer layer deposited on the surface.", json_schema_extra={"source_attribute_names": ["output_thickness"], "example_values": [], "required": "optional", "confidence": "high", "value_type": "quantity"})
    output_thickness_units: str | None = Field(None, description="Units for output_thickness.", json_schema_extra={"unit_for": "output_thickness"})
    monomer: str | None = Field(None, description="The chemical species (monomer) that is polymerized during the process.", json_schema_extra={"source_attribute_names": ["monomer"], "example_values": ["polypyrrole (PPy)"], "required": "usually_required", "confidence": "high"})
    electrolyte: str | None = Field(None, description="The solution containing ions used to conduct electricity during polymerization.", json_schema_extra={"source_attribute_names": ["electrolyte"], "example_values": [], "required": "usually_required", "confidence": "high"})

class ElectrolytePreparation(PrecursorPreparation):
    '''
    The process of preparing a chemical solution used as an electrolyte, typically involving mixing solvents, solutes, and additives to achieve specific concentrations.
    Synonyms: electrolyte solution preparation, mixing electrolyte
    '''
    process_identifier: str | None = Field("electrolyte_preparation", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Electrolyte Preparation", description="Human readable process name from the source schema.")
    electrolyte_formula: str | None = Field(None, description="The chemical composition or formula of the electrolyte solution.", json_schema_extra={"source_attribute_names": ["electrolyte_formula", "base_chemical", "chemical_a", "chemical_b"], "example_values": ["HNO 3 and H2O", "sulfuric acid"], "required": "usually_required", "confidence": "high"})
    concentration: str | None = Field(None, description="The concentration of the primary chemical component in the electrolyte.", json_schema_extra={"source_attribute_names": ["concentration"], "example_values": ["70% stock solution"], "required": "usually_required", "confidence": "high"})
    volume: float | str | None = Field(None, description="The volume of the components used to prepare the solution.", json_schema_extra={"source_attribute_names": ["electrolyte_volume", "volume", "volume_added_a", "volume_added_b"], "example_values": ["30 ml (HNO3) + 60 ml (H2O)"], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    volume_units: str | None = Field(None, description="Units for volume.", json_schema_extra={"unit_for": "volume"})
    surfactant_list: List[str] | None = Field(None, description="List of surfactants added to the electrolyte solution.", json_schema_extra={"source_attribute_names": ["surfactant_list"], "example_values": [], "required": "optional", "confidence": "medium"})

class Rolling(MechanicalProcessing):
    '''
    The process of reducing the thickness of a material (such as an alloy ingot or sheet) by passing it through rollers or applying mechanical compression to achieve a target thickness and refine the material's structure.
    Synonyms: cold rolling, hot rolling, mechanical deformation, cold working, pressing
    '''
    process_identifier: str | None = Field("rolling", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Rolling", description="Human readable process name from the source schema.")
    target_thickness: float | str | None = Field(None, description="The intended or resulting thickness of the material after the deformation process.", json_schema_extra={"source_attribute_names": ["output_thickness", "target_thickness", "sample_thickness"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    target_thickness_units: str | None = Field(None, description="The unit of measurement for the target thickness.", json_schema_extra={"source_attribute_names": ["output_thickness_unit"], "example_values": [], "required": "usually_required", "confidence": "high", "unit_for": "target_thickness"})
    material_state: str | None = Field(None, description="The state or condition of the material during the process, such as 'cold' or 'homogenized'.", json_schema_extra={"source_attribute_names": ["material_state", "condition"], "example_values": [], "required": "usually_required", "confidence": "high"})
    equipment: str | None = Field(None, description="The specific hardware or machine used to perform the deformation (e.g., rolling mill, press).", json_schema_extra={"source_attribute_names": ["equipment"], "example_values": [], "required": "optional", "confidence": "high"})
    output_geometry: str | None = Field(None, description="The geometric shape of the material after processing, typically sheets.", json_schema_extra={"source_attribute_names": ["output_geometry"], "example_values": [], "required": "optional", "confidence": "medium"})
    number_of_steps: int | None = Field(None, description="The number of individual rolling or pressing passes performed.", json_schema_extra={"source_attribute_names": ["steps"], "example_values": [], "required": "optional", "confidence": "medium"})
    deformation_frequency: float | str | None = Field(None, description="The frequency or pattern of the cold working cycles.", json_schema_extra={"source_attribute_names": ["frequency"], "example_values": [], "required": "context_dependent", "confidence": "medium", "value_type": "quantity"})
    deformation_frequency_units: str | None = Field(None, description="Units for deformation_frequency.", json_schema_extra={"unit_for": "deformation_frequency"})

class ThermalTreatment(ThermalTreatment):
    '''
    The application of heat to a material for a specific duration and often under a controlled atmosphere to modify its structural or textural properties.
    Synonyms: Annealing, Heat treatment, Thermal processing
    '''
    process_identifier: str | None = Field("thermal_treatment", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Thermal Treatment", description="Human readable process name from the source schema.")
    temperature: float | str | None = Field(None, description="The temperature at which the material is treated.", json_schema_extra={"source_attribute_names": ["temperature"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    temperature_units: str | None = Field(None, description="Units for temperature.", json_schema_extra={"unit_for": "temperature"})
    duration: float | str | None = Field(None, description="The length of time the material is exposed to the heat treatment.", json_schema_extra={"source_attribute_names": ["duration"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    duration_units: str | None = Field(None, description="Units for duration.", json_schema_extra={"unit_for": "duration"})
    atmosphere: str | None = Field(None, description="The gas environment surrounding the sample during treatment.", json_schema_extra={"source_attribute_names": ["atmosphere"], "example_values": [], "required": "context_dependent", "confidence": "high"})

class AcidTreatment(ChemicalTreatment):
    '''
    Immersion of a material in an acidic solution to chemically modify the surface or internal structure.
    Synonyms: Acid immersion, Chemical etching, Acid wash
    '''
    process_identifier: str | None = Field("acid_treatment", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Acid Treatment", description="Human readable process name from the source schema.")
    medium: str | None = Field(None, description="The type of acid solution used for the treatment.", json_schema_extra={"source_attribute_names": ["medium"], "example_values": [], "required": "usually_required", "confidence": "high"})
    medium_concentration: str | None = Field(None, description="The concentration of the acid in the medium.", json_schema_extra={"source_attribute_names": ["medium_concentration"], "example_values": [], "required": "usually_required", "confidence": "high"})
    duration: float | str | None = Field(None, description="The length of time the sample is immersed in the acid.", json_schema_extra={"source_attribute_names": ["duration"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    duration_units: str | None = Field(None, description="Units for duration.", json_schema_extra={"unit_for": "duration"})
    temperature: float | str | None = Field(None, description="The temperature of the acid solution during treatment.", json_schema_extra={"source_attribute_names": ["temperature"], "example_values": [], "required": "optional", "confidence": "medium", "value_type": "quantity"})
    temperature_units: str | None = Field(None, description="Units for temperature.", json_schema_extra={"unit_for": "temperature"})
    volume: float | str | None = Field(None, description="The total volume of the acid solution used.", json_schema_extra={"source_attribute_names": ["volume"], "example_values": [], "required": "optional", "confidence": "medium", "value_type": "quantity"})
    volume_units: str | None = Field(None, description="Units for volume.", json_schema_extra={"unit_for": "volume"})

class ResinImpregnation(BaseModel):
    '''
    The process of infiltrating a sample with a resin, often under vacuum, to stabilize the material or provide structural support for subsequent processing such as sectioning.
    Synonyms: epoxy impregnation, vacuum impregnation, resin infiltration
    '''
    process_identifier: str | None = Field("resin_impregnation", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Resin Impregnation", description="Human readable process name from the source schema.")
    impregnation_medium: str | None = Field(None, description="The resin or medium used to infiltrate the sample.", json_schema_extra={"source_attribute_names": ["medium"], "example_values": ["epoxy resin"], "required": "usually_required", "confidence": "high"})
    curing_temperature: float | str | None = Field(None, description="The temperature at which the impregnated sample is cured to harden the resin.", json_schema_extra={"source_attribute_names": ["temperature"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    curing_temperature_units: str | None = Field(None, description="The unit of measurement for the curing temperature.", json_schema_extra={"source_attribute_names": ["temperature_unit"], "example_values": [], "required": "usually_required", "confidence": "high", "unit_for": "curing_temperature"})
    curing_duration: float | str | None = Field(None, description="The length of time the sample is kept at the curing temperature.", json_schema_extra={"source_attribute_names": ["duration"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    curing_duration_units: str | None = Field(None, description="The unit of measurement for the curing duration.", json_schema_extra={"source_attribute_names": ["duration_unit"], "example_values": [], "required": "usually_required", "confidence": "high", "unit_for": "curing_duration"})

class SlurryPreparation(BaseModel):
    '''
    The process of mixing a powdered material with a binder to create a slurry for subsequent application.
    Synonyms: slurry preparation, powder mixing
    '''
    process_identifier: str | None = Field("slurry_preparation", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Slurry Preparation", description="Human readable process name from the source schema.")
    material: str | None = Field(None, description="The primary material used to form the slurry.", json_schema_extra={"source_attribute_names": ["material"], "example_values": ["metal powder"], "required": "usually_required", "confidence": "high"})
    binder_type: str | None = Field(None, description="The type of binder used to hold the powder particles together.", json_schema_extra={"source_attribute_names": ["binder_type"], "example_values": ["water-soluble binder"], "required": "usually_required", "confidence": "high"})

class Sintering(Sintering):
    '''
    The process of compacting and forming a solid mass of material by heat or pressure without melting it to the point of liquefaction.
    Synonyms: thermal bonding, sintering process
    '''
    process_identifier: str | None = Field("sintering", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Sintering", description="Human readable process name from the source schema.")
    sintering_temperature: float | str | None = Field(None, description="The temperature maintained during the sintering process.", json_schema_extra={"source_attribute_names": ["sintering_temperature"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    sintering_temperature_units: str | None = Field(None, description="Units for sintering_temperature.", json_schema_extra={"unit_for": "sintering_temperature"})
    sintering_duration: float | str | None = Field(None, description="The total time the material is held at the sintering temperature.", json_schema_extra={"source_attribute_names": ["sintering_duration"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    sintering_duration_units: str | None = Field(None, description="Units for sintering_duration.", json_schema_extra={"unit_for": "sintering_duration"})
    substrate: str | None = Field(None, description="The base material onto which the slurry is applied before sintering.", json_schema_extra={"source_attribute_names": ["substrate"], "example_values": ["paper sheet"], "required": "context_dependent", "confidence": "high"})

class ElectrochemicalActivation(BaseModel):
    '''
    The use of electrical potential in an electrolyte solution to remove surface oxides or modify the surface state of a sample, often using techniques like cyclic voltammetry, to prepare it for subsequent experiments.
    Synonyms: Electrochemical reduction, Electrochemical cleaning, Electrochemical surface preparation
    '''
    process_identifier: str | None = Field("Electrochemical Activation", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Electrochemical Activation", description="Human readable process name from the source schema.")
    electrolyte_formula: str | None = Field(None, description="Chemical formula of the electrolyte used for activation", json_schema_extra={"source_attribute_names": ["electrolyte_formula"], "example_values": [], "required": "usually_required", "confidence": "high"})
    electrolyte_concentration: str | None = Field(None, description="Concentration of the electrolyte used for activation", json_schema_extra={"source_attribute_names": ["electrolyte_concentration"], "example_values": [], "required": "usually_required", "confidence": "high"})
    reference_electrode: str | None = Field(None, description="Reference electrode used during activation", json_schema_extra={"source_attribute_names": ["reference_electrode"], "example_values": [], "required": "usually_required", "confidence": "high"})
    counter_electrode: str | None = Field(None, description="Counter electrode used during activation", json_schema_extra={"source_attribute_names": ["counter_electrode"], "example_values": [], "required": "usually_required", "confidence": "high"})
    potential_range: str | None = Field(None, description="The range of electrical potentials applied during the activation process", json_schema_extra={"source_attribute_names": ["potential_range"], "example_values": [], "required": "usually_required", "confidence": "high"})
    scan_rate: float | str | None = Field(None, description="The rate at which the potential is scanned during cyclic voltammetry", json_schema_extra={"source_attribute_names": ["scan_rate"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    scan_rate_units: str | None = Field(None, description="Units for scan_rate.", json_schema_extra={"unit_for": "scan_rate"})
    temperature: float | str | None = Field(None, description="Temperature at which the activation process is performed", json_schema_extra={"source_attribute_names": ["temperature"], "example_values": [], "required": "optional", "confidence": "high", "value_type": "quantity"})
    temperature_units: str | None = Field(None, description="Units for temperature.", json_schema_extra={"unit_for": "temperature"})
    duration: float | str | None = Field(None, description="Total time duration of the activation process", json_schema_extra={"source_attribute_names": ["duration"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    duration_units: str | None = Field(None, description="Units for duration.", json_schema_extra={"unit_for": "duration"})

class BlowCasting(BaseModel):
    '''
    A metal casting process where a precursor alloy is shaped into a specific geometry, such as a rod, using a blowing technique.
    Synonyms: Blow casting
    '''
    process_identifier: str | None = Field("Blow casting", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Blow Casting", description="Human readable process name from the source schema.")
    casting_technique: str | None = Field(None, description="The specific variant or technique of casting used.", json_schema_extra={"source_attribute_names": ["technique"], "example_values": ["blow casting"], "required": "usually_required", "confidence": "high"})
    output_geometry: str | None = Field(None, description="The geometric shape of the produced part.", json_schema_extra={"source_attribute_names": ["output_geometry"], "example_values": ["rod"], "required": "usually_required", "confidence": "high"})

class Polishing(BaseModel):
    '''
    The mechanical process of smoothing or refining a material surface using abrasive agents to achieve a specific finish, planarity, or cleanliness.
    Synonyms: surface polishing, mechanical abrasion, surface preparation
    '''
    process_identifier: str | None = Field("polishing", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Polishing", description="Human readable process name from the source schema.")
    abrasive_material: str | None = Field(None, description="The substance or tool used to perform the abrasive polishing.", json_schema_extra={"source_attribute_names": ["abrasive_material", "polishing_medium"], "example_values": ["abrasive pastes", "powders", "SiC paper"], "required": "usually_required", "confidence": "high"})
    abrasive_grit_size: float | str | None = Field(None, description="The particle size or grit grade of the abrasive material.", json_schema_extra={"source_attribute_names": ["abrasive_size", "grit_size", "abrasive_grit"], "example_values": ["1 um"], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    abrasive_grit_size_units: str | None = Field(None, description="Units for abrasive_grit_size.", json_schema_extra={"unit_for": "abrasive_grit_size"})
    target_surface_finish: str | None = Field(None, description="The desired final state of the surface (e.g., mirror finish, specific roughness).", json_schema_extra={"source_attribute_names": ["output_surface_quality", "finish"], "example_values": ["diamond finish"], "required": "optional", "confidence": "medium"})
    polished_region: str | None = Field(None, description="The specific area or face of the sample that underwent polishing.", json_schema_extra={"source_attribute_names": ["side_polished", "polished_surface"], "example_values": ["one side"], "required": "context_dependent", "confidence": "medium"})
    substrate_material: str | None = Field(None, description="The material of the sample being polished.", json_schema_extra={"source_attribute_names": ["material"], "example_values": [], "required": "optional", "confidence": "medium"})

class ThermalCoarsening(HeatTreatment):
    '''
    A thermal process applied to nanoporous materials to induce structural evolution, specifically the coarsening of ligaments and adjustment of pore size through heating.
    Synonyms: annealing, thermal annealing, heat treatment, ligament coarsening
    '''
    process_identifier: str | None = Field("thermal coarsening", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Thermal Coarsening", description="Human readable process name from the source schema.")
    temperature: float | str | None = Field(None, description="The temperature at which the thermal treatment is performed.", json_schema_extra={"source_attribute_names": ["temperature"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    temperature_units: str | None = Field(None, description="The unit of measurement for temperature.", json_schema_extra={"source_attribute_names": ["temperature_unit"], "example_values": [], "required": "usually_required", "confidence": "high", "unit_for": "temperature"})
    duration: float | str | None = Field(None, description="The length of time the sample is exposed to the heating temperature.", json_schema_extra={"source_attribute_names": ["duration"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    duration_units: str | None = Field(None, description="The unit of measurement for duration.", json_schema_extra={"source_attribute_names": ["duration_unit"], "example_values": [], "required": "usually_required", "confidence": "high", "unit_for": "duration"})
    atmosphere: str | None = Field(None, description="The gaseous environment in which the heating is performed.", json_schema_extra={"source_attribute_names": ["atmosphere"], "example_values": [], "required": "usually_required", "confidence": "high"})
    equipment: str | None = Field(None, description="The heating instrument or furnace used.", json_schema_extra={"source_attribute_names": ["equipment"], "example_values": [], "required": "optional", "confidence": "medium"})
    coarsening_mechanism: str | None = Field(None, description="The physical mechanism driving the coarsening process.", json_schema_extra={"source_attribute_names": ["coarsening_mechanism"], "example_values": ["coalescence", "Ostwald ripening"], "required": "optional", "confidence": "medium"})
    target_ligament_size: float | str | None = Field(None, description="The intended final size of the ligaments after treatment.", json_schema_extra={"source_attribute_names": ["target_ligament_size"], "example_values": [], "required": "optional", "confidence": "medium", "value_type": "quantity"})
    target_ligament_size_units: str | None = Field(None, description="Units for target_ligament_size.", json_schema_extra={"unit_for": "target_ligament_size"})
    input_sample_state: str | None = Field(None, description="The state or characteristics of the sample before the process.", json_schema_extra={"source_attribute_names": ["input_sample_state"], "example_values": [], "required": "context_dependent", "confidence": "medium"})
    output_sample_state: str | None = Field(None, description="The state or characteristics of the sample after the process.", json_schema_extra={"source_attribute_names": ["output_sample_state"], "example_values": [], "required": "context_dependent", "confidence": "medium"})
    atmosphere_hydrogen_percentage: float | str | None = Field(None, description="The percentage of hydrogen in the process atmosphere.", json_schema_extra={"source_attribute_names": ["atmosphere_hydrogen_percentage"], "example_values": [], "required": "optional", "confidence": "medium", "value_type": "quantity"})
    atmosphere_hydrogen_percentage_units: str | None = Field(None, description="Units for atmosphere_hydrogen_percentage.", json_schema_extra={"unit_for": "atmosphere_hydrogen_percentage"})
    input_material: str | None = Field(None, description="The composition of the material being treated.", json_schema_extra={"source_attribute_names": ["input_material"], "example_values": ["NPG", "NPG-Pt"], "required": "optional", "confidence": "medium"})
    sample_relative_density: float | str | None = Field(None, description="The relative density of the sample.", json_schema_extra={"source_attribute_names": ["sample_relative_density"], "example_values": [], "required": "optional", "confidence": "medium", "value_type": "quantity"})
    sample_relative_density_units: str | None = Field(None, description="Units for sample_relative_density.", json_schema_extra={"unit_for": "sample_relative_density"})

class MeltSpinning(BaseModel):
    '''
    A process of rapid solidification where a molten material is ejected onto a rotating cold disk or roller to produce thin ribbons or flakes with a controlled microstructure (often amorphous or fine-grained).
    Synonyms: melt-spinning, rapid solidification spinning
    '''
    process_identifier: str | None = Field("melt_spinning", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Melt Spinning", description="Human readable process name from the source schema.")
    rotation_speed: float | str | None = Field(None, description="The angular or linear speed of the rotating roller during the spinning process.", json_schema_extra={"source_attribute_names": ["spinning_speed", "speed", "rotation_speed"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    rotation_speed_units: str | None = Field(None, description="Units for rotation_speed.", json_schema_extra={"unit_for": "rotation_speed"})
    roller_diameter: float | str | None = Field(None, description="The diameter of the rotating copper or metal roller used for quenching the melt.", json_schema_extra={"source_attribute_names": ["roller_diameter"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    roller_diameter_units: str | None = Field(None, description="Units for roller_diameter.", json_schema_extra={"unit_for": "roller_diameter"})
    input_material: str | None = Field(None, description="The chemical composition or identity of the alloy/material being spun.", json_schema_extra={"source_attribute_names": ["material_composition", "input_material", "alloy_composition"], "example_values": [], "required": "usually_required", "confidence": "high"})
    atmosphere: str | None = Field(None, description="The gaseous environment maintained during the spinning process to prevent oxidation.", json_schema_extra={"source_attribute_names": ["atmosphere"], "example_values": ["argon"], "required": "optional", "confidence": "high"})
    output_geometry: str | None = Field(None, description="The physical form or dimensions of the resulting solidified material.", json_schema_extra={"source_attribute_names": ["sample_form", "output_geometry"], "example_values": ["ribbons"], "required": "optional", "confidence": "medium"})
    roller_material: str | None = Field(None, description="The material of the rotating roller used for cooling.", json_schema_extra={"source_attribute_names": ["roller_material"], "example_values": ["copper"], "required": "optional", "confidence": "medium"})
    heating_method: str | None = Field(None, description="The method used to melt the pre-alloyed ingot before spinning.", json_schema_extra={"source_attribute_names": ["heating_method"], "example_values": ["induction heating"], "required": "context_dependent", "confidence": "medium"})
    tube_material: str | None = Field(None, description="The material of the crucible or tube holding the melt.", json_schema_extra={"source_attribute_names": ["tubing_material", "tube_material"], "example_values": [], "required": "context_dependent", "confidence": "medium"})
    equipment: str | None = Field(None, description="The specific apparatus or model of the melt spinner.", json_schema_extra={"source_attribute_names": ["equipment", "equipment_type"], "example_values": [], "required": "optional", "confidence": "medium"})

class SurfaceGrinding(BaseModel):
    '''
    The process of removing material from the surface of a sample using abrasives to achieve a specific surface finish, flatness, or smoothness.
    Synonyms: abrasive grinding, surface polishing
    '''
    process_identifier: str | None = Field("surface_grinding", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Surface Grinding", description="Human readable process name from the source schema.")
    abrasive_material: str | None = Field(None, description="The material used as an abrasive for the grinding process.", json_schema_extra={"source_attribute_names": ["abrasive_material"], "example_values": [], "required": "usually_required", "confidence": "high"})

class MechanicalGrinding(MechanicalProcessing):
    '''
    The process of reducing the bulk size of a material into smaller particles or a powder form through mechanical force.
    Synonyms: pulverization, size reduction, milling
    '''
    process_identifier: str | None = Field("mechanical_grinding", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Mechanical Grinding", description="Human readable process name from the source schema.")
    target_material_state: str | None = Field(None, description="The physical state or particle size of the material after the grinding process.", json_schema_extra={"source_attribute_names": ["material_state"], "example_values": ["fine powder"], "required": "usually_required", "confidence": "high"})

class SampleCutting(BaseModel):
    '''
    The process of dividing a bulk material into smaller pieces or specific shapes to prepare samples for subsequent experimental analysis.
    Synonyms: sectioning, dicing, cutting
    '''
    process_identifier: str | None = Field("sample_cutting", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Sample Cutting", description="Human readable process name from the source schema.")
    sample_shape: str | None = Field(None, description="The geometric shape of the resulting cut samples.", json_schema_extra={"source_attribute_names": ["sample_shape"], "example_values": [], "required": "usually_required", "confidence": "high"})

class TemGridMounting(SamplePreparation):
    '''
    The process of transferring sample slices or sections onto a support grid for Transmission Electron Microscopy (TEM) analysis.
    Synonyms: TEM mounting, grid loading, sample transfer to grid
    '''
    process_identifier: str | None = Field("TEM grid mounting", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("TEM Grid Mounting", description="Human readable process name from the source schema.")
    grid_type: str | None = Field(None, description="The material or design type of the grid used for mounting the sample.", json_schema_extra={"source_attribute_names": ["grid_type"], "example_values": [], "required": "usually_required", "confidence": "high"})
    grid_mesh: int | str | None = Field(None, description="The mesh size (number of wires per inch) of the support grid.", json_schema_extra={"source_attribute_names": ["grid_mesh"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    grid_mesh_units: str | None = Field(None, description="Units for grid_mesh.", json_schema_extra={"unit_for": "grid_mesh"})

class SpinCoating(Coating):
    '''
    A procedure where a liquid solution is applied to a substrate and rotated at high speed to produce a uniform thin film via centrifugal force.
    Synonyms: spin-coating
    '''
    process_identifier: str | None = Field("spin coating", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Spin Coating", description="Human readable process name from the source schema.")
    medium: str | None = Field(None, description="The liquid solution used for coating", json_schema_extra={"source_attribute_names": ["medium"], "example_values": [], "required": "usually_required", "confidence": "high"})
    medium_formula: str | None = Field(None, description="Chemical formula of the solvent or medium", json_schema_extra={"source_attribute_names": ["medium_formula"], "example_values": [], "required": "optional", "confidence": "high"})
    substrate: str | None = Field(None, description="The substrate material being coated", json_schema_extra={"source_attribute_names": ["substrate"], "example_values": [], "required": "usually_required", "confidence": "high"})
    output_state: str | None = Field(None, description="The state of the substrate after coating", json_schema_extra={"source_attribute_names": ["output_state"], "example_values": [], "required": "optional", "confidence": "medium"})

class ElectrochemicalReduction(BaseModel):
    '''
    The use of an electrochemical cell to induce the reduction of a sample, often utilizing techniques such as potential cycling to modify structural characteristics.
    Synonyms: Electrochemical Potential Cycling, Potential Cycling Reduction
    '''
    process_identifier: str | None = Field("Electrochemical Reduction", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Electrochemical Reduction", description="Human readable process name from the source schema.")
    electrolyte_formula: str | None = Field(None, description="Chemical formula of the electrolyte used", json_schema_extra={"source_attribute_names": ["electrolyte_formula"], "example_values": [], "required": "usually_required", "confidence": "high"})
    electrolyte_concentration: str | None = Field(None, description="Concentration of the electrolyte", json_schema_extra={"source_attribute_names": ["electrolyte_concentration"], "example_values": [], "required": "usually_required", "confidence": "high"})
    electrolyte_concentration_unit: str | None = Field(None, description="Unit of electrolyte concentration", json_schema_extra={"source_attribute_names": ["electrolyte_concentration_unit"], "example_values": [], "required": "usually_required", "confidence": "high"})
    potential_range_min: float | str | None = Field(None, description="Minimum potential applied during cycling", json_schema_extra={"source_attribute_names": ["potential_range_min"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    potential_range_min_units: str | None = Field(None, description="Units for potential_range_min.", json_schema_extra={"unit_for": "potential_range_min"})
    potential_range_max: float | str | None = Field(None, description="Maximum potential applied during cycling", json_schema_extra={"source_attribute_names": ["potential_range_max"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    potential_range_max_units: str | None = Field(None, description="Units for potential_range_max.", json_schema_extra={"unit_for": "potential_range_max"})
    cycle_count: int | None = Field(None, description="Number of potential cycles performed", json_schema_extra={"source_attribute_names": ["cycles"], "example_values": [], "required": "usually_required", "confidence": "high"})
    scan_rate: float | str | None = Field(None, description="Scan rate of the potential cycling", json_schema_extra={"source_attribute_names": ["scan_rate"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    scan_rate_unit: str | None = Field(None, description="Unit of scan rate", json_schema_extra={"source_attribute_names": ["scan_rate_unit"], "example_values": [], "required": "usually_required", "confidence": "high", "unit_for": "scan_rate"})
    potentiostat_model: str | None = Field(None, description="Model of the potentiostat used", json_schema_extra={"source_attribute_names": ["potentiostat_model"], "example_values": [], "required": "optional", "confidence": "high"})
    potentiostat_manufacturer: str | None = Field(None, description="Manufacturer of the potentiostat", json_schema_extra={"source_attribute_names": ["potentiostat_manufacturer"], "example_values": [], "required": "optional", "confidence": "high"})
    reference_electrode: str | None = Field(None, description="Reference electrode used", json_schema_extra={"source_attribute_names": ["reference_electrode"], "example_values": [], "required": "usually_required", "confidence": "high"})
    counter_electrode: str | None = Field(None, description="Counter electrode used", json_schema_extra={"source_attribute_names": ["counter_electrode"], "example_values": [], "required": "usually_required", "confidence": "high"})
    electrolyte_purity: str | None = Field(None, description="Purity of the electrolyte", json_schema_extra={"source_attribute_names": ["electrolyte_purity"], "example_values": [], "required": "optional", "confidence": "high"})
    electrolyte_supplier: str | None = Field(None, description="Supplier of the electrolyte", json_schema_extra={"source_attribute_names": ["electrolyte_supplier"], "example_values": [], "required": "optional", "confidence": "high"})
    output_ligament_diameter: float | str | None = Field(None, description="Resulting mean ligament diameter of the reduced sample", json_schema_extra={"source_attribute_names": ["output_ligament_diameter"], "example_values": [], "required": "context_dependent", "confidence": "high", "value_type": "quantity"})
    output_ligament_diameter_units: str | None = Field(None, description="Units for output_ligament_diameter.", json_schema_extra={"unit_for": "output_ligament_diameter"})

class HydrogenTreatment(BaseModel):
    '''
    Exposure of a material to a hydrogen-containing atmosphere, potentially in a cyclic manner, to evaluate its response or modify its hydride content.
    Synonyms: hydrogen exposure, hydrogenation treatment
    '''
    process_identifier: str | None = Field("hydrogen_treatment", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Hydrogen Treatment", description="Human readable process name from the source schema.")
    hydrogen_content: str | None = Field(None, description="The concentration or partial pressure of hydrogen in the treatment atmosphere.", json_schema_extra={"source_attribute_names": ["hydrogen_content"], "example_values": [], "required": "usually_required", "confidence": "high"})
    atmosphere_composition: str | None = Field(None, description="The overall composition of the gas atmosphere used during the treatment.", json_schema_extra={"source_attribute_names": ["atmosphere"], "example_values": [], "required": "usually_required", "confidence": "high"})
    exposure_sequence: str | None = Field(None, description="The order or pattern of changes in hydrogen content or atmospheric conditions during cyclic exposure.", json_schema_extra={"source_attribute_names": ["sequence"], "example_values": [], "required": "context_dependent", "confidence": "medium"})

class Lithography(Patterning):
    '''
    A process of patterning a substrate or resist to create specific geometric shapes, often using a beam of light or electrons.
    Synonyms: Electron beam lithography, E-beam lithography, Patterning
    '''
    process_identifier: str | None = Field("Lithography", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Lithography", description="Human readable process name from the source schema.")
    tool: str | None = Field(None, description="The lithography technique or instrument used to create the pattern.", json_schema_extra={"source_attribute_names": ["tool"], "example_values": ["electron beam"], "required": "usually_required", "confidence": "high"})
    pattern_shape: str | None = Field(None, description="The geometric shape of the fabricated specimen or pattern.", json_schema_extra={"source_attribute_names": ["shape"], "example_values": ["dog-bone"], "required": "usually_required", "confidence": "high"})
    gauge_length: float | str | None = Field(None, description="The length of the gauge section of the specimen.", json_schema_extra={"source_attribute_names": ["gauge_length"], "example_values": [], "required": "context_dependent", "confidence": "high", "value_type": "quantity"})
    gauge_length_units: str | None = Field(None, description="The unit of measurement for the gauge length.", json_schema_extra={"source_attribute_names": ["gauge_length_unit"], "example_values": [], "required": "context_dependent", "confidence": "high", "unit_for": "gauge_length"})
    width: float | str | None = Field(None, description="The width of the specimen or pattern.", json_schema_extra={"source_attribute_names": ["width"], "example_values": [], "required": "context_dependent", "confidence": "high", "value_type": "quantity"})
    width_units: str | None = Field(None, description="The unit of measurement for the width.", json_schema_extra={"source_attribute_names": ["width_unit"], "example_values": [], "required": "context_dependent", "confidence": "high", "unit_for": "width"})

class ElectricalContacting(SensorAssembly):
    '''
    The process of establishing a conductive electrical connection between two or more components using a conductive medium such as paint, adhesive, or solder.
    Synonyms: Electrical Connection, Conductive Contacting
    '''
    process_identifier: str | None = Field("Electrical Contacting", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Electrical Contacting", description="Human readable process name from the source schema.")
    contacting_agent: str | None = Field(None, description="The material used to create the electrical contact between components.", json_schema_extra={"source_attribute_names": ["contacting_agent"], "example_values": ["silver paint"], "required": "usually_required", "confidence": "high"})
    contact_agent_manufacturer: str | None = Field(None, description="The manufacturer of the conductive material used for contacting.", json_schema_extra={"source_attribute_names": ["contact_agent_manufacturer"], "example_values": [], "required": "optional", "confidence": "high"})

class SparkPlasmaSintering(Sintering):
    '''
    A field-assisted sintering technique that utilizes pulsed direct current and uniaxial pressure to rapidly consolidate powder into a dense solid.
    Synonyms: SPS, Field Assisted Sintering Technique, FAST
    '''
    process_identifier: str | None = Field("Spark Plasma Sintering", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Spark Plasma Sintering", description="Human readable process name from the source schema.")
    heating_rate: float | str | None = Field(None, description="The rate at which the temperature is increased during the sintering cycle.", json_schema_extra={"source_attribute_names": ["heating_rate"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    heating_rate_units: str | None = Field(None, description="Unit of measurement for the heating rate.", json_schema_extra={"source_attribute_names": ["heating_rate_unit"], "example_values": [], "required": "usually_required", "confidence": "high", "unit_for": "heating_rate"})
    sintering_temperature: float | str | None = Field(None, description="The target or maximum temperature reached during the sintering process.", json_schema_extra={"source_attribute_names": ["sintering_temperature"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    sintering_temperature_units: str | None = Field(None, description="Unit of measurement for the temperature.", json_schema_extra={"source_attribute_names": ["temperature_unit"], "example_values": [], "required": "usually_required", "confidence": "high", "unit_for": "sintering_temperature"})
    sintering_pressure: float | str | None = Field(None, description="The uniaxial pressure applied to the sample during the sintering process.", json_schema_extra={"source_attribute_names": ["sintering_pressure"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    sintering_pressure_units: str | None = Field(None, description="Unit of measurement for the pressure.", json_schema_extra={"source_attribute_names": ["pressure_unit"], "example_values": [], "required": "usually_required", "confidence": "high", "unit_for": "sintering_pressure"})
    holding_time: float | str | None = Field(None, description="The duration the sample is held at the maximum sintering temperature.", json_schema_extra={"source_attribute_names": ["holding_time"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    holding_time_units: str | None = Field(None, description="Unit of measurement for the holding time.", json_schema_extra={"source_attribute_names": ["time_unit"], "example_values": [], "required": "usually_required", "confidence": "high", "unit_for": "holding_time"})
    input_state: str | None = Field(None, description="The physical state or form of the material prior to the sintering operation.", json_schema_extra={"source_attribute_names": ["input_state"], "example_values": [], "required": "optional", "confidence": "high"})
    output_state: str | None = Field(None, description="The physical state or form of the material resulting from the sintering operation.", json_schema_extra={"source_attribute_names": ["output_state"], "example_values": [], "required": "optional", "confidence": "high"})

class Encapsulation(SensorAssembly):
    '''
    The process of sealing a device, component, or sensor within a protective enclosure or chamber to isolate it from the external environment or to facilitate a controlled environment.
    Synonyms: sealing, enclosure, device packaging
    '''
    process_identifier: str | None = Field("encapsulation", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Encapsulation", description="Human readable process name from the source schema.")
    enclosure_material: str | None = Field(None, description="The material used to construct the sealing enclosure or chamber.", json_schema_extra={"source_attribute_names": ["chamber_material"], "example_values": ["glass"], "required": "usually_required", "confidence": "high"})
    enclosure_features: str | None = Field(None, description="Specific design features of the enclosure, such as ports, inlets, or outlets.", json_schema_extra={"source_attribute_names": ["chamber_features"], "example_values": ["gas inlet/outlet"], "required": "optional", "confidence": "high"})

class BallMilling(BaseModel):
    '''
    A process of grinding or mixing materials using spherical balls in a rotating or vibrating container to achieve particle size reduction, homogenization, or mechanical alloying.
    Synonyms: mechanical alloying, high energy ball milling, planetary ball milling
    '''
    process_identifier: str | None = Field("ball_milling", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Ball Milling", description="Human readable process name from the source schema.")
    starting_materials: List[str] | None = Field(None, description="The materials used as input for the milling process.", json_schema_extra={"source_attribute_names": ["material_1", "material_2"], "example_values": ["Al", "Pd"], "required": "usually_required", "confidence": "high"})
    material_purity: str | None = Field(None, description="The purity level of the starting material powders.", json_schema_extra={"source_attribute_names": ["material_1_purity", "material_2_purity"], "example_values": [], "required": "optional", "confidence": "high"})
    material_particle_size: str | None = Field(None, description="The initial particle size of the powders.", json_schema_extra={"source_attribute_names": ["material_1_size", "material_2_size"], "example_values": [], "required": "optional", "confidence": "high"})
    target_composition: str | None = Field(None, description="The intended chemical composition of the resulting alloy.", json_schema_extra={"source_attribute_names": ["composition"], "example_values": [], "required": "usually_required", "confidence": "medium"})
    atmosphere: str | None = Field(None, description="The gas or vacuum environment inside the milling vial.", json_schema_extra={"source_attribute_names": ["atmosphere"], "example_values": ["vacuum"], "required": "usually_required", "confidence": "high"})
    ball_to_powder_ratio: float | str | None = Field(None, description="The mass ratio of the grinding media (balls) to the process powder.", json_schema_extra={"source_attribute_names": ["ball_to_powder_mass_ratio"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    ball_to_powder_ratio_units: str | None = Field(None, description="Units for ball_to_powder_ratio.", json_schema_extra={"unit_for": "ball_to_powder_ratio"})
    rotational_speed: float | str | None = Field(None, description="The speed of rotation or vibration of the milling equipment.", json_schema_extra={"source_attribute_names": ["angular_speed"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    rotational_speed_units: str | None = Field(None, description="The unit used to measure the rotational speed.", json_schema_extra={"source_attribute_names": ["angular_speed_unit"], "example_values": [], "required": "optional", "confidence": "high", "unit_for": "rotational_speed"})
    duration: float | str | None = Field(None, description="The total time the materials were subjected to milling.", json_schema_extra={"source_attribute_names": ["duration"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    duration_units: str | None = Field(None, description="The unit of time for the milling duration.", json_schema_extra={"source_attribute_names": ["duration_unit"], "example_values": [], "required": "optional", "confidence": "high", "unit_for": "duration"})

class ElectrochemicalCharging(BaseModel):
    '''
    The process of applying an electrical potential to a material surface immersed in an electrolyte to modify its charge state or electrical properties, such as resistance.
    Synonyms: electrochemical charging, surface charging
    '''
    process_identifier: str | None = Field("electrochemical_charging", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Electrochemical Charging", description="Human readable process name from the source schema.")
    electrolyte: str | None = Field(None, description="The chemical composition of the electrolyte used during the charging process.", json_schema_extra={"source_attribute_names": ["electrolyte"], "example_values": [], "required": "usually_required", "confidence": "high"})
    electrolyte_concentration: str | None = Field(None, description="The concentration of the electrolyte solution.", json_schema_extra={"source_attribute_names": ["electrolyte_concentration"], "example_values": [], "required": "usually_required", "confidence": "high"})
    potentiostat_model: str | None = Field(None, description="The model or brand of the potentiostat used to apply the voltage.", json_schema_extra={"source_attribute_names": ["potentiostat_model"], "example_values": [], "required": "optional", "confidence": "high"})
    potential_range: str | None = Field(None, description="The range of electrical potential applied during the charging process.", json_schema_extra={"source_attribute_names": ["potential_range"], "example_values": [], "required": "usually_required", "confidence": "high"})
    voltage_step: float | str | None = Field(None, description="The increment size of the voltage applied in a stepped charging process.", json_schema_extra={"source_attribute_names": ["voltage_step"], "example_values": [], "required": "context_dependent", "confidence": "high", "value_type": "quantity"})
    voltage_step_units: str | None = Field(None, description="The unit of measurement for the voltage step.", json_schema_extra={"source_attribute_names": ["voltage_step_unit"], "example_values": [], "required": "context_dependent", "confidence": "high", "unit_for": "voltage_step"})
    time_interval: float | str | None = Field(None, description="The duration of time spent at each voltage step.", json_schema_extra={"source_attribute_names": ["time_interval"], "example_values": [], "required": "context_dependent", "confidence": "high", "value_type": "quantity"})
    time_interval_units: str | None = Field(None, description="Units for time_interval.", json_schema_extra={"unit_for": "time_interval"})
    charging_regime: str | None = Field(None, description="The electrochemical regime of charging (e.g., double layer charging or chemisorption).", json_schema_extra={"source_attribute_names": ["regime"], "example_values": ["double layer", "chemisorption"], "required": "optional", "confidence": "high"})
    reference_electrode: str | None = Field(None, description="The electrode used as a stable reference potential.", json_schema_extra={"source_attribute_names": ["reference_electrode"], "example_values": [], "required": "usually_required", "confidence": "high"})
    counter_electrode: str | None = Field(None, description="The electrode that completes the circuit to allow current to flow.", json_schema_extra={"source_attribute_names": ["counter_electrode"], "example_values": [], "required": "usually_required", "confidence": "high"})
    measurement_method: str | None = Field(None, description="The specific electrochemical method used for charging (e.g., chronoamperometry, cyclic voltammetry).", json_schema_extra={"source_attribute_names": ["measurement_method"], "example_values": ["chronoamperometric"], "required": "usually_required", "confidence": "high"})

class CyclicVoltammetry(BaseModel):
    '''
    An electrochemical measurement technique where the potential of a working electrode is swept linearly with time and then reversed, used to determine potential ranges or monitor redox behavior and resistance.
    Synonyms: Cyclovoltammetric Scanning, CV
    '''
    process_identifier: str | None = Field("cyclic_voltammetry", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Cyclic Voltammetry", description="Human readable process name from the source schema.")
    scan_rate: float | str | None = Field(None, description="The rate at which the electrode potential is varied during the scan.", json_schema_extra={"source_attribute_names": ["scan_rate"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    scan_rate_units: str | None = Field(None, description="The unit of measurement for the scan rate (e.g., mV/s).", json_schema_extra={"source_attribute_names": ["scan_rate_unit"], "example_values": [], "required": "usually_required", "confidence": "high", "unit_for": "scan_rate"})
    purpose: str | None = Field(None, description="The objective of the scanning, such as determining potential ranges or monitoring resistance.", json_schema_extra={"source_attribute_names": ["purpose"], "example_values": [], "required": "optional", "confidence": "medium"})
    reference_electrode: str | None = Field(None, description="The electrode used as a stable reference point for potential measurements.", json_schema_extra={"source_attribute_names": ["reference_electrode"], "example_values": [], "required": "usually_required", "confidence": "high"})

class CoatingProcess(ElectrodeAssembly):
    '''
    The application of a material, such as a catalyst ink, onto a substrate surface to form a functional layer.
    Synonyms: drop casting, ink deposition, electrode coating
    '''
    process_identifier: str | None = Field("coating", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Coating", description="Human readable process name from the source schema.")
    ink_volume: float | str | None = Field(None, description="The volume of the ink applied to the substrate.", json_schema_extra={"source_attribute_names": ["ink_volume"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    ink_volume_units: str | None = Field(None, description="The unit of measurement for the ink volume.", json_schema_extra={"source_attribute_names": ["ink_volume_unit"], "example_values": [], "required": "usually_required", "confidence": "high", "unit_for": "ink_volume"})
    substrate_material: str | None = Field(None, description="The material composition of the substrate being coated.", json_schema_extra={"source_attribute_names": ["substrate_material"], "example_values": [], "required": "usually_required", "confidence": "high"})
    substrate_diameter: float | str | None = Field(None, description="The diameter of the substrate.", json_schema_extra={"source_attribute_names": ["substrate_diameter"], "example_values": [], "required": "optional", "confidence": "high", "value_type": "quantity"})
    substrate_diameter_units: str | None = Field(None, description="The unit of measurement for the substrate diameter.", json_schema_extra={"source_attribute_names": ["substrate_diameter_unit"], "example_values": [], "required": "optional", "confidence": "high", "unit_for": "substrate_diameter"})

class Mixing(BaseModel):
    '''
    The process of combining multiple components, such as powders, solvents, and binders, to create a uniform mixture or suspension.
    Synonyms: dispersion preparation, suspension preparation, blending
    '''
    process_identifier: str | None = Field("mixing", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Mixing", description="Human readable process name from the source schema.")
    solvent_volume: float | str | None = Field(None, description="The volume of the solvent used in the mixing process.", json_schema_extra={"source_attribute_names": ["volume_of_isopropanol"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    solvent_volume_units: str | None = Field(None, description="The unit of measurement for the solvent volume.", json_schema_extra={"source_attribute_names": ["volume_of_isopropanol_unit"], "example_values": [], "required": "usually_required", "confidence": "high", "unit_for": "solvent_volume"})
    binder_volume: float | str | None = Field(None, description="The volume of the binder solution added.", json_schema_extra={"source_attribute_names": ["volume_of_nafion"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    binder_volume_units: str | None = Field(None, description="Units for binder_volume.", json_schema_extra={"unit_for": "binder_volume"})
    binder_concentration: str | None = Field(None, description="The concentration of the binder solution used.", json_schema_extra={"source_attribute_names": ["binder_concentration"], "example_values": [], "required": "optional", "confidence": "high"})
    mixing_equipment: str | None = Field(None, description="The tool or instrument used to perform the mixing operation.", json_schema_extra={"source_attribute_names": ["equipment"], "example_values": [], "required": "usually_required", "confidence": "high"})

class Flattening(SurfaceTreatment):
    '''
    The process of applying pressure or force using a smooth surface to flatten and planarize a coated layer or material surface.
    Synonyms: planarization, surface flattening, smoothing
    '''
    process_identifier: str | None = Field("flattening", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Flattening", description="Human readable process name from the source schema.")
    tool: str | None = Field(None, description="The tool or smooth surface used to apply pressure for flattening.", json_schema_extra={"source_attribute_names": ["tool"], "example_values": [], "required": "usually_required", "confidence": "high"})
    output_thickness: float | str | None = Field(None, description="The target thickness of the layer achieved after the flattening process.", json_schema_extra={"source_attribute_names": ["output_thickness"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    output_thickness_units: str | None = Field(None, description="The unit of measurement for the output thickness.", json_schema_extra={"source_attribute_names": ["output_thickness_unit"], "example_values": [], "required": "usually_required", "confidence": "high", "unit_for": "output_thickness"})

class SurfaceExposure(BaseModel):
    '''
    The process of exposing a sample surface to specific gases to modify the surface chemistry, induce strain, or achieve other surface-level modifications.
    Synonyms: gas exposure, surface gas treatment, chemical gas exposure
    '''
    process_identifier: str | None = Field("surface_exposure", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Surface Exposure", description="Human readable process name from the source schema.")
    gas_type: str | None = Field(None, description="The type of gas used for the exposure process.", json_schema_extra={"source_attribute_names": ["gas_type"], "example_values": ["Ozone", "Carbon Monoxide"], "required": "usually_required", "confidence": "high"})
    concentration: str | None = Field(None, description="The concentration or partial pressure of the gas during exposure.", json_schema_extra={"source_attribute_names": ["concentration"], "example_values": ["~7 vol % O3"], "required": "usually_required", "confidence": "high"})
    atmosphere: str | None = Field(None, description="The overall gaseous environment or carrier gas during exposure.", json_schema_extra={"source_attribute_names": ["atmosphere"], "example_values": ["O2", "Pure CO"], "required": "usually_required", "confidence": "high"})
    purpose: str | None = Field(None, description="The intended outcome of the surface exposure process.", json_schema_extra={"source_attribute_names": ["purpose"], "example_values": ["surface engineering", "actuation", "cleaning"], "required": "optional", "confidence": "high"})

class ProtectiveCoatingApplication(SamplePreparation):
    '''
    The process of applying a protective layer (such as a lacquer or polymer) to specific areas of a sample to protect it, secure it, or isolate it during subsequent processing steps.
    Synonyms: protective coating, lacquer coating, sample edging, edge protection
    '''
    process_identifier: str | None = Field("protective coating application", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Protective Coating Application", description="Human readable process name from the source schema.")
    coating_material: str | None = Field(None, description="The material used to create the protective layer.", json_schema_extra={"source_attribute_names": ["coating_material"], "example_values": ["lacquer"], "required": "usually_required", "confidence": "high"})
    coating_location: str | None = Field(None, description="The specific area or region of the sample where the coating is applied.", json_schema_extra={"source_attribute_names": ["coating_location"], "example_values": ["borders of the film samples"], "required": "usually_required", "confidence": "high"})
    coating_purpose: str | None = Field(None, description="The intended goal or reason for applying the protective coating.", json_schema_extra={"source_attribute_names": ["coating_purpose"], "example_values": ["secure them during processing"], "required": "optional", "confidence": "high"})

class PotentialCycling(ElectrochemicalConditioning):
    '''
    The process of repeatedly cycling the electrical potential of an electrode between specific values to stabilize the material, remove impurities, or prepare the sample for subsequent measurements.
    Synonyms: electrochemical cycling, voltage cycling, potential scan cycling
    '''
    process_identifier: str | None = Field("potential_cycling", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Potential Cycling", description="Human readable process name from the source schema.")
    cycle_count: int | None = Field(None, description="The number of complete potential cycles performed.", json_schema_extra={"source_attribute_names": ["cycles"], "example_values": [], "required": "usually_required", "confidence": "high"})
    potential_range: str | None = Field(None, description="The range of potential values applied during the cycling.", json_schema_extra={"source_attribute_names": ["potential_range"], "example_values": [], "required": "usually_required", "confidence": "high"})
    reference_electrode: str | None = Field(None, description="The electrode used as a reference point for the applied potential.", json_schema_extra={"source_attribute_names": ["reference_electrode"], "example_values": [], "required": "usually_required", "confidence": "high"})
    scan_rate: float | str | None = Field(None, description="The rate at which the potential is varied.", json_schema_extra={"source_attribute_names": ["scan_rate"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    scan_rate_units: str | None = Field(None, description="The unit of measurement for the scan rate (e.g., mV/s).", json_schema_extra={"source_attribute_names": ["scan_rate_unit"], "example_values": [], "required": "usually_required", "confidence": "high", "unit_for": "scan_rate"})
    electrolyte: str | None = Field(None, description="The chemical composition of the electrolyte used during cycling.", json_schema_extra={"source_attribute_names": ["electrolyte"], "example_values": [], "required": "usually_required", "confidence": "high"})
    electrolyte_concentration: str | None = Field(None, description="The concentration of the electrolyte solution.", json_schema_extra={"source_attribute_names": ["electrolyte_concentration"], "example_values": [], "required": "usually_required", "confidence": "high"})

class FilmDeposition(FilmFabrication):
    '''
    The process of applying a thin layer of material onto a substrate surface.
    Synonyms: thin film deposition, layer deposition
    '''
    process_identifier: str | None = Field("film_deposition", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Film Deposition", description="Human readable process name from the source schema.")
    substrate_material: str | None = Field(None, description="The material of the substrate upon which the film is deposited.", json_schema_extra={"source_attribute_names": ["substrate_material"], "example_values": [], "required": "usually_required", "confidence": "high"})
    barrier_layer_thickness: float | str | None = Field(None, description="The thickness of the diffusion barrier layer on the substrate.", json_schema_extra={"source_attribute_names": ["substrate_thickness"], "example_values": [], "required": "optional", "confidence": "medium", "value_type": "quantity"})
    barrier_layer_thickness_units: str | None = Field(None, description="Units for barrier_layer_thickness.", json_schema_extra={"unit_for": "barrier_layer_thickness"})
    deposited_material: str | None = Field(None, description="The material being deposited to form the film.", json_schema_extra={"source_attribute_names": ["deposited_material"], "example_values": [], "required": "usually_required", "confidence": "high"})
    deposited_composition: str | None = Field(None, description="The atomic or weight percentage composition of the deposited material.", json_schema_extra={"source_attribute_names": ["deposited_composition"], "example_values": [], "required": "optional", "confidence": "high"})
    deposition_tool: str | None = Field(None, description="The equipment used to perform the deposition.", json_schema_extra={"source_attribute_names": ["tool"], "example_values": [], "required": "usually_required", "confidence": "high"})

class ComponentMounting(SensorAssembly):
    '''
    The process of fixing a component or device onto a substrate or support structure to ensure stability or establish electrical connections.
    Synonyms: mounting, component attachment, substrate mounting
    '''
    process_identifier: str | None = Field("component_mounting", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Component Mounting", description="Human readable process name from the source schema.")
    substrate: str | None = Field(None, description="The material or object onto which the component is mounted.", json_schema_extra={"source_attribute_names": ["substrate"], "example_values": ["glass slide"], "required": "usually_required", "confidence": "high"})
    contact_wires: str | None = Field(None, description="Wires used to provide electrical connectivity to the component during or as part of the mounting process.", json_schema_extra={"source_attribute_names": ["contact_wires"], "example_values": ["conducting wires"], "required": "context_dependent", "confidence": "high"})

class HeatTreatmentProc(ThermalTreatment):
    '''
    The process of heating and cooling a material to a specific temperature and duration to change its physical or chemical properties, such as relieving internal stress.
    Synonyms: Thermal treatment, Thermal stress relief
    '''
    process_identifier: str | None = Field("heat_treatment", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Heat Treatment", description="Human readable process name from the source schema.")
    temperature: float | str | None = Field(None, description="The temperature at which the heat treatment is performed.", json_schema_extra={"source_attribute_names": ["temperature"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    temperature_units: str | None = Field(None, description="The unit of measurement for the heat treatment temperature.", json_schema_extra={"source_attribute_names": ["temperature_unit"], "example_values": [], "required": "usually_required", "confidence": "high", "unit_for": "temperature"})
    duration: float | str | None = Field(None, description="The length of time the material is held at the specified temperature.", json_schema_extra={"source_attribute_names": ["duration"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    duration_units: str | None = Field(None, description="The unit of measurement for the heat treatment duration.", json_schema_extra={"source_attribute_names": ["duration_unit"], "example_values": [], "required": "usually_required", "confidence": "high", "unit_for": "duration"})

class SampleStabilization(PostProcessing):
    '''
    The process of immersing a sample in a specific medium to stabilize its chemical or physical state, typically to prevent unwanted reactions such as oxidation or combustion.
    Synonyms: Stabilization, Quenching, Dipping stabilization
    '''
    process_identifier: str | None = Field("sample_stabilization", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Sample Stabilization", description="Human readable process name from the source schema.")
    immersion_medium: str | None = Field(None, description="The substance used to immerse the sample for stabilization.", json_schema_extra={"source_attribute_names": ["immersion_medium"], "example_values": ["distilled water"], "required": "usually_required", "confidence": "high"})
    duration: float | str | None = Field(None, description="The length of time the sample remains in the stabilization medium.", json_schema_extra={"source_attribute_names": ["duration"], "example_values": [], "required": "optional", "confidence": "high", "value_type": "quantity"})
    duration_units: str | None = Field(None, description="The unit of time used for the duration.", json_schema_extra={"source_attribute_names": ["duration_unit"], "example_values": [], "required": "optional", "confidence": "high", "unit_for": "duration"})
    purpose: str | None = Field(None, description="The specific goal of the stabilization step (e.g., preventing oxidation).", json_schema_extra={"source_attribute_names": ["purpose"], "example_values": ["prevent oxidation or combustion of the porous Pd"], "required": "usually_required", "confidence": "high"})

class ThermalCycling(HeatTreatment):
    '''
    A process of repeatedly cycling a material through a range of temperatures to induce structural changes, such as coarsening, or to study material behavior such as stress evolution.
    Synonyms: cyclic thermal treatment, thermal cycling
    '''
    process_identifier: str | None = Field("thermal_cycling", description="Stable process identifier from the source schema.")
    process_name: str | None = Field("Thermal Cycling", description="Human readable process name from the source schema.")
    temperature: float | str | None = Field(None, description="The temperature levels reached during the thermal cycling process.", json_schema_extra={"source_attribute_names": ["temperature"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    temperature_units: str | None = Field(None, description="Units for temperature.", json_schema_extra={"unit_for": "temperature"})
    temperature_cycle_range: float | str | None = Field(None, description="The range of temperatures involved in the cycling process.", json_schema_extra={"source_attribute_names": ["cycle_range"], "example_values": [], "required": "usually_required", "confidence": "high", "value_type": "quantity"})
    temperature_cycle_range_units: str | None = Field(None, description="Units for temperature_cycle_range.", json_schema_extra={"unit_for": "temperature_cycle_range"})

PROCESS_CLASSES = {
    "mechanical_surface_cleaning": MechanicalSurfaceCleaning,
    "electrochemical_surface_cleaning": ElectrochemicalSurfaceCleaning,
    "sputtering": Sputtering,
    "atomic_layer_deposition": AtomicLayerDeposition,
    "annealing": Annealing,
    "rinsing": Rinsing,
    "drying": Drying,
    "quenching": Quenching,
    "electrochemical_dealloying": ElectrochemicalDealloying,
    "chemical_dealloying": ChemicalDealloying,
    "cutting": Cutting,
    "wire_drawing": WireDrawing,
    "ultramicrotomy": Ultramicrotomy,
    "free_corrosion_dealloying": FreeCorrosionDealloying,
    "alloy_melting": AlloyMelting,
    "electrochemical_polymerization": ElectrochemicalPolymerization,
    "electrolyte_preparation": ElectrolytePreparation,
    "rolling": Rolling,
    "thermal_treatment": ThermalTreatment,
    "acid_treatment": AcidTreatment,
    "resin_impregnation": ResinImpregnation,
    "slurry_preparation": SlurryPreparation,
    "sintering": Sintering,
    "electrochemical_activation": ElectrochemicalActivation,
    "blow_casting": BlowCasting,
    "polishing": Polishing,
    "thermal_coarsening": ThermalCoarsening,
    "melt_spinning": MeltSpinning,
    "surface_grinding": SurfaceGrinding,
    "mechanical_grinding": MechanicalGrinding,
    "sample_cutting": SampleCutting,
    "tem_grid_mounting": TemGridMounting,
    "spin_coating": SpinCoating,
    "electrochemical_reduction": ElectrochemicalReduction,
    "hydrogen_treatment": HydrogenTreatment,
    "lithography": Lithography,
    "electrical_contacting": ElectricalContacting,
    "spark_plasma_sintering": SparkPlasmaSintering,
    "encapsulation": Encapsulation,
    "ball_milling": BallMilling,
    "electrochemical_charging": ElectrochemicalCharging,
    "cyclic_voltammetry": CyclicVoltammetry,
    "coating": CoatingProcess,
    "mixing": Mixing,
    "flattening": Flattening,
    "surface_exposure": SurfaceExposure,
    "protective_coating_application": ProtectiveCoatingApplication,
    "potential_cycling": PotentialCycling,
    "film_deposition": FilmDeposition,
    "component_mounting": ComponentMounting,
    "heat_treatment": HeatTreatmentProc,
    "sample_stabilization": SampleStabilization,
    "thermal_cycling": ThermalCycling,
}

PROCESS_CLASS_NAMES = {
    "annealing": ["Cluster 4", "Cluster 42"],
    "electrochemical_dealloying": ["Cluster 9", "Cluster 12"],
    "ball_milling": ["Cluster 33"],
}

