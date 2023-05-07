**4xHFA2k**

Name: 4xHFA2k  
License: CC BY 4.0  
Network: RRDBNet  
Scale: 4  
Purpose: An anime images 4x upscaling model based on musl's HFA2k dataset  
Iterations: 91,000  
batch_size: 9  
HR_size: 256  
Epoch: 318 (require iter number per epoch: 286)  
Dataset: HFA2k  
Number of train images: 2568  
OTF Training: Yes  
Pretrained_Model_G: RealESRGAN_x4plus.pth  
Training time: 36h on a  P100 GPU  

Description: 4x anime image upscaler with otf jpg compression and blur. Trained on musl's latest dataset release for Anime SISR, which has been extracted from modern anime films, where the selection criteria was high SNR, no DOF and high frequency information.  

Examples: https://imgsli.com/MTc2NDgx (PS Example input images are small, each around 500x280 px)  
Example input files: https://drive.google.com/drive/folders/1RI6gGqRy-KxDujbaIrpEMdvFkIWHvfPt  
Example output files: https://drive.google.com/drive/folders/1GqHwPlFp6bIQl4R1AxmrmJ6vUUD8FUxH  