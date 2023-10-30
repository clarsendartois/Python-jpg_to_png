# # Use your Terminal, if you are on
# # windows type: python JPG_to_PNG.py JPG/ PNG/
# # It will create a new folder
# # and put your PNGs in this folder.

# # ---------------------------------------------------------------
# # from PIL import Image

# # # Open the image
# # img = Image.open("img.jpg")

# # # Save the image with PNG format
# # img.save("img.png", format="PNG")

# # ---------------------------------------------------------------
# import sys
# import os
# from PIL import Image
# # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/learn/lecture/16136599#overview

# path = len(sys.argv)
# print(path)
# # directory = sys.argv[1]

# # if not os.path.exists(directory):
# #     os.makedirs(directory)


# # for filename in os.listdir(path):
# #     clean_name = os.path.splitext(filename)[0]
# #     img = Image.open(f'{path}{filename}')
# #     img.save(f'{directory}/{clean_name}.png', 'png')
# #     print('all done!')

# # ---------------------------------------------------------------

# # from PIL import Image
# # from os import listdir
# # from os.path import splitext

# # target_directory = '.'
# # target = '.png'

# # for file in listdir(target_directory):
# #     filename, extension = splitext(file)
# #     try:
# #         if extension not in ['.py', target]:
# #             im = Image.open(filename + extension)
# #             im.save(filename + target)
# #     except OSError:
# #         print('Cannot convert %s' % file)

# # ---------------------------------------------------------------
# # https://www.quora.com/How-do-you-fix-Sys-argv-1-indexerror-list-index-out-of-range-Python-3-9

# # This code will not cause the error and will handle it gracefully

# # import sys

# # try:
# #     print(sys.argv[1])
# # except IndexError:
# #     print("No command-line argument provided")


from PIL import Image, ImageFilter

img = Image.open("./JPG/pikachu.jpg")
blur_img = img.convert("L")
blur_img.save("grey.png", "png")

# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/learn/lecture/16136569#overview
