**4xHFA2kLUDVAESRFormer_light**

Name: 4xHFA2kLUDVAESRFormer_light  
License: CC BY 4.0  
Network: SRFormer  
Scale: 4  
Purpose: An anime images 4x upscaling model with realistic degradations, based on musl's HFA2k_LUDVAE dataset   
Iterations: 300,000  
batch_size: 3  
HR_size: 128  
Epoch: 88 (require iter number per epoch: 3424)  
Dataset: HFA2kLUDVAE  
Number of train images: 10270  
OTF Training: No  
Pretrained_Model_G: None  

Description: 4x anime image upscaler with realistic degradations. This is part of a Series I am doing where I am trying out different Networks on the same dataset with similiar settings. For example 4xHFA2kLUDVAESwinIR_light used the same settings also to 300k iter. If I like a model, I will try to improve on it still, but I wanted the same settings to be able to compare network outputs and speed.

Since this is from a Set, the visual outputs can be found in /home/phips/Documents/GitHub/models/4xHFA2kLUDVAE_results (also timestamps to compare inference speed on the val set on my system)
