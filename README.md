# Models

This is a repo for me to publish my self trained single image super resolution (sisr) models.

Update 08.04.2024:  
I am currently in the process of updating this repo by creating a [github release on this repo](https://github.com/Phhofm/models/releases) for each released model, check out the [Released Section](https://github.com/Phhofm/models?tab=readme-ov-file#released-sorted-by-new) in this partly updated README. Then I can also remove most file folders in this repo.

As an example, you can have a look at my [4xRealWebPhoto_v3_atd release](https://github.com/Phhofm/models/releases/tag/4xRealWebPhoto_v3_atd) which you can try out currently with chaiNNer nightly, or then the [dat2 model version](https://github.com/Phhofm/models/releases/tag/4xRealWebPhoto_v4_dat2) of this with normal chaiNNer.

For convenience, you can download a zip file of all my 111 released models (mostly as safetensors files) [here](https://github.com/Phhofm/models/releases/tag/all_models).

After releasing all models here as github releases, I will also release them on [Hugging Face](https://huggingface.co/Phips) so they are automatically downloadable if used in an application, or used in a huggingface space for example, which i had made two just to showcase, youll find them in the link.

I recommend running these models locally with [chaiNNer](https://github.com/chaiNNer-org/chaiNNer).
I made a [youtube video on how to set up and use chaiNNer](https://youtu.be/_r-nhJ_Cf1k). Btw they externalized their upscaling code into the [Spandrel Library](https://github.com/chaiNNer-org/spandrel)

Results for some of these can be compared on my [interactive visual comparison website](https://phhofm.github.io/upscale/selftrained.html), but this site is currently not up-to-date since it became a 70GB repo so automatic deployment became unfeasible and updating a bit more cumbersome, maybe I will be able in the future to reduce it a bit with [BFG Repo-Cleaner](https://rtyley.github.io/bfg-repo-cleaner/). 

I also made some youtube videos you might find interesting, like [this one](https://www.youtube.com/watch?v=QS4ZF7yzH88).

Find more sisr models trained by the community in [openmodeldb](https://openmodeldb.info/).

Here also a link to the [Enhance Everything! Discord Server](https://discord.gg/enhance-everything-547949405949657098) where I had been active.

Also this weekend I played around with a comfyui workflow using SUPIR, I just uploaded the result in the SUPIR folder. Basically diffusion based upscalers in general have the tendency to produce output that is pretty different to an input image as to resemble more an 'img2img enlarger' process than super resolving. My play around was to try to use the consistency of transformers as the upscale, and then SUPIR in the second step but with settings that enforce consistency. Use case would be for very degraded input image where my transformer model hits a limit. Examples and readme and workflow in the folder.

### Released (sorted by new)  

-- Newly Updated Section --  

[All my 111 released models as safetensors files in a zip file](https://github.com/Phhofm/models/releases/tag/all_models)

Model releases sorted by date, linked to their github release:

04.04.2024 - [4xRealWebPhoto_v4_dat2](https://github.com/Phhofm/models/releases/tag/4xRealWebPhoto_v4_dat2) 4x upscaling photos downloaded from the web, handles jpg&webp compression, some realistic noise and some lens blur, [DAT2](https://github.com/zhengchen1999/dat) model.   
25.03.2024 - [Ludvae200](https://github.com/Phhofm/models/releases/tag/Ludvae200) 1x realistic noise degradation model for training dataset creation, [LUD-VAE](https://github.com/zhengdharia/LUD-VAE) model.   
22.03.2024 - [4xRealWebPhoto_v3_atd](https://github.com/Phhofm/models/releases/tag/4xRealWebPhoto_v3_atd) 4x upscaling photos downloaded from the web, handles jpg&webp compression, some realistic noise and some lens blur, [ATD](https://github.com/LabShuHangGU/Adaptive-Token-Dictionary) model - recommended to try out ;)   
22.03.2024 - [4xNomos8k_atd_jpg](https://github.com/Phhofm/models/releases/tag/4xNomos8k_atd_jpg) 4x photo upscaler, handles jpg compression, preserves noise, [ATD](https://github.com/LabShuHangGU/Adaptive-Token-Dictionary) model.   
10.03.2024 - [4xRealWebPhoto_v2_rgt_s](https://github.com/Phhofm/models/releases/tag/4xRealWebPhoto_v2_rgt_s) 4x upscaling photos downloaded from the web, handles jpg&webp compression, some realistic noise and some lens blur, [RGT-S](https://github.com/zhengchen1999/RGT) model.   
20.02.2024 - [4xNomosUni_rgt_multijpg](https://github.com/Phhofm/models/releases/tag/4xNomosUni_rgt_multijpg) 4x universal DoF preserving upscaler, handles jpg compression, [RGT](https://github.com/zhengchen1999/RGT) model.   
16.02.2024 - [4xNomosUni_rgt_s_multijpg](https://github.com/Phhofm/models/releases/tag/4xNomosUni_rgt_s_multijpg) 4x universal DoF preserving upscaler, handles jpg compression, [RGT-S](https://github.com/zhengchen1999/RGT) model.   
12.02.2024 - [2xEvangelion_dat2](https://github.com/Phhofm/models/releases/tag/2xEvangelion_dat2) 2x upscaler for the Community Evangelion Ep16 upscale project, [DAT2](https://github.com/zhengchen1999/dat) model.   
08.02.2024 [2xEvangelion_omnisr](https://github.com/Phhofm/models/releases/tag/2xEvangelion_omnisr) 2x upscaler for the Community Evangelion Ep16 upscale project, [OmniSR](https://github.com/Francis0625/Omni-SR) model.   
04.02.2024 - [2xEvangelion_compact](https://github.com/Phhofm/models/releases/tag/2xEvangelion_compact) 2x upscaler for the Community Evangelion Ep16 upscale project, [SRVGGNetCompact](https://github.com/XPixelGroup/BasicSR/blob/master/basicsr/archs/srvgg_arch.py) model.   
28.01.2024 - [4xNomosUniDAT2_multijpg_ldl & 4xNomosUniDAT2_multijpg_ldl_sharp](https://github.com/Phhofm/models/releases/tag/4xNomosUniDAT2_multijpg_ldl) 4x universal DoF preserving upscaler, handles jpg compression, [DAT2](https://github.com/zhengchen1999/dat) models.   
27.01.2024 - [1xExposureCorrection_compact & 1xOverExposureCorrection_compact & 1xUnderExposureCorrection_compact](https://github.com/Phhofm/models/releases/tag/1xExposureCorrection_compact) 1x Exposure correction, [SRVGGNetCompact](https://github.com/XPixelGroup/BasicSR/blob/master/basicsr/archs/srvgg_arch.py) models.   
13.01.2024 - [2xNomosUni_span_multijpg_ldl](https://github.com/Phhofm/models/releases/tag/2xNomosUni_span_multijpg_ldl) 2x fast universal DoF preserving upscaler, handles jpg compression, [SPAN](https://github.com/hongyuanyu/SPAN) model.   

-- still making github releases for the following released models on this repo --

11.01.2024 - 2xNomosUni_compact_multijpg_ldl   
11.01.2024 - 2xNomosUni_compact_otf_medium   
04.01.2024 - 4xHFA2k_VCISR_GRLGAN_ep200   
04.01.2024 - 2xHFA2kShallowESRGAN   
26.12.2024 - 2xHFA2kSPAN   
26.12.2024 - 2xHFA2k_LUDVAE_SPAN   
26.12.2024 - 2xHFA2k_LUDVAE_compact   
26.12.2024 - 2xHFA2k_compact_multijpg   
26.12.2024 - 2xHFA2Real-CUGAN   
26.12.2024 - 2xHFA2OmniSR   
26.12.2024 - 2xHFA2SwinIR-S   
20.12.2023 - 2xNomosUni_esrgan_multijpg   
13.12.2023 - 2xNomosUni_span_multijpg   
13.12.2023 - 2xNomosUni_compact_multijpg   
13.12.2023 - 4xTextureDAT2_otf   
09.12.2023 - 4xNomosUni_span_multijpg   
09.12.2023 - 4xNomos8k_span_otf_weak & 4xNomos8k_span_otf_medium & 4xNomos8k_span_otf_strong   
01.11.2023 - 4xNomosUniDAT_otf   
01.11.2023 - 4xLexicaDAT2_otf   
01.11.2023 - 4xNomos8kHAT-L_otf   
05.10.2023 - 4xNomos8kHAT-L_bokeh_jpg   
23.09.2023 - 4xNomosUniDAT_otf   
14.09.2023 - 4xNomosUniDAT_bokeh_jpg   
10.09.2023 - 4xNomosUniDAT2_box   
10.09.2023 - 4xLSDIRDAT   
10.09.2023 - 4xSSDIRDAT   
02.09.2023 - 4xFaceUpDAT & 4xFaceUpLDAT & 4xFaceUpSharpDAT & 4xFaceUpSharpLDAT   
25.08.2023 - 4xFFHQDAT & 4xFFHQLDAT   
13.08.2023 - 4xNomos8kDAT   
02.08.2023 - 1xDeJPG_SRFormer_light, 1xDeJPG_OmniSR   
11.07.2023 - 2xHFA2kAVCSRFormer_light   
30.06.2023 - 4xNomos8kSCHAT-L & 4xNomos8kSCHAT-S  
26.06.2023 - 4xNomos8kSCSRFormer  
18.06.2023 - 2xHFA2kAVCCompact & 2xHFA2kAVCEDSR_M & 2xHFA2kAVCOmniSR  
14.06.2023 - 4xHFA2kLUDVAEGRL_small  
10.06.2023 - 4xHFA2kLUDVAESwinIR_light & 4xHFA2kLUDVAESRFormer_light  
01.06.2023 - 2xLexicaRRDBNet & 2xLexicaRRDBNet_Sharp  
10.05.2023 - 4xNomos8kSC  
07.05.2023 - 4xHFA2k  
05.05.2023 - 2xParimgCompact  
18.04.2023 - 2xHFA2kCompact  
11.04.2023 - 4xLSDIRCompactv3 (Series 3)  
25.03.2023 - 4xLSDIRCompactv2 (Series 2)  
17.03.2023 - 4xLSDIRCompactC & 4xLSDIRCompactR  
11.03.2023 - 4xLSDIRCompact  

---
   
Previous README 

Released (sorted by new)  

07.07.23  
**2xHFA2kAVCSRFormer_light**  
A SRFormer light model for upscaling anime videos downloaded from the web, handling AVC (h264) compression.  

06.07.23  
**2xLexicaSwinIR, 4xLexicaHAT, 4xLSDIR, 4xLSDIRplus, 4xLSDIRplusC, 4xLSDIRplusN, 4xLSDIRplusR**  
I upladed my model on [openmodeldb](https://openmodeldb.info/?q=Helaman&sort=date-desc) and therefore 'release' these models, the Lexica models handle no degradations and are for upscaling AI generated outputs further. The LSDIRplus are the official ESRGAN plus model further finetunes with LSDIR, the 4xLSDIRplus is an interpolation of C and R and handles compression and a bit of noise/blur. The 4xLSDIRplusN handles no degradation, the 4xLSDIRplusC handles compression, and 4xLSDIRplusR used the official Real-ESRGAN configs but its only for extremer cases since it destroys details, the 4xLSDIRplusC models should be sufficient for most cases.  

30.06.23  
**4xNomos8kSCHAT-L & 4xNomos8kSCHAT-S**  
My twelfth release, this time a [HAT](https://github.com/XPixelGroup/HAT) large and small model (they uploaded HAT-S codes and models two months ago) - a 4x realistic photo upscaling model handling JPG compression, trained on the [HAT](https://github.com/XPixelGroup/HAT) network (small and large model) with musl's Nomos8k_sfw dataset together with OTF (on the fly degradation) jpg compression and blur.   

26.06.23  
**4xNomos8kSCSRFormer**  
My eleventh release, a 4x realistic photo upscaling model handling JPG compression, trained on the [SRFormer](https://github.com/HVision-NKU/SRFormer) network (base model) with musl's Nomos8k_sfw dataset together with OTF (on the fly degradation) jpg compression and blur.   

18.06.23  
**2xHFA2kAVCOmniSR & 2xHFA2kAVCOmniSR_Sharp**  
My tenth release, a 2x anime upscaling model that handles AVC (h264) compression trained on the [OmniSR](https://github.com/Francis0625/Omni-SR) network (second released community model to use this network, which paper released less than two months ago, on the 24.04.23).  

18.06.23  
**2xHFA2kAVCEDSR_M**  
My ninth release, a fast 2x anime upscaling model that handles AVC (h264) compression trained on the [EDSR](https://github.com/LimBee/NTIRE2017) network (M model).  

18.06.23  
**2xHFA2kAVCCompact**  
Also in my ninth release, a compact 2x anime upscaling model that handles AVC (h264) compression trained on the [SRVGGNet, also called Real-ESRGAN Compact](https://github.com/xinntao/Real-ESRGAN) network.  

14.06.23  
**4xHFA2kLUDVAEGRL_small**  
My eight release - 4x anime upscaling model handling real degradation, trained on the [GRL](https://github.com/ofsoundof/GRL-Image-Restoration) network (small model) with musl's HFA2kLUDVAE dataset.  

10.06.23  
**4xHFA2kLUDAVESwinIR_light**  
My seventh release - 4x anime upscaling model handling real degradation, trained on the [SwinIR](https://github.com/JingyunLiang/SwinIR) network (small model) with musl's HFA2kLUDVAE dataset.   

10.06.23  
**4xHFA2kLUDVAESRFormer_light**  
Also in my seventh release - 4x anime upscaling model handling real degradation, trained on the [SRFormer](https://github.com/HVision-NKU/SRFormer) network (light model) with musl's HFA2kLUDVAE dataset.  

01.06.23  
**2xLexicaRRDBNet & 2xLexicaRRDBNet_Sharp**  
My sixth release - a 2x upscaler for AI generated images (no degradations), trained on the [ESRGAN (RRDBNet)](https://github.com/xinntao/ESRGAN) network (base model) with around 34k images from lexica.art.  

10.05.23  
**4xNomos8kSC**  
My fifth release - a 4x realistic photo upscaling model handling JPG compression, trained on the [ESRGAN (RRDBNet)](https://github.com/xinntao/ESRGAN) network (base model) with musl's Nomos8k_sfw dataset together with OTF (on the fly degradation) jpg compression and blur.   

07.05.23  
**4xHFA2k**  
My fourth release - a 4x anime image upscaling model, trained on the [ESRGAN (RRDBNet)](https://github.com/xinntao/ESRGAN) network (base model) with musl's HFA2k dataset together with OTF (on the fly degradation) jpg compression and blur.    

05.05.23  
**2xParimgCompact**  
My third release - a 2x compact photo upscaling model trained on the [SRVGGNet, also called Real-ESRGAN Compact](https://github.com/xinntao/Real-ESRGAN) network with Microsofts ImagePairs (11,421 images, 111 GB ). Was one of the very first models I had started training and finished it now.  

18.04.23  
**2xHFA2kCompact**  
My second release - a 2x anime compact upscaling model trained on the [SRVGGNet, also called Real-ESRGAN Compact](https://github.com/xinntao/Real-ESRGAN) network with musl's HFA2k dataset together with OTF (on the fly degradation) jpg compression and blur.  

11.03.23  
**4xLSDIRCompact**  
My very first release - a 4x compact model for photo upscaling trained on the [SRVGGNet, also called Real-ESRGAN Compact](https://github.com/xinntao/Real-ESRGAN) network. Up to 3 versions, version 3 contains N C R models, version 2 is a general model interpolated of C and R. Trained on the huge LSDIR dataset (84991 images *2 for paired training C around 160 GB). Suggested is the 4xLSDIRCompactC3 model  


### Models Summary

*Photos*  
4xNomos8kSCHAT-L - Photo upscaler, handles a bit of jpg compression and blur, HAT-L model (good results but very slow since huge model)  
4xNomos8kSCHAT-S - Photo upscaler, handles a bit of jpg compression and blur, HAT-S model  
4xNomos8kSCSRFormer - Photo upscaler, handles a bit of jpg compression and blur, SRFormer base model (also good results but also slow since big model)  
4xNomos8kSC - Photo upscaler, handles a bit of jpg compression and blur, RRDBNet base model  
4xLSDIR - Photo upscaler, no degradation handling, RRDBNet base model  
4xLSDIRplus - Photo upscaler, handles a bit of jpg compression and blur, RRDBNet base model  
4xLSDIRplusC - Photo upscaler, handles a bit of jpg compression, RRDBNet base model  
4xLSDIRplusN - Photo upscaler, almost no degradation handling, RRDBNet base model  
4xLSDIRplusR - Photo upscaler, handles degradation but too strong so loses details, RRDBNet base model    
4xLSDIRCompact3 - Photo upscaler, handles a bit of jpg compression and blur, SRVGGNet model    
4xLSDIRCompactC3 - Photo upscaler, handles a bit of jpg compression, SRVGGNet model    
4xLSDIRCompactN3 - Photo upscaler, handles no degradations, SRVGGNet model   
4xLSDIRCompactR3 - Photo upscaler, handles degradation but too strong so loses details, SRVGGNet model  
4xLSDIRCompact2 - Photo upscaler, handles a bit of jpg compression and blur, SRVGGNet model    
4xLSDIRCompactC2 - Photo upscaler, handles a bit of jpg compression, SRVGGNet model    
4xLSDIRCompactR2 - Photo upscaler, handles degradation but too strong so loses details, SRVGGNet model  
4xLSDIRCompact1 - Photo upscaler, handles a bit of jpg compression and blur, SRVGGNet model    
4xLSDIRCompactC1 - Photo upscaler, handles a bit of jpg compression, SRVGGNet model    
4xLSDIRCompactR1 - Photo upscaler, handles degradation but too strong so loses details, SRVGGNet model   
2xParimgCompact - Photo upscaler that does some color shifting since based on ImagePairs, SRVGGNet model   

*Anime*  
2xHFA2kAVCOmniSR - Anime frame upscaler that handles AVC (h264) video compression, OmniSR model   
2xHFA2kAVCOmniSR_Sharp - Anime frame upscaler that handles AVC (h264) video compression with sharper outputs, OmniSR model  
4xHFA2kAVCSRFormer_light - Anime frame upscaler that handles AVC (h264) video compression, SRFormer lightweight model  
2xHFA2kAVCEDSR_M - Anime frame upscaler that handles AVC (h264) video compression, EDSR-M model  
2xHFA2kAVCCompact - Anime frame upscaler that handles AVC (h264) video compression, SRVGGNet model  
4xHFA2kLUDVAESwinIR_light - Anime image upscaler that handles various realistic degradations, SwinIR light model  
4xHFA2kLUDVAEGRL_small - Anime image upscaler that handles various realistic degradations, GRL small model  
4xHFA2kLUDVAESRFormer_light - Anime image upscaler that handles various realistic degradations, SRFormer light model   
4xHFA2k - Anime image upscaler that handles some jpg compression and blur, RRDBNet base model   
2xHFA2kCompact - Anime image upscaler that handles some jpg compression and blur, SRVGGNet model  
4xHFA2kLUDVAESAFMN - dropped model since there were artifacts on the outputs when training with SAFMN arch 

*AI generated*  
4xLexicaHAT - An AI generated image upscaler, does not handle any degradations, HAT base model  
2xLexicaSwinIR - An AI generated image upscaler, does not handle any degradations, SwinIR base model  
2xLexicaRRDBNet - An AI generated image upscaler, does not handle any degradations, RRDBNet base model  
2xLexicaRRDBNet_Sharp - An AI generated image upscaler with sharper outputs, does not handle any degradations, RRDBNet base model 


### Interpolations

These models can be found in the "Interpolated" folder, it consists of

**4xInt-Ultracri**  
[UltraSharp](https://openmodeldb.info/models/4x-UltraSharp) + [Remacri](https://openmodeldb.info/models/4x-Remacri)  
  
**4xInt-Superscri**  
[NMKD Superscale](https://openmodeldb.info/models/4x-NMKD-Superscale) + [Remacri](https://openmodeldb.info/models/4x-Remacri)  

**4xInt-Siacri**  
[NMKD Siax ("CX")](https://openmodeldb.info/models/4x-NMKD-Siax-CX) + [Remacri](https://openmodeldb.info/models/4x-Remacri)  

**4xInt-RemDF2K**  
[Remacri](https://openmodeldb.info/models/4x-Remacri) + [RealSR_DF2K_JPEG](https://openmodeldb.info/models/4x-realsr-df2k-jpeg)  

**4xInt-RemArt**  
[Remacri](https://openmodeldb.info/models/4x-Remacri) + [VolArt](https://openmodeldb.info/models/4x-VolArt)  

**4xInt-RemAnime**  
[Remacri](https://openmodeldb.info/models/4x-Remacri) + [AnimeSharp](https://openmodeldb.info/models/4x-AnimeSharp)  

**4xInt-RemacRestore**  
[Remacri](https://openmodeldb.info/models/4x-Remacri) + UltraMix_Restore  

**4xInt-AnimeArt**  
[AnimeSharp](https://openmodeldb.info/models/4x-AnimeSharp) + [VolArt](https://openmodeldb.info/models/4x-VolArt)  

**2xInt-LD-AnimeJaNai**  
[LD-Anime](https://openmodeldb.info/models/2x-LD-Anime-Compact) + [AnimeJaNai](https://openmodeldb.info/models/2x-AnimeJaNai-Standard-v1-Compact)  


### Series

**Lexica**   
Training different models for AI generated image upscaling without degradations. (RRDBNet, [HAT](https://github.com/XPixelGroup/HAT), SwinIR)   

**HFA2kLUDVAE**   
Training lightweight models of different networks to test for interence speed and metrics for anime upscaling with realistic degradations. See results in the corresponding results folder.   

**LSDIR**   
A series trained on the big LSDIR dataset. Mostly interpolated output result. Then N for no degradation, C for compression (should be sufficient for most cases) and R for noise, blur and compression (only use in extremer cases).  

**LSDIRplus**   
An RRDBNet experiment to see what influence a huge dataset has on the official x4plus model for photo upscaling.  

**HFA2kAVC**  
Model series handling AVC (h264) compression usually found on videos from the web. So for upscaling videos downloaded from the web basically.  

### Dropped 

**SAFMN**  
More specifically the 4xHFA2kLUDVAESAFMN model, this network had a tendency to generate artifacts on certain outputs. Dropped the whole network from future models because of artifacts introduction.  

**1xUnstroyer Series - Deleted**  
Was a series of srvggnet models that I started training to remove various degradations simultaneously (compression: MPEG, MPEG-2, H264, HEVC, webp, jpg ; noise, blur etc) but results were not to my liking since it was too many different degradations for such a small network, dropped the project and worked on others  


### Pretrains  

**CompactPretrains**  
These pretrains have been provided by Zarxrax and they are great to use to kick off training a compact model.  

<br><br>

## Visual Results
<br>

### Folder Files

Some of these model folders contain examples, meaning inputs and outputs to visually see the effects of such a model. Series like LUDVAE or AVC have their own results folder where and encompass the outputs of multiple models trained on the same dataset and similiar settings, most of the time models of different networks, so these outputs can be compared with each other, coming from the same input. visual outputs (and inputs).  
<br>
LUDVAE Model Series comparison images (Input, [SwinIR](https://github.com/JingyunLiang/SwinIR) small, [SRFormer](https://github.com/HVision-NKU/SRFormer) lightweight, [GRL](https://github.com/ofsoundof/GRL-Image-Restoration) small). Specific model in bottom caption:

![0550](https://raw.githubusercontent.com/Phhofm/models/main/4xHFA2kLUDVAE_results/0550.png)
![0045](https://raw.githubusercontent.com/Phhofm/models/main/4xHFA2kLUDVAE_results/0045.png)

AVC Model Series comparison images (Input, [EDSR](https://github.com/LimBee/NTIRE2017), [SRVGGNet](https://github.com/xinntao/Real-ESRGAN), [OmniSR](https://github.com/Francis0625/Omni-SR)). Specific model in bottom caption:

![AVC Example 0](2xHFA2kAVC_results/Output_0.png)
![AVC Example 1](2xHFA2kAVC_results/Output_1.png)

Nomos8kSC Series comparison images (Input, [ESRGAN (RRDBNet)](https://github.com/xinntao/ESRGAN), [SRFormer](https://github.com/HVision-NKU/SRFormer) base, [HAT](https://github.com/XPixelGroup/HAT) large. 

![Nomos Example 0](4xNomos8kSC_results/dearalice.png)
![Nomos Example 1](4xNomos8kSC_results/bibli.png)
![Nomos Example 2](4xNomos8kSC_results/seeufer.png)

<br><br>
### Website with Image Slider

I also made the [Selftrained page](https://phhofm.github.io/upscale/selftrained.html) where you can find with a slider the different outputs of my models but also with the example below together with over 600 other models so my self trained model outputs can be compared with a lot of other official paper models or community trained models.  
<br>
Website Selftrained Page screenshot, click corresponding link above to get to the actual interactive version:

![Website Selftrained Page screenshot](screenshot_website_selftrained.png)
<br><br>

### Quick Test Anime Opening from Youtube

And then I started doing quick tests like downloading an anime opening in 360p from youtube with one of those yt2mp4 converters online (so the input has the compression artifacts for this usecase) and using my models on extracted frames. 

For this anime opening I often liked my 2xHFA2kCompact model which is very fast for inference and gave good results which can be seen on these example frames

Frame 933: https://imgsli.com/MTg2OTc5/0/4  
Frame 475: https://imgsli.com/MTg2OTc3/0/4  
Frame 1375: https://imgsli.com/MTg2OTk0/0/4   

But then 2xHFA2kCompact deblurs scenes that have intentional blur/bokeh effect (see railing in the background) where I personally liked the AVC series better, so 2xHFA2kAVCOmniSR (or 2xHFA2kAVCCompact) since it kept that effect / stayed more truthful to the input in that sense

Frame 1069 https://imgsli.com/MTg2OTg3/0/2  
Frame 2241 https://imgsli.com/MTg2OTgy/0/1  

<br>
Frame 933 screenshot as a single example of the above imgsli comparison links, click corresponding links above to get to the actual interactive versions:  

![Frame 933 screenshot](screenshot_imgsli_frame933.png)
