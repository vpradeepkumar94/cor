
from camelcase import CamelCase

c = CamelCase()


def convert_to_camel_case(sentence):
    print(c.hump(sentence))
# This is a Sentence That Needs CamelCasing!
