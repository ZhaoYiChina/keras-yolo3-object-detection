import xml
import xml.etree.ElementTree as ET

"""
实现从xml中读取节点数据，递归遍历所有节点
"""

result_list = []
unique_id = 1

# 遍历所有节点
def walkData(root_node, level, result_list):
    global unique_id
    temp_list = [unique_id, root_node.text]
    if root_node.tag == 'name':
        if len(result_list) != 0:
            hasLabel = False
            for item in result_list:
                if item[1] == root_node.text:
                    hasLabel = True
                    break
            if hasLabel == False:
                result_list.append(temp_list)
                unique_id += 1
        else:
            result_list.append(temp_list)
            unique_id += 1

    # 遍历每个子节点
    children_node = root_node.getchildren()
    if len(children_node) == 0:
        return
    for child in children_node:
        walkData(child, level + 1, result_list)
    return

def delete_gbk(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()
    if root != None and root.find('path') != None:
        root.remove(root.find('path'))
        tree.write(file_name)



def getXmlData(file_name):
    level = 1 # 节点的深度从1开始
    delete_gbk(file_name)
    root = ET.parse(file_name).getroot()
    walkData(root, level, result_list)
    return result_list

if __name__ == '__main__':
    for i in range(1001):
        t = 0
        s = '0'
        l = 5 - len(str(i))
        while(l):
            s += '0'
            l -= 1
        pre = 'C:\\Users\\Administrator\\Documents\\My_Documents\\ZY\\project\\keras-yolo3-object-detection\\VOCdevkit\\VOC2021\\Annotations\\'
        file_name = pre + s + str(i) + '.xml'
        R = getXmlData(file_name)

    for x in R:
        print(x)
        pass

    result = ''
    for x in R:
        result_string = "\"" +x[1] + "\"" + ","
        result += result_string
        pass

    print(result)