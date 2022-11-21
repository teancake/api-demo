class Feature:
    def __init__(self):
        width = 0
        height = 0
        name = "some"

    @staticmethod
    def obtain_feature(width, height, name):
        feature = Feature()
        feature.width = width
        feature.height = height
        feature.name = name
        return feature


class SomeModel:
    def infer(self, feature):
        if "abc" == feature.name:
            return feature.width * feature.height
        else:
            return feature.width + feature.height
