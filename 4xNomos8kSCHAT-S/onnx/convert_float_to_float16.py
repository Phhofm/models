import onnx
from onnxconverter_common import float16

model = onnx.load("4xNomos8kSCHAT-S_131616_onnxsim.onnx")
model_fp16 = float16.convert_float_to_float16(model)
onnx.save(model_fp16,"4xNomos8kSCHAT-S_131616_onnxsim_fp16.onnx")
