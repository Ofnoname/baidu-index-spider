import json

original_json = [
  {
    "label": "全国",
    "key": "0"
  },
  {
    "label": "全国所有省份和地区单独统计（非常耗时）",
    "key": "999"
  },
  {
    "label": "山东",
    "key": "901",
    "children": [
      {
        "label": "济南",
        "key": "1"
      },
      {
        "label": "滨州",
        "key": "76"
      },
      {
        "label": "青岛",
        "key": "77"
      },
      {
        "label": "烟台",
        "key": "78"
      },
      {
        "label": "临沂",
        "key": "79"
      },
      {
        "label": "潍坊",
        "key": "80"
      },
      {
        "label": "淄博",
        "key": "81"
      },
      {
        "label": "东营",
        "key": "82"
      },
      {
        "label": "聊城",
        "key": "83"
      },
      {
        "label": "菏泽",
        "key": "84"
      },
      {
        "label": "枣庄",
        "key": "85"
      },
      {
        "label": "德州",
        "key": "86"
      },
      {
        "label": "威海",
        "key": "88"
      },
      {
        "label": "济宁",
        "key": "352"
      },
      {
        "label": "泰安",
        "key": "353"
      },
      {
        "label": "莱芜",
        "key": "356"
      },
      {
        "label": "日照",
        "key": "366"
      }
    ]
  },
  {
    "label": "贵州",
    "key": "902",
    "children": [
      {
        "label": "贵阳",
        "key": "2"
      },
      {
        "label": "黔南",
        "key": "3"
      },
      {
        "label": "六盘水",
        "key": "4"
      },
      {
        "label": "遵义",
        "key": "59"
      },
      {
        "label": "黔东南",
        "key": "61"
      },
      {
        "label": "铜仁",
        "key": "422"
      },
      {
        "label": "安顺",
        "key": "424"
      },
      {
        "label": "毕节",
        "key": "426"
      },
      {
        "label": "黔西南",
        "key": "588"
      }
    ]
  },
  {
    "label": "江西",
    "key": "903",
    "children": [
      {
        "label": "南昌",
        "key": "5"
      },
      {
        "label": "九江",
        "key": "6"
      },
      {
        "label": "鹰潭",
        "key": "7"
      },
      {
        "label": "抚州",
        "key": "8"
      },
      {
        "label": "上饶",
        "key": "9"
      },
      {
        "label": "赣州",
        "key": "10"
      },
      {
        "label": "吉安",
        "key": "115"
      },
      {
        "label": "萍乡",
        "key": "136"
      },
      {
        "label": "景德镇",
        "key": "137"
      },
      {
        "label": "新余",
        "key": "246"
      },
      {
        "label": "宜春",
        "key": "256"
      }
    ]
  },
  {
    "label": "重庆",
    "key": "904",
    "children": []
  },
  {
    "label": "内蒙古",
    "key": "905",
    "children": [
      {
        "label": "呼和浩特",
        "key": "20"
      },
      {
        "label": "包头",
        "key": "13"
      },
      {
        "label": "鄂尔多斯",
        "key": "14"
      },
      {
        "label": "巴彦淖尔",
        "key": "15"
      },
      {
        "label": "乌海",
        "key": "16"
      },
      {
        "label": "阿拉善盟",
        "key": "17"
      },
      {
        "label": "锡林郭勒盟",
        "key": "19"
      },
      {
        "label": "赤峰",
        "key": "21"
      },
      {
        "label": "通辽",
        "key": "22"
      },
      {
        "label": "呼伦贝尔",
        "key": "25"
      },
      {
        "label": "乌兰察布",
        "key": "331"
      },
      {
        "label": "兴安盟",
        "key": "333"
      }
    ]
  },
  {
    "label": "湖北",
    "key": "906",
    "children": [
      {
        "label": "武汉",
        "key": "28"
      },
      {
        "label": "黄石",
        "key": "30"
      },
      {
        "label": "荆州",
        "key": "31"
      },
      {
        "label": "襄阳",
        "key": "32"
      },
      {
        "label": "黄冈",
        "key": "33"
      },
      {
        "label": "荆门",
        "key": "34"
      },
      {
        "label": "宜昌",
        "key": "35"
      },
      {
        "label": "十堰",
        "key": "36"
      },
      {
        "label": "随州",
        "key": "37"
      },
      {
        "label": "恩施",
        "key": "38"
      },
      {
        "label": "鄂州",
        "key": "39"
      },
      {
        "label": "咸宁",
        "key": "40"
      },
      {
        "label": "孝感",
        "key": "41"
      },
      {
        "label": "仙桃",
        "key": "42"
      },
      {
        "label": "天门",
        "key": "73"
      },
      {
        "label": "潜江",
        "key": "74"
      },
      {
        "label": "神农架",
        "key": "687"
      }
    ]
  },
  {
    "label": "辽宁",
    "key": "907",
    "children": [
      {
        "label": "沈阳",
        "key": "150"
      },
      {
        "label": "大连",
        "key": "29"
      },
      {
        "label": "盘锦",
        "key": "151"
      },
      {
        "label": "鞍山",
        "key": "215"
      },
      {
        "label": "朝阳",
        "key": "216"
      },
      {
        "label": "锦州",
        "key": "217"
      },
      {
        "label": "铁岭",
        "key": "218"
      },
      {
        "label": "丹东",
        "key": "219"
      },
      {
        "label": "本溪",
        "key": "220"
      },
      {
        "label": "营口",
        "key": "221"
      },
      {
        "label": "抚顺",
        "key": "222"
      },
      {
        "label": "阜新",
        "key": "223"
      },
      {
        "label": "辽阳",
        "key": "224"
      },
      {
        "label": "葫芦岛",
        "key": "225"
      }
    ]
  },
  {
    "label": "湖南",
    "key": "908",
    "children": [
      {
        "label": "长沙",
        "key": "43"
      },
      {
        "label": "岳阳",
        "key": "44"
      },
      {
        "label": "衡阳",
        "key": "45"
      },
      {
        "label": "株洲",
        "key": "46"
      },
      {
        "label": "湘潭",
        "key": "47"
      },
      {
        "label": "益阳",
        "key": "48"
      },
      {
        "label": "郴州",
        "key": "49"
      },
      {
        "label": "湘西",
        "key": "65"
      },
      {
        "label": "娄底",
        "key": "66"
      },
      {
        "label": "怀化",
        "key": "67"
      },
      {
        "label": "常德",
        "key": "68"
      },
      {
        "label": "张家界",
        "key": "226"
      },
      {
        "label": "永州",
        "key": "269"
      },
      {
        "label": "邵阳",
        "key": "405"
      }
    ]
  },
  {
    "label": "福建",
    "key": "909",
    "children": [
      {
        "label": "福州",
        "key": "50"
      },
      {
        "label": "莆田",
        "key": "51"
      },
      {
        "label": "三明",
        "key": "52"
      },
      {
        "label": "龙岩",
        "key": "53"
      },
      {
        "label": "厦门",
        "key": "54"
      },
      {
        "label": "泉州",
        "key": "55"
      },
      {
        "label": "漳州",
        "key": "56"
      },
      {
        "label": "宁德",
        "key": "87"
      },
      {
        "label": "南平",
        "key": "253"
      }
    ]
  },
  {
    "label": "上海",
    "key": "910",
    "children": []
  },
  {
    "label": "北京",
    "key": "911",
    "children": []
  },
  {
    "label": "广西",
    "key": "912",
    "children": [
      {
        "label": "南宁",
        "key": "90"
      },
      {
        "label": "柳州",
        "key": "89"
      },
      {
        "label": "桂林",
        "key": "91"
      },
      {
        "label": "贺州",
        "key": "92"
      },
      {
        "label": "贵港",
        "key": "93"
      },
      {
        "label": "玉林",
        "key": "118"
      },
      {
        "label": "河池",
        "key": "119"
      },
      {
        "label": "北海",
        "key": "128"
      },
      {
        "label": "钦州",
        "key": "129"
      },
      {
        "label": "防城港",
        "key": "130"
      },
      {
        "label": "百色",
        "key": "131"
      },
      {
        "label": "梧州",
        "key": "132"
      },
      {
        "label": "来宾",
        "key": "506"
      },
      {
        "label": "崇左",
        "key": "665"
      }
    ]
  },
  {
    "label": "广东",
    "key": "913",
    "children": [
      {
        "label": "广州",
        "key": "95"
      },
      {
        "label": "深圳",
        "key": "94"
      },
      {
        "label": "东莞",
        "key": "133"
      },
      {
        "label": "云浮",
        "key": "195"
      },
      {
        "label": "佛山",
        "key": "196"
      },
      {
        "label": "湛江",
        "key": "197"
      },
      {
        "label": "江门",
        "key": "198"
      },
      {
        "label": "惠州",
        "key": "199"
      },
      {
        "label": "珠海",
        "key": "200"
      },
      {
        "label": "韶关",
        "key": "201"
      },
      {
        "label": "阳江",
        "key": "202"
      },
      {
        "label": "茂名",
        "key": "203"
      },
      {
        "label": "潮州",
        "key": "204"
      },
      {
        "label": "揭阳",
        "key": "205"
      },
      {
        "label": "中山",
        "key": "207"
      },
      {
        "label": "清远",
        "key": "208"
      },
      {
        "label": "肇庆",
        "key": "209"
      },
      {
        "label": "河源",
        "key": "210"
      },
      {
        "label": "梅州",
        "key": "211"
      },
      {
        "label": "汕头",
        "key": "212"
      },
      {
        "label": "汕尾",
        "key": "213"
      }
    ]
  },
  {
    "label": "四川",
    "key": "914",
    "children": [
      {
        "label": "成都",
        "key": "97"
      },
      {
        "label": "宜宾",
        "key": "96"
      },
      {
        "label": "绵阳",
        "key": "98"
      },
      {
        "label": "广元",
        "key": "99"
      },
      {
        "label": "遂宁",
        "key": "100"
      },
      {
        "label": "巴中",
        "key": "101"
      },
      {
        "label": "内江",
        "key": "102"
      },
      {
        "label": "泸州",
        "key": "103"
      },
      {
        "label": "南充",
        "key": "104"
      },
      {
        "label": "德阳",
        "key": "106"
      },
      {
        "label": "乐山",
        "key": "107"
      },
      {
        "label": "广安",
        "key": "108"
      },
      {
        "label": "资阳",
        "key": "109"
      },
      {
        "label": "自贡",
        "key": "111"
      },
      {
        "label": "攀枝花",
        "key": "112"
      },
      {
        "label": "达州",
        "key": "113"
      },
      {
        "label": "雅安",
        "key": "114"
      },
      {
        "label": "眉山",
        "key": "291"
      },
      {
        "label": "甘孜",
        "key": "417"
      },
      {
        "label": "阿坝",
        "key": "457"
      },
      {
        "label": "凉山",
        "key": "479"
      }
    ]
  },
  {
    "label": "云南",
    "key": "915",
    "children": [
      {
        "label": "昆明",
        "key": "117"
      },
      {
        "label": "玉溪",
        "key": "123"
      },
      {
        "label": "楚雄",
        "key": "124"
      },
      {
        "label": "大理",
        "key": "334"
      },
      {
        "label": "昭通",
        "key": "335"
      },
      {
        "label": "红河",
        "key": "337"
      },
      {
        "label": "曲靖",
        "key": "339"
      },
      {
        "label": "丽江",
        "key": "342"
      },
      {
        "label": "临沧",
        "key": "350"
      },
      {
        "label": "文山",
        "key": "437"
      },
      {
        "label": "保山",
        "key": "438"
      },
      {
        "label": "普洱",
        "key": "666"
      },
      {
        "label": "西双版纳",
        "key": "668"
      },
      {
        "label": "德宏",
        "key": "669"
      },
      {
        "label": "怒江",
        "key": "671"
      },
      {
        "label": "迪庆",
        "key": "672"
      }
    ]
  },
  {
    "label": "江苏",
    "key": "916",
    "children": [
      {
        "label": "南京",
        "key": "125"
      },
      {
        "label": "苏州",
        "key": "126"
      },
      {
        "label": "无锡",
        "key": "127"
      },
      {
        "label": "连云港",
        "key": "156"
      },
      {
        "label": "淮安",
        "key": "157"
      },
      {
        "label": "扬州",
        "key": "158"
      },
      {
        "label": "泰州",
        "key": "159"
      },
      {
        "label": "盐城",
        "key": "160"
      },
      {
        "label": "徐州",
        "key": "161"
      },
      {
        "label": "常州",
        "key": "162"
      },
      {
        "label": "南通",
        "key": "163"
      },
      {
        "label": "镇江",
        "key": "169"
      },
      {
        "label": "宿迁",
        "key": "172"
      }
    ]
  },
  {
    "label": "浙江",
    "key": "917",
    "children": [
      {
        "label": "杭州",
        "key": "138"
      },
      {
        "label": "丽水",
        "key": "134"
      },
      {
        "label": "金华",
        "key": "135"
      },
      {
        "label": "温州",
        "key": "149"
      },
      {
        "label": "台州",
        "key": "287"
      },
      {
        "label": "衢州",
        "key": "288"
      },
      {
        "label": "宁波",
        "key": "289"
      },
      {
        "label": "绍兴",
        "key": "303"
      },
      {
        "label": "嘉兴",
        "key": "304"
      },
      {
        "label": "湖州",
        "key": "305"
      },
      {
        "label": "舟山",
        "key": "306"
      }
    ]
  },
  {
    "label": "青海",
    "key": "918",
    "children": [
      {
        "label": "西宁",
        "key": "139"
      },
      {
        "label": "海西",
        "key": "608"
      },
      {
        "label": "海东",
        "key": "652"
      },
      {
        "label": "玉树",
        "key": "659"
      },
      {
        "label": "海南",
        "key": "676"
      },
      {
        "label": "海北",
        "key": "682"
      },
      {
        "label": "黄南",
        "key": "685"
      },
      {
        "label": "果洛",
        "key": "688"
      }
    ]
  },
  {
    "label": "宁夏",
    "key": "919",
    "children": [
      {
        "label": "银川",
        "key": "140"
      },
      {
        "label": "吴忠",
        "key": "395"
      },
      {
        "label": "固原",
        "key": "396"
      },
      {
        "label": "石嘴山",
        "key": "472"
      },
      {
        "label": "中卫",
        "key": "480"
      }
    ]
  },
  {
    "label": "河北",
    "key": "920",
    "children": [
      {
        "label": "石家庄",
        "key": "141"
      },
      {
        "label": "衡水",
        "key": "143"
      },
      {
        "label": "张家口",
        "key": "144"
      },
      {
        "label": "承德",
        "key": "145"
      },
      {
        "label": "秦皇岛",
        "key": "146"
      },
      {
        "label": "廊坊",
        "key": "147"
      },
      {
        "label": "沧州",
        "key": "148"
      },
      {
        "label": "保定",
        "key": "259"
      },
      {
        "label": "唐山",
        "key": "261"
      },
      {
        "label": "邯郸",
        "key": "292"
      },
      {
        "label": "邢台",
        "key": "293"
      }
    ]
  },
  {
    "label": "黑龙江",
    "key": "921",
    "children": [
      {
        "label": "哈尔滨",
        "key": "152"
      },
      {
        "label": "大庆",
        "key": "153"
      },
      {
        "label": "伊春",
        "key": "295"
      },
      {
        "label": "大兴安岭",
        "key": "297"
      },
      {
        "label": "黑河",
        "key": "300"
      },
      {
        "label": "鹤岗",
        "key": "301"
      },
      {
        "label": "七台河",
        "key": "302"
      },
      {
        "label": "齐齐哈尔",
        "key": "319"
      },
      {
        "label": "佳木斯",
        "key": "320"
      },
      {
        "label": "牡丹江",
        "key": "322"
      },
      {
        "label": "鸡西",
        "key": "323"
      },
      {
        "label": "绥化",
        "key": "324"
      },
      {
        "label": "双鸭山",
        "key": "359"
      }
    ]
  },
  {
    "label": "吉林",
    "key": "922",
    "children": [
      {
        "label": "长春",
        "key": "154"
      },
      {
        "label": "四平",
        "key": "155"
      },
      {
        "label": "辽源",
        "key": "191"
      },
      {
        "label": "松原",
        "key": "194"
      },
      {
        "label": "吉林",
        "key": "270"
      },
      {
        "label": "通化",
        "key": "407"
      },
      {
        "label": "白山",
        "key": "408"
      },
      {
        "label": "白城",
        "key": "410"
      },
      {
        "label": "延边",
        "key": "525"
      }
    ]
  },
  {
    "label": "天津",
    "key": "923",
    "children": []
  },
  {
    "label": "陕西",
    "key": "924",
    "children": [
      {
        "label": "西安",
        "key": "165"
      },
      {
        "label": "铜川",
        "key": "271"
      },
      {
        "label": "安康",
        "key": "272"
      },
      {
        "label": "宝鸡",
        "key": "273"
      },
      {
        "label": "商洛",
        "key": "274"
      },
      {
        "label": "渭南",
        "key": "275"
      },
      {
        "label": "汉中",
        "key": "276"
      },
      {
        "label": "咸阳",
        "key": "277"
      },
      {
        "label": "榆林",
        "key": "278"
      },
      {
        "label": "延安",
        "key": "401"
      }
    ]
  },
  {
    "label": "甘肃",
    "key": "925",
    "children": [
      {
        "label": "兰州",
        "key": "166"
      },
      {
        "label": "庆阳",
        "key": "281"
      },
      {
        "label": "定西",
        "key": "282"
      },
      {
        "label": "武威",
        "key": "283"
      },
      {
        "label": "酒泉",
        "key": "284"
      },
      {
        "label": "张掖",
        "key": "285"
      },
      {
        "label": "嘉峪关",
        "key": "286"
      },
      {
        "label": "平凉",
        "key": "307"
      },
      {
        "label": "天水",
        "key": "308"
      },
      {
        "label": "白银",
        "key": "309"
      },
      {
        "label": "金昌",
        "key": "343"
      },
      {
        "label": "陇南",
        "key": "344"
      },
      {
        "label": "临夏",
        "key": "346"
      },
      {
        "label": "甘南",
        "key": "673"
      }
    ]
  },
  {
    "label": "新疆",
    "key": "926",
    "children": [
      {
        "label": "乌鲁木齐",
        "key": "467"
      },
      {
        "label": "石河子",
        "key": "280"
      },
      {
        "label": "吐鲁番",
        "key": "310"
      },
      {
        "label": "昌吉",
        "key": "311"
      },
      {
        "label": "哈密",
        "key": "312"
      },
      {
        "label": "阿克苏",
        "key": "315"
      },
      {
        "label": "克拉玛依",
        "key": "317"
      },
      {
        "label": "博尔塔拉",
        "key": "318"
      },
      {
        "label": "阿勒泰",
        "key": "383"
      },
      {
        "label": "喀什",
        "key": "384"
      },
      {
        "label": "和田",
        "key": "386"
      },
      {
        "label": "巴音郭楞",
        "key": "499"
      },
      {
        "label": "伊犁",
        "key": "520"
      },
      {
        "label": "塔城",
        "key": "563"
      },
      {
        "label": "克孜勒苏柯尔克孜",
        "key": "653"
      },
      {
        "label": "五家渠",
        "key": "661"
      },
      {
        "label": "阿拉尔",
        "key": "692"
      },
      {
        "label": "图木舒克",
        "key": "693"
      }
    ]
  },
  {
    "label": "河南",
    "key": "927",
    "children": [
      {
        "label": "郑州",
        "key": "168"
      },
      {
        "label": "南阳",
        "key": "262"
      },
      {
        "label": "新乡",
        "key": "263"
      },
      {
        "label": "开封",
        "key": "264"
      },
      {
        "label": "焦作",
        "key": "265"
      },
      {
        "label": "平顶山",
        "key": "266"
      },
      {
        "label": "许昌",
        "key": "268"
      },
      {
        "label": "安阳",
        "key": "370"
      },
      {
        "label": "驻马店",
        "key": "371"
      },
      {
        "label": "信阳",
        "key": "373"
      },
      {
        "label": "鹤壁",
        "key": "374"
      },
      {
        "label": "周口",
        "key": "375"
      },
      {
        "label": "商丘",
        "key": "376"
      },
      {
        "label": "洛阳",
        "key": "378"
      },
      {
        "label": "漯河",
        "key": "379"
      },
      {
        "label": "濮阳",
        "key": "380"
      },
      {
        "label": "三门峡",
        "key": "381"
      },
      {
        "label": "济源",
        "key": "667"
      }
    ]
  },
  {
    "label": "安徽",
    "key": "928",
    "children": [
      {
        "label": "合肥",
        "key": "189"
      },
      {
        "label": "铜陵",
        "key": "173"
      },
      {
        "label": "黄山",
        "key": "174"
      },
      {
        "label": "池州",
        "key": "175"
      },
      {
        "label": "宣城",
        "key": "176"
      },
      {
        "label": "巢湖",
        "key": "177"
      },
      {
        "label": "淮南",
        "key": "178"
      },
      {
        "label": "宿州",
        "key": "179"
      },
      {
        "label": "六安",
        "key": "181"
      },
      {
        "label": "滁州",
        "key": "182"
      },
      {
        "label": "淮北",
        "key": "183"
      },
      {
        "label": "阜阳",
        "key": "184"
      },
      {
        "label": "马鞍山",
        "key": "185"
      },
      {
        "label": "安庆",
        "key": "186"
      },
      {
        "label": "蚌埠",
        "key": "187"
      },
      {
        "label": "芜湖",
        "key": "188"
      },
      {
        "label": "亳州",
        "key": "391"
      }
    ]
  },
  {
    "label": "山西",
    "key": "929",
    "children": [
      {
        "label": "太原",
        "key": "231"
      },
      {
        "label": "大同",
        "key": "227"
      },
      {
        "label": "长治",
        "key": "228"
      },
      {
        "label": "忻州",
        "key": "229"
      },
      {
        "label": "晋中",
        "key": "230"
      },
      {
        "label": "临汾",
        "key": "232"
      },
      {
        "label": "运城",
        "key": "233"
      },
      {
        "label": "晋城",
        "key": "234"
      },
      {
        "label": "朔州",
        "key": "235"
      },
      {
        "label": "阳泉",
        "key": "236"
      },
      {
        "label": "吕梁",
        "key": "237"
      }
    ]
  },
  {
    "label": "海南",
    "key": "930",
    "children": [
      {
        "label": "海口",
        "key": "239"
      },
      {
        "label": "万宁",
        "key": "241"
      },
      {
        "label": "琼海",
        "key": "242"
      },
      {
        "label": "三亚",
        "key": "243"
      },
      {
        "label": "儋州",
        "key": "244"
      },
      {
        "label": "东方",
        "key": "456"
      },
      {
        "label": "五指山",
        "key": "582"
      },
      {
        "label": "文昌",
        "key": "670"
      },
      {
        "label": "陵水",
        "key": "674"
      },
      {
        "label": "澄迈",
        "key": "675"
      },
      {
        "label": "乐东",
        "key": "679"
      },
      {
        "label": "临高",
        "key": "680"
      },
      {
        "label": "定安",
        "key": "681"
      },
      {
        "label": "昌江",
        "key": "683"
      },
      {
        "label": "屯昌",
        "key": "684"
      },
      {
        "label": "保亭",
        "key": "686"
      },
      {
        "label": "白沙",
        "key": "689"
      },
      {
        "label": "琼中",
        "key": "690"
      }
    ]
  },
  {
    "label": "台湾",
    "key": "931",
    "children": []
  },
  {
    "label": "西藏",
    "key": "932",
    "children": [
      {
        "label": "拉萨",
        "key": "466"
      },
      {
        "label": "日喀则",
        "key": "516"
      },
      {
        "label": "那曲",
        "key": "655"
      },
      {
        "label": "林芝",
        "key": "656"
      },
      {
        "label": "山南",
        "key": "677"
      },
      {
        "label": "昌都",
        "key": "678"
      },
      {
        "label": "阿里",
        "key": "691"
      }
    ]
  },
  {
    "label": "香港",
    "key": "933",
    "children": []
  },
  {
    "label": "澳门",
    "key": "934",
    "children": []
    }
    ]


# Function to traverse the original JSON and generate a new JSON
def traverse_and_generate(json_input):
    new_json = {}
    for item in json_input:
        # Add the current item's key and label to the new JSON
        new_json[item["key"]] = item["label"]
        # If the current item has children, recursively process them
        if "children" in item:
            children_new_json = traverse_and_generate(item["children"])
            new_json.update(children_new_json)
    return new_json

# Generate the new JSON
new_json = traverse_and_generate(original_json)

# output new_json to webui/public/city.json
with open("webui/public/city.json", "w", encoding="utf-8") as f:
    json.dump(new_json, f, ensure_ascii=False)