import xml.sax

from util.world import Country


class AsianHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.countries = []
        self.country = Country()
        self.supported_tags = {
            "Code": "code",
            "Name": "name",
            "Continent": "continent",
            "Population": "population",
            "SurfaceArea": "surface_area"
        }

    def startElement(self, tag, attributes):
        self.opening_tag = tag

    def characters(self, content):
        if self.opening_tag in self.supported_tags.keys():
            prop = self.supported_tags[self.opening_tag]
            setattr(self.country, prop, content)

    def endElement(self, tag):
        self.opening_tag = ""
        if tag == "country":
            if self.country.continent == "Asia":
                self.countries.append(self.country)
            self.country = Country()


parser = xml.sax.make_parser()
handler = AsianHandler()
parser.setContentHandler(handler)
parser.parse("resources/countries.xml")
for country in sorted(handler.countries, key=lambda ctry: ctry.name, reverse=True):
    print(country)
