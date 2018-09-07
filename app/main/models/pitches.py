class Pitch:

    all_pitches = []

    def __init__(self,pitch):
        self.pitch


    def save_pitch(self):
        Pitch.all_pitches.append(self)


    @classmethod
    def clear_pitches(cls):
        Pitch.all_pitches.clear()


    @classmethod
    def get_pitches(cls,id):

        response = []

        for pitch in cls.all_pitches:
            response.append(pitch)
            
            return response     