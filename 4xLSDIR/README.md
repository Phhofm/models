Name: 4xLSDIR
License: CC BY 4.0
Network: RRDBNet
Scale: 4
Purpose: 4x undegraded photo upscaling

Iterations: 225000  
batch_size: 1-5  
HR_size: 192  
Dataset: LSDIR  
Number of train images: 2x 84991
OTF Training: No
Pretrained_Model_G: None

Description: A normal ESRGAN model without degradations and without any pretrain, simply an RRDBNet model trained on paired dataset (4x downsampled) on the full LSDIR dataset (84,991 images / 165 GB)
