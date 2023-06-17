**2xHFA2kAVCEDSR_M**

Name: 2xHFA2kAVCEDSR_M  
License: CC BY 4.0  
Network: EDSR  
Scale: 2  
Purpose: Fast 2x anime upscaling model that handles AVC (h264) degradation   
Iterations: 186,000  
batch_size: 2-5  
HR_size: 384  
Epoch: 317 (require iter number per epoch: 1284)  
Dataset: HFA2k_h264  
Number of train images: 2568  
OTF Training: No  
Pretrained_Model_G: None  

Description: 2x anime upscale that handles AVC (h264) degradation. Applied h264 crf 20-28 degradation and bicubic,bilinear,box,lanczos downsampling on the HFA2k dataset with Kim's dataset destroyer (check the applied_degradations.txt on my repo for exact info). On my local system tests this is one of my fastest released models yet (EDSR M).
