crop_images
=====
本代码适用于对标注的图片文字框进行裁剪，并且将裁剪的图片进行了仿射，透视变换，得到的文字图片都是矫正的文字图。
--------
Run this code with these three parameters
-------
```
python crop_img.py input_path txt_path save_path
```
    input_path表示需要裁剪的图片的文件夹
    txt_path表示保存裁剪下来子图片的坐标的文件夹
    save_path表示保存裁剪下来子图片的文件夹
# 输入图片
![image](https://github.com/zcswdt/crop_images/raw/master/input_path/tr_img_03001.jpg)
![image](https://github.com/zcswdt/crop_images/blob/master/save_path/tr_img_03001_p1.jpg)
<img src="./save_path/*.jpg" width="1000" height="600" title="crop_image">
