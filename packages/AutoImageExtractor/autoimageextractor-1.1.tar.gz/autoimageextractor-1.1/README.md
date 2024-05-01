# AutoImageExtractor

This is a python module used to automatically extract features from a directory of images in a single line.

## Code

### from AutoImageExtractor import FeatureExtractor

### data=FeatureExtractor.extract(image_path,classname,technique_list)

## Parameters

Image path- provide the path of the directory of images

Classname- Mention the name of the class the images belong to, if any

technique_list- mention the list of techniques, available- GLCM, LBP, BRIEF. If not, default statistical parameters are calculated.