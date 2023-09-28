## Face detect and identify faces using one-shot learning for recognition of your face.

The model has been built using siamese neural networks for one-shot learning. The dataset has been put into three sub-directories within dirctory `dataset`.
 ## Model Training
The model has been trained with images with augmentation.

`true_images` are for the validation of the input images, that means: are these images similar to the images inside the `true_images` folder. 
 `False_images` are validating that the input images are dissimilar to the images inside the False images folder. And the label corresponds to the `input_image` and `false_images` will be 0 because of their dissimilarity.

 The model has been trained for few epochs and is save with name `SmartSense.h5`


 ## Model Testing/usage

 Model can be tested using two ways:

1. App: Streamlit app has been developed. The application needs to be run using command below in root directory.

    ```
    streamlit run app.py
    ```

    - Once the application is running, the web UI has to be launched and capture the image using webcam. (The app asks you permission to capture your image)
    - Once the image is captured, it is verified again the image in verfication_folder to detect and recognize the face. (Verification indicates that the person is in our database). So, before running application, make sure one photo of yours is in `application_data/verification_images`
2. test.py:
put a copy of your image in the `application_data/verification_images` folder. Click a new image of yourself and put in `application_data/input_image`

use the below command to run the script:
```
python3 test.py 
```

