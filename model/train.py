class Train:
    def __init__(self, num, going_straight, current_checkpoint):
        self.number = num
        self.is_going_straight = going_straight
        self.current_checkpoint = current_checkpoint

        self.in_accident = False
        self.accident = None
        self.accident_ticks = 0

    def tick(self):
        if self.in_accident:
            self.accident_ticks += 1
            if self.accident.hardness == self.accident_ticks:
                self.accident = None
                self.accident_ticks = 0
                self.in_accident = False
            return

        if self.is_going_straight:
            self.current_checkpoint += 1
        else:
            self.current_checkpoint -= 1


    def start_lap(self, new_checkpoint):
        self.current_checkpoint = new_checkpoint


    def end_lap(self):
        self.is_going_straight = not self.is_going_straight
        self.current_checkpoint = -1