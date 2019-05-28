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
