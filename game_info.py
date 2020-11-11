GAME_VERSION="0.1.0dev5.11.2020"

class GameInfo():

    def __init__(self):
        self.current_fps = 0
        self.last_fps = []
        self.last_fps_amount = 1000
        self.avg_fps = 0

    def add_record(self, fps):
        self.current_fps = fps
        if len(self.last_fps) < self.last_fps_amount + 1:
            self.last_fps.append(fps)
        else:
            del self.last_fps[0]
            self.last_fps.append(fps)

    def update(self):
        total_fps = 0
        for record in self.last_fps:
            total_fps += record
        self.avg_fps = total_fps // len(self.last_fps)
