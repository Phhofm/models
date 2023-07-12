ONNX Conversions

These are onnx conversion files. I provide them since the .pth file can only be run if the program/application/code used to upscale actually includes the SRFormer_arch information. So with these files, this model can stil be used with chaiNNer since the onnx file includes the arch information, it includes basically everything an upscaler would need to know to use this model.

I made two versions here, depending on the input dimensions (width and hight) of your input:
The _16 (as in 2xHFA2kAVCSRFormer_light_16) meaning image input dimensions (both width and hight) need to be divisible by 16
The _64 (as in 2xHFA2kAVCSRFormer_light_64) meaning image input dimensions (both width and hight) need to be divisible by 64

Then you find the fp32 and fp16 conversions of these
And then both of these have been simplified/optimized with onnxsim

so the final versions are (recommended to try out)
2xHFA2kAVCSRFormer_light_16_onnxsim_fp16.onnx
2xHFA2kAVCSRFormer_light_64_onnxsim_fp16.onnx

if these dont work for some reason you can try out the fp32 versions
2xHFA2kAVCSRFormer_light_16_onnxsim_fp32.onnx
2xHFA2kAVCSRFormer_light_64_onnxsim_fp32.onnx

if these do also not work then there was a problem in the optimization step, try the unoptimized versions
2xHFA2kAVCSRFormer_light_16_fp16.onnx
2xHFA2kAVCSRFormer_light_32_fp16.onnx

And then, as a last resort, you could try the original conversions straight from the .pth file
2xHFA2kAVCSRFormer_light_16_fp32.onnx
2xHFA2kAVCSRFormer_light_32_fp32.onnx
