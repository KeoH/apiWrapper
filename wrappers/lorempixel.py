from urllib2 import urlopen

class LoremPixelWrapper():

    base_url = "http://www.lorempixel.com"

    image_categories = [
        "abstract", "animals", "business", "cats", "city", "food",
        "nightlife", "fashion", "people", "nature", "sports", "technies",
        "transport"
    ]

    options = {
        "category" : None,
    }

    def __init__(self, category=None, color=True, width=300, height=300, image_number=0, filename="image.jpg"):
        if category in self.image_categories:
            self.options['category'] = category

        self.options['color'] = color
        self.options['width'] = width
        self.options['height'] = height
        self.options['filename'] = filename
        self.options['image_number'] = image_number

    def say_categories(self):
        for cat in self.image_categories:
            print "Categoria: %s" % cat

    def _build_url(self):
        url = self.base_url
        if not self.options["color"]:
            url += "/g"
        url += "/%s/%s" %(self.options["width"], self.options["height"])
        if self.options["category"]:
            url += "/%s" % self.options["category"]
        if self.options["image_number"] > 0 and self.options["image_number"] <= 10:
            url += "/%s" % self.options["image_number"]
        return url

    def get_url(self):
        return self._build_url()

    def download(self):
        result = urlopen(self._build_url())
        data = result.read()
        file = open(self.options["filename"], "wb")
        file.write(data)
        file.close()
