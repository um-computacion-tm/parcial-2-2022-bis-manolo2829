class Encoder:

    def __init__(self):
        self.dictionary = {}
    
    def encode(self, text):
        for i in text:
            print(i)

    def decode(self):
        print('decode')



encoder = Encoder()
result_dict = encoder.encode('While')