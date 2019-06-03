from uuid import uuid4
import pyqrcode
from serviceManProject import settings

class appUtils:

    # global qrCodePath = ''
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
        # print(order)
        return str(order)

    @staticmethod
    def generateOrderQrCode(data, path, orderNumber):
        # qr = qrcode.QRCode(
        #     version=1,
        #     error_correction=qrcode.constants.ERROR_CORRECT_L,
        #     box_size=10,
        #     border=4,
        # )
        # qr.add_data(data)
        # qr.make(fit=True)
        # # filename = 'qrcode-code1.png'

        # return qr.make_image()
        print(settings.MEDIA_URL)
        big_code = pyqrcode.create(
            data, error='L', version=27, mode='binary')
        file_name = str(path)+str(orderNumber)+'.png'
        big_code.png(settings.MEDIA_ROOT+file_name, scale=6, module_color=[
                     0, 0, 0, 128], background=[0xff, 0xff, 0xcc])

        return file_name
