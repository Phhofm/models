Image Super Resolution Training Dataset Preparation

This Section is about preparing an unpaired HR training dataset.

I will demonstrate how I created my FaceUp training dataset here, which could serve as a process or a guideline for other dataset preparations.

1. Think about what you want your dataset to be used for / what use case this dataset is fullfilling. Is it for upscaling images/frames from a specific anime? Is it for upscaling photos of faces? Is it for upscaling outdoor scene photographs (like mountains, fields, forests, cloudy skies)? Or a specific objects like photos of airplanes? Or for general photo upscaling (so some faces, portraits, landscapes, cars, mountains, clothes, buildings, rivers, lakes, etc). This dictates the content of the images. 

In my case, I wanted to build a dataset of face images for face/portrait photo upscale dataset.

2. Gather HR images for your dataset. This simply means you want multiple good quality images (>= 1k images, the more the better for this step) for the above described usecase. You can take images from already existing public datasets, or combine images of those, or extract different scene frames of a specific anime episode and so forth. If you use a public dataset, and there are also 'test images' make sure to exclude those, those are used to evaluate upscaling models and should not be in the training dataset, otherwise it defeats their purpose.

In my case, I used the FFHQ Dataset, with its 70k 1024x1024px images, so there is enough content for sure.

Public Datasets I see fitting / you could use in this step:

[ImageNet](https://image-net.org/index.php) (1,281,167 training images, 50,000 validation images and 100,000 test images)
CelebA (202'599 images of faces, but these are only 178x218 .. so too small to use as HR. So check image sizes and image count before you suggest any dataset here ..)
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

So the average FFHQ hyperiqa score is 0.5311755728915932
Highest Score: 33630.png with 0.760104060173035
Lowest Score: 68564.png with 0.203323021531105

I cutoff the top 2k images and we now achieve an average score of 0.683929971337318, folder size of 2.7GB

The second route: Score-based cutoff. In this case, you decide on a specific score after which you will only keep images that performed better. If this step is feasable depends on how many images you have available and if you will have a sufficient amount of images left after that. I suggest going with the image-count cutoff. But this could be an alternative, a cutoff score I might suggest is somewhere around 0.6565659766966426, adjust as needed.

TODO: Describe how to run hyperIAQ here

PS additionally you can also from the next 100 images (when ordered by score) extract a few validation images, around 4 might suffice, its just to track training status/changes. From those I subjectively selected 4 which I like to look at because during a training process I will look a lot at those images to check progression of the model training and if it goes into a direction I like or if config parameters need to be adjusted.


4. Generate multiscales

What we are doing here is to create multiscale images from our current processed dataset. In my FaceUp case, it is because the dataset consists of photos of faces which are all around the same distance to the camera lense, filling out a big portion of the photograph. But someones input image might be a photograph of 2 people, where the faces make up like a fourth of the image, meaning they are further away. Since our model is trained on crops, we create multiscales, so the model also learns like what maybe a whole face would look like in a single crop. (imagine looking at a selection of puzzle pieces. But you would have never seen the whole puzzle.)

In my case for FaceUp I simply apply 1, 0.75 and 0.5 scale, 0.5 in this case corresponds to the smallest image for this dataset which will be 512x512.

scale_list = [1, 0.75]
shortest_edge = 512

the shortest_edge will save the smallest image additionally, which in this case corresponds to 512x512 (so if i had 1, 0.57, 0.5 in this case would output 4 images, the 512x512 being duplicates, since it additionally saves the shortest_edge image 

this will basically triple my dataset

Folder size now 5.1GB with 6k images

5. Crop to sub-images

This increases training speed, specifically the input speed for processing. We crop to 512x512 pixel images.

Folder size now 19.4GB with 52k image files

Average hyperiqa score of FaceUp/ with 52000 images is: 0.7059247512565209

6. After-Processing-Cleanup

Like seen above ran hyperiqa again on all the 52k sub-images.
Now since they are a lot, we can again repeat the process. Sort according to score descending. Then check how many images received a score >= 0.656, in this case 44952. We dont need that many images, I can cut off way sooner. If I take the top 30k images, I stay above 0.7 score, which is great. In this case though I believe the top 25k images suffice, should be a sufficient number for also training a DAT model.

Like this we arrive at a new average hyperiqa score of 0.743899064958096
Folder size is now 10.3GB with 25k 512x512 images

After sorting after file size, looking at the resulting smallest images I decided to go even lower. From 25k to 15k images. hyperiqa score is now 0.75733778428634, Folder size 6.2GB with 15k 512x512 images. This feels nice.

Lets try out the top 10k images. hyperiqa score 0.766106883633137, Folder size 4.2GB, 10k 512x512 images.

I then renamed all the 10k files and simply gave them each a number starting from 0 to 9999. I also created a hyperiqa_score.txt file again with those images.

I will keep the other folder though in case of training a model gives not the desired results.

7. Validation Images

Insice the validation folder with the 4 images I created a hr folder, moved them there, then created x2 and x4 folders, and created box downscales of these images in these corresponding folders.

6. Generate meta info txt file

I then created a meta_info.txt file

7. Release

Then I simply took the FaceUp (with the 10k images), validation, hyperiqa_score.txt (this is not needed but I wanted to integrate it) and the meta_info.txt file and zipped them up in a 7zip file which I then uploaded to google drive.

Then I started training a model, so I could then in discord release the model (to showcase the dataset) together with this dataset. 
