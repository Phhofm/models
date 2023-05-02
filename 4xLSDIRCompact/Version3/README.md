**4xLSDIRCompact3**

[Examples](https://imgsli.com/MTY4NTc5) with its [files](https://drive.google.com/drive/folders/1CIHGv0t2GdyEUwL0m-29NnLC1l9MKFHb). This corresponds to 'CompactIntCR' in the example.

In here you find different versions again for different purposes.

The general model files are the one present here. It is an interpolation (meaning combined/average weights) of the C3 model, which is meant to handle compression, and the R3 model, which was meant to handle even more degradations like noise and blur. Interpolated with 75% C3 and 25% R3.

In the subfolders you find the specifically trained models which might be better for your use case:

N: Stands for 'No Degradations' as in your input quality image should already be of good quality. If this is the case than this model should keep most details / give best outputs of your input when upscaling.

C: Stands for 'Compression', this model can handle jpg compression additionally. For example images from the internet often have been compressed to increase page loading speeds. This model had been trained by manually compressing the input images with jpg quality 30-0) and uncompressed ones to keep good quality too.

R: Stands for 'Real-ESRGAN' meaning it used their otf (on the fly) degradations to degrade the images while training by adding noise, blur, compression. This can be used for images that suffer from more degradations than just jpg compression.

The interpolated version on here should therefore handle jpg compression plus also a bit of more degradations. This interpolation is provided because the R models here had rather high degradation values for training.