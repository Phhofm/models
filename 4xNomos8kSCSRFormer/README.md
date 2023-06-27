**4xNomos8kSCSRFormer**

Name: 4xNomos8kSCSRFormer  
License: CC BY 4.0  
Network: SRFormer  
Scale: 4  
Purpose: A photo 4x upscaling model based on musl's Nomos8k_sfw dataset for realistic sr  
Iterations: 115,000  
batch_size: 4  
HR_size: 256  
Dataset: Nomos8k_sfw  
Number of train images: 6118  
OTF Training: Yes  
Pretrained_Model_G: SRFormer_SRx4_DF2K.pth  

Description: 4x photo upscaler with otf jpg compression and blur, trained on musl's Nomos8k_sfw dataset for realisic sr

Important: The "4xNomos8kSCSRFormer.7z" file in here is a 7zip compressed archive (LZMA2, ultra) and needs to be exctracted first to use the containing pth file which is 185.4 MB, I compressed it because I can only push smaller than 100 MB files to github without needing git lfs.  
[Link to uncompressed pth file (google drive)](https://drive.google.com/file/d/1VpMity5vqrEN7YFaPwawhVTdWYdJK8DG)
