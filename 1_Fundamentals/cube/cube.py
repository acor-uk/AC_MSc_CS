class cube:
    def __init__(self, length):
        self.length = length
        self.face_area = length * length
        self.surface_area = 6 * self.face_area
        self.volume = self.face_area * length
    
    def __str__(self):
        return f"CUBE VALUES:\nFace Area: {self.face_area}\nSurface Area: {self.surface_area}\nVolume: {self.volume}"