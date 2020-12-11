import time
import os
import shutil
import glob

# 文件路径对比
## /diseraserepAno/src/yfjz/com/nipsoft/nipis/yfjz/batchvaccine/action/AddBatchVaccineAction.java
## /diseraserepAno/WebRoot/WEB-INF/classes/com/nipsoft/nipis/yfjz/batchvaccine/action/AddBatchVaccineAction
WORK_PLACE_PATH = 'E:\\工作\\部署文件夹' # 部属用文件夹所在位置
PROJECT_PREFIX = 'WebRoot/WEB-INF/classes/production/ipis-svn' # 工程class放置地址
PROJECT_REAL_PATH_PREFIX = 'E:\\工作\\workPlace\\ipis-svn\\' # 本地工程的绝对路径
PROJECT_DEPLO_PATH_PREFIX = 'WebRoot/WEB-INF/classes/'
# PROJECT_REAL_PATH_PREFIX = 'D:\\WorkSpace\\nipBJ\\nipis-packag\\' # 本地工程的绝对路径（国哥）

def generateFile(file_path):
    # 交互信息
    success = True
    message = ""
    # 得到当前日期
    curTime = time.strftime('%Y%m%d', time.localtime())
    error_message = str()
    file_path = file_path.strip()

    #n = input("请输入文件数量：")
    #for i in range(int(n)):

    # 对文件路径进行处理
    #file_path = input("【" + str(i) + "】请输入文件路径：")
    # file_path = '/diseraserepAno/src/yfjz/com/nipsoft/nipis/yfjz/batchvaccine/action/AddBatchVaccineAction.java' 

    final_point_loc = file_path.rfind('.') # 最后一共.的位置
    file_suffix = file_path[final_point_loc + 1:] # 文件后缀

    res2 = file_path.rfind('/') # java文件路径结尾位置（不包含文件名）
    file_name = file_path[res2 + 1 : final_point_loc] # 文件名称（不包含后缀）
    try:
        # 1.1 java文件路径
        if file_suffix == 'java': 
            res = file_path[file_path.find('src') + 4 :].find('/') + 4 # java文件路径的开头位置/

            class_file_path_prefix = PROJECT_PREFIX + file_path[res : res2] # 从文件路径截取出来的相对路径
            file_to_prepath_add = class_file_path_prefix.replace('/', '\\') # ——【优化】根据系统变更路径分隔符
            file_from_path = file_to_prepath_add  + '\\' + file_name + '.class' # class 文件应该所在路径
            # 正式环境class文件夹路径和本地不一样，需要删除掉原路径中的部分字符串
            com_pos = file_to_prepath_add.find('com') # com位置
            production_pos = file_to_prepath_add.find('production') # production 位置 
            file_to_prepath = file_to_prepath_add[:production_pos] + file_to_prepath_add[com_pos:]


        # 1.2 js文件
        # elif file_suffix == 'js':
           # print("js")
        # 1.3 html文件
        ## WebRoot/WEB-INF/pages/yfjz/case/vaccinationplat/platmain.html
        elif file_suffix in ('html', 'jar', 'js'):
            file_to_prepath = file_path.replace('/', '\\') # ——【优化】根据系统变更路径分隔符
            file_from_path = file_to_prepath #html 文件来源地址
            file_to_prepath = file_to_prepath[:file_to_prepath.rfind('\\')] # html文件保存地址
        # 1.4 配置文件
        #1# src/admin/com/nipsoft/nipis/admin/module/hbm/Module.hbm.xml
        elif file_suffix == 'xml':
            sec_point_pos = file_name.rfind('.')
            sec_file_suffix = file_name[sec_point_pos + 1 :]
            com_pos = int()
            if sec_file_suffix == 'hbm':
                com_pos = file_path.find('com')
            file_from_path = file_path.replace('/', '\\')
            file_to_prepath = (PROJECT_DEPLO_PATH_PREFIX + file_path[com_pos : res2]).replace('/', '\\')

            
        elif file_suffix == 'properties':
            file_from_path = file_path.replace('/', '\\')
            file_to_prepath = PROJECT_DEPLO_PATH_PREFIX

        else:
            error_message = "Something Wrong, please check the file path inputed"

        final_path = WORK_PLACE_PATH + '\\' + curTime + '\\' + file_to_prepath # 所需的文件夹最终路径
        # 创建文件夹
        if not os.path.exists(final_path):
            os.makedirs(final_path)

        file_name_list = list()
        file_real_path = PROJECT_REAL_PATH_PREFIX + file_from_path
        # 复制文件
        if file_suffix != 'java':
            shutil.copy(file_real_path, final_path)
            file_name_list.append(file_name)
        else: # 对于java文件要注意是否有多个class文件需要复制
            path_prefix = file_real_path[:file_real_path.rfind('\\') + 1]
            file_list = [file_real_path]
            file_list.extend(glob.glob(path_prefix + file_name + "$*.class"))
            for class_file in file_list:
                file_name_list.append(class_file)
                shutil.copy(class_file, final_path)
        # print(file_name + '.class 准备完成！')
        #print('程序结束！')
    except Exception as e:
        success = False
        message = file_name + '.' + file_suffix +  'transfer FAILED:' + str(e)

    if success:
        return file_name + '【{}个】.'.format(len(file_name_list)) + file_suffix +' is ready！ '
    else:
        return message


def set_WORK_PLACE_PATH(work_place_path):
    WORK_PLACE_PATH = work_place_path

def set_PROJECT_PREFIX(project_prefix):
    PROJECT_PREFIX = project_prefix

def set_PROJECT_REAL_PATH_PREFIX(prject_real_path_prefix):
    PROJECT_REAL_PATH_PREFIX = prject_real_path_prefix

def set_PROJECT_DEPLO_PATH_PREFIX(prject_deploy_path_prefix):
    PROJECT_DEPLO_PATH_PREFIX = prject_deploy_path_prefix

def get_WORK_PLACE_PATH():
    return WORK_PLACE_PATH

def get_PROJECT_PREFIX():
    return PROJECT_PREFIX

def get_PROJECT_REAL_PATH_PREFIX():
    return PROJECT_REAL_PATH_PREFIX

def get_PROJECT_DEPLO_PATH_PREFIX():
    return PROJECT_DEPLO_PATH_PREFIX