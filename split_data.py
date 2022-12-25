import os
from shutil import copyfile

# try:
#     os.mkdir('./datasets')
#     os.mkdir('./datasets/cars/images')
#     os.mkdir('./datasets/cars/labels')
#     os.mkdir('./datasets/cars/images/train')
#     os.mkdir('./datasets/cars/images/val')
#     os.mkdir('./datasets/cars/labels/train')
#     os.mkdir('./datasets/cars/labels/val')
# except OSError:
#     pass

def split_train(SOURCE, DESTINATION_TRAIN,  DESTINATION_TEST):
    with open(SOURCE + 'train.txt', 'r') as filename_train:
        for filename in filename_train:
            this_file = SOURCE + filename.replace('./', '').translate({ord('\n'): None})
            destination = DESTINATION_TRAIN[:-1].translate({ord('\n'): None}) + filename.replace('./', '').translate({ord('\n'): None})
            print(this_file,destination)
            copyfile(this_file, destination)
        
    # filename_test = open('test.txt', 'r')
    # print(filename_test)
    # for filename in filename_test:
    #     this_file = SOURCE + filename
    #     destination = DESTINATION_TEST + filename
    #     copyfile(this_file, destination)
        
def split_test(SOURCE, DESTINATION_TRAIN,  DESTINATION_TEST):
    filename_train = open('train.txt', 'r')
    for filename in filename_train:
        this_file = SOURCE + filename.replace(".jpg",".txt")
        destination = DESTINATION_TRAIN + filename.replace(".jpg",".txt")
        copyfile(this_file, destination)
        
    filename_test = open('test.txt', 'r')
    for filename in filename_test:
        this_file = SOURCE + filename.replace(".jpg",".txt")
        destination = DESTINATION_TEST + filename.replace(".jpg",".txt")
        copyfile(this_file, destination)
  
# #folder images        
source_images = './datasets/cars/'
destination_images_train = './datasets/cars/images/train/'
destination_images_val = './datasets/cars/images/val/'
split_train(source_images, destination_images_train, destination_images_val)

#folder labels
# source_labels = './datasets/cars/labels'
# destination_labels_train = './datasets/cars/labels/train/'
# destination_labels_val = './datasets/cars/labels/val/'
# split_test(source_labels, destination_labels_train, destination_labels_val)