import sqlite3
import json
import os
import time
import sys
import tempfile
import shutil

DB_NAME = "Userdata.db"


# ============================================================
# 资源释放（用于 EXE 内置 JSON 运行）
# ============================================================

def resource_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)
    return filename

def extract_weapon_avatar():
    src = resource_path("weapon_avatar.json")
    temp_dir = tempfile.gettempdir()
    dst = os.path.join(temp_dir, "weapon_avatar.json") 
    if not os.path.exists(dst):
        shutil.copy(src, dst)
    return dst

def load_weapon_avatar():
    with open(extract_weapon_avatar(),"r",encoding="utf-8") as f:
        data=json.load(f)
    return {str(i["item_id"]):i for i in data}


# ============================================================
# UIGF v3.0 导出
# ============================================================

def clean_time(t:str):
    """ 去除 +08:00 时区并兼容 T 格式 """
    return t.replace("+08:00","").replace("T"," ")

def export_uigf_v3(uid,records,avatar):
    out=[]
    for gacha_type,rec_id,item_id,query_type,t in records:
        t = clean_time(t)  #  ← ★ 重要修改

        info=avatar.get(str(item_id),{})
        out.append({
            "gacha_type":str(gacha_type),
            "id":str(rec_id),
            "item_id":str(item_id),
            "uigf_gacha_type":str(query_type),
            "time":t,
            "name":info.get("name",""),
            "rank_type":str(info.get("rank_type","")),
            "item_type":info.get("item_type",""),
            "count":str(info.get("count","1")),
        })

    data={
        "info":{
            "uid":str(uid),
            "uigf_version":"v3.0",
            "export_timestamp":int(time.time()),
            "export_app":"Userdata-Extractor",
            "export_app_version":"1.0",
        },
        "list":out
    }

    file=f"uigf_{uid}_v3.0.json"
    json.dump(data,open(file,"w",encoding="utf-8"),ensure_ascii=False,indent=4)
    print(f"✔ 导出完成 → {file}")


# ============================================================
# UIGF v4.1 导出
# ============================================================

def export_uigf_v4(uid,records,avatar):
    list_out=[]
    for gacha_type,rec_id,item_id,query_type,t in records:
        t = clean_time(t)  #  ← ★ 已同步处理

        info=avatar.get(str(item_id),{})
        list_out.append({
            "uigf_gacha_type":str(query_type),
            "gacha_type":str(gacha_type),
            "item_id":str(item_id),
            "count":str(info.get("count","1")),
            "time":t,
            "id":str(rec_id),
            "name":info.get("name",""),
            "item_type":info.get("item_type",""),
            "rank_type":str(info.get("rank_type","")),
        })

    data={
        "info":{
            "export_timestamp":int(time.time()),
            "export_app":"Userdata-Extractor",
            "export_app_version":"1.0",
            "version":"v4.1"
        },
        "hk4e":[
            {"uid":str(uid),"timezone":8,"lang":"zh-cn","list":list_out}
        ]
    }

    file=f"uigf_{uid}_v4.1.json"
    json.dump(data,open(file,"w",encoding="utf-8"),ensure_ascii=False,indent=4)
    print(f"✔ 导出完成 → {file}")


# ============================================================
# 主循环结构 — 仍支持 q 退出
# ============================================================

def main():
    avatar=load_weapon_avatar()

    while True:
        conn=sqlite3.connect(DB_NAME)
        cursor=conn.cursor()
        cursor.execute("SELECT Uid,InnerId FROM gacha_archives ORDER BY Uid ASC")
        accounts=cursor.fetchall()
        conn.close()

        print("\n=== 可导出 UID ===")
        for i,(u,_) in enumerate(accounts):
            print(f"[{i+1}] UID {u}")

        uid_input=input("\n输入序号导出，输入 q 退出：")
        if uid_input.lower()=="q": return print("\n👋 程序已退出")

        if not uid_input.isdigit(): continue
        idx=int(uid_input)-1
        uid,inner_id=accounts[idx]

        conn=sqlite3.connect(DB_NAME)
        cursor=conn.cursor()
        cursor.execute("""
            SELECT GachaType,Id,ItemId,QueryType,Time
            FROM gacha_items WHERE ArchiveId=? ORDER BY Time ASC
        """,(inner_id,))
        records=cursor.fetchall()
        conn.close()

        print("\n选择导出格式：")
        print("1 = UIGF v4.1（新）")
        print("2 = UIGF v3.0（旧）")
        f=input("输入：")

        export_uigf_v4(uid,records,avatar) if f=="1" else export_uigf_v3(uid,records,avatar)
        print("\n继续导出或输入 q 退出\n")


if __name__=="__main__":
    main()
