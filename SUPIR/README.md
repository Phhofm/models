SUPIR comfyui workflow to enforce consistency based on the transformer upscale first stage -

This was something I was experimenting with over the weekend.

The one big problem I have with diffusion based upscalers is that due to their nature with adding and removing noise to create details, they tend to change the image a bit too much so that rather than an super resolved version of the input, it feels like a different image.

That had been very apparent to me by the time magnific ai came around and had a website which featured example images, because when I first visited that website, the very first example image, includes some plant with leafes, and they completely change. It would basically be a completely different plant species with their holes and structure, also completely different amount of leafes.

I really likes how the creators of DemoDusion described it:
"... We carefully avoid using the term "super resolution", as the outputs tend to lean towards the latent data distribution of the base LDM, making this process more akin to image generation based on a real image."

Diffusion based upscaling always felt more like an 'img2img enlarger' or 'img2img enhancer' to me, since it had a tendency of changing the image too much, in that it is not the same image anymore.

But that is my personal opinion. Others might like this effect, and call it 'extreme detail adding' or someething. I guess it also depends on what type of content it is used on, as I can image on AI generated images that consistency might be of less importance to the user, but simply wanting a 'more detailed version' of the input.

Since I like the consistency of transformers in contrast, I thought this could maybe be combined.

In this comfyui-supir workflow I basically use my 4xRealWebPhoto_v4_dat2 sisr model on the input first, and then a 1x SUPIR run, experimented with the settings (around 75 upscales later) to find these so that consistency to the input is basically enforced on SUPIR (limited in its creativity). 

The use case, or question in mind, was that diffusion based upscalers could help in cases where the image is in such a degraded state that my transformer sisr models would not be able to handle it because of consistency. So the more degraded an input is the more leeway/creativity we could give the diffusion based step after to be able to restore the image (hallucinating a degradation free version, so to say).

I used ColorMatching right after the model in case of there being a colorshifting trained into the upscaling model, and at the end in case SUPIR or the SDXL checkpoint it uses does something funky concerning colors. I used the Juggernaut lightning checkpoint for faster uspcales, and the WD14 tagger for automatic positic prompt generation, well a specific model of it (wd-v1-4-convnextv2-tagger-v2) that did not include no_humans tag into photos with humans. I had also tried moondream v1 and v2 but running it makes the upscales take way longer.

I deload the models in the chain to cope with vram requirements, since it will first do a transformer upscale, then tagging, then SUPIR processing with the sd checkpoint. But if you have a lot of vram you can of course also try to keep all the models in memory for faster subsequent upscales.

I also used the manual seed 919117296619733 for all these tests in this chain. Sometimes a specific different seed would produce noisy output.

I also tested with only a normal 4x upsampling step first (thins lanzcos, or nearest), and even though there is a supir denoise step right after, the transformer upscale would give more details and better consistency at least in my tests.

So feel free to test this out if you want, and play around.

You can find some examples in this folder, or in on [SlowPic](https://slow.pics/c/kUN5wRyT), where its first the input image, then 4xRealWebPhoto_v4_dat2 upscale, then 4xRealWebPhoto_v4_dat2_comfyui_supir

- Philip Hofmann