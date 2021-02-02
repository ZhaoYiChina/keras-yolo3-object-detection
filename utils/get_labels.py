import xml
import xml.etree.ElementTree as ET

"""
实现从xml中读取节点数据，递归遍历所有节点
"""

unique_id = 1

# 遍历所有节点
def walkData(root_node, level, result_list):
    global unique_id
    temp_list = [unique_id, level, root_node.tag, root_node.attrib]
    result_list.append(temp_list)
    unique_id += 1

    # 遍历每个子节点
    children_node = root_node.getchildren()
    if len(children_node) == 0:
        return
    for child in children_node:
        walkData(child, level + 1, result_list)
    return

def getXmlData(file_name):
    level = 1 # 节点的深度从1开始
    result_list = []
    root = ET.parse(file_name).getroot()
    walkData(root, level, result_list)
    return result_list

if __name__ == '__main__':
    file_name = 'C:\\Users\\Administrator\\Documents\\My_Documents\\ZY\\project\\keras-yolo3-object-detection\\VOCdevkit\\VOC2021\\Annotations\\000002.xml'
    R = getXmlData(file_name)
    for x in R:
        print(x)
        pass