# BrainGenix-NES
# AGPLv3


class Configuration():

    def __init__(self):
        
        # Create Attributes
        self.Name:str = None
        self.SourceCompartment = None
        self.DestinationCompartment = None
        self.Neurotransmitter:str = None
        self.Conductance_nS:float = None
        self.TimeConstantRise_ms:float = None
        self.TimeConstantDecay_ms:float = None
        self.ReceptorMorphology:int = None
        # self.ReceptorLocation_um:list = None
    
