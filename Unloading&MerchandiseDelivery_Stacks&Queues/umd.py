class LoadingForTransportation:
    def __init__(self, time_dock_to_TorP, max_items_each_TorP):
        self.time_dock_to_TorP = time_dock_to_TorP
        self.max_items_each_TorP = max_items_each_TorP
        self.current_count = 0
        self.time_finished_loading_all_items = 0

    def time_for_loading_item(self, time_worker_picked_loading_item):
        self.current_count += 1
        if self.current_count == self.max_items_each_TorP:
            self.time_finished_loading_all_items = time_worker_picked_loading_item + self.time_dock_to_TorP
        return time_worker_picked_loading_item + 2 * self.time_dock_to_TorP

class UMD:
    def __init__(self, num_item_each_train_list, num_item_each_plane_list, train_item_destination_list, plane_item_destination_list):
        self.train = []
        self.plane = []
        self.train_queue_of_stack = []
        self.plane_queue = []

        for i, num_item_train in enumerate(num_item_each_train_list):
            train_num = i + 1
            self.train.append(LoadingForTransportation(train_num, num_item_train))

        for i, num_item_plane in enumerate(num_item_each_plane_list):
            plane_num = i + 1
            self.plane.append(LoadingForTransportation(plane_num*5, num_item_plane))

        for item in plane_item_destination_list:
            self.plane_queue.append(item)

        self.stacking_train_items(train_item_destination_list)
        self.loading_item_on_train()
        self.loading_item_on_plane()

    def stacking_train_items(self, train_item_destination_list):
        train_stack = []
        for item in train_item_destination_list:
            if len(self.train_queue_of_stack) == 5:
                self.train_queue_of_stack.append(train_stack)
                train_stack = []
            train_stack.append(item)
        self.train_queue_of_stack.append(train_stack)

    def loading_item_on_train(self):
        train_current_time = 0
        while len(self.train_queue_of_stack) != 0:
            Front_stack = self.train_queue_of_stack.pop(0)
            while len(Front_stack) != 0:
                item = Front_stack.pop()
                train_current_time = self.train[item - 1].time_for_loading_item(train_current_time)

    def loading_item_on_plane(self):
        plane_current_time = 0
        while len(self.plane_queue) != 0:
            item = self.plane_queue.pop(0)
            plane_current_time = self.plane[item - 1].time_for_loading_item(plane_current_time)

    def str_output_time(self):
        print(" ".join(str(tr.time_finished_loading_all_items) for tr in self.train))
        print(" ".join(str(pl.time_finished_loading_all_items) for pl in self.plane))

