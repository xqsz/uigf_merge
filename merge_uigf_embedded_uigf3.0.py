import json
import sys
import os
from datetime import datetime, timedelta

def resource_path(relative_path):
    """PyInstaller 读取内部文件路径"""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(data, file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_hours(time_str, hours):
    try:
        dt = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
        dt += timedelta(hours=hours)
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except:
        return time_str

def main():
    # exe 内部资源路径
    b_path = resource_path("weapon_avatar.json")

    # 用户自行放置的抽卡历史文件
    a_path = "Snap Hutao UIGF.json"
    out_path = "uigf_merged_uigf3.0.json"

    # 加载 JSON
    A = load_json(a_path)
    B = load_json(b_path)

    weapon_map = {str(x["item_id"]): x for x in B}

    info = A.get("info", {})
    info["uid"] = A["hk4e"][0].get("uid")
    info["uigf_version"] = "v3.0"
    info["timezone"] = 8
    if "version" in info:
        del info["version"]

    gacha_list = A["hk4e"][0].get("list", [])

    new_list = []
    for item in gacha_list:
        item_id = str(item.get("item_id"))
        weapon_info = weapon_map.get(item_id, {})

        new_time = add_hours(item.get("time"), 8)

        merged = {
            "uigf_gacha_type": item.get("uigf_gacha_type"),
            "gacha_type": item.get("gacha_type"),
            "item_id": item.get("item_id"),
            "count": weapon_info.get("count"),
            "time": new_time,
            "name": weapon_info.get("name"),
            "item_type": weapon_info.get("item_type"),
            "rank_type": weapon_info.get("rank_type"),
            "id": item.get("id"),
        }

        new_list.append(merged)

    new_json = {
        "info": info,
        "list": new_list
    }

    save_json(new_json, out_path)
    print(f"合并完成 → {out_path}")


if __name__ == "__main__":
    main()