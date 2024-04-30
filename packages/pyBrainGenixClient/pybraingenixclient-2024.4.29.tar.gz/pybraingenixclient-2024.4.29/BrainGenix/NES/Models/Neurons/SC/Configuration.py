# BrainGenix-NES
# AGPLv3


class Configuration():

    def __init__(self):
        
        # Create Attributes
        self.Name:str = None
        self.SomaIDs:list = None
        self.AxonIDs:list = None
        self.DendriteIDs:list = None
        self.MembranePotential_mV:float = None
        self.RestingPotential_mV:float = None
        self.SpikeThreshold_mV:float = None
        self.DecayTime_ms:float = None
        self.AfterHyperpolarizationAmplitude_mV:float = None
        self.PostsynapticPotentialRiseTime_ms:float = None
        self.PostsynapticPotentialDecayTime_ms:float = None
        self.PostsynapticPotentialAmplitude_nA:float = None
