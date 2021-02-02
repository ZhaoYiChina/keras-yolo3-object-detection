import xml.etree.ElementTree as ET
from os import getcwd

sets=[('2021', 'train'), ('2021', 'val'), ('2021', 'test')]

classes = ["Thyroid_BQ_Ds", "Thyroid_BQ_D", "Thyroid_BQ_W", "Thyroid_BQ_S", "Thyroid_BQ_Ws", "Thyroid_BM_D", "Thyroid_ZB", "Thyroid_BQ_Sh", "Thyroid_BM_Wf", "Thyroid_BM_Sd", "Thyroid_BM_Ds", "Thyroid_BQ_Wh", "Thyroid_BQ_H", "Thyroid_BM_Wh", "Thyroid_BQ_Dh", "Thyroid_BQ_Sw", "Thyroid_BM_Ws", "Thyroid_BM_Dh", "Thyroid_BQ_Sd", "Thyroid_BM_S", "Thyroid_BQ_Wf", "Thyroid_BQ_Dw", "Thyroid_BM_W", "Thyroid_BM_Dw", "Thyroid_BM_Sh"]

def convert_annotation(year, image_id, list_file):
    in_file = open('VOCdevkit/VOC%s/Annotations/%s.xml'%(year, image_id))
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

wd = getcwd()

for year, image_set in sets:
    image_ids = open('VOCdevkit/VOC%s/ImageSets/Main/%s.txt'%(year, image_set)).read().strip().split()
    list_file = open('%s_%s.txt'%(year, image_set), 'w')
    for image_id in image_ids:
        list_file.write('%s/VOCdevkit/VOC%s/JPEGImages/%s.jpg'%(wd, year, image_id))
        convert_annotation(year, image_id, list_file)
        list_file.write('\n')
    list_file.close()

