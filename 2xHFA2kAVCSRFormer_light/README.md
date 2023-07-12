**2xHFA2kAVCSRFormer_light**

Name: 2xHFA2kAVCSRFormer_light  
License: CC BY 4.0  
Network: SRFormer_light  
Scale: 2  
Purpose: 2x anime upscaling model that handles AVC (h264) compression   
Iterations: 140000  
batch_size: 2-4  
HR_size: 128-192  
Dataset: HFA2k_h264  
Number of train images: 2568  
OTF Training: No  
Pretrained_Model_G: SRFormerLight_SRx2_DIV2K.pth  

Description: 2x SRFormer_light anime upscale model that handles AVC (h264) compression since h264 crf 20-28 degradation together with bicubic, bilinear, box and lanczos downsampling has been applied on musl's HFA2k dataset with Kim's dataset destroyer.  

An onnx folder is provided since this pth file cannot be run with for example chaiNNer since the SRFormer arch info needs to be present. But the onnx files can be run with chaiNNer, since onnx bundles/includes all the necessary information for the model file to be run with the file.

If your image input dimensions (both width and hight of the input image you want to upscale) are divisible by 16, try the 2xHFA2kAVCSRFormer_light_16_onnxsim_fp16.onnx file. If they are divisible by 64, try out the 2xHFA2kAVCSRFormer_light_64_onnxsim_fp16.onnx file. More infos in the README file inside the onnx folder itself.
