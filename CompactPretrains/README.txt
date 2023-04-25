These models are intended to be used as Pretrain models when training a super resolution model using the SRVGG Compact network architechture used by Real-ESRGAN.
By using these models as your pretrain, it will ensure that your models can be interpolated with other models that used the same pretrain.

There are two versions of each model available. If you are training with the official Real-ESRGAN code (https://github.com/xinntao/Real-ESRGAN/) then the standard version should be used. If you intend to train using Colab-traiNNer (https://github.com/styler00dollar/Colab-traiNNer) then you need to ensure that you use the versions inside the Colab-traiNNer folder.
Both versions of the models are exactly the same, they are just saved in different formats.

Compact models are an order of magnitude faster than ESRGAN models, and require less VRAM. Despite this, they are quite effective on Anime and Cartoon content.
I have also included "UltraCompact" and "SuperUltraCompact" models. These models are faster but less effective. "UltraCompact" models have simply had the num_conv reduced from 16 to 8. "SuperUltraCompact" models have additionally had the num_feat reduced from 64 to 24.
An UltraCompact model should perform around 2x the speed of a regular compact model. SuperUltraCompact models should be another 2x faster than UltraCompact.
In general, I recommend sticking with regular compact models unless speed is your most important concern. The regular compact models are already reasonably quick.

*"SuperUltraCompact" was formerly known as "SubCompact" but I have decided to rename it in order to avoid confusion.

All of these models are free to use for any purpose.