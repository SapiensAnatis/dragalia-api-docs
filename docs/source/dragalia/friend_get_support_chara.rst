/friend/get_support_chara
============================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: 94e58eeb39e0f05c528aa0582d4032f8	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: 5f7d426cb80a8e890ab40e65393ee0280f6b693d1f1080451829653f5434d921	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27883481535088877	Request-Time: 1661985010	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 1

Request body
----------------

.. code-block:: json

	{}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 485	Expires: Wed, 31 Aug 2022 22:30:11 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Wed, 31 Aug 2022 22:30:11 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "result": 1,
	        "setting_support": {
	            "last_active_time": 1661984335,
	            "chara_id": 10140101,
	            "equip_dragon_key_id": 0,
	            "equip_weapon_body_id": 0,
	            "equip_crest_slot_type_1_crest_id_1": 0,
	            "equip_crest_slot_type_1_crest_id_2": 0,
	            "equip_crest_slot_type_1_crest_id_3": 0,
	            "equip_crest_slot_type_2_crest_id_1": 0,
	            "equip_crest_slot_type_2_crest_id_2": 0,
	            "equip_crest_slot_type_3_crest_id_1": 0,
	            "equip_crest_slot_type_3_crest_id_2": 0,
	            "equip_talisman_key_id": 0,
	            "user_level_group": 0
	        },
	        "update_data_list": {
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
