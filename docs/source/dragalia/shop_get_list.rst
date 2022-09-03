/shop/get_list
============================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com
	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)
	Accept: */*
	Accept-Encoding: deflate, gzip
	App-Ver: 2.19.0
	Device: 2
	Platform: 2
	Carrier: OnePlus
	DeviceId: <device_id>
	DeviceName: OnePlus ONEPLUS A6003
	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)
	GraphicsDeviceName: Adreno (TM) 540
	SID: 5f7d426cb80a8e890ab40e65393ee0280f6b693d1f1080451829653f5434d921
	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862
	Res-Ver: y2XM6giU6zz56wCm
	Request-Token: 27883477776992484
	Request-Time: 1661984786
	Content-Type: application/x-msgpack
	X-Unity-Version: 2019.4.31f1
	Content-Length: 1


Request body
----------------

.. code-block:: json

	{}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack
	Access-Control-Allow-Origin: *
	Content-Length: 11818
	Expires: Wed, 31 Aug 2022 22:26:28 GMT
	Cache-Control: max-age=0, no-cache, no-store
	Pragma: no-cache
	Date: Wed, 31 Aug 2022 22:26:28 GMT
	Connection: keep-alive


Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "is_quest_bonus": 0,
	        "is_stone_bonus": 0,
	        "is_stamina_bonus": 0,
	        "stone_bonus": [],
	        "stamina_bonus": [],
	        "quest_bonus": [],
	        "material_shop_purchase": [],
	        "normal_shop_purchase": [],
	        "special_shop_purchase": [],
	        "product_lock_list": [],
	        "user_item_summon": {
	            "daily_summon_count": 0,
	            "last_summon_time": 0
	        },
	        "product_list": [
	            {
	                "id": 101001,
	                "sku": "com.nintendo.zaga.starter.tier8",
	                "paid_diamond_quantity": 384,
	                "free_diamond_quantity": 1116,
	                "price": 980
	            },
	            {
	                "id": 101002,
	                "sku": "com.nintendo.zaga.pocket.tier10",
	                "paid_diamond_quantity": 480,
	                "free_diamond_quantity": 480,
	                "price": 1220
	            },
	            {
	                "id": 101003,
	                "sku": "com.nintendo.zaga.startdash.tier25",
	                "paid_diamond_quantity": 1200,
	                "free_diamond_quantity": 300,
	                "price": 3060
	            },
	            {
	                "id": 101004,
	                "sku": "com.nintendo.zaga.starter2.tier8",
	                "paid_diamond_quantity": 384,
	                "free_diamond_quantity": 1116,
	                "price": 980
	            },
	            {
	                "id": 101005,
	                "sku": "com.nintendo.zaga.startdash2.tier25",
	                "paid_diamond_quantity": 1200,
	                "free_diamond_quantity": 300,
	                "price": 3060
	            },
	            {
	                "id": 102001,
	                "sku": "com.nintendo.zaga.login.tier10",
	                "paid_diamond_quantity": 480,
	                "free_diamond_quantity": 0,
	                "price": 1220
	            },
	            {
	                "id": 103001,
	                "sku": "com.nintendo.zaga.story.mission.n.tier10",
	                "paid_diamond_quantity": 480,
	                "free_diamond_quantity": 270,
	                "price": 1220
	            },
	            {
	                "id": 103002,
	                "sku": "com.nintendo.zaga.story.mission.h.tier10",
	                "paid_diamond_quantity": 480,
	                "free_diamond_quantity": 270,
	                "price": 1220
	            },
	            {
	                "id": 103003,
	                "sku": "com.nintendo.zaga.chara.mission.tier20",
	                "paid_diamond_quantity": 960,
	                "free_diamond_quantity": 540,
	                "price": 2440
	            },
	            {
	                "id": 103004,
	                "sku": "com.nintendo.zaga.weapon.mission.tier20",
	                "paid_diamond_quantity": 960,
	                "free_diamond_quantity": 540,
	                "price": 2440
	            },
	            {
	                "id": 103005,
	                "sku": "com.nintendo.zaga.dbattle.mission.tier20",
	                "paid_diamond_quantity": 960,
	                "free_diamond_quantity": 540,
	                "price": 2440
	            },
	            {
	                "id": 103007,
	                "sku": "com.nintendo.zaga.story2.mission.n.tier10",
	                "paid_diamond_quantity": 480,
	                "free_diamond_quantity": 270,
	                "price": 1220
	            },
	            {
	                "id": 103008,
	                "sku": "com.nintendo.zaga.story2.mission.h.tier10",
	                "paid_diamond_quantity": 480,
	                "free_diamond_quantity": 270,
	                "price": 1220
	            },
	            {
	                "id": 103009,
	                "sku": "com.nintendo.zaga.chara2.mission.tier20",
	                "paid_diamond_quantity": 960,
	                "free_diamond_quantity": 540,
	                "price": 2440
	            },
	            {
	                "id": 104001,
	                "sku": "com.nintendo.zaga.2019.newyearpack1.tier8",
	                "paid_diamond_quantity": 384,
	                "free_diamond_quantity": 116,
	                "price": 980
	            },
	            {
	                "id": 104002,
	                "sku": "com.nintendo.zaga.2019.newyearpack2.tier10",
	                "paid_diamond_quantity": 480,
	                "free_diamond_quantity": 480,
	                "price": 1220
	            },
	            {
	                "id": 104003,
	                "sku": "com.nintendo.zaga.2019.newyearpack3.tier40",
	                "paid_diamond_quantity": 1920,
	                "free_diamond_quantity": 80,
	                "price": 4900
	            },
	            {
	                "id": 104004,
	                "sku": "com.nintendo.zaga.2019.newyearpack4.tier40",
	                "paid_diamond_quantity": 1920,
	                "free_diamond_quantity": 80,
	                "price": 4900
	            },
	            {
	                "id": 104005,
	                "sku": "com.nintendo.zaga.2019.newyearpack5.tier56",
	                "paid_diamond_quantity": 3920,
	                "free_diamond_quantity": 580,
	                "price": 10000
	            },
	            {
	                "id": 104006,
	                "sku": "com.nintendo.zaga.2019.newyearpack6.tier25",
	                "paid_diamond_quantity": 1200,
	                "free_diamond_quantity": 300,
	                "price": 3060
	            },
	            {
	                "id": 104007,
	                "sku": "com.nintendo.zaga.2019.newyearpack7.tier25",
	                "paid_diamond_quantity": 1200,
	                "free_diamond_quantity": 300,
	                "price": 3060
	            },
	            {
	                "id": 104008,
	                "sku": "com.nintendo.zaga.20190426pack1.tier25",
	                "paid_diamond_quantity": 1200,
	                "free_diamond_quantity": 300,
	                "price": 3060
	            },
	            {
	                "id": 104009,
	                "sku": "com.nintendo.zaga.20190426pack2.tier4",
	                "paid_diamond_quantity": 192,
	                "free_diamond_quantity": 8,
	                "price": 490
	            },
	            {
	                "id": 104010,
	                "sku": "com.nintendo.zaga.20190731pack1.tier25",
	                "paid_diamond_quantity": 1200,
	                "free_diamond_quantity": 30,
	                "price": 3060
	            },
	            {
	                "id": 104011,
	                "sku": "com.nintendo.zaga.20190731pack2.tier40",
	                "paid_diamond_quantity": 1920,
	                "free_diamond_quantity": 480,
	                "price": 4900
	            },
	            {
	                "id": 104012,
	                "sku": "com.nintendo.zaga.20190813pack1.tier25",
	                "paid_diamond_quantity": 1200,
	                "free_diamond_quantity": 30,
	                "price": 3060
	            },
	            {
	                "id": 104013,
	                "sku": "com.nintendo.zaga.20190813pack2.tier40",
	                "paid_diamond_quantity": 1920,
	                "free_diamond_quantity": 480,
	                "price": 4900
	            },
	            {
	                "id": 104014,
	                "sku": "com.nintendo.zaga.20190927pack1.tier4",
	                "paid_diamond_quantity": 192,
	                "free_diamond_quantity": 108,
	                "price": 490
	            },
	            {
	                "id": 104015,
	                "sku": "com.nintendo.zaga.20190927pack2.tier25",
	                "paid_diamond_quantity": 1200,
	                "free_diamond_quantity": 300,
	                "price": 3060
	            },
	            {
	                "id": 104016,
	                "sku": "com.nintendo.zaga.20190927pack3.tier25",
	                "paid_diamond_quantity": 1200,
	                "free_diamond_quantity": 300,
	                "price": 3060
	            },
	            {
	                "id": 104017,
	                "sku": "com.nintendo.zaga.20190927pack4.tier25",
	                "paid_diamond_quantity": 1200,
	                "free_diamond_quantity": 300,
	                "price": 3060
	            },
	            {
	                "id": 104018,
	                "sku": "com.nintendo.zaga.20190927pack5.tier40",
	                "paid_diamond_quantity": 1920,
	                "free_diamond_quantity": 480,
	                "price": 4900
	            },
	            {
	                "id": 104019,
	                "sku": "com.nintendo.zaga.20190927pack6.tier56",
	                "paid_diamond_quantity": 3920,
	                "free_diamond_quantity": 880,
	                "price": 10000
	            },
	            {
	                "id": 104021,
	                "sku": "com.nintendo.zaga.20191128pack1.tier40",
	                "paid_diamond_quantity": 1920,
	                "free_diamond_quantity": 480,
	                "price": 4900
	            },
	            {
	                "id": 104022,
	                "sku": "com.nintendo.zaga.20191128pack2.tier25",
	                "paid_diamond_quantity": 1200,
	                "free_diamond_quantity": 30,
	                "price": 3060
	            },
	            {
	                "id": 104023,
	                "sku": "com.nintendo.zaga.20191128pack3.tier25",
	                "paid_diamond_quantity": 1200,
	                "free_diamond_quantity": 30,
	                "price": 3060
	            },
	            {
	                "id": 104031,
	                "sku": "com.nintendo.zaga.20191231pack1.tier8",
	                "paid_diamond_quantity": 384,
	                "free_diamond_quantity": 116,
	                "price": 980
	            },
	            {
	                "id": 104032,
	                "sku": "com.nintendo.zaga.20191231pack2.tier56",
	                "paid_diamond_quantity": 3920,
	                "free_diamond_quantity": 580,
	                "price": 10000
	            },
	            {
	                "id": 104033,
	                "sku": "com.nintendo.zaga.20191231pack3.tier25",
	                "paid_diamond_quantity": 1200,
	                "free_diamond_quantity": 30,
	                "price": 3060
	            },
	            {
	                "id": 104034,
	                "sku": "com.nintendo.zaga.20191231pack4.tier25",
	                "paid_diamond_quantity": 1200,
	                "free_diamond_quantity": 30,
	                "price": 3060
	            },
	            {
	                "id": 104035,
	                "sku": "com.nintendo.zaga.20191231pack5.tier10",
	                "paid_diamond_quantity": 480,
	                "free_diamond_quantity": 480,
	                "price": 1220
	            },
	            {
	                "id": 104041,
	                "sku": "com.nintendo.zaga.20200129pack1.tier40",
	                "paid_diamond_quantity": 1920,
	                "free_diamond_quantity": 480,
	                "price": 4900
	            },
	            {
	                "id": 104042,
	                "sku": "com.nintendo.zaga.20200129pack2.tier40",
	                "paid_diamond_quantity": 1920,
	                "free_diamond_quantity": 480,
	                "price": 4900
	            },
	            {
	                "id": 104043,
	                "sku": "com.nintendo.zaga.20200129pack3.tier4",
	                "paid_diamond_quantity": 192,
	                "free_diamond_quantity": 108,
	                "price": 490
	            },
	            {
	                "id": 104044,
	                "sku": "com.nintendo.zaga.20200129pack4.tier25",
	                "paid_diamond_quantity": 1200,
	                "free_diamond_quantity": 30,
	                "price": 3060
	            },
	            {
	                "id": 104045,
	                "sku": "com.nintendo.zaga.20200129pack5.tier40",
	                "paid_diamond_quantity": 1920,
	                "free_diamond_quantity": 480,
	                "price": 4900
	            },
	            {
	                "id": 104046,
	                "sku": "com.nintendo.zaga.20200129pack6.tier25",
	                "paid_diamond_quantity": 1200,
	                "free_diamond_quantity": 30,
	                "price": 3060
	            },
	            {
	                "id": 104051,
	                "sku": "com.nintendo.zaga.20200327pack1.tier25",
	                "paid_diamond_quantity": 1200,
	                "free_diamond_quantity": 300,
	                "price": 3060
	            },
	            {
	                "id": 104058,
	                "sku": "com.nintendo.zaga.20200327pack8.tier56",
	                "paid_diamond_quantity": 3920,
	                "free_diamond_quantity": 880,
	                "price": 10000
	            },
	            {
	                "id": 104061,
	                "sku": "com.nintendo.zaga.20200430pack1.tier56",
	                "paid_diamond_quantity": 3920,
	                "free_diamond_quantity": 880,
	                "price": 10000
	            },
	            {
	                "id": 104062,
	                "sku": "com.nintendo.zaga.20200430pack2.tier25",
	                "paid_diamond_quantity": 1200,
	                "free_diamond_quantity": 300,
	                "price": 3060
	            },
	            {
	                "id": 104067,
	                "sku": "com.nintendo.zaga.20200507pack7.tier10",
	                "paid_diamond_quantity": 480,
	                "free_diamond_quantity": 220,
	                "price": 1220
	            },
	            {
	                "id": 104071,
	                "sku": "com.nintendo.zaga.20200601pack1.tier25",
	                "paid_diamond_quantity": 1200,
	                "free_diamond_quantity": 300,
	                "price": 3060
	            },
	            {
	                "id": 104084,
	                "sku": "com.nintendo.zaga.20200730pack4.tier56",
	                "paid_diamond_quantity": 3920,
	                "free_diamond_quantity": 1780,
	                "price": 10000
	            },
	            {
	                "id": 104091,
	                "sku": "com.nintendo.zaga.20200927pack1.tier56",
	                "paid_diamond_quantity": 3920,
	                "free_diamond_quantity": 1780,
	                "price": 10000
	            },
	            {
	                "id": 104092,
	                "sku": "com.nintendo.zaga.20200927pack2.tier56",
	                "paid_diamond_quantity": 3920,
	                "free_diamond_quantity": 880,
	                "price": 10000
	            },
	            {
	                "id": 104093,
	                "sku": "com.nintendo.zaga.20200927pack3.tier56",
	                "paid_diamond_quantity": 3920,
	                "free_diamond_quantity": 880,
	                "price": 10000
	            },
	            {
	                "id": 104111,
	                "sku": "com.nintendo.zaga.20210131pack1.tier56",
	                "paid_diamond_quantity": 3920,
	                "free_diamond_quantity": 1780,
	                "price": 10000
	            },
	            {
	                "id": 104112,
	                "sku": "com.nintendo.zaga.20210131pack2.tier56",
	                "paid_diamond_quantity": 3920,
	                "free_diamond_quantity": 880,
	                "price": 10000
	            },
	            {
	                "id": 104113,
	                "sku": "com.nintendo.zaga.20210131pack3.tier40",
	                "paid_diamond_quantity": 1920,
	                "free_diamond_quantity": 480,
	                "price": 4900
	            },
	            {
	                "id": 104117,
	                "sku": "com.nintendo.zaga.20210131pack7.tier17",
	                "paid_diamond_quantity": 840,
	                "free_diamond_quantity": 360,
	                "price": 2080
	            },
	            {
	                "id": 104141,
	                "sku": "com.nintendo.zaga.20210927pack1.tier56",
	                "paid_diamond_quantity": 3920,
	                "free_diamond_quantity": 1780,
	                "price": 10000
	            },
	            {
	                "id": 104143,
	                "sku": "com.nintendo.zaga.20210927pack3.tier56",
	                "paid_diamond_quantity": 3920,
	                "free_diamond_quantity": 880,
	                "price": 10000
	            },
	            {
	                "id": 104145,
	                "sku": "com.nintendo.zaga.20210927pack5.tier25",
	                "paid_diamond_quantity": 1200,
	                "free_diamond_quantity": 300,
	                "price": 3060
	            },
	            {
	                "id": 104151,
	                "sku": "com.nintendo.zaga.20211231pack1.tier56",
	                "paid_diamond_quantity": 3920,
	                "free_diamond_quantity": 880,
	                "price": 10000
	            },
	            {
	                "id": 104152,
	                "sku": "com.nintendo.zaga.20211231pack7.tier56",
	                "paid_diamond_quantity": 3920,
	                "free_diamond_quantity": 1780,
	                "price": 10000
	            },
	            {
	                "id": 104154,
	                "sku": "com.nintendo.zaga.20211231pack4.tier40",
	                "paid_diamond_quantity": 1920,
	                "free_diamond_quantity": 480,
	                "price": 4900
	            },
	            {
	                "id": 104161,
	                "sku": "com.nintendo.zaga.20220327pack1.tier56",
	                "paid_diamond_quantity": 3920,
	                "free_diamond_quantity": 1780,
	                "price": 10000
	            },
	            {
	                "id": 104162,
	                "sku": "com.nintendo.zaga.20220327pack2.tier56",
	                "paid_diamond_quantity": 3920,
	                "free_diamond_quantity": 880,
	                "price": 10000
	            },
	            {
	                "id": 104163,
	                "sku": "com.nintendo.zaga.20220327pack3.tier56",
	                "paid_diamond_quantity": 3920,
	                "free_diamond_quantity": 880,
	                "price": 10000
	            },
	            {
	                "id": 202001,
	                "sku": "com.nintendo.zaga.flame.resource.pack.tier8",
	                "paid_diamond_quantity": 384,
	                "free_diamond_quantity": 16,
	                "price": 980
	            },
	            {
	                "id": 202002,
	                "sku": "com.nintendo.zaga.water.resource.pack.tier8",
	                "paid_diamond_quantity": 384,
	                "free_diamond_quantity": 16,
	                "price": 980
	            },
	            {
	                "id": 202003,
	                "sku": "com.nintendo.zaga.wind.resource.pack.tier8",
	                "paid_diamond_quantity": 384,
	                "free_diamond_quantity": 16,
	                "price": 980
	            },
	            {
	                "id": 202004,
	                "sku": "com.nintendo.zaga.light.resource.pack.tier8",
	                "paid_diamond_quantity": 384,
	                "free_diamond_quantity": 16,
	                "price": 980
	            },
	            {
	                "id": 202005,
	                "sku": "com.nintendo.zaga.shadow.resource.pack.tier8",
	                "paid_diamond_quantity": 384,
	                "free_diamond_quantity": 16,
	                "price": 980
	            },
	            {
	                "id": 202006,
	                "sku": "com.nintendo.zaga.weapon.strength.pack.tier8",
	                "paid_diamond_quantity": 384,
	                "free_diamond_quantity": 16,
	                "price": 980
	            },
	            {
	                "id": 202008,
	                "sku": "com.nintendo.zaga.chara.traning.pack.tier8",
	                "paid_diamond_quantity": 384,
	                "free_diamond_quantity": 16,
	                "price": 980
	            },
	            {
	                "id": 202016,
	                "sku": "com.nintendo.zaga.flame.resource.20190701.pack.tier8",
	                "paid_diamond_quantity": 384,
	                "free_diamond_quantity": 16,
	                "price": 980
	            },
	            {
	                "id": 202017,
	                "sku": "com.nintendo.zaga.water.resource.20190701.pack.tier8",
	                "paid_diamond_quantity": 384,
	                "free_diamond_quantity": 16,
	                "price": 980
	            },
	            {
	                "id": 202018,
	                "sku": "com.nintendo.zaga.wind.resource.20190701.pack.tier8",
	                "paid_diamond_quantity": 384,
	                "free_diamond_quantity": 16,
	                "price": 980
	            },
	            {
	                "id": 202019,
	                "sku": "com.nintendo.zaga.light.resource.20190701.pack.tier8",
	                "paid_diamond_quantity": 384,
	                "free_diamond_quantity": 16,
	                "price": 980
	            },
	            {
	                "id": 202020,
	                "sku": "com.nintendo.zaga.shadow.resource.20190701.pack.tier8",
	                "paid_diamond_quantity": 384,
	                "free_diamond_quantity": 16,
	                "price": 980
	            },
	            {
	                "id": 202021,
	                "sku": "com.nintendo.zaga.dragon.strength.20190701.pack.tier8",
	                "paid_diamond_quantity": 384,
	                "free_diamond_quantity": 16,
	                "price": 980
	            },
	            {
	                "id": 202022,
	                "sku": "com.nintendo.zaga.amulet.strength.20190701.pack.tier8",
	                "paid_diamond_quantity": 384,
	                "free_diamond_quantity": 16,
	                "price": 980
	            },
	            {
	                "id": 202023,
	                "sku": "com.nintendo.zaga.weapon.strength.20190701.pack.tier8",
	                "paid_diamond_quantity": 384,
	                "free_diamond_quantity": 16,
	                "price": 980
	            },
	            {
	                "id": 202024,
	                "sku": "com.nintendo.zaga.chara.traning.20190701.pack.tier8",
	                "paid_diamond_quantity": 384,
	                "free_diamond_quantity": 16,
	                "price": 980
	            },
	            {
	                "id": 203001,
	                "sku": "com.nintendo.zaga.weapon.release.tier40",
	                "paid_diamond_quantity": 1920,
	                "free_diamond_quantity": 80,
	                "price": 4900
	            },
	            {
	                "id": 203002,
	                "sku": "com.nintendo.zaga.dragon.release.tier40",
	                "paid_diamond_quantity": 1920,
	                "free_diamond_quantity": 80,
	                "price": 4900
	            },
	            {
	                "id": 203003,
	                "sku": "com.nintendo.zaga.amulet.release.tier40",
	                "paid_diamond_quantity": 1920,
	                "free_diamond_quantity": 80,
	                "price": 4900
	            },
	            {
	                "id": 203004,
	                "sku": "com.nintendo.zaga.manacircle.release.tier40",
	                "paid_diamond_quantity": 1920,
	                "free_diamond_quantity": 80,
	                "price": 4900
	            },
	            {
	                "id": 203006,
	                "sku": "com.nintendo.zaga.weapon6.release.tier40",
	                "paid_diamond_quantity": 1920,
	                "free_diamond_quantity": 80,
	                "price": 4900
	            },
	            {
	                "id": 203007,
	                "sku": "com.nintendo.zaga.weapon.20201101.release.tier40",
	                "paid_diamond_quantity": 1920,
	                "free_diamond_quantity": 80,
	                "price": 4900
	            },
	            {
	                "id": 301001,
	                "sku": "com.nintendo.zaga.tier1",
	                "paid_diamond_quantity": 48,
	                "free_diamond_quantity": 0,
	                "price": 120
	            },
	            {
	                "id": 301002,
	                "sku": "com.nintendo.zaga.tier4",
	                "paid_diamond_quantity": 192,
	                "free_diamond_quantity": 1,
	                "price": 490
	            },
	            {
	                "id": 301003,
	                "sku": "com.nintendo.zaga.tier10",
	                "paid_diamond_quantity": 480,
	                "free_diamond_quantity": 4,
	                "price": 1220
	            },
	            {
	                "id": 301004,
	                "sku": "com.nintendo.zaga.tier20",
	                "paid_diamond_quantity": 960,
	                "free_diamond_quantity": 20,
	                "price": 2440
	            },
	            {
	                "id": 301005,
	                "sku": "com.nintendo.zaga.tier32",
	                "paid_diamond_quantity": 1520,
	                "free_diamond_quantity": 40,
	                "price": 3920
	            },
	            {
	                "id": 301006,
	                "sku": "com.nintendo.zaga.tier40",
	                "paid_diamond_quantity": 1920,
	                "free_diamond_quantity": 80,
	                "price": 4900
	            },
	            {
	                "id": 301007,
	                "sku": "com.nintendo.zaga.tier56",
	                "paid_diamond_quantity": 3920,
	                "free_diamond_quantity": 280,
	                "price": 10000
	            },
	            {
	                "id": 301008,
	                "sku": "com.nintendo.zaga.weekly.tier1",
	                "paid_diamond_quantity": 48,
	                "free_diamond_quantity": 27,
	                "price": 120
	            },
	            {
	                "id": 301009,
	                "sku": "com.nintendo.zaga.weekly.tier2",
	                "paid_diamond_quantity": 96,
	                "free_diamond_quantity": 54,
	                "price": 250
	            },
	            {
	                "id": 301010,
	                "sku": "com.nintendo.zaga.weekly.tier4",
	                "paid_diamond_quantity": 192,
	                "free_diamond_quantity": 108,
	                "price": 490
	            },
	            {
	                "id": 301011,
	                "sku": "com.nintendo.zaga.tier25",
	                "paid_diamond_quantity": 1200,
	                "free_diamond_quantity": 30,
	                "price": 3060
	            }
	        ],
	        "infancy_paid_diamond_limit": 4800,
	        "update_data_list": {
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
