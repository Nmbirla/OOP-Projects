from umd import UMD

# Accepting the input from user
# split using empty spaces
# Create a list of each input line

Num_item_each_train_list = list(map(int, input().split()))
# print(Num_item_each_train_list)
Num_item_each_plane_list = list(map(int, input().split()))
# print(Num_item_each_plane_list)
train_item_destination_list = list(map(int, input().split()))
# print(train_item_destination_list)
plane_item_destination_list = list(map(int, input().split()))
# print(plane_item_destination_list)


Unloading_Loading = UMD(Num_item_each_train_list, Num_item_each_plane_list, train_item_destination_list, plane_item_destination_list)
Unloading_Loading.str_output_time()
