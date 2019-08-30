import sys
import os
import coremltools
from coremltools.models.neural_network.quantization_utils import *

model_folder = "../../models/20190829_gpu5000/"
quantized_folder = "quantized/"

try:
    os.mkdir(model_folder+quantized_folder)
except OSError:
    print ("Could not create the quantized folder")

mode_name = "uniformRecognizer"

model = coremltools.models.MLModel(model_folder+mode_name+".mlmodel")
#model.visualize_spec()

functions = ["kmeans"]
#functions = ["linear", "linear_lut", "kmeans", "kmeans_lut"]

for function in functions :
    for bit in [16,8]:
    #for bit in [16,8,4,2,1]:
        print("processing ",function," on ",bit,".")    
        lin_quant_model = quantize_weights(model, bit, function)
        lin_quant_model.short_description = str(bit)+" bit per quantized weight, using "+function+"."
        lin_quant_model.save(model_folder+quantized_folder+mode_name+"_"+function+"_"+str(bit)+".mlmodel")