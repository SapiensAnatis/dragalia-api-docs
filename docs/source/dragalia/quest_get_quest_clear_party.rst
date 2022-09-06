/quest/get_quest_clear_party
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
	Request-Token: 27883461318543553
	Request-Time: 1661983805
	Content-Type: application/x-msgpack
	X-Unity-Version: 2019.4.31f1
	Content-Length: 15


Request body
----------------

.. code-block:: json

	{
	    "quest_id": 100010101
	}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack
	Access-Control-Allow-Origin: *
	Content-Length: 129
	Expires: Wed, 31 Aug 2022 22:10:07 GMT
	Cache-Control: max-age=0, no-cache, no-store
	Pragma: no-cache
	Date: Wed, 31 Aug 2022 22:10:07 GMT
	Connection: keep-alive


Response
----------------

.. code-block:: json

	{
		"data_headers": {
			"result_code": 1
		},
		"data": {
			"quest_clear_party_setting_list": [
				{
					"unit_no": 1,
					"chara_id": 10950403,
					"equip_dragon_key_id": 9076602,
					"equip_weapon_body_id": 30960401,
					"equip_weapon_skin_id": 0,
					"equip_crest_slot_type_1_crest_id_1": 40050106,
					"equip_crest_slot_type_1_crest_id_2": 40050105,
					"equip_crest_slot_type_1_crest_id_3": 40050130,
					"equip_crest_slot_type_2_crest_id_1": 40040090,
					"equip_crest_slot_type_2_crest_id_2": 40040091,
					"equip_crest_slot_type_3_crest_id_1": 40090012,
					"equip_crest_slot_type_3_crest_id_2": 40090004,
					"equip_talisman_key_id": 0,
					"edit_skill_1_chara_id": 0,
					"edit_skill_2_chara_id": 10650505
				},
				{
					"unit_no": 2,
					"chara_id": 10650403,
					"equip_dragon_key_id": 17598662,
					"equip_weapon_body_id": 30660401,
					"equip_weapon_skin_id": 0,
					"equip_crest_slot_type_1_crest_id_1": 40050147,
					"equip_crest_slot_type_1_crest_id_2": 40050130,
					"equip_crest_slot_type_1_crest_id_3": 40050076,
					"equip_crest_slot_type_2_crest_id_1": 40040058,
					"equip_crest_slot_type_2_crest_id_2": 40040003,
					"equip_crest_slot_type_3_crest_id_1": 40090007,
					"equip_crest_slot_type_3_crest_id_2": 40090002,
					"equip_talisman_key_id": 0,
					"edit_skill_1_chara_id": 10840501,
					"edit_skill_2_chara_id": 10440301
				},
				{
					"unit_no": 3,
					"chara_id": 10250402,
					"equip_dragon_key_id": 18111961,
					"equip_weapon_body_id": 30260401,
					"equip_weapon_skin_id": 0,
					"equip_crest_slot_type_1_crest_id_1": 40050130,
					"equip_crest_slot_type_1_crest_id_2": 40050122,
					"equip_crest_slot_type_1_crest_id_3": 40050067,
					"equip_crest_slot_type_2_crest_id_1": 40040080,
					"equip_crest_slot_type_2_crest_id_2": 40040100,
					"equip_crest_slot_type_3_crest_id_1": 40090001,
					"equip_crest_slot_type_3_crest_id_2": 40090007,
					"equip_talisman_key_id": 0,
					"edit_skill_1_chara_id": 10840501,
					"edit_skill_2_chara_id": 10440301
				},
				{
					"unit_no": 4,
					"chara_id": 10850401,
					"equip_dragon_key_id": 7442475,
					"equip_weapon_body_id": 30860401,
					"equip_weapon_skin_id": 0,
					"equip_crest_slot_type_1_crest_id_1": 40050008,
					"equip_crest_slot_type_1_crest_id_2": 40050147,
					"equip_crest_slot_type_1_crest_id_3": 40050020,
					"equip_crest_slot_type_2_crest_id_1": 40040062,
					"equip_crest_slot_type_2_crest_id_2": 40030004,
					"equip_crest_slot_type_3_crest_id_1": 40090018,
					"equip_crest_slot_type_3_crest_id_2": 40090024,
					"equip_talisman_key_id": 2307,
					"edit_skill_1_chara_id": 10840501,
					"edit_skill_2_chara_id": 10440301
				},
				{
					"unit_no": 5,
					"chara_id": 10840202,
					"equip_dragon_key_id": 7868063,
					"equip_weapon_body_id": 30860201,
					"equip_weapon_skin_id": 0,
					"equip_crest_slot_type_1_crest_id_1": 40050008,
					"equip_crest_slot_type_1_crest_id_2": 40050070,
					"equip_crest_slot_type_1_crest_id_3": 40050109,
					"equip_crest_slot_type_2_crest_id_1": 40040062,
					"equip_crest_slot_type_2_crest_id_2": 40030004,
					"equip_crest_slot_type_3_crest_id_1": 40090018,
					"equip_crest_slot_type_3_crest_id_2": 40090022,
					"equip_talisman_key_id": 0,
					"edit_skill_1_chara_id": 10850502,
					"edit_skill_2_chara_id": 10150201
				},
				{
					"unit_no": 6,
					"chara_id": 10250203,
					"equip_dragon_key_id": 14557772,
					"equip_weapon_body_id": 30260201,
					"equip_weapon_skin_id": 0,
					"equip_crest_slot_type_1_crest_id_1": 40050067,
					"equip_crest_slot_type_1_crest_id_2": 40050100,
					"equip_crest_slot_type_1_crest_id_3": 40050090,
					"equip_crest_slot_type_2_crest_id_1": 40040100,
					"equip_crest_slot_type_2_crest_id_2": 40040048,
					"equip_crest_slot_type_3_crest_id_1": 40090002,
					"equip_crest_slot_type_3_crest_id_2": 40090001,
					"equip_talisman_key_id": 0,
					"edit_skill_1_chara_id": 10550101,
					"edit_skill_2_chara_id": 10850502
				},
				{
					"unit_no": 7,
					"chara_id": 10150201,
					"equip_dragon_key_id": 4905892,
					"equip_weapon_body_id": 30160201,
					"equip_weapon_skin_id": 0,
					"equip_crest_slot_type_1_crest_id_1": 40050145,
					"equip_crest_slot_type_1_crest_id_2": 40050058,
					"equip_crest_slot_type_1_crest_id_3": 40050067,
					"equip_crest_slot_type_2_crest_id_1": 40040048,
					"equip_crest_slot_type_2_crest_id_2": 40040003,
					"equip_crest_slot_type_3_crest_id_1": 40090001,
					"equip_crest_slot_type_3_crest_id_2": 40090002,
					"equip_talisman_key_id": 766,
					"edit_skill_1_chara_id": 10840501,
					"edit_skill_2_chara_id": 10440301
				},
				{
					"unit_no": 8,
					"chara_id": 10450202,
					"equip_dragon_key_id": 13714264,
					"equip_weapon_body_id": 30460201,
					"equip_weapon_skin_id": 0,
					"equip_crest_slot_type_1_crest_id_1": 40050100,
					"equip_crest_slot_type_1_crest_id_2": 40050066,
					"equip_crest_slot_type_1_crest_id_3": 40050020,
					"equip_crest_slot_type_2_crest_id_1": 40030004,
					"equip_crest_slot_type_2_crest_id_2": 40040072,
					"equip_crest_slot_type_3_crest_id_1": 40090007,
					"equip_crest_slot_type_3_crest_id_2": 40090029,
					"equip_talisman_key_id": 0,
					"edit_skill_1_chara_id": 10550101,
					"edit_skill_2_chara_id": 10150201
				}
			],
			"lost_unit_list": [
				{
					"unit_no": 1,
					"entity_type": 41,
					"entity_id": 50950401
				},
				{
					"unit_no": 2,
					"entity_type": 41,
					"entity_id": 50150503
				},
				{
					"unit_no": 3,
					"entity_type": 41,
					"entity_id": 50950401
				}
			],
			"update_data_list": {
				"functional_maintenance_list": [
				]
			}
		}
	}

Notes
------

- The above response is for a master Sinister Dominion quest, hence the 8 units.
- In this case, lost_unit_list likely referred to some Kaleidoscape prints I no longer had, but it could also extend to dragons.