# uigf_merge
补齐胡桃工具箱导出UIGF4文件缺失字段，以导入其他祈愿分析

如需导入提瓦特小助手等不支持uigf4.X格式的工具，下述步骤中所需文件请自行替换为带有uigf3.0后缀的文件

方法A：
  下载release中的可执行文件，和胡桃工具箱导出的默认名称json文件放在相同目录下，直接运行即可生成标准字段的uigf_merged.json


方法B：

  1、直接下载weapon_avatar.json、merge_uigf.py或clone本项目至本地
  
  2、胡桃工具箱导出UIGF4标准json文件至相同目录下，保持默认名称不变
  
  3、直接运行py文件，获得合并字段后的uigf_merged.json
