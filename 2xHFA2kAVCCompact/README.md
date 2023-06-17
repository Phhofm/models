**2xHFA2kAVCCompact**

Name: 2xHFA2kAVCCompact  
License: CC BY 4.0  
Network: SRVGGNet  
Scale: 2  
Purpose: Fast 2x anime upscaling model that handles AVC (h264) degradation   
Iterations: 111,000  
batch_size: 4  
HR_size: 256  
Dataset: HFA2k_h264  
Number of train images: 2568  
OTF Training: No  
Pretrained_Model_G: None  

Description: 2x anime upscale that handles AVC (h264) degradation. Applied h264 crf 20-28 degradation together with bicubic, bilinear, box and lanczos downsampling on the HFA2k dataset with Kim's dataset destroyer (check the applied_degradations.txt on my repo for exact info).  
