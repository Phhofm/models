# Models

A repo for me to publish trained models. After having made my [interactive visual comparison site of upscaling models](https://phhofm.github.io/upscale/) I started training image models myself. Released models have been trained for a minimum of 24 hours. Each folder should contain its own *README.md* file with infos to the model. Most of these models can be run as a demo in this corresponding [gradio space](https://huggingface.co/spaces/Phips/upscale_demo) but inference times will be long.

### Released  

**4xLSDIRCompact** - My first release - a 4x compact model for photo upscaling. Up to 3 versions, version 3 contains N C R models, version 2 is a general model interpolated of C and R. Trained on the huge LSDIR dataset (84991 images *2 for paired training C around 160 GB).  

**2xHFA2kCompact** - My second release - a 2x anime compact (=fast) upscaling model for anime video clips, can also be used for still images, trained on musl's HFA2k dataset.

**2xParimgCompact** - My third release - a 2x compact model based on Microsofts ImagePairs (11,421 images, 111 GB ) for photo upscaling. Was one of the very first models I had started training and finished it now. 

**4xHFA2k** - My fourth release - a 4x anime image upscaling RRDBNet model, trained on musl's HFA2k dataset.    

**4xNomos8kSC** - My fifth release - a realistic photo upscaling RRDBNet model based on musl's Nomos8k_sfw dataset.   

**2xLexicaRRDBNet & 2xLexicaRRDBNet_Sharp** - My sixth release - a 2x upscaler for AI generated images (no degradations), trained on around 34k images from lexica.art

**4xHFA2kLUDAVESwinIR_light** - My seventh release - 4x anime super-resolution with real degradation. trained on musl's HFA2kLUDVAE dataset (SwinIR small model).  

**4xHFA2kLUDVAESRFormer_light** - Also in my seventh release - 4x anime super-resolution with real degradation, trained on musl's HFA2kLUDVAE dataset (SRFormer light model).  

**4xHFA2kLUDVAEGRL_small** - My eight release - 4x anime super-resolution with real degradation, trained on musl's HFA2kLUDVAE dataset (GRL small model). 

### Experimental / In Progress    

**4xLSDIR** - A RRDBNet model, simple ESRGAN experiment without any degradations and without any pretrain for photo upscaling.  

**4xLSDIRplus** - An RRDBNet experiment to see what influence a huge dataset has on the official x4plus model for photo upscaling.  

**4xHFA2kLUDVAE** - Training lightweight models of different networks to test for interence speed and metrics for anime upscaling with realistic degradations. See results in the corresponding results folder.  

**Lexica** - Also training different models for AI generated image upscaling. (RRDBNet, HAT, SwinIR)  

### Pretrains  

**CompactPretrains** - These pretrains have been provided by Zarxrax and they are great to use to kick off training a compact model.  

### Interpolations

4xInt-Ultracri (UltraSharp + Remacri)  
4xInt-Superscri (Superscale + Remacri)  
4xInt-Siacri(Siax + Remacri)  
4xInt-RemDF2K (Remacri + RealSR_DF2K_JPEG)  
4xInt-RemArt (Remacri + VolArt)  
4xInt-RemAnime (Remacri + AnimeSharp)  
4xInt-RemacRestore (Remacri + UltraMix_Restore)  
4xInt-AnimeArt (AnimeSharp + VolArt)  
2xInt-LD-AnimeJaNai (LD-Anime + AnimeJaNai)  

### Dropped 

**SAFMN** - More specifically the 4xHFA2kLUDVAESAFMN model, this network had a tendency to generate artifacts on certain outputs. Dropped the whole network from future models because of artifacts introduction.

**1xUnstroyer Series** - Was a series of srvggnet models that I started training to remove various degradations (compression: MPEG, MPEG-2, H264, HEVC, webp, jpg ; noise, blur etc) but results were not to my liking, dropped the project and worked on others


