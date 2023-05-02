**4xHFA2k**

Name: 4xHFA2k  
License: CC BY 4.0  
Network: RRDBNet  
Scale: 4  
Purpose: An anime 4x upscaling model based on musl's HFA2k dataset, can handle a bit of JPG compression and blur.

Iterations: 91,000
batch_size: 9
HR_size: 256
Epoch: 318 (require iter number per epoch: 286)
Dataset: HFA2k
Number of train images: 2568
OTF Training: Yes
Pretrained_Model_G: RealESRGAN_x4plus.pth
Training time: 36h on a  P100 GPU

Description: 4x anime upscaler with otf compression and blur. Trained on musl's latest dataset release for Anime SISR, which has been extracted from modern anime films, where the selection criteria was high SNR, no DOF and high frequency information.

Examples: https://imgsli.com/MTcxNjA4
Example input files: https://drive.google.com/drive/folders/1VSPw8m7VbZO6roM9syE7Nf2QYwwn7GUz 
Example output files: https://drive.google.com/drive/folders/1NFfomnv6d5RtWy_GwOsKO3uZ_HNOo-2i

Future work: Started training a 4xRRDBNet version of this, bigger model so maybe better results but slower, for still/ single anime images. Will release in the future or drop, based on achieved results.