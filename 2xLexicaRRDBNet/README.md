## 2xLexicaRRDBNet  

Name: 2xLexicaRRDBNet  
License: CC BY 4.0  
Network: RRDBNet  
Scale: 2  
Purpose: Upscaling AI generated images  
Iterations: 185'000  
batch_size: 4  
HR_size: 128  
Epoch: 17 (require iter number per epoch: 10964)  
Dataset: lexica-aperture-v3-small  
Number of train images: 43856  
OTF Training: No  
Pretrained_Model_G: None  

Description: 2x upscaler for AI generated images. Trained on 43856 images from lexica.art, so its trained specifically on that model but should work in general on ai generated images.   

16 Examples with Input, Upscaled (Normal and Sharp) and GT Files, plus example data: https://drive.google.com/drive/folders/1LT20d5u1m8CryCrXOJ7pWJd0mlN7X5yA  
 
Name: 2xLexicaRRDBNet_Sharp  
License: CC BY 4.0  
Network: RRDBNet  
Scale: 2  
Purpose: Upscaling AI generated images - a bit sharper outputs then above model  
Iterations: 220'000  
batch_size: 4  
HR_size: 128  
Epoch: 18 (require iter number per epoch: 10964)  
Dataset: lexica-aperture-v3-small  
Number of train images: 43856  
OTF Training: No  
Pretrained_Model_G: None  

Description: Its like the above model, but trained for some more with l1_gt_usm and percep_gt_usm set to true, resulting in sharper outputs. I provide both so they can be chosen based on preferrence of the user.  

