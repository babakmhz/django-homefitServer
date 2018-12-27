
from uuid import uuid4

class OrderNumber():
    def generate():
        const = 'jix-O-'
        hex = str(uuid4().hex)
        order=const+hex[1:8]
        print(order)
        return str(order)
