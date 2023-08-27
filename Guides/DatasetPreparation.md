Image Super Resolution Training Dataset Preparation

This Section is about preparing an unpaired HR training dataset.

I will demonstrate how I created my FaceUp training dataset here, which could serve as a process or a guideline for other dataset preparations.

1. Think about what you want your dataset to be used for / what use case this dataset is fullfilling. Is it for upscaling images/frames from a specific anime? Is it for upscaling photos of faces? Is it for upscaling outdoor scene photographs (like mountains, fields, forests, cloudy skies)? Or a specific objects like photos of airplanes? Or for general photo upscaling (so some faces, portraits, landscapes, cars, mountains, clothes, buildings, rivers, lakes, etc). This dictates the content of the images. 

In my case, I wanted to build a dataset of face images for face/portrait photo upscale dataset.

2. Gather HR images for your dataset. This simply means you want multiple good quality images (>= 1k images, the more the better for this step) for the above described usecase. You can take images from already existing public datasets, or combine images of those, or extract different scene frames of a specific anime episode and so forth. If you use a public dataset, and there are also 'test images' make sure to exclude those, those are used to evaluate upscaling models and should not be in the training dataset, otherwise it defeats their purpose.

In my case, I used the FFHQ Dataset, with its 70k 1024x1024px images, so there is enough content for sure.

Public Datasets I see fitting / you could use in this step:

[ImageNet](https://image-net.org/index.php) (1,281,167 training images, 50,000 validation images and 100,000 test images)
CelebA (202'599 images of faces)
FFHQ
CelebA-HQ
DIV2K

TODO: expand this list

3. Now we gathered all these images, we will actually weed out bad images. Since there are too many images to manually evaluate, we will make use of hyperIQA, which will give us a visual score of every image. Keep in mind though, I am doing this on a dataset with only faces so I can simply delete images without loosing the required repesentation of faces. If you have a dataset that needs specific things represented, so like you have outdoor scenes, indoor scenes and humans, you can do this step for each of those sections individually to ensure to still have outdoor scenes, indoor scenes and humans present in the final dataset.

Now from out dataset, we only want to keep good images. Meaning we cut off at a specific score. There are two routes we can go basically.

The first route: Image-count cutoff. In this case, you decide how many images you will keep, which i suggest is >=1k and <=5k. We basically sort all the image scores from best to worst, and then cut off when we reach the specific image count, to keep only the best of the best images.

This is the route I went with FaceUp, image-count cutoff being 2k, with hr images of 1024x1024px, which will in the end result in a 20GB folder with around 52k images inside.

hyperiqa of 69999.png: 0.6110466718673706: 100%|█| 69999/69999 [2:10:10<00:00,
Average hyperiqa score of ./images1024x1024/ with 69999 images is: 0.5311755728915932
Done! Results are in ./hyperiqa_score_images1024.txt.

The second route: Score-based cutoff. In this case, you decide on a specific score after which you will only keep images that performed better. If this step is feasable depends on how many images you have available and if you will have a sufficient amount of images left after that. I suggest going with the image-count cutoff. But this could be an alternative, a cutoff score I might suggest is somewhere around 0.6565659766966426, adjust as needed.

TODO: Describe how to run hyperIAQ here


4. Generate multiscales

What we are doing here is to create multiscale images from our current processed dataset. In my FaceUp case, it is because the dataset consists of photos of faces which are all around the same distance to the camera lense, filling out a big portion of the photograph. But someones input image might be a photograph of 2 people, where the faces make up like a fourth of the image, meaning they are further away. Since our model is trained on crops, we create multiscales, so the model also learns like what maybe a whole face would look like in a single crop. (imagine looking at a selection of puzzle pieces. But you would have never seen the whole puzzle.)

5. Crop to sub-images

This increases training speed, specifically the input speed for processing. We crop to 512x512 pixel images.

6. Generate meta info txt file

7. Release


