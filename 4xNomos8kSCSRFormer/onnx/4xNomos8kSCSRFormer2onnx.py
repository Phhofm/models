from traiNNer.archs.srformer_arch import SRFormer
import torch

print("Converting")

# parameters depend on model and you need to set them manually if it errors
model = SRFormer(type=SRFormer, upscale=4, in_chans=3, img_size=48, window_size=22, img_range=1., embed_dim=180, mlp_ratio=2, upsampler='pixelshuffle', resi_connection='1conv', depths=[6, 6, 6, 6, 6, 6], num_heads=[6, 6, 6, 6, 6, 6])

state_dict = torch.load("/home/phips/Downloads/net_g_75000.pth")

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
dummy_input = torch.rand(1, 3, 12, 12).cuda()

# fp32
torch.onnx.export(
    model,
    dummy_input,
    "model.onnx",
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
#    "model_fp16.onnx",
#    opset_version=14,
#    verbose=False,
#    input_names=["input"],
#    output_names=["output"],
#    dynamic_axes=dynamic_axes,
#)
print("Finished")
