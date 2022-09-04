/party/update_party_name
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: ce498daff57c3b6b8464d1172b4cc0043b75a80296a53d9a92f0297ad85d7c77	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27888785886808762	Request-Time: 1662301175	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 30

Request body
----------------

.. code-block:: json

	{
	    "party_no": 1,
	    "party_name": "Team 1a"
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 1863	Expires: Sun, 04 Sep 2022 14:19:37 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sun, 04 Sep 2022 14:19:37 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "update_data_list": {
	            "party_list": [
	                {
	                    "party_no": 1,
	                    "party_name": "Team 1a",
	                    "party_setting_list": [
	                        {
	                            "unit_no": 1,
	                            "chara_id": 10140101,
	                            "equip_dragon_key_id": 19126830,
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
	                            "edit_skill_1_chara_id": 10540201,
	                            "edit_skill_2_chara_id": 10440301
	                        },
	                        {
	                            "unit_no": 2,
	                            "chara_id": 10830101,
	                            "equip_dragon_key_id": 19126822,
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
	                            "edit_skill_1_chara_id": 10840501,
	                            "edit_skill_2_chara_id": 10440301
	                        },
	                        {
	                            "unit_no": 3,
	                            "chara_id": 10130102,
	                            "equip_dragon_key_id": 19126832,
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
	                            "edit_skill_1_chara_id": 10840501,
	                            "edit_skill_2_chara_id": 10440301
	                        },
	                        {
	                            "unit_no": 4,
	                            "chara_id": 10850403,
	                            "equip_dragon_key_id": 19126829,
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
	                            "edit_skill_1_chara_id": 10840501,
	                            "edit_skill_2_chara_id": 10440301
	                        }
	                    ]
	                }
	            ],
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
