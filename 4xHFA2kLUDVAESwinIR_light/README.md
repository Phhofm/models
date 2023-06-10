**4xHFA2kLUDVAESwinIR_light**

Name: 4xHFA2kLUDVAESwinIR_light  
License: CC BY 4.0  
Network: SwinIR  
Scale: 4  
Purpose: An anime images 4x upscaling model with realistic degradations, based on musl's HFA2k_LUDVAE dataset   
Iterations: 350,000  
batch_size: 3  
HR_size: 256  
Epoch: 99 (require iter number per epoch: 3424)  
Dataset: HFA2kLUDVAE  
Number of train images: 10270  
OTF Training: No  
Pretrained_Model_G: None  

Description: 4x anime image upscaler with realistic degradations (compression, noise, blur). Visual outputs can be found in the 4xHFA2kLUDVAE_results folder, together with timestamps and metrics to compare inference speed on the val set with other trained models/networks on this dataset.

---

Name: 4xHFA2kLUDVAESwinIR_light_gt128  
License: CC BY 4.0  
Network: SwinIR  
Scale: 4  
Purpose: An anime images 4x upscaling model with realistic degradations, based on musl's HFA2k_LUDVAE dataset   
Iterations: 300,000  
batch_size: 3  
HR_size: 128  
Epoch: 85 (require iter number per epoch: 3424)  
Dataset: HFA2kLUDVAE  
Number of train images: 10270  
OTF Training: No  
Pretrained_Model_G: None  

Description: 4x anime image upscaler with realistic degradations. This is the older version of this model with gt_size set to 128 for the future for me to compare with other networks, since training higher gt_size takes longer. This is part of a Series I am doing where I am trying out different Networks on the same dataset with similiar settings. For example 4xHFA2kLUDVAESRFormer_light_gt128 used the same settings also to 300k iter. If I like a model, I will try to improve on it still, but I wanted the same settings to be able to compare network outputs and speed. PS 'SwinIR_light' and 'SwinIR Small' are the same.
