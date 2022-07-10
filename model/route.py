import random
from model.checkpoint import Checkpoint
from model.train import Train


class Route:
    def __init__(self, num):
        self.number = num
        self.interval = random.randint(10, 14)
        self.start_tick = random.randint(0, 2)
        self.last_tick = -1
        self.end_tick = 100

        self.checkpoints = []
        self.trains_straight = []
        self.trains_reversed = []
        self.trains_on_the_go = []

        self.last_checkpoint_index = self.setup_checkpoints()
        self.setup_trains()


    def display_stations(self):
        for station in self.checkpoints:
            if not station.is_checkpoint:
                print("|" + str(station.number) + "|", end="")
            else:
                print("_", end="")
            if station == self.checkpoints[-1]:
                print()
            else:
                print(" >> ", end="")


    def setup_checkpoints(self):
        last_checkpoint_index = -1
        number_of_stations = random.randint(4, 7)

        for current_station_number in range(number_of_stations):
            self.checkpoints.append(Checkpoint(current_station_number, False))
            last_checkpoint_index += 1
            if (current_station_number == number_of_stations - 1):
                break
            number_of_checkpoints_for_current_station = random.randint(2, 4)

            for _ in range(number_of_checkpoints_for_current_station):
                self.checkpoints.append(Checkpoint(current_station_number + 100, True))
                last_checkpoint_index += 1
        return last_checkpoint_index

    def setup_trains(self):
        number_of_trains_needed_for_one_way = len(self.checkpoints) // self.interval + 1
        for train_number in range(0, number_of_trains_needed_for_one_way):
            self.trains_straight.append(Train(100 + train_number, True, -1))
            self.trains_reversed.append(Train(200 + train_number, False, -1))


    def load_upcoming_trains_schedule_by_index(self, index):
        return [], []


    def display_upcoming_trains_by_index(self, index):
        pass


    def load_planned_timetable_by_index(self, index):
        first_train_tick_straight = self.start_tick + index
        next_train_tick_straight = first_train_tick_straight + self.interval

        first_train_tick_reversed = self.start_tick + len(self.checkpoints) - index - 1
        next_train_tick_reversed = first_train_tick_reversed + self.interval

        timetable_straight = [first_train_tick_straight]
        timetable_reversed = [first_train_tick_reversed]

        while next_train_tick_straight < self.end_tick or next_train_tick_reversed < self.end_tick:
            timetable_straight.append(next_train_tick_straight)
            timetable_reversed.append(next_train_tick_reversed)

            next_train_tick_straight += self.interval
            next_train_tick_reversed += self.interval

        return (timetable_straight, timetable_reversed)


    def display_timetable_by_index(self, index):
        timetable_straight, timetable_reversed = self.load_planned_timetable_by_index(index)

        print("Schedule for station with index " + str(index))

        print("Straight way: ")
        for next_train in timetable_straight:
            print(next_train)

        print("Reversed way: ")
        for next_train in timetable_reversed:
            print(next_train)

        print()


    # needed new logic, what to do when there is 4 trains and 1 in an accident
    def tick(self, tick):
        self.last_tick = tick

        for train in self.trains_on_the_go:
            train.tick()

        if len(self.trains_on_the_go) != 0 and self.trains_on_the_go[-1].current_checkpoint == self.last_checkpoint_index + 1: 
            self.trains_reversed.insert(0, self.trains_on_the_go.pop())
            self.trains_reversed[0].end_lap()

            self.trains_straight.insert(0, self.trains_on_the_go.pop())
            self.trains_straight[0].end_lap()

        if tick % self.interval == 0:
            self.trains_on_the_go.insert(0, self.trains_straight.pop())
            self.trains_on_the_go[0].start_lap(0)
            self.trains_on_the_go.insert(0, self.trains_reversed.pop())
            self.trains_on_the_go[0].start_lap(self.last_checkpoint_index)
