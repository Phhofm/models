from traiNNer.archs.omnisr_arch import OmniSRNet, OSAG
import torch

print("Converting")

# parameters depend on model and you need to set them manually if it errors
model = OmniSRNet(
type=OmniSRNet,
  num_in_ch=3,
  num_out_ch=3,
  num_feat=64,
  upsampling=2,
  res_num=5,
  block_num=1,
  bias=True,
  block_script_name=OSAG,
  block_class_name=OSAG,
  window_size=8,
  pe=True,
  ffn_bias=True
)

state_dict = torch.load("2xHFA2kAVCOmniSR.pth")

if "params_ema" in state_dict.keys():
    model.load_state_dict(state_dict["params_ema"])
else:
    model.load_state_dict(state_dict)

model.eval().cuda()
# https://github.com/onnx/onnx/issues/654
dynamic_axes = {
    "input": {0: "batch_size", 2: "width", 3: "height"},
    "output": {0: "batch_size", 2: "width", 3: "height"},
}
#dummy_input = torch.rand(1, 3, 64, 64).cuda()
dummy_input = torch.rand(1, 3, 64, 64).cuda()

# fp32
torch.onnx.export(
    model,
    dummy_input,
    "2xHFA2kAVCOmniSR_64.onnx",
    opset_version=14,
    verbose=False,
    input_names=["input"],
    output_names=["output"],
    dynamic_axes=dynamic_axes,
)
# fp16
#torch.onnx.export(
#    model.half(),
#    dummy_input.half(),
#    "2xHFA2kAVCOmniSR_fp16.onnx",
#    opset_version=14,
#    verbose=False,
#    input_names=["input"],
#    output_names=["output"],
#    dynamic_axes=dynamic_axes,
#)
print("Finished")
