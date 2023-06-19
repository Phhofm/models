**2xHFA2kAVCOmniSR**

Name: 2xHFA2kAVCOmniSR  
License: CC BY 4.0  
Network: OmniSR  
Scale: 2  
Purpose: 2x anime upscaling model that handles AVC (h264) compression   
Iterations: 175,000  
batch_size: 2-5  
HR_size: 128-192  
Dataset: HFA2k_h264  
Number of train images: 2568  
OTF Training: No  
Pretrained_Model_G: None  

Description: The second released community trained model on the OmniSR network. Trained with multiscale discriminator to fix decreased output brightness occuring with OmniSR. 2x anime upscale that handles AVC (h264) compression since h264 crf 20-28 degradation together with bicubic, bilinear, box and lanczos downsampling has been applied on the HFA2k dataset with Kim's dataset destroyer.  

Examples:  
https://imgsli.com/MTg2ODcz  
https://imgsli.com/MTg2ODc1  



**2xHFA2kAVCOmniSR_Sharp**

Name: 2xHFA2kAVCOmniSR_Sharp  
License: CC BY 4.0  
Network: OmniSR  
Scale: 2  
Purpose: 2x sharp anime upscaling model that handles AVC (h264) compression   
Iterations: 229,000  
batch_size: 2-5  
HR_size: 128-192  
Dataset: HFA2k_h264  
Number of train images: 2568  
OTF Training: No  
Pretrained_Model_G: None  

Description: A sharper version of 2xHFA2kAVCOmniSR since it has been further trained with some additional USM applied. I recommend using 2xHFA2kAVCOmniSR in general, but if more sharpness is desired or you simply like these results better for your input source, you can of course also give this model a go :)
