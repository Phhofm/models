**4xLSDIRCompact2**

**Name:** 4xLSDIRCompact2  
**License:** CC BY 4.0   
**Model Architecture:** SRVGG  
**Scale:** 4  
**Purpose:** Upscale photos to x4 their size

**Iterations:** CompactC2 205’000 & CompactR2 150’000  
**batch_size:** Variable(1-10)  
**HR_size:** 256  
**Dataset:** LSDIR  
**Dataset_size:** 84991  
**OTF Training** No/Yes  
**Pretrained_Model_G:** 4x_Compact_Pretrain.pth
  
**Description:** 4xLSDIRCompactv2 supersedes the previously released models, it combines all my progress on my compact model. Both CompactC and CompactR had received around 8 hours more training since release with batch size 10 (CompactR had only been up to 5 on release), and these two were then interpolated together. This allows v2 to handle some degradations, while preserving the details of the CompactC model. Examples: https://imgsli.com/MTY0Njgz/0/2 