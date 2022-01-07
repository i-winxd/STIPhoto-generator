# STIPhoto-generator
Quickly create Survive the Internet photo images

## How do I use this??
1. Run the program.
2. Choose the folder the exe/python file prompts you to. This program will then gather all the PNG/JPG files in that folder. If there are too many image files, this program sorts images alphebatically. NOTE: Only RGB and RGBA images are supported. If any image isn't RGB/RGBA, it will be skipped.
4. In the same directory of the exe/python file, it will create a new folder called ``export`` and create a bunch of image files compatible with survive the internet.
STI has around 130-135 images (I don't remember which one). Drag all the images in ``export`` to ``C:\Program Files (x86)\Steam\steamapps\common\The Jackbox Party Pack 4\games\SurviveTheInternet\content\STIPhoto``.

## Example:
I run the program, and select the folder ``pictures`` with the following file: ``image.png``. The program then creates a folder named ``export`` in the same file as the exe file you opened, and will shrink ``image.png`` down to ``425x320`` and name it ``Airplane.jpg``. The next image would be named ``ApplePicking.jpg``, and so on.

## I don't like installing .exe files off the internet by random people. What should I do?
1. Install python 3.9 or later on your computer. Best to install the one by the windows store.
2. Make sure ``pip`` is installed on your computer. If not, search it up.
3. Install pillow using the following commands:
```
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
```

(Adapted from https://pillow.readthedocs.io/en/stable/installation.html)
