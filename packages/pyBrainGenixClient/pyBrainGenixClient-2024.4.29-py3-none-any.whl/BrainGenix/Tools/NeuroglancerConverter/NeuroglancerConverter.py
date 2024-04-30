# BrainGenix-NES
# AGPLv3

import BrainGenix.NES as NES
import math
import json
import os

from PIL import Image

DATA_TYPE:str = "jpeg"

InfoStr = '''{
  "data_type": "uint8",
  "num_channels": 3,
  "scales": [
    {
      "chunk_sizes": [
        [
          1024,
          1024,
          1
        ]
      ],
      "encoding": "png",
      "key": "Data",
      "resolution": [
        20,
        20,
        40
      ],
      "size": [
        1024,
        1024,
        9
      ],
      "voxel_offset": [
        0,
        0,
        0
      ]
    }
  ],
  "type": "image"
}
'''

ProvenanceStr = '''
{
  "description": "",
  "owners": [],
  "processing": [],
  "sources": []
}'''


def NeuroglancerConverter(_VSDA_EM_Instnce:object, _OutputDirectory:str = "NeuroglancerOutput"):

    # Convenience
    Cfg = _VSDA_EM_Instnce.Configuration

    # Build Directory Structure
    try:    
        os.makedirs(f"{_OutputDirectory}/Data")
    except FileExistsError:
        pass
    
    try:    
      os.makedirs(f"{_OutputDirectory}/Temp")
    except FileExistsError:
        pass


    # Get Images
    _VSDA_EM_Instnce.SaveImageStack(f"{_OutputDirectory}/Temp")


    # Firstly, Get the Index Data
    RawImageJSONData = _VSDA_EM_Instnce.GetIndexData()




    # Now, Build the Format Info

    InfoDict = json.loads(InfoStr)
    InfoDict["scales"][0]["chunk_sizes"][0][0] = Cfg.ImageWidth_px
    InfoDict["scales"][0]["chunk_sizes"][0][1] = Cfg.ImageHeight_px


    MaxXIndex = math.ceil(RawImageJSONData["RegionEndXIndex"] / Cfg.ImageWidth_px) * Cfg.ImageWidth_px
    MaxYIndex = math.ceil(RawImageJSONData["RegionEndYIndex"] / Cfg.ImageHeight_px) * Cfg.ImageHeight_px
    MaxZIndex = RawImageJSONData["RegionEndZIndex"]

    InfoDict["scales"][0]["resolution"][0] = int(Cfg.PixelResolution_nm * 1000.0) # convert from um to nm
    InfoDict["scales"][0]["resolution"][1] = int(Cfg.PixelResolution_nm * 1000.0) # convert from um to nm
    InfoDict["scales"][0]["resolution"][2] = int(int(Cfg.SliceThickness_nm / Cfg.PixelResolution_nm) * 1000.0 * Cfg.PixelResolution_nm) # convert from um to nm

    InfoDict["scales"][0]["encoding"] = DATA_TYPE

    InfoDict["scales"][0]["size"][0] = MaxXIndex
    InfoDict["scales"][0]["size"][1] = MaxYIndex
    InfoDict["scales"][0]["size"][2] = MaxZIndex

    with open(f"{_OutputDirectory}/info", "w") as f:
        f.write(json.dumps(InfoDict))

    with open(f"{_OutputDirectory}/provenance", "w") as f:
        f.write(ProvenanceStr)

    # Limit Indices to a capped value
  


    # Now Move All The Files
    ImageProperties = RawImageJSONData["ImageProperties"]
    for i in range(len(ImageProperties)):
        
        ThisImage = ImageProperties[i]

        X1 = min(ThisImage["StartXIndex"], MaxXIndex)
        X2 = min(ThisImage["EndXIndex"], MaxXIndex)
        Y1 = min(ThisImage["StartYIndex"], MaxYIndex)
        Y2 = min(ThisImage["EndYIndex"], MaxYIndex)
        Z1 = min(ThisImage["StartZIndex"], MaxZIndex)
        Z2 = min(ThisImage["EndZIndex"], MaxZIndex)
        NewFilename = f"{X1}-{X2}_{Y1}-{Y2}_{Z1}-{Z2}"
        OldFilename = ThisImage["Handle"].replace("/", "_").strip("Renders")[1:]


        # Neuroglancer does not like png for some reason
        #os.rename(f"{_OutputDirectory}/Temp/{OldFilename}", f"{_OutputDirectory}/Data/{NewFilename}")


        LoadedImg = Image.open(f"{_OutputDirectory}/Temp/{OldFilename}")
        RGBImage = LoadedImg.convert("RGB")
        RGBImage.save(f"{_OutputDirectory}/Data/{NewFilename}.{DATA_TYPE}")
        os.rename(f"{_OutputDirectory}/Data/{NewFilename}.{DATA_TYPE}", f"{_OutputDirectory}/Data/{NewFilename}")
        print(f"Processed {i}/{len(ImageProperties)} ({_OutputDirectory}/Data/{NewFilename})")