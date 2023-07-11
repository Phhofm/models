from traiNNer.archs.srformer_arch import SRFormer
import torch

print("Converting")

# parameters depend on model and you need to set them manually if it errors
model = SRFormer(type=SRFormer, upscale=2, in_chans=3, img_size=64, window_size=16, img_range=1., embed_dim=60, mlp_ratio=2, upsampler='pixelshuffledirect', resi_connection='1conv', depths=[6, 6, 6, 6], num_heads=[6, 6, 6, 6])

state_dict = torch.load("2xHFA2kAVCSRFormer_light.pth")

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
dummy_input = torch.rand(1, 3, 16, 16).cuda()

# fp32
torch.onnx.export(
    model,
    dummy_input,
    "2xHFA2kAVCSRFormer_light.onnx",
    opset_version=14,
    verbose=False,
    input_names=["input"],
    output_names=["output"],
    dynamic_axes=dynamic_axes,
)
# fp16
torch.onnx.export(
    model.half(),
    dummy_input.half(),
    "2xHFA2kAVCSRFormer_light_fp16.onnx",
    opset_version=14,
    verbose=False,
    input_names=["input"],
    output_names=["output"],
    dynamic_axes=dynamic_axes,
)
print("Finished")
