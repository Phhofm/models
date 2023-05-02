Status: Experimental

**Name:** 2xParimgCompact  
**License:** CC BY 4.0  
**Model Architecture:** SRVGG  
**Scale:** 2  
**Purpose:** Restore images  
**Iterations:** 88'0000  
**Epoch:** 143  
**batch_size:** 2  
**HR_size:** 128  
**Dataset:** ImagePairs  

**Dataset_size:** 2x 11,421  
**OTF Training** No (PairedImageDataset)  
**Pretrained_Model_G:** None  
**Description:** This was a compact model I started when trying out to get the whole model training code running. As a paired image dataset, the ImagePairs (11,421 pairs of low- and high-resolution images of diverse scenes, 111 GB). I abandoned this project and worked on the 4xLSDIRCompact which became my first model.