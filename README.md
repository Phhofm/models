# Models

A repo for me to publish trained models. After having made my [interactive visual comparison site of upscaling models](https://phhofm.github.io/upscale/) I started  training image models myself. Released models have been trained for a minimum of 24 hours. Each folder should contain its own *README.md* file with infos to the model.

### Released  

**4xLSDIRCompact** - My first release - a compact model for photo upscaling. Up to 3 versions, version 3 contains N C R models, version 2 is a general model interpolated of C and R. Trained on the huge LSDIR dataset (84991 images *2 for paired training C around 160 GB).  

**2xHFA2xCompact** - My second release - an anime compact (=fast) upscaling model for anime video clips, can also be used for still images.  

### Experimental / In Progress  

**4xHFA2k** - Anime upscaling RRDBNet model for still images (can also be used for clips but will be way slower).  

**4xNomos8kS** - A photo upscaling RRDBNet model based on musl's Nomos8k_sfw dataset.  

**1xunstroyerCompact** - A compact model removing various degradations (blur, noise, compression) from an image. Trained with using kim's destroyer script on musl's Nomos8k_sfw dataset.  

**1xunvideoCompact** - A compact model removing video compression (MPEG, MPEG-2, H264, HEVC) from an image. Trained with using kim's destroyer script on musl's Nomos8k_sfw dataset. 

**1xunstroyerAnimeCompact** - Like 1xunstroyerCompact but trained on anime images, musl's HFA2k dataset, using kim's destroyer.  

**1xunvideoAnimeCompact** - Like 1xunvideCompact to remove video compression but trained on anime images, musl's HFA2k dataset, using kim's destroyer.  

**2xParimgCompact** - The very first training process I had started without any adaptation to the dataset, a compact model on Microsofts ImagePairs (11,421 images, 111 GB ) for photo upscaling.  

**4xLSDIR** - A RRDBNet model, simple ESRGAN experiment without any degradations and without any pretrain for photo upscaling.  

**4xLSDIRplus** - An RRDBNet experiment to see what influence a huge dataset has on the official x4plus model for photo upscaling.  

### Pretrains  

**CompactPretrains** - These pretrains have been provided by Zarxrax and they are great to use to kick off training a compact model.  
