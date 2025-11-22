import json
import sys
import os
import tempfile
import shutil
from datetime import datetime, timedelta

def get_embedded_json(filename: str):
    """
    从 PyInstaller 打包的 EXE 内部释放内置数据文件
    """
    if hasattr(sys, "_MEIPASS"):
        # PyInstaller 打包后的临时目录
        embedded_path = os.path.join(sys._MEIPASS, filename)
    else:
        # 运行 .py 时读取当前目录
        embedded_path = os.path.join(os.path.dirname(__file__), filename)

    # 复制文件到系统临时目录
    tmp_dir = tempfile.gettempdir()
    dst_file = os.path.join(tmp_dir, filename)
    shutil.copyfile(embedded_path, dst_file)
    return dst_file


def main():
    uigf_file = "Snap Hutao UIGF.json"
    output_file = "uigf_merged.json"

    # ----------- 从 EXE 内部读取 weapon_avatar.json --------------
    embedded_json_path = get_embedded_json("weapon_avatar.json")

    with open(embedded_json_path, "r", encoding="utf-8") as f:
        weapon_data = json.load(f)
    # ------------------------------------------------------------

    # 读取 UIGF 主文件
    with open(uigf_file, "r", encoding="utf-8") as f:
        uigf = json.load(f)

    # item_id → item
    item_dict = {str(i["item_id"]): i for i in weapon_data}

    # 字段顺序
    field_order = [
        "uigf_gacha_type",
        "gacha_type",
        "item_id",
        "count",
        "time",
        "name",
        "item_type",
        "rank_type",
        "id"
    ]

    for uid_block in uigf["hk4e"]:

        # timezone 0 → 8
        if uid_block.get("timezone") == 0:
            uid_block["timezone"] = 8

        for record in uid_block["list"]:
            item_id = record.get("item_id")
            extra = item_dict.get(item_id, {})
            merged = {**extra, **record}

            # time 字段 +8 小时
            if "time" in merged:
                try:
                    dt = datetime.strptime(merged["time"], "%Y-%m-%d %H:%M:%S")
                    dt += timedelta(hours=8)
                    merged["time"] = dt.strftime("%Y-%m-%d %H:%M:%S")
                except:
                    pass

            # 字段排序
            sorted_record = {k: merged.get(k, None) for k in field_order}

            # 追加其他字段（可删除）
            for k, v in merged.items():
                if k not in field_order:
                    sorted_record[k] = v

            record.clear()
            record.update(sorted_record)

    # 输出最终 JSON
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(uigf, f, ensure_ascii=False, indent=4)

    print("处理完成！输出文件：", output_file)


if __name__ == "__main__":
    main()
