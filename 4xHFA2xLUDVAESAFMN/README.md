## 4xHFA2kLUDVAESFMN

Name: 4xHFA2kLUDVAESFMN  
License: CC BY 4.0  
Network: SAFMN  
Scale: 4  
Purpose: Upscaling anime images with real-world degradation  
Iterations: 250'000  
batch_size: 5-40  
HR_size: 128-256  
Epoch: 77 (require iter number per epoch: 2568)  
Dataset: HFA2k-LUDVAE  
Number of train images: 10270 (last two used for val)  
OTF Training: No  
Pretrained_Model_G: None  

Description: Upscale anime images with real-world degradations with a fast network. This is part of the HFA2kLUDVAE series where I test out different networks on the same dataset so outputs (and speed test on the val set) can also be found there. Note that this model created artifacts on some of the val images. I therefore would use one of the other models since this one tends to create artifacts.  

