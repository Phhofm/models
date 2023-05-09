## Interpolated Models
Instead of training, we can also create new models by interpolating (combining the model weights of) two existing models that share a pretrained model ancestor.   

I found these interpolated models to have a tendency to introduce a slight color shift, so I often used an average color fix on the output.  

I have tried out around almost 100 different interpolations, and out of these, I provide here 9 interpolated models where I personally found the output to be good/acceptable:  

4xInt-Ultracri (UltraSharp + Remacri)  
4xInt-Superscri (Superscale + Remacri)  
4xInt-Siacri(Siax + Remacri)  
4xInt-RemDF2K (Remacri + RealSR_DF2K_JPEG)  
4xInt-RemArt (Remacri + VolArt)  
4xInt-RemAnime (Remacri + AnimeSharp)  
4xInt-RemacRestore (Remacri + UltraMix_Restore)  
4xInt-AnimeArt (AnimeSharp + VolArt)  
2xInt-LD-AnimeJaNai (LD-Anime + AnimeJaNai)  

These are the combinations I had tried out:
(You can find the corresponding image outputs of a specific image input [here](https://github.com/Phhofm/upscale/tree/main/sources/output/lossless/interpolated/fate))  

2x_LD-Anime_Compact_330k_net_g + 2x_AnimeJaNai_Standard_V1.6_Compact_net_g_64000  
4x_BSRGAN + 4x_Deviance_60000G  
4x_BSRGAN + 4x_DF2K_JPEG  
4x_BSRGAN + 4x_foolhardy_Remacri  
4x_BSRGAN + 4x_NMKD-Siax_200k  
4x_BSRGAN + 4x_NMKDSuperscale  
4x_BSRGAN + 4x_RealisticRescaler_100000_G  
4x_BSRGAN + 4x_Struzan_300000  
4x_BSRGAN + 4x-AnimeSharp  
4x_BSRGAN + 4x-UltraMix_Balanced  
4x_BSRGAN + 4x-UltraMix_Restore  
4x_BSRGAN + 4x-UltraSharp  
4x_BSRGAN + 4x-VolArt  
4x_BSRGAN + 4xRealSR_DF2K_JPEG  
4x_Deviance_60000G + 4x_DF2K_JPEG  
4x_Deviance_60000G + 4x_foolhardy_Remacri  
4x_Deviance_60000G + 4x_NMKD-Siax_200k  
4x_Deviance_60000G + 4x_NMKDSuperscale  
4x_Deviance_60000G + 4x_RealisticRescaler_100000_G  
4x_Deviance_60000G + 4x_Struzan_300000  
4x_Deviance_60000G + 4x-AnimeSharp  
4x_Deviance_60000G + 4x-UltraMix_Balanced  
4x_Deviance_60000G + 4x-UltraMix_Restore  
4x_Deviance_60000G + 4x-UltraSharp  
4x_Deviance_60000G + 4x-VolArt  
4x_Deviance_60000G + 4xRealSR_DF2K_JPEG  
4x_DF2K_JPEG + 4x_foolhardy_Remacri  
4x_DF2K_JPEG + 4x_NMKD-Siax_200k  
4x_DF2K_JPEG + 4x_NMKDSuperscale  
4x_DF2K_JPEG + 4x_RealisticRescaler_100000_G  
4x_DF2K_JPEG + 4x_Struzan_300000  
4x_DF2K_JPEG + 4x-AnimeSharp  
4x_DF2K_JPEG + 4x-UltraMix_Balanced  
4x_DF2K_JPEG + 4x-UltraMix_Restore  
4x_DF2K_JPEG + 4x-UltraSharp  
4x_DF2K_JPEG + 4x-VolArt  
4x_DF2K_JPEG + 4xRealSR_DF2K_JPEG  
4x_foolhardy_Remacri + 4x_NMKD-Siax_200k  
4x_foolhardy_Remacri + 4x_NMKDSuperscale  
4x_foolhardy_Remacri + 4x_RealisticRescaler_100000_G  
4x_foolhardy_Remacri + 4x_Struzan_300000  
4x_foolhardy_Remacri + 4x-AnimeSharp  
4x_foolhardy_Remacri + 4x-UltraMix_Balanced  
4x_foolhardy_Remacri + 4x-UltraMix_Restore  
4x_foolhardy_Remacri + 4x-UltraSharp  
4x_foolhardy_Remacri + 4x-VolArt  
4x_foolhardy_Remacri + 4xRealSR_DF2K_JPEG  
4x_NMKD-Siax_200k + 4x_NMKDSuperscale  
4x_NMKD-Siax_200k + 4x_RealisticRescaler_100000_G  
4x_NMKD-Siax_200k + 4x_Struzan_300000  
4x_NMKD-Siax_200k + 4x-AnimeSharp  
4x_NMKD-Siax_200k + 4x-UltraMix_Balanced  
4x_NMKD-Siax_200k + 4x-UltraMix_Restore  
4x_NMKD-Siax_200k + 4x-UltraSharp  
4x_NMKD-Siax_200k + 4x-VolArt  
4x_NMKD-Siax_200k + 4xRealSR_DF2K_JPEG  
4x_NMKDSuperscale + 4x_RealisticRescaler_100000_G  
4x_NMKDSuperscale + 4x_Struzan_300000  
4x_NMKDSuperscale + 4x-AnimeSharp  
4x_NMKDSuperscale + 4x-UltraMix_Balanced  
4x_NMKDSuperscale + 4x-UltraMix_Restore  
4x_NMKDSuperscale + 4x-UltraSharp  
4x_NMKDSuperscale + 4x-VolArt  
4x_NMKDSuperscale + 4xRealSR_DF2K_JPEG  
4x_RealisticRescaler_100000_G + 4x_Struzan_300000  
4x_RealisticRescaler_100000_G + 4x-AnimeSharp  
4x_RealisticRescaler_100000_G + 4x-UltraMix_Balanced  
4x_RealisticRescaler_100000_G + 4x-UltraMix_Restore  
4x_RealisticRescaler_100000_G + 4x-UltraSharp  
4x_RealisticRescaler_100000_G + 4x-VolArt  
4x_RealisticRescaler_100000_G + 4xRealSR_DF2K_JPEG  
4x_Struzan_300000 + 4x-AnimeSharp  
4x_Struzan_300000 + 4x-UltraMix_Balanced  
4x_Struzan_300000 + 4x-UltraMix_Restore  
4x_Struzan_300000 + 4x-UltraSharp  
4x_Struzan_300000 + 4x-VolArt  
4x_Struzan_300000 + 4xRealSR_DF2K_JPEG  
4x-AnimeSharp + 4x-UltraMix_Balanced  
4x-AnimeSharp + 4x-UltraMix_Restore  
4x-AnimeSharp + 4x-UltraSharp  
4x-AnimeSharp + 4x-VolArt  
4x-AnimeSharp + 4xRealSR_DF2K_JPEG  
4x-UltraMix_Balanced + 4x-UltraMix_Restore  
4x-UltraMix_Balanced + 4x-UltraSharp  
4x-UltraMix_Balanced + 4x-VolArt  
4x-UltraMix_Restore + 4x-UltraSharp  
4x-UltraMix_Restore + 4x-VolArt  
4x-UltraSharp + 4x-VolArt  
4xRealSR_DF2K_JPEG + 4x-UltraMix_Balanced  
4xRealSR_DF2K_JPEG + 4x-UltraMix_Restore  
4xRealSR_DF2K_JPEG + 4x-UltraSharp  
4xRealSR_DF2K_JPEG + 4x-VolArt   