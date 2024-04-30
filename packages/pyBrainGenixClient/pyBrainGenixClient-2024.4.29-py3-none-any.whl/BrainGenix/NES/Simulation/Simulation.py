# BrainGenix-NES
# AGPLv3

from .. import Models
from . import Configuration

from BrainGenix.NES.Client import RequestHandler

from BrainGenix.NES.Shapes import Sphere
from BrainGenix.NES.Shapes import Box
from BrainGenix.NES.Shapes import Cylinder

from BrainGenix.NES.VSDA import EM
from BrainGenix.NES.VSDA import Calcium
from BrainGenix.NES.Models.Connections import Staple, Receptor
from BrainGenix.NES.Visualizer import Visualizer
from BrainGenix.NES import Tools

import BrainGenix.LibUtils.ConfigCheck
import BrainGenix.LibUtils.GetID
import time

import yaspin



class Simulation():

    # create=False is used when this object is needed during loading (see BG_API.py)
    def __init__(self, _Configuration:Configuration, _RequestHandler:RequestHandler, _Create:bool=True):
        # Create Attributes
        self.RequestHandler = _RequestHandler

        if _Create:

            self.Name = _Configuration.Name
            

            # Run Configuration Check
            BrainGenix.LibUtils.ConfigCheck.ConfigCheck(_Configuration)

            # Create Sim On Server
            QueryList:list = []
            QueryList.append({
                "Simulation/Create": {
                    "Name": _Configuration.Name,
                }
            })
            Response = self.RequestHandler.BuildPostQuery(QueryList, "/NES")[0]
            assert(Response != None)
            self.ID = Response["SimulationID"]

            # Send Seed
            QueryList:list = []
            QueryList.append({
                "Simulation/SetRandomSeed": {
                    "SimulationID": self.ID,
                    "Seed": _Configuration.Seed,
                }
            })
            Response = self.RequestHandler.BuildPostQuery(QueryList, "/NES")[0]
            assert(Response != None)
        else:
            self.ID = 0 # Will be replaced after loading, but a valid number is provided for temporary use.


    ## Methods For Adding Objects

     # Tool Init Commands
    def AddPatchClampDAC(self, _PatchClampDACConfig:Tools.PatchClampDAC.Configuration):
        return Tools.PatchClampDAC.PatchClampDAC(_PatchClampDACConfig, self.RequestHandler, self.ID)

    def AddPatchClampADC(self, _PatchClampADCConfig:Tools.PatchClampADC.Configuration):
        return Tools.PatchClampADC.PatchClampADC(_PatchClampADCConfig, self.RequestHandler, self.ID)


     # Connection Init Commands
    def AddReceptor(self, _ReceptorConfig:Receptor.Configuration):
        return Receptor.Receptor(_ReceptorConfig, self.RequestHandler, self.ID)

    def AddStaple(self, _StapleConfig:Staple.Configuration):
        return Staple.Staple(_StapleConfig, self.RequestHandler, self.ID)

    def AddStaples(self, _StapleConfigs:list):
        return Staple.BatchCreate(_StapleConfigs, self.RequestHandler, self.ID)




     # VSDA Init Commands
    def AddVSDAEM(self, _VSDAEMConfig:EM.Configuration):
        return EM.EM(_VSDAEMConfig, self.RequestHandler, self.ID)

    def AddVSDACa(self, _VSDACAConfig:Calcium.Configuration):
        return Calcium.Calcium(_VSDACAConfig, self.RequestHandler, self.ID)



     # Compartments Add Methods
    def AddBSCompartment(self, _BSCompartmentConfig:Models.Compartments.BS.Configuration):
        return Models.Compartments.BS.BS(_BSCompartmentConfig, self.RequestHandler, self.ID)


    def AddBSCompartments(self, _BSCompartmentConfigs:list):
        return Models.Compartments.BS.BatchCreate(_BSCompartmentConfigs, self.RequestHandler, self.ID)

     # Compartments Add Methods
    def AddSCCompartment(self, _SCCompartmentConfig:Models.Compartments.SC.Configuration):
        return Models.Compartments.SC.SC(_SCCompartmentConfig, self.RequestHandler, self.ID)


    def AddSCCompartments(self, _SCCompartmentConfigs:list):
        return Models.Compartments.SC.BatchCreate(_SCCompartmentConfigs, self.RequestHandler, self.ID)

       
    # Neurons Add Methods
    def AddBSNeuron(self, _BSNeuronConfig:Models.Neurons.BS.Configuration):
        return Models.Neurons.BS.BSNeuron(_BSNeuronConfig, self.RequestHandler, self.ID)

    # Neurons Add Methods
    def AddSCNeuron(self, _SCNeuronConfig:Models.Neurons.SC.Configuration):
        return Models.Neurons.SC.SCNeuron(_SCNeuronConfig, self.RequestHandler, self.ID)

    
     # Geometry Add Methods
    def AddSphere(self, _SphereConfig:Sphere.Configuration):
        return Sphere.Sphere(_SphereConfig, self.RequestHandler, self.ID)

    def AddSpheres(self, _SphereConfigs:list):
        return Sphere.BatchCreate(_SphereConfigs, self.RequestHandler, self.ID)

    def AddBox(self, _BoxConfig:Box.Configuration):
        return Box.Box(_BoxConfig, self.RequestHandler, self.ID)

    def AddBoxes(self, _BoxConfigs:list):
        return Box.BatchCreate(_BoxConfigs, self.RequestHandler, self.ID)

    def AddCylinder(self, _CylinderConfig:Cylinder.Configuration):
        return Cylinder.Cylinder(_CylinderConfig, self.RequestHandler, self.ID)

    def AddCylinders(self, _CylinderConfigs:list):
        return Cylinder.BatchCreate(_CylinderConfigs, self.RequestHandler, self.ID)


    ## Simulation Update Routes
    def Reset(self):
        QueryList:list = []
        QueryList.append({
            "Simulation/Reset": {
                "SimulationID": self.ID
            }
        })
        Response = self.RequestHandler.BuildPostQuery(QueryList, "/NES")[0]
        assert(Response != None)
        return Response

    def RunFor(self, _SimulationDuration_ms:float):
        QueryList:list = []
        QueryList.append({
            "Simulation/RunFor": {
                "SimulationID": self.ID,
                "Runtime_ms": _SimulationDuration_ms
            }
        })
        Response = self.RequestHandler.BuildPostQuery(QueryList, "/NES")[0]
        assert(Response != None)
        return Response

    def RecordAll(self, _MaxRecordTime_ms:float):
        QueryList:list = []
        QueryList.append({
            "Simulation/RecordAll": {
                "SimulationID": self.ID,
                "MaxRecordTime_ms": _MaxRecordTime_ms
            }
        })
        Response = self.RequestHandler.BuildPostQuery(QueryList, "/NES")[0]
        assert(Response != None)
        return Response

    def GetRecording(self):
        QueryList:list = []
        QueryList.append({
            "Simulation/GetRecording": {
                "SimulationID": self.ID,
            }
        })
        Response = self.RequestHandler.BuildPostQuery(QueryList, "/NES")[0]
        assert(Response != None)
        return Response

    def GetStatus(self):
        QueryList:list = []
        QueryList.append({
            "Simulation/GetStatus": {
                "SimulationID": self.ID,
            }
        })
        Response = self.RequestHandler.BuildPostQuery(QueryList, "/NES")[0]
        assert(Response != None)
        return Response


    ## Wait Helpers
    def WaitUntilNotBusy(self, _Text:str="Waiting For Simulation Processing To Complete"):
        WaitSpinner = yaspin.yaspin(text=_Text, color="green", timer=True)
        WaitSpinner.start()
        while (self.GetStatus()["IsSimulating"]):
            time.sleep(0.25)
        WaitSpinner.ok()


    ## Visualizer Setup Methods
    def SetupVisualizer(self):
        return Visualizer(self.RequestHandler, self.ID)