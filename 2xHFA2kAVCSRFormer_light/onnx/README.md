ONNX Conversions

_16 means input dimensions need to be divisible by 16
_64 means input dimensions need to be divisible by 64

Try out the onnxsim 16fp


Conversion process

1. I did a pth to _fp32 conversion
2. Then I onnxsim'd that one (_onnxsim)
3. Then I made a _fp16 out of that one

So 2xHFA2kAVCSRFormer.pth > 2xHFA2kAVCSRFormer_64_fp32.onnx > 2xHFA2kAVCSRFormer_onnxsim_fp32.onnx > 2xHFA2kAVCSRFormer_onnxsim_fp16.onnx

And

So 2xHFA2kAVCSRFormer.pth > 2xHFA2kAVCSRFormer_16_fp32.onnx > 2xHFA2kAVCSRFormer_16_onnxsim_fp32.onnx > 2xHFA2kAVCSRFormer_16_onnxsim_fp16.onnx
