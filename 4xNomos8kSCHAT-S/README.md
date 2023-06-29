**4xNomos8kSCHAT-S**

Name: 4xNomos8kSCHAT-S
File Links:
pth(316.2MB):https://drive.google.com/file/d/18codpbxYcQecX7FNbYooUskfJR3lDBpr
Onnxfp16(154.1MB):https://drive.google.com/file/d/18codpbxYcQecX7FNbYooUskfJR3lDBpr
License: CC BY 4.0
Network: HAT
Scale: 4
Purpose: A photo 4x upscaling model based on musl's Nomos8k_sfw dataset for realistic sr
Iterations: 169,000
batch_size: 4
HR_size: 256
Dataset: Nomos8k_sfw
Number of train images: 6118
OTF Training: Yes
Pretrained_Model_G: HAT-S_SRx4.pth

Description: 4x photo upscaler with otf jpg compression and blur, trained on musl's Nomos8k_sfw dataset for realisic sr. (PS be aware of potentially RAM filling up and crashing the backend in chaiNNer when testing the onnx model, recognizable by the 'failed to fetch' error message)

Results in the 4xNomos8kSC_results folder.
