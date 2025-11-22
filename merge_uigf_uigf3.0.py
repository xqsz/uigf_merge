import json
from datetime import datetime, timedelta

def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(data, file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_hours(time_str, hours):
    """将时间字符串 +hours 小时"""
    try:
        dt = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
        dt += timedelta(hours=hours)
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except:
        return time_str  # 若格式异常，不修改

def main():
    a_path = "Snap Hutao UIGF.json"
    b_path = "weapon_avatar.json"
    out_path = "uigf_merged_uigf3.0.json"

    # 加载 JSON
    A = load_json(a_path)
    B = load_json(b_path)

    # weapon_avatar 建索引
    weapon_map = {str(x["item_id"]): x for x in B}

    # --- 修改 info ---
    info = A.get("info", {})
    info["uid"] = A["hk4e"][0].get("uid")
    info["uigf_version"] = "v3.0"
    info["timezone"] = 8   # 新增要求：0 → 8

    if "version" in info:
        del info["version"]

    # --- 获取抽卡记录 ---
    gacha_list = A["hk4e"][0].get("list", [])

    new_list = []
    for item in gacha_list:
        item_id = str(item.get("item_id"))
        weapon_info = weapon_map.get(item_id, {})

        # time +8 小时
        new_time = add_hours(item.get("time"), 8)

        merged = {
            "uigf_gacha_type": item.get("uigf_gacha_type"),
            "gacha_type": item.get("gacha_type"),
            "item_id": item.get("item_id"),
            "count": weapon_info.get("count"),
            "time": new_time,                       # 已修改时间
            "name": weapon_info.get("name"),
            "item_type": weapon_info.get("item_type"),
            "rank_type": weapon_info.get("rank_type"),
            "id": item.get("id"),
        }

        new_list.append(merged)

    # --- 最终输出 ---
    new_json = {
        "info": info,
        "list": new_list
    }

    save_json(new_json, out_path)
    print(f"合并完成 → {out_path}")


if __name__ == "__main__":
    main()