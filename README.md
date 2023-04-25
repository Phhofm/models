# Models

A repo for me to publish trained models. Complete models have all been trained for a minimum of 24 hours.

If there are N, C and R versions this means that N is without (No) degradation (for good quality small input), C for compression handling (web sources) and R to handle additional degradations like noise. C and R can often be interpolated with 75% and 25% to handle compression and just a little bit of noise.

Since Github does not like files above 100MB (unless LFS were used) not all .pth files will be uploaded but the conversions (ONNX, NCNN) produce a way smaller file so these should all be presentr on this repo.

### Released

**4xLSDIRCompact** - my first released / completely trained model for photo upscaling. Up to 3 versions, version 3 contains N C R models, version 2 is a general model interpolated of C and R. Trained on the huge LSDIR dataset (84991 images *2 for paired training C around 160 GB)

**2xHFA2xCompact** - my second release - an anime compact (=fast) upscaling model for anime video clips, can also be used for still images

### In Progress

**4xHFA2k** - Anime upscaling model for still images (can also be used for clips but will be way slower)

**4xNomos8kS** - a photo upscaling model based on musl's nomos8k_sfw dataset

### Experiments

**2xParimgCompact** - the very first training process I had started without any adaptation to the dataset, a compact model on Microsofts ImagePairs (11,421 images, 111 GB ). Photo upscaling.

**4xLSDIR** - A non-compact model, simple ESRGAN experiment without any degradations and without any pretrain. Photo upscaling.

**4xLSDIRplus** - An experiment to see what influence a huge dataset has on the official x4plus model. Photo upscaling.

### Pretrains

**CompactPretrains** - these pretrains have been provided by Zarxrax and they are great to use to kick off training a compact model





