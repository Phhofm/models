Status: Experimental / Incomplete

This was a try to see if more data improves a model since the LSDIR dataset is huge. I got away from using the full dataset after the compact model and these tries. All only with batch size 1. Would need further training, but dataset is huge.

4xLSDIRplusN  
iter: 110000  
degradations: none  
dataset: LSDIR  
RRDBNet  
pretrain: x4plus  
batch size: 1  

4xLSDIRplusC  
iter: 85000  
degradations: compression  
dataset: LSDIR  
RRDBNet  
pretrain: x4plus  
batch size: 1  

4xLSDIRplusR  
iter: 100000  
degradations: otf real-esrgan - blur, noise, compression  
dataset: LSDIR  
RRDBNet  
pretrain: x4plus  
batch size: 1  
