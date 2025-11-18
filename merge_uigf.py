import json

def main():
    # 输入文件名
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

    # 遍历所有记录
    for uid_block in uigf["hk4e"]:
        for record in uid_block["list"]:
            item_id = record.get("item_id")
            extra = item_dict.get(item_id, {})

            # 合并但保持主文件字段优先
            merged = {**extra, **record}

            # 按指定字段顺序重建
            sorted_record = {k: merged.get(k, None) for k in field_order}

            # 把剩余字段追加（如果你不需要可以删掉）
            for k, v in merged.items():
                if k not in field_order:
                    sorted_record[k] = v

            # 覆盖原记录
            record.clear()
            record.update(sorted_record)

    # 输出文件
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(uigf, f, ensure_ascii=False, indent=4)

    print(f"处理完成！输出文件：{output_file}")


if __name__ == "__main__":
    main()
