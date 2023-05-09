## Interpolated Models
Instead of training, we can also create new models by interpolating (combining the model weights of) two existing models that share a pretrained model ancestor. I tried out different combinations and are providing some the models here that, in my opinion, produce acceptable results (many of the combinations I tried did not work out concerning the results). Since these interpolated models seem to have a tendency to introduce a slight color shift, one can use an average color fix on the output.  

These are the interpolated models found in this folder:  

4xInt-Ultracri (UltraSharp + Remacri)  
4xInt-Superscri (Superscale + Remacri)  
4xInt-Siacri(Siax + Remacri)  
4xInt-RemDF2K (Remacri + RealSR_DF2K_JPEG)  
4xInt-RemArt (Remacri + VolArt)  
4xInt-RemAnime (Remacri + AnimeSharp)  
4xInt-RemacRestore (Remacri + UltraMix_Restore)  
4xInt-AnimeArt (AnimeSharp + VolArt)  
2xInt-LD-AnimeJaNai (LD-Anime + AnimeJaNai)