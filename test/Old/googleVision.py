from google.cloud import vision
import io

# Path to your image file
image_path = './test/images/IMG_9855.JPG'

# Create a client
client = vision.ImageAnnotatorClient()

# Load the image into memory
with io.open(image_path, 'rb') as image_file:
    content = image_file.read()
image = vision.Image(content=content)

# Perform text detection
response = client.text_detection(image=image)
texts = response.text_annotations

print('Texts:')
for text in texts:
    print('\n"{}"'.format(text.description))
    vertices = ['({},{})'.format(vertex.x, vertex.y) for vertex in text.bounding_poly.vertices]
    print('bounds: {}'.format(','.join(vertices)))
