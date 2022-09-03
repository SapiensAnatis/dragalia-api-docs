/quest/set_quest_clear_party
============================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com<device_id>
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
	Request-Token: 27883470478903505
	Request-Time: 1661984350
	Content-Type: application/x-msgpack
	X-Unity-Version: 2019.4.31f1
	Content-Length: 2083


Request body
----------------

.. code-block:: json

	{
	    "quest_id": 100010101,
	    "request_party_setting_list": [
	        {
	            "unit_no": 1,
	            "chara_id": 10140101,
	            "equip_weapon_key_id": 0,
	            "equip_dragon_key_id": 19273109,
	            "equip_amulet_key_id": 0,
	            "equip_amulet_2_key_id": 0,
	            "equip_skin_weapon_id": 0,
	            "equip_weapon_body_id": 30129901,
	            "equip_weapon_skin_id": 0,
	            "equip_crest_slot_type_1_crest_id_1": 0,
	            "equip_crest_slot_type_1_crest_id_2": 0,
	            "equip_crest_slot_type_1_crest_id_3": 0,
	            "equip_crest_slot_type_2_crest_id_1": 0,
	            "equip_crest_slot_type_2_crest_id_2": 0,
	            "equip_crest_slot_type_3_crest_id_1": 0,
	            "equip_crest_slot_type_3_crest_id_2": 0,
	            "equip_talisman_key_id": 0,
	            "edit_skill_1_chara_id": 0,
	            "edit_skill_2_chara_id": 0
	        },
	        {
	            "unit_no": 2,
	            "chara_id": 10230101,
	            "equip_weapon_key_id": 0,
	            "equip_dragon_key_id": 19273108,
	            "equip_amulet_key_id": 0,
	            "equip_amulet_2_key_id": 0,
	            "equip_skin_weapon_id": 0,
	            "equip_weapon_body_id": 0,
	            "equip_weapon_skin_id": 0,
	            "equip_crest_slot_type_1_crest_id_1": 0,
	            "equip_crest_slot_type_1_crest_id_2": 0,
	            "equip_crest_slot_type_1_crest_id_3": 0,
	            "equip_crest_slot_type_2_crest_id_1": 0,
	            "equip_crest_slot_type_2_crest_id_2": 0,
	            "equip_crest_slot_type_3_crest_id_1": 0,
	            "equip_crest_slot_type_3_crest_id_2": 0,
	            "equip_talisman_key_id": 0,
	            "edit_skill_1_chara_id": 0,
	            "edit_skill_2_chara_id": 0
	        },
	        {
	            "unit_no": 3,
	            "chara_id": 10630101,
	            "equip_weapon_key_id": 0,
	            "equip_dragon_key_id": 0,
	            "equip_amulet_key_id": 0,
	            "equip_amulet_2_key_id": 0,
	            "equip_skin_weapon_id": 0,
	            "equip_weapon_body_id": 0,
	            "equip_weapon_skin_id": 0,
	            "equip_crest_slot_type_1_crest_id_1": 0,
	            "equip_crest_slot_type_1_crest_id_2": 0,
	            "equip_crest_slot_type_1_crest_id_3": 0,
	            "equip_crest_slot_type_2_crest_id_1": 0,
	            "equip_crest_slot_type_2_crest_id_2": 0,
	            "equip_crest_slot_type_3_crest_id_1": 0,
	            "equip_crest_slot_type_3_crest_id_2": 0,
	            "equip_talisman_key_id": 0,
	            "edit_skill_1_chara_id": 0,
	            "edit_skill_2_chara_id": 0
	        },
	        {
	            "unit_no": 4,
	            "chara_id": 10830101,
	            "equip_weapon_key_id": 0,
	            "equip_dragon_key_id": 19273093,
	            "equip_amulet_key_id": 0,
	            "equip_amulet_2_key_id": 0,
	            "equip_skin_weapon_id": 0,
	            "equip_weapon_body_id": 0,
	            "equip_weapon_skin_id": 0,
	            "equip_crest_slot_type_1_crest_id_1": 0,
	            "equip_crest_slot_type_1_crest_id_2": 0,
	            "equip_crest_slot_type_1_crest_id_3": 0,
	            "equip_crest_slot_type_2_crest_id_1": 0,
	            "equip_crest_slot_type_2_crest_id_2": 0,
	            "equip_crest_slot_type_3_crest_id_1": 0,
	            "equip_crest_slot_type_3_crest_id_2": 0,
	            "equip_talisman_key_id": 0,
	            "edit_skill_1_chara_id": 0,
	            "edit_skill_2_chara_id": 0
	        }
	    ]
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack
	Access-Control-Allow-Origin: *
	Content-Length: 89
	Expires: Wed, 31 Aug 2022 22:19:12 GMT
	Cache-Control: max-age=0, no-cache, no-store
	Pragma: no-cache
	Date: Wed, 31 Aug 2022 22:19:12 GMT
	Connection: keep-alive


Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "result": 1,
	        "update_data_list": {
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
