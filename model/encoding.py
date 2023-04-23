import numpy as np

class Encoder:
    def __init__(self, length):
        self.length: int = length
    
    def encode(self, num):
        raise NotImplementedError()

    def decode(self, encoded):
        raise NotImplementedError()

class BinaryEncoder(Encoder):
    def __init__(self, length):
        self.length: int = length
        self.d: dict[bytes, int] = {}
        for v in range(2**length):
            encoded = self.encode(v).tobytes()
            self.d[encoded] = v

    def encode(self, num):
        encoded_str = bin(num)[2:]
        encoded_str = '0'*(self.length - len(encoded_str)) + encoded_str
        encoded = np.array(list(encoded_str), dtype=bytes)
        return encoded
    
    def decode(self, encoded):
        return self.d[encoded.tobytes()]

class GrayEncoder(Encoder):
    def __init__(self, length):
        self.length: int = length
        self.d: dict[bytes, int] = {}
        for v in range(2**length):
            encoded = self.encode(v).tobytes()
            self.d[encoded] = v
    
    def encode(self, num):
        num ^= (num >> 1)
        encoded_str = bin(num)[2:]
        encoded_str = '0'*(self.length - len(encoded_str)) + encoded_str
        encoded = np.array(list(encoded_str), dtype=bytes)
        return encoded
    
    def decode(self, encoded):
        return self.d[encoded.tobytes()]

class FloatEncoder(Encoder):
    def __init__(self, lower_bound, upper_bound, length, is_gray=False):
        super().__init__(length)
        self.lower_bound: float = lower_bound
        self.upper_bound: float = upper_bound
        self.__decoding_multiplier = (self.upper_bound - self.lower_bound) / (2 ** self.length - 1)
        self.__encoding_multiplier = 1 / self.__decoding_multiplier

        if is_gray:
            self.sub_encoder: Encoder = GrayEncoder(length)
        else:
            self.sub_encoder: Encoder = BinaryEncoder(length)
    
    def encode(self, num):
        n = round((num - self.lower_bound) * self.__encoding_multiplier)
        encoded = self.sub_encoder.encode(n)
        return encoded
    
    def decode(self, encoded):
        n = self.sub_encoder.decode(encoded)
        decoded = round(self.lower_bound + n * self.__decoding_multiplier, 2)
        return decoded


# Testing
if __name__ == '__main__':
    xs = np.arange(-5.12, 0, 0.01)
    encoder = FloatEncoder(-5.12, 5.11, 10, is_gray=True)
    for x in xs:
        print(f'{x:.2f} -> {encoder.encode(x)} -> {encoder.decode(encoder.encode(x)):.2f}')
