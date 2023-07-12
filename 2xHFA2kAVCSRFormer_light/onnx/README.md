ONNX Conversions

These are onnx conversion files. I provide them since the .pth file can only be run if the program/application/code used to upscale actually includes the SRFormer_arch information. So with these files, this model can stil be used with chaiNNer since the onnx file includes the arch information, it includes basically everything an upscaler would need to know to use this model.

I made two versions here, depending on the input dimensions (width and hight) of your input:
If your image input dimensions are divisible by 16, use the _16 version (as in 2xHFA2kAVCSRFormer_light_16)
If your image input dimensions are divisible by 64, use the _64 version (as in 2xHFA2kAVCSRFormer_light_64)

I made fp16 and fp32 conversions of these and simplified/optimized them with onnxsim.

So the final versions are (recommended to try out):
2xHFA2kAVCSRFormer_light_16_onnxsim_fp16.onnx
2xHFA2kAVCSRFormer_light_64_onnxsim_fp16.onnx

If these dont work for you some reason you can try out the fp32 versions
2xHFA2kAVCSRFormer_light_16_onnxsim_fp32.onnx
2xHFA2kAVCSRFormer_light_64_onnxsim_fp32.onnx

If these still do not work on your system then there might be a problem in the optimization step, try the unoptimized versions
2xHFA2kAVCSRFormer_light_16_fp16.onnx
2xHFA2kAVCSRFormer_light_32_fp16.onnx

And then, as a last resort, you could try the original conversions straight from the .pth file
2xHFA2kAVCSRFormer_light_16_fp32.onnx
2xHFA2kAVCSRFormer_light_32_fp32.onnx
