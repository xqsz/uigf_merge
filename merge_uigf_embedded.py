import json

# Embedded weapon_avatar.json content
weapon_avatar_json = [
  {
    "item_id": 11101,
    "item_type": "武器",
    "rank_type": 1,
    "name": "无锋剑",
    "count": 1
  },
  {
    "item_id": 11201,
    "item_type": "武器",
    "rank_type": 2,
    "name": "银剑",
    "count": 1
  },
  {
    "item_id": 11301,
    "item_type": "武器",
    "rank_type": 3,
    "name": "冷刃",
    "count": 1
  },
  {
    "item_id": 11302,
    "item_type": "武器",
    "rank_type": 3,
    "name": "黎明神剑",
    "count": 1
  },
  {
    "item_id": 11303,
    "item_type": "武器",
    "rank_type": 3,
    "name": "旅行剑",
    "count": 1
  },
  {
    "item_id": 11304,
    "item_type": "武器",
    "rank_type": 3,
    "name": "暗铁剑",
    "count": 1
  },
  {
    "item_id": 11305,
    "item_type": "武器",
    "rank_type": 3,
    "name": "吃虎鱼刀",
    "count": 1
  },
  {
    "item_id": 11306,
    "item_type": "武器",
    "rank_type": 3,
    "name": "飞天御剑",
    "count": 1
  },
  {
    "item_id": 11401,
    "item_type": "武器",
    "rank_type": 4,
    "name": "西风剑",
    "count": 1
  },
  {
    "item_id": 11402,
    "item_type": "武器",
    "rank_type": 4,
    "name": "笛剑",
    "count": 1
  },
  {
    "item_id": 11403,
    "item_type": "武器",
    "rank_type": 4,
    "name": "祭礼剑",
    "count": 1
  },
  {
    "item_id": 11404,
    "item_type": "武器",
    "rank_type": 4,
    "name": "宗室长剑",
    "count": 1
  },
  {
    "item_id": 11405,
    "item_type": "武器",
    "rank_type": 4,
    "name": "匣里龙吟",
    "count": 1
  },
  {
    "item_id": 11406,
    "item_type": "武器",
    "rank_type": 4,
    "name": "试作斩岩",
    "count": 1
  },
  {
    "item_id": 11407,
    "item_type": "武器",
    "rank_type": 4,
    "name": "铁蜂刺",
    "count": 1
  },
  {
    "item_id": 11408,
    "item_type": "武器",
    "rank_type": 4,
    "name": "黑岩长剑",
    "count": 1
  },
  {
    "item_id": 11409,
    "item_type": "武器",
    "rank_type": 4,
    "name": "黑剑",
    "count": 1
  },
  {
    "item_id": 11410,
    "item_type": "武器",
    "rank_type": 4,
    "name": "暗巷闪光",
    "count": 1
  },
  {
    "item_id": 11412,
    "item_type": "武器",
    "rank_type": 4,
    "name": "降临之剑",
    "count": 1
  },
  {
    "item_id": 11413,
    "item_type": "武器",
    "rank_type": 4,
    "name": "腐殖之剑",
    "count": 1
  },
  {
    "item_id": 11414,
    "item_type": "武器",
    "rank_type": 4,
    "name": "天目影打刀",
    "count": 1
  },
  {
    "item_id": 11415,
    "item_type": "武器",
    "rank_type": 4,
    "name": "辰砂之纺锤",
    "count": 1
  },
  {
    "item_id": 11416,
    "item_type": "武器",
    "rank_type": 4,
    "name": "笼钓瓶一心",
    "count": 1
  },
  {
    "item_id": 11417,
    "item_type": "武器",
    "rank_type": 4,
    "name": "原木刀",
    "count": 1
  },
  {
    "item_id": 11418,
    "item_type": "武器",
    "rank_type": 4,
    "name": "西福斯的月光",
    "count": 1
  },
  {
    "item_id": 11422,
    "item_type": "武器",
    "rank_type": 4,
    "name": "东花坊时雨",
    "count": 1
  },
  {
    "item_id": 11424,
    "item_type": "武器",
    "rank_type": 4,
    "name": "狼牙",
    "count": 1
  },
  {
    "item_id": 11425,
    "item_type": "武器",
    "rank_type": 4,
    "name": "海渊终曲",
    "count": 1
  },
  {
    "item_id": 11426,
    "item_type": "武器",
    "rank_type": 4,
    "name": "灰河渡手",
    "count": 1
  },
  {
    "item_id": 11427,
    "item_type": "武器",
    "rank_type": 4,
    "name": "船坞长剑",
    "count": 1
  },
  {
    "item_id": 11428,
    "item_type": "武器",
    "rank_type": 4,
    "name": "水仙十字之剑",
    "count": 1
  },
  {
    "item_id": 11430,
    "item_type": "武器",
    "rank_type": 4,
    "name": "弥坚骨",
    "count": 1
  },
  {
    "item_id": 11431,
    "item_type": "武器",
    "rank_type": 4,
    "name": "息燧之笛",
    "count": 1
  },
  {
    "item_id": 11432,
    "item_type": "武器",
    "rank_type": 4,
    "name": "厄水之祸",
    "count": 1
  },
  {
    "item_id": 11433,
    "item_type": "武器",
    "rank_type": 4,
    "name": "谧音吹哨",
    "count": 1
  },
  {
    "item_id": 11434,
    "item_type": "武器",
    "rank_type": 4,
    "name": "织月者的曙色",
    "count": 1
  },
  {
    "item_id": 11501,
    "item_type": "武器",
    "rank_type": 5,
    "name": "风鹰剑",
    "count": 1
  },
  {
    "item_id": 11502,
    "item_type": "武器",
    "rank_type": 5,
    "name": "天空之刃",
    "count": 1
  },
  {
    "item_id": 11503,
    "item_type": "武器",
    "rank_type": 5,
    "name": "苍古自由之誓",
    "count": 1
  },
  {
    "item_id": 11504,
    "item_type": "武器",
    "rank_type": 5,
    "name": "斫峰之刃",
    "count": 1
  },
  {
    "item_id": 11505,
    "item_type": "武器",
    "rank_type": 5,
    "name": "磐岩结绿",
    "count": 1
  },
  {
    "item_id": 11509,
    "item_type": "武器",
    "rank_type": 5,
    "name": "雾切之回光",
    "count": 1
  },
  {
    "item_id": 11510,
    "item_type": "武器",
    "rank_type": 5,
    "name": "波乱月白经津",
    "count": 1
  },
  {
    "item_id": 11511,
    "item_type": "武器",
    "rank_type": 5,
    "name": "圣显之钥",
    "count": 1
  },
  {
    "item_id": 11512,
    "item_type": "武器",
    "rank_type": 5,
    "name": "裁叶萃光",
    "count": 1
  },
  {
    "item_id": 11513,
    "item_type": "武器",
    "rank_type": 5,
    "name": "静水流涌之辉",
    "count": 1
  },
  {
    "item_id": 11514,
    "item_type": "武器",
    "rank_type": 5,
    "name": "有乐御簾切",
    "count": 1
  },
  {
    "item_id": 11515,
    "item_type": "武器",
    "rank_type": 5,
    "name": "赦罪",
    "count": 1
  },
  {
    "item_id": 11516,
    "item_type": "武器",
    "rank_type": 5,
    "name": "岩峰巡歌",
    "count": 1
  },
  {
    "item_id": 11517,
    "item_type": "武器",
    "rank_type": 5,
    "name": "苍耀",
    "count": 1
  },
  {
    "item_id": 12101,
    "item_type": "武器",
    "rank_type": 1,
    "name": "训练大剑",
    "count": 1
  },
  {
    "item_id": 12201,
    "item_type": "武器",
    "rank_type": 2,
    "name": "佣兵重剑",
    "count": 1
  },
  {
    "item_id": 12301,
    "item_type": "武器",
    "rank_type": 3,
    "name": "铁影阔剑",
    "count": 1
  },
  {
    "item_id": 12302,
    "item_type": "武器",
    "rank_type": 3,
    "name": "沐浴龙血的剑",
    "count": 1
  },
  {
    "item_id": 12303,
    "item_type": "武器",
    "rank_type": 3,
    "name": "白铁大剑",
    "count": 1
  },
  {
    "item_id": 12305,
    "item_type": "武器",
    "rank_type": 3,
    "name": "以理服人",
    "count": 1
  },
  {
    "item_id": 12306,
    "item_type": "武器",
    "rank_type": 3,
    "name": "飞天大御剑",
    "count": 1
  },
  {
    "item_id": 12401,
    "item_type": "武器",
    "rank_type": 4,
    "name": "西风大剑",
    "count": 1
  },
  {
    "item_id": 12402,
    "item_type": "武器",
    "rank_type": 4,
    "name": "钟剑",
    "count": 1
  },
  {
    "item_id": 12403,
    "item_type": "武器",
    "rank_type": 4,
    "name": "祭礼大剑",
    "count": 1
  },
  {
    "item_id": 12404,
    "item_type": "武器",
    "rank_type": 4,
    "name": "宗室大剑",
    "count": 1
  },
  {
    "item_id": 12405,
    "item_type": "武器",
    "rank_type": 4,
    "name": "雨裁",
    "count": 1
  },
  {
    "item_id": 12406,
    "item_type": "武器",
    "rank_type": 4,
    "name": "试作古华",
    "count": 1
  },
  {
    "item_id": 12407,
    "item_type": "武器",
    "rank_type": 4,
    "name": "白影剑",
    "count": 1
  },
  {
    "item_id": 12408,
    "item_type": "武器",
    "rank_type": 4,
    "name": "黑岩斩刀",
    "count": 1
  },
  {
    "item_id": 12409,
    "item_type": "武器",
    "rank_type": 4,
    "name": "螭骨剑",
    "count": 1
  },
  {
    "item_id": 12410,
    "item_type": "武器",
    "rank_type": 4,
    "name": "千岩古剑",
    "count": 1
  },
  {
    "item_id": 12411,
    "item_type": "武器",
    "rank_type": 4,
    "name": "雪葬的星银",
    "count": 1
  },
  {
    "item_id": 12412,
    "item_type": "武器",
    "rank_type": 4,
    "name": "衔珠海皇",
    "count": 1
  },
  {
    "item_id": 12414,
    "item_type": "武器",
    "rank_type": 4,
    "name": "桂木斩长正",
    "count": 1
  },
  {
    "item_id": 12415,
    "item_type": "武器",
    "rank_type": 4,
    "name": "玛海菈的水色",
    "count": 1
  },
  {
    "item_id": 12416,
    "item_type": "武器",
    "rank_type": 4,
    "name": "恶王丸",
    "count": 1
  },
  {
    "item_id": 12417,
    "item_type": "武器",
    "rank_type": 4,
    "name": "森林王器",
    "count": 1
  },
  {
    "item_id": 12418,
    "item_type": "武器",
    "rank_type": 4,
    "name": "饰铁之花",
    "count": 1
  },
  {
    "item_id": 12424,
    "item_type": "武器",
    "rank_type": 4,
    "name": "聊聊棒",
    "count": 1
  },
  {
    "item_id": 12425,
    "item_type": "武器",
    "rank_type": 4,
    "name": "浪影阔剑",
    "count": 1
  },
  {
    "item_id": 12426,
    "item_type": "武器",
    "rank_type": 4,
    "name": "「究极霸王超级魔剑」",
    "count": 1
  },
  {
    "item_id": 12427,
    "item_type": "武器",
    "rank_type": 4,
    "name": "便携动力锯",
    "count": 1
  },
  {
    "item_id": 12430,
    "item_type": "武器",
    "rank_type": 4,
    "name": "硕果钩",
    "count": 1
  },
  {
    "item_id": 12431,
    "item_type": "武器",
    "rank_type": 4,
    "name": "撼地者",
    "count": 1
  },
  {
    "item_id": 12432,
    "item_type": "武器",
    "rank_type": 4,
    "name": "拾慧铸熔",
    "count": 1
  },
  {
    "item_id": 12433,
    "item_type": "武器",
    "rank_type": 4,
    "name": "万能钥匙",
    "count": 1
  },
  {
    "item_id": 12501,
    "item_type": "武器",
    "rank_type": 5,
    "name": "天空之傲",
    "count": 1
  },
  {
    "item_id": 12502,
    "item_type": "武器",
    "rank_type": 5,
    "name": "狼的末路",
    "count": 1
  },
  {
    "item_id": 12503,
    "item_type": "武器",
    "rank_type": 5,
    "name": "松籁响起之时",
    "count": 1
  },
  {
    "item_id": 12504,
    "item_type": "武器",
    "rank_type": 5,
    "name": "无工之剑",
    "count": 1
  },
  {
    "item_id": 12510,
    "item_type": "武器",
    "rank_type": 5,
    "name": "赤角石溃杵",
    "count": 1
  },
  {
    "item_id": 12511,
    "item_type": "武器",
    "rank_type": 5,
    "name": "苇海信标",
    "count": 1
  },
  {
    "item_id": 12512,
    "item_type": "武器",
    "rank_type": 5,
    "name": "裁断",
    "count": 1
  },
  {
    "item_id": 12513,
    "item_type": "武器",
    "rank_type": 5,
    "name": "山王长牙",
    "count": 1
  },
  {
    "item_id": 12514,
    "item_type": "武器",
    "rank_type": 5,
    "name": "焚曜千阳",
    "count": 1
  },
  {
    "item_id": 13101,
    "item_type": "武器",
    "rank_type": 1,
    "name": "新手长枪",
    "count": 1
  },
  {
    "item_id": 13201,
    "item_type": "武器",
    "rank_type": 2,
    "name": "铁尖枪",
    "count": 1
  },
  {
    "item_id": 13301,
    "item_type": "武器",
    "rank_type": 3,
    "name": "白缨枪",
    "count": 1
  },
  {
    "item_id": 13302,
    "item_type": "武器",
    "rank_type": 3,
    "name": "钺矛",
    "count": 1
  },
  {
    "item_id": 13303,
    "item_type": "武器",
    "rank_type": 3,
    "name": "黑缨枪",
    "count": 1
  },
  {
    "item_id": 13401,
    "item_type": "武器",
    "rank_type": 4,
    "name": "匣里灭辰",
    "count": 1
  },
  {
    "item_id": 13402,
    "item_type": "武器",
    "rank_type": 4,
    "name": "试作星镰",
    "count": 1
  },
  {
    "item_id": 13403,
    "item_type": "武器",
    "rank_type": 4,
    "name": "流月针",
    "count": 1
  },
  {
    "item_id": 13404,
    "item_type": "武器",
    "rank_type": 4,
    "name": "黑岩刺枪",
    "count": 1
  },
  {
    "item_id": 13405,
    "item_type": "武器",
    "rank_type": 4,
    "name": "决斗之枪",
    "count": 1
  },
  {
    "item_id": 13406,
    "item_type": "武器",
    "rank_type": 4,
    "name": "千岩长枪",
    "count": 1
  },
  {
    "item_id": 13407,
    "item_type": "武器",
    "rank_type": 4,
    "name": "西风长枪",
    "count": 1
  },
  {
    "item_id": 13408,
    "item_type": "武器",
    "rank_type": 4,
    "name": "宗室猎枪",
    "count": 1
  },
  {
    "item_id": 13409,
    "item_type": "武器",
    "rank_type": 4,
    "name": "龙脊长枪",
    "count": 1
  },
  {
    "item_id": 13414,
    "item_type": "武器",
    "rank_type": 4,
    "name": "喜多院十文字",
    "count": 1
  },
  {
    "item_id": 13415,
    "item_type": "武器",
    "rank_type": 4,
    "name": "「渔获」",
    "count": 1
  },
  {
    "item_id": 13416,
    "item_type": "武器",
    "rank_type": 4,
    "name": "断浪长鳍",
    "count": 1
  },
  {
    "item_id": 13417,
    "item_type": "武器",
    "rank_type": 4,
    "name": "贯月矢",
    "count": 1
  },
  {
    "item_id": 13419,
    "item_type": "武器",
    "rank_type": 4,
    "name": "风信之锋",
    "count": 1
  },
  {
    "item_id": 13424,
    "item_type": "武器",
    "rank_type": 4,
    "name": "峡湾长歌",
    "count": 1
  },
  {
    "item_id": 13425,
    "item_type": "武器",
    "rank_type": 4,
    "name": "公义的酬报",
    "count": 1
  },
  {
    "item_id": 13426,
    "item_type": "武器",
    "rank_type": 4,
    "name": "沙中伟贤的对答",
    "count": 1
  },
  {
    "item_id": 13427,
    "item_type": "武器",
    "rank_type": 4,
    "name": "勘探钻机",
    "count": 1
  },
  {
    "item_id": 13430,
    "item_type": "武器",
    "rank_type": 4,
    "name": "镇山之钉",
    "count": 1
  },
  {
    "item_id": 13431,
    "item_type": "武器",
    "rank_type": 4,
    "name": "虹的行迹",
    "count": 1
  },
  {
    "item_id": 13432,
    "item_type": "武器",
    "rank_type": 4,
    "name": "且住亭御咄",
    "count": 1
  },
  {
    "item_id": 13433,
    "item_type": "武器",
    "rank_type": 4,
    "name": "掘金之锹",
    "count": 1
  },
  {
    "item_id": 13434,
    "item_type": "武器",
    "rank_type": 4,
    "name": "圣祭者的辉杖",
    "count": 1
  },
  {
    "item_id": 13501,
    "item_type": "武器",
    "rank_type": 5,
    "name": "护摩之杖",
    "count": 1
  },
  {
    "item_id": 13502,
    "item_type": "武器",
    "rank_type": 5,
    "name": "天空之脊",
    "count": 1
  },
  {
    "item_id": 13504,
    "item_type": "武器",
    "rank_type": 5,
    "name": "贯虹之槊",
    "count": 1
  },
  {
    "item_id": 13505,
    "item_type": "武器",
    "rank_type": 5,
    "name": "和璞鸢",
    "count": 1
  },
  {
    "item_id": 13507,
    "item_type": "武器",
    "rank_type": 5,
    "name": "息灾",
    "count": 1
  },
  {
    "item_id": 13509,
    "item_type": "武器",
    "rank_type": 5,
    "name": "薙草之稻光",
    "count": 1
  },
  {
    "item_id": 13511,
    "item_type": "武器",
    "rank_type": 5,
    "name": "赤沙之杖",
    "count": 1
  },
  {
    "item_id": 13512,
    "item_type": "武器",
    "rank_type": 5,
    "name": "赤月之形",
    "count": 1
  },
  {
    "item_id": 13513,
    "item_type": "武器",
    "rank_type": 5,
    "name": "柔灯挽歌",
    "count": 1
  },
  {
    "item_id": 13514,
    "item_type": "武器",
    "rank_type": 5,
    "name": "香韵奏者",
    "count": 1
  },
  {
    "item_id": 13515,
    "item_type": "武器",
    "rank_type": 5,
    "name": "支离轮光",
    "count": 1
  },
  {
    "item_id": 13516,
    "item_type": "武器",
    "rank_type": 5,
    "name": "血染荒城",
    "count": 1
  },
  {
    "item_id": 14101,
    "item_type": "武器",
    "rank_type": 1,
    "name": "学徒笔记",
    "count": 1
  },
  {
    "item_id": 14201,
    "item_type": "武器",
    "rank_type": 2,
    "name": "口袋魔导书",
    "count": 1
  },
  {
    "item_id": 14301,
    "item_type": "武器",
    "rank_type": 3,
    "name": "魔导绪论",
    "count": 1
  },
  {
    "item_id": 14302,
    "item_type": "武器",
    "rank_type": 3,
    "name": "讨龙英杰谭",
    "count": 1
  },
  {
    "item_id": 14303,
    "item_type": "武器",
    "rank_type": 3,
    "name": "异世界行记",
    "count": 1
  },
  {
    "item_id": 14304,
    "item_type": "武器",
    "rank_type": 3,
    "name": "翡玉法球",
    "count": 1
  },
  {
    "item_id": 14305,
    "item_type": "武器",
    "rank_type": 3,
    "name": "甲级宝珏",
    "count": 1
  },
  {
    "item_id": 14401,
    "item_type": "武器",
    "rank_type": 4,
    "name": "西风秘典",
    "count": 1
  },
  {
    "item_id": 14402,
    "item_type": "武器",
    "rank_type": 4,
    "name": "流浪乐章",
    "count": 1
  },
  {
    "item_id": 14403,
    "item_type": "武器",
    "rank_type": 4,
    "name": "祭礼残章",
    "count": 1
  },
  {
    "item_id": 14404,
    "item_type": "武器",
    "rank_type": 4,
    "name": "宗室秘法录",
    "count": 1
  },
  {
    "item_id": 14405,
    "item_type": "武器",
    "rank_type": 4,
    "name": "匣里日月",
    "count": 1
  },
  {
    "item_id": 14406,
    "item_type": "武器",
    "rank_type": 4,
    "name": "试作金珀",
    "count": 1
  },
  {
    "item_id": 14407,
    "item_type": "武器",
    "rank_type": 4,
    "name": "万国诸海图谱",
    "count": 1
  },
  {
    "item_id": 14408,
    "item_type": "武器",
    "rank_type": 4,
    "name": "黑岩绯玉",
    "count": 1
  },
  {
    "item_id": 14409,
    "item_type": "武器",
    "rank_type": 4,
    "name": "昭心",
    "count": 1
  },
  {
    "item_id": 14410,
    "item_type": "武器",
    "rank_type": 4,
    "name": "暗巷的酒与诗",
    "count": 1
  },
  {
    "item_id": 14412,
    "item_type": "武器",
    "rank_type": 4,
    "name": "忍冬之果",
    "count": 1
  },
  {
    "item_id": 14413,
    "item_type": "武器",
    "rank_type": 4,
    "name": "嘟嘟可故事集",
    "count": 1
  },
  {
    "item_id": 14414,
    "item_type": "武器",
    "rank_type": 4,
    "name": "白辰之环",
    "count": 1
  },
  {
    "item_id": 14415,
    "item_type": "武器",
    "rank_type": 4,
    "name": "证誓之明瞳",
    "count": 1
  },
  {
    "item_id": 14416,
    "item_type": "武器",
    "rank_type": 4,
    "name": "流浪的晚星",
    "count": 1
  },
  {
    "item_id": 14417,
    "item_type": "武器",
    "rank_type": 4,
    "name": "盈满之实",
    "count": 1
  },
  {
    "item_id": 14424,
    "item_type": "武器",
    "rank_type": 4,
    "name": "遗祀玉珑",
    "count": 1
  },
  {
    "item_id": 14425,
    "item_type": "武器",
    "rank_type": 4,
    "name": "纯水流华",
    "count": 1
  },
  {
    "item_id": 14426,
    "item_type": "武器",
    "rank_type": 4,
    "name": "无垠蔚蓝之歌",
    "count": 1
  },
  {
    "item_id": 14427,
    "item_type": "武器",
    "rank_type": 4,
    "name": "苍纹角杯",
    "count": 1
  },
  {
    "item_id": 14430,
    "item_type": "武器",
    "rank_type": 4,
    "name": "乘浪的回旋",
    "count": 1
  },
  {
    "item_id": 14431,
    "item_type": "武器",
    "rank_type": 4,
    "name": "木棉之环",
    "count": 1
  },
  {
    "item_id": 14432,
    "item_type": "武器",
    "rank_type": 4,
    "name": "天光的纺琴",
    "count": 1
  },
  {
    "item_id": 14433,
    "item_type": "武器",
    "rank_type": 4,
    "name": "乌髓孑灯",
    "count": 1
  },
  {
    "item_id": 14434,
    "item_type": "武器",
    "rank_type": 4,
    "name": "霜辰",
    "count": 1
  },
  {
    "item_id": 14501,
    "item_type": "武器",
    "rank_type": 5,
    "name": "天空之卷",
    "count": 1
  },
  {
    "item_id": 14502,
    "item_type": "武器",
    "rank_type": 5,
    "name": "四风原典",
    "count": 1
  },
  {
    "item_id": 14504,
    "item_type": "武器",
    "rank_type": 5,
    "name": "尘世之锁",
    "count": 1
  },
  {
    "item_id": 14505,
    "item_type": "武器",
    "rank_type": 5,
    "name": "碧落之珑",
    "count": 1
  },
  {
    "item_id": 14506,
    "item_type": "武器",
    "rank_type": 5,
    "name": "不灭月华",
    "count": 1
  },
  {
    "item_id": 14509,
    "item_type": "武器",
    "rank_type": 5,
    "name": "神乐之真意",
    "count": 1
  },
  {
    "item_id": 14511,
    "item_type": "武器",
    "rank_type": 5,
    "name": "千夜浮梦",
    "count": 1
  },
  {
    "item_id": 14512,
    "item_type": "武器",
    "rank_type": 5,
    "name": "图莱杜拉的回忆",
    "count": 1
  },
  {
    "item_id": 14513,
    "item_type": "武器",
    "rank_type": 5,
    "name": "金流监督",
    "count": 1
  },
  {
    "item_id": 14514,
    "item_type": "武器",
    "rank_type": 5,
    "name": "万世流涌大典",
    "count": 1
  },
  {
    "item_id": 14515,
    "item_type": "武器",
    "rank_type": 5,
    "name": "鹤鸣余音",
    "count": 1
  },
  {
    "item_id": 14516,
    "item_type": "武器",
    "rank_type": 5,
    "name": "冲浪时光",
    "count": 1
  },
  {
    "item_id": 14517,
    "item_type": "武器",
    "rank_type": 5,
    "name": "祭星者之望",
    "count": 1
  },
  {
    "item_id": 14518,
    "item_type": "武器",
    "rank_type": 5,
    "name": "寝正月初晴",
    "count": 1
  },
  {
    "item_id": 14519,
    "item_type": "武器",
    "rank_type": 5,
    "name": "溢彩心念",
    "count": 1
  },
  {
    "item_id": 14520,
    "item_type": "武器",
    "rank_type": 5,
    "name": "纺夜天镜",
    "count": 1
  },
  {
    "item_id": 14521,
    "item_type": "武器",
    "rank_type": 5,
    "name": "真语秘匣",
    "count": 1
  },
  {
    "item_id": 15101,
    "item_type": "武器",
    "rank_type": 1,
    "name": "猎弓",
    "count": 1
  },
  {
    "item_id": 15201,
    "item_type": "武器",
    "rank_type": 2,
    "name": "历练的猎弓",
    "count": 1
  },
  {
    "item_id": 15301,
    "item_type": "武器",
    "rank_type": 3,
    "name": "鸦羽弓",
    "count": 1
  },
  {
    "item_id": 15302,
    "item_type": "武器",
    "rank_type": 3,
    "name": "神射手之誓",
    "count": 1
  },
  {
    "item_id": 15303,
    "item_type": "武器",
    "rank_type": 3,
    "name": "反曲弓",
    "count": 1
  },
  {
    "item_id": 15304,
    "item_type": "武器",
    "rank_type": 3,
    "name": "弹弓",
    "count": 1
  },
  {
    "item_id": 15305,
    "item_type": "武器",
    "rank_type": 3,
    "name": "信使",
    "count": 1
  },
  {
    "item_id": 15401,
    "item_type": "武器",
    "rank_type": 4,
    "name": "西风猎弓",
    "count": 1
  },
  {
    "item_id": 15402,
    "item_type": "武器",
    "rank_type": 4,
    "name": "绝弦",
    "count": 1
  },
  {
    "item_id": 15403,
    "item_type": "武器",
    "rank_type": 4,
    "name": "祭礼弓",
    "count": 1
  },
  {
    "item_id": 15404,
    "item_type": "武器",
    "rank_type": 4,
    "name": "宗室长弓",
    "count": 1
  },
  {
    "item_id": 15405,
    "item_type": "武器",
    "rank_type": 4,
    "name": "弓藏",
    "count": 1
  },
  {
    "item_id": 15406,
    "item_type": "武器",
    "rank_type": 4,
    "name": "试作澹月",
    "count": 1
  },
  {
    "item_id": 15407,
    "item_type": "武器",
    "rank_type": 4,
    "name": "钢轮弓",
    "count": 1
  },
  {
    "item_id": 15408,
    "item_type": "武器",
    "rank_type": 4,
    "name": "黑岩战弓",
    "count": 1
  },
  {
    "item_id": 15409,
    "item_type": "武器",
    "rank_type": 4,
    "name": "苍翠猎弓",
    "count": 1
  },
  {
    "item_id": 15410,
    "item_type": "武器",
    "rank_type": 4,
    "name": "暗巷猎手",
    "count": 1
  },
  {
    "item_id": 15411,
    "item_type": "武器",
    "rank_type": 4,
    "name": "落霞",
    "count": 1
  },
  {
    "item_id": 15412,
    "item_type": "武器",
    "rank_type": 4,
    "name": "幽夜华尔兹",
    "count": 1
  },
  {
    "item_id": 15413,
    "item_type": "武器",
    "rank_type": 4,
    "name": "风花之颂",
    "count": 1
  },
  {
    "item_id": 15414,
    "item_type": "武器",
    "rank_type": 4,
    "name": "破魔之弓",
    "count": 1
  },
  {
    "item_id": 15415,
    "item_type": "武器",
    "rank_type": 4,
    "name": "掠食者",
    "count": 1
  },
  {
    "item_id": 15416,
    "item_type": "武器",
    "rank_type": 4,
    "name": "曚云之月",
    "count": 1
  },
  {
    "item_id": 15417,
    "item_type": "武器",
    "rank_type": 4,
    "name": "王下近侍",
    "count": 1
  },
  {
    "item_id": 15418,
    "item_type": "武器",
    "rank_type": 4,
    "name": "竭泽",
    "count": 1
  },
  {
    "item_id": 15419,
    "item_type": "武器",
    "rank_type": 4,
    "name": "鹮穿之喙",
    "count": 1
  },
  {
    "item_id": 15424,
    "item_type": "武器",
    "rank_type": 4,
    "name": "烈阳之嗣",
    "count": 1
  },
  {
    "item_id": 15425,
    "item_type": "武器",
    "rank_type": 4,
    "name": "静谧之曲",
    "count": 1
  },
  {
    "item_id": 15426,
    "item_type": "武器",
    "rank_type": 4,
    "name": "筑云",
    "count": 1
  },
  {
    "item_id": 15427,
    "item_type": "武器",
    "rank_type": 4,
    "name": "测距规",
    "count": 1
  },
  {
    "item_id": 15430,
    "item_type": "武器",
    "rank_type": 4,
    "name": "缀花之翎",
    "count": 1
  },
  {
    "item_id": 15431,
    "item_type": "武器",
    "rank_type": 4,
    "name": "碎链",
    "count": 1
  },
  {
    "item_id": 15432,
    "item_type": "武器",
    "rank_type": 4,
    "name": "冷寂迸音",
    "count": 1
  },
  {
    "item_id": 15433,
    "item_type": "武器",
    "rank_type": 4,
    "name": "罗网勾针",
    "count": 1
  },
  {
    "item_id": 15501,
    "item_type": "武器",
    "rank_type": 5,
    "name": "天空之翼",
    "count": 1
  },
  {
    "item_id": 15502,
    "item_type": "武器",
    "rank_type": 5,
    "name": "阿莫斯之弓",
    "count": 1
  },
  {
    "item_id": 15503,
    "item_type": "武器",
    "rank_type": 5,
    "name": "终末嗟叹之诗",
    "count": 1
  },
  {
    "item_id": 15507,
    "item_type": "武器",
    "rank_type": 5,
    "name": "冬极白星",
    "count": 1
  },
  {
    "item_id": 15508,
    "item_type": "武器",
    "rank_type": 5,
    "name": "若水",
    "count": 1
  },
  {
    "item_id": 15509,
    "item_type": "武器",
    "rank_type": 5,
    "name": "飞雷之弦振",
    "count": 1
  },
  {
    "item_id": 15511,
    "item_type": "武器",
    "rank_type": 5,
    "name": "猎人之径",
    "count": 1
  },
  {
    "item_id": 15512,
    "item_type": "武器",
    "rank_type": 5,
    "name": "最初的大魔术",
    "count": 1
  },
  {
    "item_id": 15513,
    "item_type": "武器",
    "rank_type": 5,
    "name": "白雨心弦",
    "count": 1
  },
  {
    "item_id": 15514,
    "item_type": "武器",
    "rank_type": 5,
    "name": "星鹫赤羽",
    "count": 1
  },
  {
    "item_id": 10000002,
    "item_type": "角色",
    "rank_type": 5,
    "name": "神里绫华",
    "count": 1
  },
  {
    "item_id": 10000003,
    "item_type": "角色",
    "rank_type": 5,
    "name": "琴",
    "count": 1
  },
  {
    "item_id": 10000006,
    "item_type": "角色",
    "rank_type": 4,
    "name": "丽莎",
    "count": 1
  },
  {
    "item_id": 10000014,
    "item_type": "角色",
    "rank_type": 4,
    "name": "芭芭拉",
    "count": 1
  },
  {
    "item_id": 10000015,
    "item_type": "角色",
    "rank_type": 4,
    "name": "凯亚",
    "count": 1
  },
  {
    "item_id": 10000016,
    "item_type": "角色",
    "rank_type": 5,
    "name": "迪卢克",
    "count": 1
  },
  {
    "item_id": 10000020,
    "item_type": "角色",
    "rank_type": 4,
    "name": "雷泽",
    "count": 1
  },
  {
    "item_id": 10000021,
    "item_type": "角色",
    "rank_type": 4,
    "name": "安柏",
    "count": 1
  },
  {
    "item_id": 10000022,
    "item_type": "角色",
    "rank_type": 5,
    "name": "温迪",
    "count": 1
  },
  {
    "item_id": 10000023,
    "item_type": "角色",
    "rank_type": 4,
    "name": "香菱",
    "count": 1
  },
  {
    "item_id": 10000024,
    "item_type": "角色",
    "rank_type": 4,
    "name": "北斗",
    "count": 1
  },
  {
    "item_id": 10000025,
    "item_type": "角色",
    "rank_type": 4,
    "name": "行秋",
    "count": 1
  },
  {
    "item_id": 10000026,
    "item_type": "角色",
    "rank_type": 5,
    "name": "魈",
    "count": 1
  },
  {
    "item_id": 10000027,
    "item_type": "角色",
    "rank_type": 4,
    "name": "凝光",
    "count": 1
  },
  {
    "item_id": 10000029,
    "item_type": "角色",
    "rank_type": 5,
    "name": "可莉",
    "count": 1
  },
  {
    "item_id": 10000030,
    "item_type": "角色",
    "rank_type": 5,
    "name": "钟离",
    "count": 1
  },
  {
    "item_id": 10000031,
    "item_type": "角色",
    "rank_type": 4,
    "name": "菲谢尔",
    "count": 1
  },
  {
    "item_id": 10000032,
    "item_type": "角色",
    "rank_type": 4,
    "name": "班尼特",
    "count": 1
  },
  {
    "item_id": 10000033,
    "item_type": "角色",
    "rank_type": 5,
    "name": "达达利亚",
    "count": 1
  },
  {
    "item_id": 10000034,
    "item_type": "角色",
    "rank_type": 4,
    "name": "诺艾尔",
    "count": 1
  },
  {
    "item_id": 10000035,
    "item_type": "角色",
    "rank_type": 5,
    "name": "七七",
    "count": 1
  },
  {
    "item_id": 10000036,
    "item_type": "角色",
    "rank_type": 4,
    "name": "重云",
    "count": 1
  },
  {
    "item_id": 10000037,
    "item_type": "角色",
    "rank_type": 5,
    "name": "甘雨",
    "count": 1
  },
  {
    "item_id": 10000038,
    "item_type": "角色",
    "rank_type": 5,
    "name": "阿贝多",
    "count": 1
  },
  {
    "item_id": 10000039,
    "item_type": "角色",
    "rank_type": 4,
    "name": "迪奥娜",
    "count": 1
  },
  {
    "item_id": 10000041,
    "item_type": "角色",
    "rank_type": 5,
    "name": "莫娜",
    "count": 1
  },
  {
    "item_id": 10000042,
    "item_type": "角色",
    "rank_type": 5,
    "name": "刻晴",
    "count": 1
  },
  {
    "item_id": 10000043,
    "item_type": "角色",
    "rank_type": 4,
    "name": "砂糖",
    "count": 1
  },
  {
    "item_id": 10000044,
    "item_type": "角色",
    "rank_type": 4,
    "name": "辛焱",
    "count": 1
  },
  {
    "item_id": 10000045,
    "item_type": "角色",
    "rank_type": 4,
    "name": "罗莎莉亚",
    "count": 1
  },
  {
    "item_id": 10000046,
    "item_type": "角色",
    "rank_type": 5,
    "name": "胡桃",
    "count": 1
  },
  {
    "item_id": 10000047,
    "item_type": "角色",
    "rank_type": 5,
    "name": "枫原万叶",
    "count": 1
  },
  {
    "item_id": 10000048,
    "item_type": "角色",
    "rank_type": 4,
    "name": "烟绯",
    "count": 1
  },
  {
    "item_id": 10000049,
    "item_type": "角色",
    "rank_type": 5,
    "name": "宵宫",
    "count": 1
  },
  {
    "item_id": 10000050,
    "item_type": "角色",
    "rank_type": 4,
    "name": "托马",
    "count": 1
  },
  {
    "item_id": 10000051,
    "item_type": "角色",
    "rank_type": 5,
    "name": "优菈",
    "count": 1
  },
  {
    "item_id": 10000052,
    "item_type": "角色",
    "rank_type": 5,
    "name": "雷电将军",
    "count": 1
  },
  {
    "item_id": 10000053,
    "item_type": "角色",
    "rank_type": 4,
    "name": "早柚",
    "count": 1
  },
  {
    "item_id": 10000054,
    "item_type": "角色",
    "rank_type": 5,
    "name": "珊瑚宫心海",
    "count": 1
  },
  {
    "item_id": 10000055,
    "item_type": "角色",
    "rank_type": 4,
    "name": "五郎",
    "count": 1
  },
  {
    "item_id": 10000056,
    "item_type": "角色",
    "rank_type": 4,
    "name": "九条裟罗",
    "count": 1
  },
  {
    "item_id": 10000057,
    "item_type": "角色",
    "rank_type": 5,
    "name": "荒泷一斗",
    "count": 1
  },
  {
    "item_id": 10000058,
    "item_type": "角色",
    "rank_type": 5,
    "name": "八重神子",
    "count": 1
  },
  {
    "item_id": 10000059,
    "item_type": "角色",
    "rank_type": 4,
    "name": "鹿野院平藏",
    "count": 1
  },
  {
    "item_id": 10000060,
    "item_type": "角色",
    "rank_type": 5,
    "name": "夜兰",
    "count": 1
  },
  {
    "item_id": 10000061,
    "item_type": "角色",
    "rank_type": 4,
    "name": "绮良良",
    "count": 1
  },
  {
    "item_id": 10000062,
    "item_type": "角色",
    "rank_type": 5,
    "name": "埃洛伊",
    "count": 1
  },
  {
    "item_id": 10000063,
    "item_type": "角色",
    "rank_type": 5,
    "name": "申鹤",
    "count": 1
  },
  {
    "item_id": 10000064,
    "item_type": "角色",
    "rank_type": 4,
    "name": "云堇",
    "count": 1
  },
  {
    "item_id": 10000065,
    "item_type": "角色",
    "rank_type": 4,
    "name": "久岐忍",
    "count": 1
  },
  {
    "item_id": 10000066,
    "item_type": "角色",
    "rank_type": 5,
    "name": "神里绫人",
    "count": 1
  },
  {
    "item_id": 10000067,
    "item_type": "角色",
    "rank_type": 4,
    "name": "柯莱",
    "count": 1
  },
  {
    "item_id": 10000068,
    "item_type": "角色",
    "rank_type": 4,
    "name": "多莉",
    "count": 1
  },
  {
    "item_id": 10000069,
    "item_type": "角色",
    "rank_type": 5,
    "name": "提纳里",
    "count": 1
  },
  {
    "item_id": 10000070,
    "item_type": "角色",
    "rank_type": 5,
    "name": "妮露",
    "count": 1
  },
  {
    "item_id": 10000071,
    "item_type": "角色",
    "rank_type": 5,
    "name": "赛诺",
    "count": 1
  },
  {
    "item_id": 10000072,
    "item_type": "角色",
    "rank_type": 4,
    "name": "坎蒂丝",
    "count": 1
  },
  {
    "item_id": 10000073,
    "item_type": "角色",
    "rank_type": 5,
    "name": "纳西妲",
    "count": 1
  },
  {
    "item_id": 10000074,
    "item_type": "角色",
    "rank_type": 4,
    "name": "莱依拉",
    "count": 1
  },
  {
    "item_id": 10000075,
    "item_type": "角色",
    "rank_type": 5,
    "name": "流浪者",
    "count": 1
  },
  {
    "item_id": 10000076,
    "item_type": "角色",
    "rank_type": 4,
    "name": "珐露珊",
    "count": 1
  },
  {
    "item_id": 10000077,
    "item_type": "角色",
    "rank_type": 4,
    "name": "瑶瑶",
    "count": 1
  },
  {
    "item_id": 10000078,
    "item_type": "角色",
    "rank_type": 5,
    "name": "艾尔海森",
    "count": 1
  },
  {
    "item_id": 10000079,
    "item_type": "角色",
    "rank_type": 5,
    "name": "迪希雅",
    "count": 1
  },
  {
    "item_id": 10000080,
    "item_type": "角色",
    "rank_type": 4,
    "name": "米卡",
    "count": 1
  },
  {
    "item_id": 10000081,
    "item_type": "角色",
    "rank_type": 4,
    "name": "卡维",
    "count": 1
  },
  {
    "item_id": 10000082,
    "item_type": "角色",
    "rank_type": 5,
    "name": "白术",
    "count": 1
  },
  {
    "item_id": 10000083,
    "item_type": "角色",
    "rank_type": 4,
    "name": "琳妮特",
    "count": 1
  },
  {
    "item_id": 10000084,
    "item_type": "角色",
    "rank_type": 5,
    "name": "林尼",
    "count": 1
  },
  {
    "item_id": 10000085,
    "item_type": "角色",
    "rank_type": 4,
    "name": "菲米尼",
    "count": 1
  },
  {
    "item_id": 10000086,
    "item_type": "角色",
    "rank_type": 5,
    "name": "莱欧斯利",
    "count": 1
  },
  {
    "item_id": 10000087,
    "item_type": "角色",
    "rank_type": 5,
    "name": "那维莱特",
    "count": 1
  },
  {
    "item_id": 10000088,
    "item_type": "角色",
    "rank_type": 4,
    "name": "夏洛蒂",
    "count": 1
  },
  {
    "item_id": 10000089,
    "item_type": "角色",
    "rank_type": 5,
    "name": "芙宁娜",
    "count": 1
  },
  {
    "item_id": 10000090,
    "item_type": "角色",
    "rank_type": 4,
    "name": "夏沃蕾",
    "count": 1
  },
  {
    "item_id": 10000091,
    "item_type": "角色",
    "rank_type": 5,
    "name": "娜维娅",
    "count": 1
  },
  {
    "item_id": 10000092,
    "item_type": "角色",
    "rank_type": 4,
    "name": "嘉明",
    "count": 1
  },
  {
    "item_id": 10000093,
    "item_type": "角色",
    "rank_type": 5,
    "name": "闲云",
    "count": 1
  },
  {
    "item_id": 10000094,
    "item_type": "角色",
    "rank_type": 5,
    "name": "千织",
    "count": 1
  },
  {
    "item_id": 10000095,
    "item_type": "角色",
    "rank_type": 5,
    "name": "希格雯",
    "count": 1
  },
  {
    "item_id": 10000096,
    "item_type": "角色",
    "rank_type": 5,
    "name": "阿蕾奇诺",
    "count": 1
  },
  {
    "item_id": 10000097,
    "item_type": "角色",
    "rank_type": 4,
    "name": "赛索斯",
    "count": 1
  },
  {
    "item_id": 10000098,
    "item_type": "角色",
    "rank_type": 5,
    "name": "克洛琳德",
    "count": 1
  },
  {
    "item_id": 10000099,
    "item_type": "角色",
    "rank_type": 5,
    "name": "艾梅莉埃",
    "count": 1
  },
  {
    "item_id": 10000100,
    "item_type": "角色",
    "rank_type": 4,
    "name": "卡齐娜",
    "count": 1
  },
  {
    "item_id": 10000101,
    "item_type": "角色",
    "rank_type": 5,
    "name": "基尼奇",
    "count": 1
  },
  {
    "item_id": 10000102,
    "item_type": "角色",
    "rank_type": 5,
    "name": "玛拉妮",
    "count": 1
  },
  {
    "item_id": 10000103,
    "item_type": "角色",
    "rank_type": 5,
    "name": "希诺宁",
    "count": 1
  },
  {
    "item_id": 10000104,
    "item_type": "角色",
    "rank_type": 5,
    "name": "恰斯卡",
    "count": 1
  },
  {
    "item_id": 10000105,
    "item_type": "角色",
    "rank_type": 4,
    "name": "欧洛伦",
    "count": 1
  },
  {
    "item_id": 10000106,
    "item_type": "角色",
    "rank_type": 5,
    "name": "玛薇卡",
    "count": 1
  },
  {
    "item_id": 10000107,
    "item_type": "角色",
    "rank_type": 5,
    "name": "茜特拉莉",
    "count": 1
  },
  {
    "item_id": 10000108,
    "item_type": "角色",
    "rank_type": 4,
    "name": "蓝砚",
    "count": 1
  },
  {
    "item_id": 10000109,
    "item_type": "角色",
    "rank_type": 5,
    "name": "梦见月瑞希",
    "count": 1
  },
  {
    "item_id": 10000110,
    "item_type": "角色",
    "rank_type": 4,
    "name": "伊安珊",
    "count": 1
  },
  {
    "item_id": 10000111,
    "item_type": "角色",
    "rank_type": 5,
    "name": "瓦雷莎",
    "count": 1
  },
  {
    "item_id": 10000112,
    "item_type": "角色",
    "rank_type": 5,
    "name": "爱可菲",
    "count": 1
  },
  {
    "item_id": 10000113,
    "item_type": "角色",
    "rank_type": 4,
    "name": "伊法",
    "count": 1
  },
  {
    "item_id": 10000114,
    "item_type": "角色",
    "rank_type": 5,
    "name": "丝柯克",
    "count": 1
  },
  {
    "item_id": 10000115,
    "item_type": "角色",
    "rank_type": 4,
    "name": "塔利雅",
    "count": 1
  },
  {
    "item_id": 10000116,
    "item_type": "角色",
    "rank_type": 5,
    "name": "伊涅芙",
    "count": 1
  },
  {
    "item_id": 10000119,
    "item_type": "角色",
    "rank_type": 5,
    "name": "菈乌玛",
    "count": 1
  },
  {
    "item_id": 10000120,
    "item_type": "角色",
    "rank_type": 5,
    "name": "菲林斯",
    "count": 1
  },
  {
    "item_id": 10000121,
    "item_type": "角色",
    "rank_type": 4,
    "name": "爱诺",
    "count": 1
  },
  {
    "item_id": 10000122,
    "item_type": "角色",
    "rank_type": 5,
    "name": "奈芙尔",
    "count": 1
  }
]

def main():
    uigf_file = "Snap Hutao UIGF.json"
    output_file = "merged_uigf.json"

    with open(uigf_file, "r", encoding="utf-8") as f:
        uigf = json.load(f)

    items = weapon_avatar_json
    item_dict = {str(i["item_id"]): i for i in items}

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
        for record in uid_block["list"]:
            item_id = record.get("item_id")
            extra = item_dict.get(item_id, {})
            merged = {**extra, **record}

            sorted_record = {k: merged.get(k, None) for k in field_order}

            for k, v in merged.items():
                if k not in field_order:
                    sorted_record[k] = v

            record.clear()
            record.update(sorted_record)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(uigf, f, ensure_ascii=False, indent=4)

    print("处理完成！输出文件：", output_file)


if __name__ == "__main__":
    main()
