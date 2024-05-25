import urandom

#Obatined using ChatGPT
class Random:
    def __init__(self):
        pass

    def randint(self, a, b):
        # Generate a random integer between a and b (inclusive)
        return a + urandom.getrandbits(32) % (b - a + 1)

    def choice(self, sequence):
        # Choose a random element from the sequence
        return sequence[self.randint(0, len(sequence) - 1)]

    def shuffle(self, sequence):
        # Shuffle the sequence in place
        for i in range(len(sequence) - 1, 0, -1):
            j = self.randint(0, i)
            sequence[i], sequence[j] = sequence[j], sequence[i]