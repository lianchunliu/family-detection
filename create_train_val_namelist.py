import os
import sys
import glob
import pandas as pd
import xml.etree.ElementTree as ET
import tensorflow as tf

flags = tf.app.flags
flags.DEFINE_string("image_dir", '/floyd/input/family', 'image directory')
flags.DEFINE_string("output_dir", '/floyd/input/family_data', 'image directory')
flags.DEFINE_integer("val_count", 10, 'image directory')

FLAGS = flags.FLAGS

def xml_to_csv(image_dir, path):
    val_count = 0
    val_file = open(path + "/family_val.txt", 'w')
    train_file = open(path + "/family_train.txt", 'w')

    for xml_file in glob.glob(image_dir + '/*.xml'):
        file_name = xml_file[-23:-4]
        if val_count < 10:
            val_file.write(file_name)
            val_file.write("\n")
        else:
            train_file.write(file_name)
            train_file.write("\n")
        val_count += 1

    val_file.close()
    train_file.close()

def main():
    image_path = FLAGS.image_dir
    output_path = FLAGS.output_dir
    xml_df = xml_to_csv(image_path, output_path)
    print('Done!', output_path)


if __name__ == '__main__':
    main()
