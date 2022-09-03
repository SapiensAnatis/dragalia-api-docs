/guild_search/auto_search
============================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: 1a5a3cb1aa568946e14a539ae29b79f74c58858365dc2bb0dbe8d8e5150215ed	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27886514755078342	Request-Time: 1662165803	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 91

Request body
----------------

.. code-block:: json

	{
	    "joining_condition_type_list": [
	        1,
	        2
	    ],
	    "activity_policy_type_list": [
	        1,
	        2,
	        3,
	        4,
	        5
	    ],
	    "member_count_type_list": [
	        1,
	        2,
	        3
	    ]
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 13596	Expires: Sat, 03 Sep 2022 00:43:25 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sat, 03 Sep 2022 00:43:25 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "auto_search_guild_list": [
	            {
	                "guild_id": 42844374,
	                "guild_name": "\u2606\u30c9\u30e9\u30ac\u30ea\u30a2\u30ed\u30b9\u30c8\u2606",
	                "guild_emblem_id": 10022,
	                "guild_introduction": "\u30b2\u30fc\u30de\u30fc\u306e\u30c9\u30e9\u30ac\u30ea\u30a2\u30ed\u30b9\u30c8",
	                "joining_condition_type": 2,
	                "activity_policy_type": 1,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 2,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 29514854,
	                "guild_name": "\u3069\u3089\u304c\u308a\u3042\u308d\u3059\u3068\u3002",
	                "guild_emblem_id": 10030,
	                "guild_introduction": "\u6b8b\u5ff5\u3067\u3059\u304c\u2026\u30b5\u30fc\u30d3\u30b9\u7d42\u4e86\u544a\u77e5\u304d\u3066\u307e\u3059\u306d\u3002\u3000\u3000\u3000\u3000\u52df\u96c6\u306f\u3057\u3066\u304a\u308a\u307e\u305b\u3093>_<",
	                "joining_condition_type": 2,
	                "activity_policy_type": 3,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 26,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 56060374,
	                "guild_name": "Masive Phallic",
	                "guild_emblem_id": 10033,
	                "guild_introduction": "Get it up and keep it up.",
	                "joining_condition_type": 1,
	                "activity_policy_type": 1,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 1,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 55308038,
	                "guild_name": "\u6625\u590f\u79cb\u51ac",
	                "guild_emblem_id": 10029,
	                "guild_introduction": "\u3088\u308d\u3057\u304f\u304a\u9858\u3044\u3057\u307e\u3059\uff01",
	                "joining_condition_type": 1,
	                "activity_policy_type": 1,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 3,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 68317942,
	                "guild_name": "The L&L Gang",
	                "guild_emblem_id": 10033,
	                "guild_introduction": "The official Alliance for the L&L discord server!",
	                "joining_condition_type": 2,
	                "activity_policy_type": 4,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 3,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 39063478,
	                "guild_name": "\u6d77\u8c79\u5fc5\u6b7b\uff01",
	                "guild_emblem_id": 10012,
	                "guild_introduction": "\u8bf7\u591a\u6307\u6559\uff01",
	                "joining_condition_type": 1,
	                "activity_policy_type": 1,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 16,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 48363254,
	                "guild_name": "7\u7d44",
	                "guild_emblem_id": 10001,
	                "guild_introduction": "\u3088\u308d\u3057\u304f\u304a\u9858\u3044\u3057\u307e\u3059\uff01",
	                "joining_condition_type": 1,
	                "activity_policy_type": 1,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 3,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 63263606,
	                "guild_name": "Lunar Nights",
	                "guild_emblem_id": 10029,
	                "guild_introduction": "Hello, fellow adventurers!",
	                "joining_condition_type": 1,
	                "activity_policy_type": 1,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 28,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 88944038,
	                "guild_name": "Epitaph Twilight",
	                "guild_emblem_id": 10033,
	                "guild_introduction": "Hello, fellow adventurers!",
	                "joining_condition_type": 1,
	                "activity_policy_type": 1,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 28,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 75526838,
	                "guild_name": "Avaritia",
	                "guild_emblem_id": 10004,
	                "guild_introduction": "Just casual.",
	                "joining_condition_type": 1,
	                "activity_policy_type": 3,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 1,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 75885542,
	                "guild_name": "Brain Damage",
	                "guild_emblem_id": 10013,
	                "guild_introduction": "Boom.",
	                "joining_condition_type": 2,
	                "activity_policy_type": 5,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 20,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 68589494,
	                "guild_name": "Corgi\u3000Lovers",
	                "guild_emblem_id": 10029,
	                "guild_introduction": "Hello,\u3000and\u3000welcome!",
	                "joining_condition_type": 1,
	                "activity_policy_type": 3,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 13,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 37047222,
	                "guild_name": "\u307e\u3063\u305f\u308a\u306e\u3093\u3073\u308a\u56e3",
	                "guild_emblem_id": 10001,
	                "guild_introduction": "\u307e\u3063\u305f\u308a\u306e\u3093\u3073\u308a\u697d\u3057\u304f\u3084\u308a\u307e\u3057\u3087\u3046\u3088\u3002",
	                "joining_condition_type": 1,
	                "activity_policy_type": 3,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 3,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 10260214,
	                "guild_name": "\u9999\u6e2f\u540c\u76df\u3000",
	                "guild_emblem_id": 10012,
	                "guild_introduction": "\u8f15\u9b06\u73a9\u904a\u6232\u3000\u653e\u9b06\u5fc3\u60c5",
	                "joining_condition_type": 2,
	                "activity_policy_type": 3,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 24,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 92550086,
	                "guild_name": "The Ungratefuls",
	                "guild_emblem_id": 10007,
	                "guild_introduction": "Join our alliance now, ya damn ingrates",
	                "joining_condition_type": 2,
	                "activity_policy_type": 1,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 29,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 46544326,
	                "guild_name": "Undeniable Squish",
	                "guild_emblem_id": 10033,
	                "guild_introduction": "Its squishiness is undeniable. [Discord required!]",
	                "joining_condition_type": 2,
	                "activity_policy_type": 4,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 28,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 85800390,
	                "guild_name": "Drytghghjooiuygg",
	                "guild_emblem_id": 10011,
	                "guild_introduction": "\u8acb\u591a\u6307\u6559\uff01",
	                "joining_condition_type": 1,
	                "activity_policy_type": 1,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 2,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 26636566,
	                "guild_name": "Knights Errant",
	                "guild_emblem_id": 10021,
	                "guild_introduction": "Alliance looking to clear content and have fun!",
	                "joining_condition_type": 2,
	                "activity_policy_type": 1,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 25,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 52012934,
	                "guild_name": "\u6bd4\u60b2\u50b7\u66f4\u60b2\u50b7\u7684\u62bd\u904b",
	                "guild_emblem_id": 10003,
	                "guild_introduction": "\u96d6\u7136\u62bd\u7684\u5f88\u975e\u4f46\u9084\u662f\u8981\u73a9",
	                "joining_condition_type": 1,
	                "activity_policy_type": 3,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 27,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 10804694,
	                "guild_name": "\u9a6c\u6876\u7cbe\u7075",
	                "guild_emblem_id": 10021,
	                "guild_introduction": "\u8f7b\u677e\u9f99\u7ea6",
	                "joining_condition_type": 2,
	                "activity_policy_type": 1,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 8,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 47453750,
	                "guild_name": "\u5c0f\u9ce5\u9a0e\u58eb\u56e3",
	                "guild_emblem_id": 10004,
	                "guild_introduction": "\u57fa\u672c\u3069\u306a\u305f\u3067\u3082\u6b53\u8fce\u3002\u7121\u8a00OK\u51fa\u5165\u308a\u81ea\u7531\u3002\u540c\u76df\u306e\u307f\u30d1\u30fc\u30c6\u30a3\u3092\u7d44\u3080\u5834\u5408\u3082\u30bf\u30a4\u30df\u30f3\u30b0\u304c\u5408\u3063\u3066\u7d44\u3081\u308c\u3070\u7d44\u3080\u3001\u30c0\u30e1\u306a\u3089\u91ce\u826f\u3068\u3044\u3046\u98a8\u306b\u6c17\u8efd\u3067OK\uff01",
	                "joining_condition_type": 1,
	                "activity_policy_type": 3,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 24,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 79095462,
	                "guild_name": "\u4e00\u8d77\u6765\u5403\u70e4\u8089\uff01",
	                "guild_emblem_id": 10029,
	                "guild_introduction": "\u4eca\u665a\u4e00\u8d77\u6765\u5403\u70e4\u8089\u5427\uff01",
	                "joining_condition_type": 2,
	                "activity_policy_type": 3,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 8,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 75748166,
	                "guild_name": "\u683c\u53e4\u6d1b",
	                "guild_emblem_id": 10001,
	                "guild_introduction": "\u8f15\u9b06\u958b\u5fc3\u73a9.\u9999\u6e2f\u73a9\u5bb6\u3000",
	                "joining_condition_type": 2,
	                "activity_policy_type": 3,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 11,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 25781814,
	                "guild_name": "\u2606\u2605Nest\u2605\u2606",
	                "guild_emblem_id": 10010,
	                "guild_introduction": "\u3068\u308a\u3042\u3048\u305a\u30ae\u30eb\u30c9\u5165\u3063\u3068\u304f\u304b\u2025\u3066\u4eba\u3001\u81ea\u7531\u306b\u53c2\u52a0\u3057\u3066\u306d\u3000\u7121\u8a00\u30de\u30a4\u30da\u30fc\u30b9\u306b\u904a\u3079\u3070OK\u3000\u9577\u671f\u30a4\u30f3\u306a\u3057\u3055\u3093\u306f\u6642\u3005\u3055\u3088\u306a\u3089\u3057\u307e\u3059\u3002",
	                "joining_condition_type": 1,
	                "activity_policy_type": 3,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 7,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 72294070,
	                "guild_name": "\u53e4\u6226\u5834\u304b\u3089\u9003\u3052\u308b\u306a",
	                "guild_emblem_id": 10017,
	                "guild_introduction": "\u3088\u308d\u3057\u304f\u304a\u9858\u3044\u3057\u307e\u3059\uff01",
	                "joining_condition_type": 2,
	                "activity_policy_type": 3,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 1,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 35645910,
	                "guild_name": "\u30c9\u30e9\u30d5\u30a7\u30b9",
	                "guild_emblem_id": 10009,
	                "guild_introduction": "\u521d\u5fc3\u8005\u3055\u3093\u6b53\u8fce\uff01\u30ac\u30c4\u30ac\u30c4\u3057\u307e\u305b\u3093\u3002\u30de\u30a4\u30da\u30fc\u30b9\u306b\u3069\u306a\u305f\u3067\u3082\u697d\u3057\u304f\u904a\u3073\u307e\u3057\u3087\u3046\u3002\u3000",
	                "joining_condition_type": 2,
	                "activity_policy_type": 2,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 13,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 70834886,
	                "guild_name": "\u72db\u72d0",
	                "guild_emblem_id": 10026,
	                "guild_introduction": "2021.9\u6708\u8a2d\u7acb\u3000\u4eca\u66f4\u306a\u304c\u3089\u306e\u30c9\u30e9\u30ac\u30ea\u306b\u30cf\u30de\u3063\u305f\u4eba\u9054\u3001\u5fa9\u5e30\u3057\u305f\u4eba\u9054\u3001\u3054\u53c2\u52a0\u304a\u5f85\u3061\u3057\u3066\u304a\u308a\u307e\u3059(\uff9f\u2200\uff9f)\u3000\u3042\u3001\u3042\u3068\u72d0\u3063\u3066\u53ef\u611b\u3044\u3068\u601d\u3046\u306e",
	                "joining_condition_type": 1,
	                "activity_policy_type": 3,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 9,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 85351782,
	                "guild_name": "Bit",
	                "guild_emblem_id": 10029,
	                "guild_introduction": "Hello, fellow adventurers!",
	                "joining_condition_type": 1,
	                "activity_policy_type": 1,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 3,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 19472038,
	                "guild_name": "Alliance",
	                "guild_emblem_id": 10030,
	                "guild_introduction": "Hello, fellow adventurers!",
	                "joining_condition_type": 2,
	                "activity_policy_type": 1,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 2,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 31982678,
	                "guild_name": "\u6708\u591c\u306e\u767d\u732b\u56e3",
	                "guild_emblem_id": 10029,
	                "guild_introduction": "\u57fa\u672c\u7121\u8a00\u3067\u69cb\u3044\u307e\u305b\u3093\u3002\u597d\u304d\u306b\u4f7f\u3063\u3066\u4e0b\u3055\u3044\u3002",
	                "joining_condition_type": 1,
	                "activity_policy_type": 3,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 26,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 69836982,
	                "guild_name": "Ethereal dragons",
	                "guild_emblem_id": 10025,
	                "guild_introduction": "fellow adventurers! If you\u2019re about getting stronger and committing ",
	                "joining_condition_type": 1,
	                "activity_policy_type": 1,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 27,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 13089574,
	                "guild_name": "\u9f8d\u306e\u7a9f",
	                "guild_emblem_id": 10027,
	                "guild_introduction": "\u8bf7\u591a\u6307\u6559\uff01",
	                "joining_condition_type": 2,
	                "activity_policy_type": 3,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 4,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 85052742,
	                "guild_name": "Black Eagle House",
	                "guild_emblem_id": 10007,
	                "guild_introduction": "Hello, fellow adventurers!",
	                "joining_condition_type": 1,
	                "activity_policy_type": 1,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 27,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 88193766,
	                "guild_name": "\u300cExiled Elites\u300d",
	                "guild_emblem_id": 10011,
	                "guild_introduction": "Active Elites Club Lv. 100+ ~ A place for the outcasts bc we too good.",
	                "joining_condition_type": 2,
	                "activity_policy_type": 4,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 23,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 45986022,
	                "guild_name": "\u3069\u3063\u304b\u3093\u3001\u3067\u3059\uff01",
	                "guild_emblem_id": 10029,
	                "guild_introduction": "\u4e00\u7dd2\u306b\u884c\u304d\u307e\u3057\u3087\u301c\uff01",
	                "joining_condition_type": 1,
	                "activity_policy_type": 1,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 7,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 58940198,
	                "guild_name": "\u82b1\u6563\u91cc",
	                "guild_emblem_id": 10004,
	                "guild_introduction": "\u76ee\u6a19\u6240\u6709\u540c\u4f34\u90fd\u80fd\u8f15\u9b06\u73a9\u3000\u4e92\u76f8\u5e6b\u52a9\u958b\u958b\u5fc3\u5fc3\u3000\u6709\u9700\u8981line\u7fa4\u7684\u8a71\u8acb\u8aaa\u3000\u6211\u6703\u5275\u3000\u82e5\u6709\u8208\u8da3\u52a0\u5165\u8acb\u79c1\u6211\u54e6~",
	                "joining_condition_type": 1,
	                "activity_policy_type": 4,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 24,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 42200374,
	                "guild_name": "\u5e1d\u723e\u9b6f",
	                "guild_emblem_id": 10004,
	                "guild_introduction": "\u8acb\u591a\u6307\u6559\uff01",
	                "joining_condition_type": 1,
	                "activity_policy_type": 1,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 3,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 24586294,
	                "guild_name": "Nat20s",
	                "guild_emblem_id": 10018,
	                "guild_introduction": "Hello, fellow adventurers!",
	                "joining_condition_type": 2,
	                "activity_policy_type": 1,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 7,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 63376806,
	                "guild_name": "\u8e66\u8e66\u9a0e\u58eb\u5718",
	                "guild_emblem_id": 10008,
	                "guild_introduction": "\u4f11\u9592\u767b\u5165",
	                "joining_condition_type": 2,
	                "activity_policy_type": 3,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 9,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 13489446,
	                "guild_name": "\u570b\u745c\u52c1\u7206\u76df",
	                "guild_emblem_id": 10014,
	                "guild_introduction": "No\u3000\u570b\u745c\u3000No\u3000Life\u3000!",
	                "joining_condition_type": 1,
	                "activity_policy_type": 3,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 3,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 58173206,
	                "guild_name": "\u8f49\u5427\u8f49\u5427\uff01\u5f69\u8272\u9f8d\u7d46\u65e5",
	                "guild_emblem_id": 10004,
	                "guild_introduction": "\u71b1\u611b\u9f8d\u7d46\u3001\u4eab\u53d7\u9f8d\u7d46\uff0c\u6211\u5011\u6b61\u8fce\u4f60\uff0c\u5927\u5bb6\u90fd\u662f\u5f69\u8272\u9f8d\u7d46\u65e5\u3002\u9019\u88e1\u53ef\u4ee5\u8f15\u9b06\u81ea\u7531\u7684\u73a9\uff0c\u6216\u8005\u662f\u653b\u7565\u771f\u9f8d\u3001\u8a0e\u4f10\u54a2\u7259\uff01\u6709line\u7fa4\uff0c\u6709\u8208\u8da3\u52a0\u5165\u8acb\u548c\u76df\u4e3b\u806f\u7d61\u54e6\uff01",
	                "joining_condition_type": 1,
	                "activity_policy_type": 3,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 25,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 99098790,
	                "guild_name": "\u304a\u4e00\u4eba\u69d8",
	                "guild_emblem_id": 10023,
	                "guild_introduction": "\u3088\u308d\u3057\u304f\u304a\u9858\u3044\u3057\u307e\u3059\uff01",
	                "joining_condition_type": 1,
	                "activity_policy_type": 1,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 3,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 15235398,
	                "guild_name": "Ranzal Support Group",
	                "guild_emblem_id": 10020,
	                "guild_introduction": "Tornado bashu",
	                "joining_condition_type": 1,
	                "activity_policy_type": 1,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 24,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 87010166,
	                "guild_name": "\u8339\u3067\u308b\u306e\u6c11",
	                "guild_emblem_id": 10014,
	                "guild_introduction": "\u3088\u308d\u3057\u304f\u304a\u9858\u3044\u3057\u307e\u3059\uff01",
	                "joining_condition_type": 2,
	                "activity_policy_type": 3,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 1,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 33633494,
	                "guild_name": "\u3069\u3089\u304c\u308a\u5927\u6226\uff01",
	                "guild_emblem_id": 10031,
	                "guild_introduction": "\u6c17\u8efd\u306b\u5165\u4f1a&\u9000\u4f1a\u30aa\u30c3\u30b1\u30fc\u3067\u3059\u3002\u307e\u305a\u306f\u5831\u916c\u3001\u5de1\u56de\u3001\u5171\u95d8\u3092\u697d\u3057\u3093\u3067\u3000\u6163\u308c\u305f\u3089\u72ec\u7acb\u3001\u79fb\u8ee2\u3001\u7d99\u7d9a\u3054\u81ea\u7531\u306b\uff01\u307e\u3063\u305f\u308a\u3001\u52a9\u3051\u5408\u3044\u306e\u30a8\u30f3\u30b8\u30e7\u30a4\u52e2\u3067\u3059",
	                "joining_condition_type": 1,
	                "activity_policy_type": 2,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 10,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            },
	            {
	                "guild_id": 43903318,
	                "guild_name": "\u3080\u306b\u3080\u306b\u53db\u9006\u6226",
	                "guild_emblem_id": 10033,
	                "guild_introduction": "\u3088\u308d\u3057\u304f\u304a\u9858\u3044\u3057\u307e\u3059\uff01",
	                "joining_condition_type": 1,
	                "activity_policy_type": 3,
	                "is_penalty_guild_name": 0,
	                "is_penalty_guild_introduction": 0,
	                "guild_member_count": 4,
	                "guild_board": "",
	                "is_penalty_guild_board": 0
	            }
	        ],
	        "update_data_list": {
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
