from PIL import Image
from string import printable


class PixImage:
	def __init__(self,
				 img: str | Image.Image = ...,
				 text: str = ...) -> None:
		self._img = None
		self._text = text

		if isinstance(img, str):
			with Image.open(img) as i:
				i.load()
				self._img = i
		elif isinstance(img, Image.Image):
			self._img = img

	@property
	def image(self) -> Image.Image:
		return self._img

	@property
	def text(self) -> str:
		return self._text

	@staticmethod
	def _rgb(src: str) -> tuple:
		x = ord(src)
		x = int(bin(x).lstrip('0b'))
		x = hex(x).lstrip('0x')

		return tuple(int(x[i:i+2], 16) for i in (0, 2, 4))

	@staticmethod
	def _char(rgb: tuple) -> str:
		x = ''
		for i in rgb:
			if i == 0:
				x += '0'
				continue
			x += hex(i).lstrip('0x')
		x = int(x, 16)
		x = int(str(x), 2)

		return chr(x)

	def getimage(self) -> Image.Image:
		"""
		Encrypts text into an image.

		:returns: Image class object from Pillow.
		"""

		width = len(self._text)
		img = Image.new('RGB', (width, 1))

		for i in range(width):
			index = printable.find(self._text[i])
			img.putpixel((i, 0), self._rgb(printable[index]))

		return img

	def getstr(self) -> str:
		"""
		Decrypts an image into text.

		:returns: Decrypted string.
		"""

		s = ''

		for i in range(self._img.size[0]):
			rgb = self._img.getpixel((i, 0))
			s += self._char(rgb)

		return s

	def save(self, filename: str) -> None:
		self.getimage().save(filename + '.png')
