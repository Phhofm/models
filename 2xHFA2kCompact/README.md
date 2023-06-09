**2xHFA2kCompact**  

Name: 2xHFA2kCompact  
License: CC BY 4.0  
Network: SRVGGNetCompact, with parameters: 600,652  
Scale: 2  
Purpose: A compact anime 2x upscaling model based on musl's HFA2k dataset  

Iterations: 93,000  
batch_size: 12  
HR_size: 384  
Epoch: 207 (require iter number per epoch: 214)  
Dataset: HFA2k  
Number of train images: 2568  
OTF Training: Yes  
Pretrained_Model_G: 4x_Compact_Pretrain  
Training time: 24h+  

Description: Compact 2x anime upscaler with otf compression and blur. The '2xHFA2kCompact.pth' (4.6 MB) is the original trained model file, the other model files are conversions using chaiNNer. Trained on musl's latest dataset release for Anime SISR, which has been extracted from modern anime films, where the selection criteria was high SNR, no DOF and high frequency information.  

Examples: https://imgsli.com/MTcxNjA4  
Example input files: https://drive.google.com/drive/folders/1VSPw8m7VbZO6roM9syE7Nf2QYwwn7GUz   
Example output files: https://drive.google.com/drive/folders/1NFfomnv6d5RtWy_GwOsKO3uZ_HNOo-2i  

Future work: Started training a 4xRRDBNet version of this, bigger model so maybe better results but slower, for still/ single anime images. Will release in the future or drop, based on achieved results.
