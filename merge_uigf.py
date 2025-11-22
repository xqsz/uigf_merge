import json
from datetime import datetime, timedelta

def main():
    uigf_file = "Snap Hutao UIGF.json"
    item_file = "weapon_avatar.json"
    output_file = "uigf_merged.json"

    # 读取主 JSON
    with open(uigf_file, "r", encoding="utf-8") as f:
        uigf = json.load(f)

    # 读取 item 信息
    with open(item_file, "r", encoding="utf-8") as f:
        items = json.load(f)

    # item_id → item 信息，统一转字符串
    item_dict = {str(i["item_id"]): i for i in items}

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

    # 遍历所有 uid 和记录
    for uid_block in uigf["hk4e"]:

        # -----------▼ 时区修改（0 → 8） ▼--------------
        if "timezone" in uid_block and uid_block["timezone"] == 0:
            uid_block["timezone"] = 8
        # ------------------------------------------------

        for record in uid_block["list"]:
            item_id = record.get("item_id")
            extra = item_dict.get(item_id, {})

            # 合并主文件字段优先
            merged = {**extra, **record}

            # -----------▼ time 字段 +8 小时 ▼--------------
            if "time" in merged:
                try:
                    dt = datetime.strptime(merged["time"], "%Y-%m-%d %H:%M:%S")
                    dt += timedelta(hours=8)
                    merged["time"] = dt.strftime("%Y-%m-%d %H:%M:%S")
                except Exception:
                    pass  # 如果格式异常则跳过
            # ------------------------------------------------

            # -----------▼ 字段排序 ▼--------------
            sorted_record = {k: merged.get(k, None) for k in field_order}

            # 追加剩余字段（如果不需要可删掉）
            for k, v in merged.items():
                if k not in field_order:
                    sorted_record[k] = v

            record.clear()
            record.update(sorted_record)
            # ---------------------------------------

    # 输出文件
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(uigf, f, ensure_ascii=False, indent=4)

    print(f"处理完成！输出文件：{output_file}")


if __name__ == "__main__":
    main()