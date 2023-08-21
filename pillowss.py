from PIL import Image, ImageDraw, ImageFont
im1 = Image.open('dummy.png', mode="r")
# im2 = Image.open('dummy1.png', mode='r')

# print(image.format, image.size, image.mode)
# image.show(title='Dummy')

# region = image.crop(box=(100, 100, 400, 400))
# region = region.transpose(Image.Transpose.ROTATE_180)
# region.show()

# out = image.filter(ImageFilter.DETAIL)
# out.show()


# def make_transparent(im: Image):
# 	rgba = im.convert('RGBA')
# 	data = rgba.getdata()
# 	new_data = []
# 	for item in data:
# 		if item[0] == 255 and item[1] == 255 and item[2] == 0:
# 			new_data.append((255, 255, 255, 0))
# 		else:
# 			new_data.append(item)
# 	rgba.putdata(new_data)
# 	rgba.save('transparent.png', 'PNG')

#
# make_transparent(im2)
# im = Image.open('transparent.png')
#
# def merge(im1: Image, im2: Image) -> Image:
# 	w = im1.size[0] + im2.size[0]
# 	h = im1.size[1] + im2.size[1]
# 	im = Image.new(mode='RGBA', size=(w, h))
#
# 	im.paste(im1)
# 	im.paste(im2, (im1.size[0]-1500, 50))
#
# 	return im
#
# merge(im1, im).show()

i = ImageDraw.Draw(im1)
font = ImageFont.truetype(r'C:\Windows\Fonts\Arial.ttf', 65)
i.text((500, 500), 'LALA', font=font, fill=(255, 0, 0),
       stroke_fill='black', stroke_width=2, direction='rtl')
# im1.show()
# im1.save()
