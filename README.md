# Models

A repo for me to publish trained models. After having made my [interactive visual comparison site of upscaling models](https://phhofm.github.io/upscale/) I started experimenting around of training such image models myself instead of just applying them and these are some of the results. Complete models here have all been trained for a minimum of 24 hours.

If there are N, C and R versions this means that N is without (No) degradation (for good quality small input), C for compression handling (web sources) and R to handle additional degradations like noise. C and R can often be interpolated with 75% and 25% to handle compression and just a little bit of noise.  

Since Github does not like files above 100MB (unless LFS were used) not all .pth files will be uploaded but the conversions (ONNX, NCNN) produce a way smaller file so these should all be present in this repo.  

### Released  

**4xLSDIRCompact** - My first released / completely trained compact model for photo upscaling. Up to 3 versions, version 3 contains N C R models, version 2 is a general model interpolated of C and R. Trained on the huge LSDIR dataset (84991 images *2 for paired training C around 160 GB).  

**2xHFA2xCompact** - My second release - an anime compact (=fast) upscaling model for anime video clips, can also be used for still images.  

### In Progress  

**4xHFA2k** - Anime upscaling RRDBNet model for still images (can also be used for clips but will be way slower).  

**4xNomos8kS** - A photo upscaling RRDBNet model based on musl's Nomos8k_sfw dataset.  

### Experiments  

**1xunstroyerCompact** - A compact model removing various degradations from an image. Trained with using kim's destroyer script on musl's Nomos8k_sfw dataset.  

**2xParimgCompact** - The very first training process I had started without any adaptation to the dataset, a compact model on Microsofts ImagePairs (11,421 images, 111 GB ) for photo upscaling.  

**4xLSDIR** - A RRDBNet model, simple ESRGAN experiment without any degradations and without any pretrain for photo upscaling.  

**4xLSDIRplus** - An RRDBNet experiment to see what influence a huge dataset has on the official x4plus model for photo upscaling.  

### Pretrains  

**CompactPretrains** - These pretrains have been provided by Zarxrax and they are great to use to kick off training a compact model.  
