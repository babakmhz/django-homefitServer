from uuid import uuid4
class appUtils:
    @staticmethod
    def resolveArrayToList(array_input):
        out = list()
        for x in array_input:
            try:
                out.append(int(x))
            except:
                pass

        return out

    @staticmethod
    def generateOrderNumber():
        # TODO:change APP Name
        const = 'homeFit-O-'
        hex = str(uuid4().hex)
        order = const+hex[1:8]
        print(order)
        return str(order)
