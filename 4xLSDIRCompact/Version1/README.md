**4xLSDIRCompact1**

**Name:** 4xLSDIRCompact1  
**License:** CC BY 4.0  
**Model Architecture:** SRVGG  
**Scale:** 4  
**Purpose:** Upscale small good quality photos to 4x their size  

**Iterations:** 160000  
**batch_size:** Variable(1-10)  
**HR_size:** 256  
**Dataset:** LSDIR  
**Dataset_size:** 84991  
**OTF Training** No  
**Pretrained_Model_G:** 4x_Compact_Pretrain.pth  

**Description:** My first ever model 😀 Well, it’s not the best, but, it’s something ;) 
I provide some 15 examples from the validation set here for you to visually see the generated output (with chaiNNer), photo dimensions are in the name: https://imgsli.com/MTYxNDk3 

**Name:** 4xLSDIRCompactC1  
**License:** CC BY 4.0  
**Model Architecture:** SRVGG  
**Scale:** 4  
**Purpose:** Upscale small  photos with compression to 4x their size  

**Iterations:** 190000  
**batch_size:** Variable(1-10)  
**HR_size:** 256  
**Dataset:** LSDIR  
**Dataset_size:** 84991  
**OTF Training** No  
**Pretrained_Model_G:** 4xLSDIRCompact.pth  

**Description:** Trying to extend my previous model to be able to handle compression (JPG 100-30) by manually altering the training dataset, since 4xLSDIRCompact1 cant handle compression. Use this instead of 4xLSDIRCompact1 if your photo has compression (like an image from the web). 

**Name:** 4xLSDIRCompactR1  
**License:** CC BY 4.0  
**Model Architecture:** SRVGG  
**Scale:** 4  
**Purpose:** Upscale small photos with compression, noise and slight blur to 4x their size

**Iterations:** 130000  
**batch_size:** Variable(1-5)  
**HR_size:** 256  
**Dataset:** LSDIR  
**Dataset_size:** 84991  
**OTF Training** Yes  
**Pretrained_Model_G:** 4xLSDIRCompact.pth  

**Description:** Extending my last 4xLSDIRCompact1 model to Real-ESRGAN, meaning trained on synthetic data instead to handle more kinds of degradations, it should be able to handle compression, noise, and slight blur.

Here is a comparison to show that 4xLSDIRCompact1 cannot handle compression artifacts, and that these two models will produce better output for that specific scenario. These models are not ‘better’ than the previous one, they are just meant to handle a different use case: https://imgsli.com/MTYyODY3 