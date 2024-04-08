## SUPIR comfyui workflow with hopefully enforced consistency

![](https://github.com/Phhofm/models/blob/main/SUPIR/screenshot1.png)

---

tldr: Since sometimes diffusion based upscalers have a tendency to change the image a bit too much for my taste (behaving like an 'img2img enlarger/enhancer'), the idea here was to use the consistency of a transformer model (used my 4xRealWebPhoto_v4_dat2) at the beginning as a first step and figure out settings to enforce this consistency on supir in the second step (so rather strict settings that is does not change the image too much). The use case is for images that are degraded to a degree that my model cant handle it anymore, so a diffusion based model would then help in the second step.

---
detailed:  

SUPIR comfyui workflow to enforce consistency based on the transformer upscale.

This was something I was experimenting with over the weekend.

One concern I have over diffusion based upscalers is that they tend to change the image quite a bit, as to give me the feel that the output is basically a completely different image rather than a super resolved version of the input.

This effect had been apparent to me by the time I first heard about magnific ai and when checking out their website, the very first (example) image one sees included some plant with leaves, and they completely change in the output. In real life, that would count as a completely different plant species with suddenly holes and structures in the leaves and also the amount of leaves in the image changes too, which gives me this completely different image vibe.  
I really like how the creators of [DemoFusion](https://ruoyidu.github.io/demofusion/demofusion.html) described this effect in their paper:
"... we carefully avoid using the term "super resolution", as the outputs tend to lean towards the latent data distribution of the base LDM, making this process more akin to image generation based on a real image."

Diffusion based upscaling often felt like an 'img2img enlarger/enhancer' to me, since it had a tendency of changing the image a bit too much.

Since I like the consistency of transformers in contrast, I thought this could maybe be combined.

In this comfyui-supir workflow I use my 4xRealWebPhoto_v4_dat2 sisr model on the input first, and then do a 1x SUPIR run, where I experimented with the settings (around 75 upscales later) to find these so that consistency to the input is rather enforced on SUPIR. 

![](https://github.com/Phhofm/models/blob/main/SUPIR/screenshot2.png)

The use case for this in mind was for degraded input where the degradation is too much for my upscaling model to handle, so a diffusion based upscale could help there in a second step.

I used ColorMatching right after the model in case of there being a colorshifting trained into the upscaling model, and at the end in case SUPIR or the SDXL checkpoint it uses does something funky concerning colors with exact-nearest upsampling as reference. I used the Juggernaut lightning checkpoint ([Juggernaut XL V9+RDPhoto2-Lightning_4x](https://civitai.com/models/133005?modelVersionId=357609)) for faster uspcales, and the [WD14 tagger](https://github.com/pythongosssss/ComfyUI-WD14-Tagger) for automatic positive prompt generation, well a specific model of it (wd-v1-4-convnextv2-tagger-v2) that did not include no_humans tag into photos with humans. I had also tried [moondream](https://github.com/kijai/ComfyUI-moondream) v1 and v2 but running it makes the upscales take way longer.

I deload the models in the chain to cope with vram requirements, since it will first do a 4x transformer upscale, then tagging, then SUPIR processing with the sd checkpoint. But if you have a lot of vram you can of course also try to keep all the models in memory for faster subsequent upscales.

I also used the manual seed 919117296619733 for all these tests in this chain. Sometimes a specific different seed would produce noisy output, and this seed gave good results and also keeps the experiments stable.

I also tested with simply doing a normal 4x upsampling instead of the dat2 model (think lanzcos or nearest) which of course went faster. But I had found, at least in my test, that there was more details to work with, the output image was better and more consistent (of course you can test for yourself).

So feel free to test this out if you want, and play around, with the workflow. (Maybe the more degraded an input is, the more creative freedom should be granted to the diffusion step with the settings. For already good quality input I prefer my sisr model output alone without supir second step.)

You can find some examples in this folder, or in on [SlowPic](https://slow.pics/c/kUN5wRyT), where its first the input image, then 4xRealWebPhoto_v4_dat2 upscale, then 4xRealWebPhoto_v4_dat2_comfyui_supir

PS I included all the image previews in the workflow are for checking and understanding what happens to the image, they can also be used to save the intermediate outputs, like that of the 4x dat2 model alone, and see what happens to the image in each step (like denoise step).

Maybe also the ColorMatch node at the end is too much, this was simply in case of something happening with the colors in the supir step, just to make sure, but in my experiments it did not really make much difference.

I am also not quite sure if the cropping to divisible by 32 is needed anymore, this was mostly to be safe from errors.

Philip Hofmann

PS the workflow is in this folder as [helaman_supir_comfyui.json](https://github.com/Phhofm/models/blob/main/SUPIR/helaman_supir_comfyui.json)

Examples (best viewed in full resolution instead of zoomed out in Github Readme View here):

Degraded inputs that hits limits on what my model can handle, therefore supir improves the output:
![](https://github.com/Phhofm/models/blob/main/SUPIR/Example1.png)
![](https://github.com/Phhofm/models/blob/main/SUPIR/Example2.png)
![](https://github.com/Phhofm/models/blob/main/SUPIR/Example3.png)
![](https://github.com/Phhofm/models/blob/main/SUPIR/Example4.png)
![](https://github.com/Phhofm/models/blob/main/SUPIR/Example7.png)
![](https://github.com/Phhofm/models/blob/main/SUPIR/Example8.png)

Good quality input, i think my personal preference here would be my model alone, without supir, but I wanted to show consistency:
![](https://github.com/Phhofm/models/blob/main/SUPIR/Example5.png)
![](https://github.com/Phhofm/models/blob/main/SUPIR/Example6.png)
