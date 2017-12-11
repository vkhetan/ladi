import Image, StringIO
img = Image.open(path)
img.thumbnail((512,512))
buffer = StringIO.StringIO()
img.save(buffer, "PNG")
content = buffer.getvalue()


