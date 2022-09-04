/repeat/end
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com	User-Agent: UnityPlayer/2019.4.31f1 (UnityWebRequest/1.0, libcurl/7.75.0-DEV)	Accept: */*	Accept-Encoding: deflate, gzip	App-Ver: 2.19.0	Device: 2	Platform: 2	Carrier: OnePlus	DeviceId: <device_id>	DeviceName: OnePlus ONEPLUS A6003	OS-Version: Android OS 11 / API-30 (RQ3A.210905.001/3c09da6222)	GraphicsDeviceName: Adreno (TM) 540	SID: 0d529f74bec02cbdd6ed8e24f91f5d1a3c8aae212bdd684643033eef032f2d95	Deploy-Hash: 13bb2827ce9e6a66015ac2808112e3442740e862	Res-Ver: y2XM6giU6zz56wCm	Request-Token: 27888750923090459	Request-Time: 1662299091	Content-Type: application/x-msgpack	X-Unity-Version: 2019.4.31f1	Content-Length: 1

Request body
----------------

.. code-block:: json

	{}

Response headers
----------------

.. code-block:: text

	Content-Type: application/x-msgpack	Access-Control-Allow-Origin: *	Content-Length: 2950	Expires: Sun, 04 Sep 2022 13:44:53 GMT	Cache-Control: max-age=0, no-cache, no-store	Pragma: no-cache	Date: Sun, 04 Sep 2022 13:44:53 GMT	Connection: keep-alive

Response
----------------

.. code-block:: json

	{
	    "data_headers": {
	        "result_code": 1
	    },
	    "data": {
	        "ingame_result_data": {
	            "dungeon_key": "0598ffdea30ae4702626c874720e180627b22140",
	            "play_type": 1,
	            "quest_id": 100010101,
	            "start_time": 1662299048,
	            "end_time": 0,
	            "is_clear": 0,
	            "state": 1,
	            "is_host": 1,
	            "is_fever_time": 0,
	            "wave_count": 0,
	            "reborn_count": 0,
	            "current_play_count": 1,
	            "reward_record": {
	                "drop_all": [
	                    {
	                        "type": 8,
	                        "id": 101001001,
	                        "quantity": 4,
	                        "place": 0
	                    },
	                    {
	                        "type": 8,
	                        "id": 202001001,
	                        "quantity": 4,
	                        "place": 0
	                    },
	                    {
	                        "type": 8,
	                        "id": 104001031,
	                        "quantity": 2,
	                        "place": 0
	                    }
	                ],
	                "first_clear_set": [],
	                "quest_bonus_list": [],
	                "reborn_bonus": [],
	                "weekly_limit_reward_list": [],
	                "challenge_quest_bonus_list": [],
	                "campaign_extra_reward_list": [],
	                "shop_quest_bonus_factor": 0,
	                "mission_complete": [],
	                "missions_clear_set": [],
	                "enemy_piece": [],
	                "take_coin": 377,
	                "take_accumulate_point": 0,
	                "take_boost_accumulate_point": 0,
	                "player_level_up_fstone": 0,
	                "first_meeting": [],
	                "take_astral_item_quantity": 2,
	                "carry_bonus": []
	            },
	            "grow_record": {
	                "take_player_exp": 60,
	                "take_chara_exp": 480,
	                "take_mana": 89,
	                "bonus_factor": 1,
	                "mana_bonus_factor": 1,
	                "chara_grow_record": [
	                    {
	                        "chara_id": 10140101,
	                        "take_exp": 480
	                    },
	                    {
	                        "chara_id": 10230101,
	                        "take_exp": 480
	                    },
	                    {
	                        "chara_id": 10130102,
	                        "take_exp": 480
	                    },
	                    {
	                        "chara_id": 10830101,
	                        "take_exp": 480
	                    }
	                ],
	                "chara_friendship_list": []
	            },
	            "event_passive_up_list": [],
	            "quest_party_setting_list": [
	                {
	                    "unit_no": 1,
	                    "chara_id": 10140101,
	                    "equip_dragon_key_id": 19126830,
	                    "equip_weapon_body_id": 30129901,
	                    "equip_weapon_skin_id": 0,
	                    "equip_talisman_key_id": 0,
	                    "equip_crest_slot_type_1_crest_id_1": 0,
	                    "equip_crest_slot_type_1_crest_id_2": 0,
	                    "equip_crest_slot_type_1_crest_id_3": 0,
	                    "equip_crest_slot_type_2_crest_id_1": 0,
	                    "equip_crest_slot_type_2_crest_id_2": 0,
	                    "equip_crest_slot_type_3_crest_id_1": 0,
	                    "equip_crest_slot_type_3_crest_id_2": 0,
	                    "edit_skill_1_chara_id": 0,
	                    "edit_skill_2_chara_id": 0
	                },
	                {
	                    "unit_no": 2,
	                    "chara_id": 10230101,
	                    "equip_dragon_key_id": 19126835,
	                    "equip_weapon_body_id": 0,
	                    "equip_weapon_skin_id": 0,
	                    "equip_talisman_key_id": 0,
	                    "equip_crest_slot_type_1_crest_id_1": 0,
	                    "equip_crest_slot_type_1_crest_id_2": 0,
	                    "equip_crest_slot_type_1_crest_id_3": 0,
	                    "equip_crest_slot_type_2_crest_id_1": 0,
	                    "equip_crest_slot_type_2_crest_id_2": 0,
	                    "equip_crest_slot_type_3_crest_id_1": 0,
	                    "equip_crest_slot_type_3_crest_id_2": 0,
	                    "edit_skill_1_chara_id": 0,
	                    "edit_skill_2_chara_id": 0
	                },
	                {
	                    "unit_no": 3,
	                    "chara_id": 10130102,
	                    "equip_dragon_key_id": 19126832,
	                    "equip_weapon_body_id": 0,
	                    "equip_weapon_skin_id": 0,
	                    "equip_talisman_key_id": 0,
	                    "equip_crest_slot_type_1_crest_id_1": 0,
	                    "equip_crest_slot_type_1_crest_id_2": 0,
	                    "equip_crest_slot_type_1_crest_id_3": 0,
	                    "equip_crest_slot_type_2_crest_id_1": 0,
	                    "equip_crest_slot_type_2_crest_id_2": 0,
	                    "equip_crest_slot_type_3_crest_id_1": 0,
	                    "equip_crest_slot_type_3_crest_id_2": 0,
	                    "edit_skill_1_chara_id": 0,
	                    "edit_skill_2_chara_id": 0
	                },
	                {
	                    "unit_no": 4,
	                    "chara_id": 10830101,
	                    "equip_dragon_key_id": 19126822,
	                    "equip_weapon_body_id": 0,
	                    "equip_weapon_skin_id": 0,
	                    "equip_talisman_key_id": 0,
	                    "equip_crest_slot_type_1_crest_id_1": 0,
	                    "equip_crest_slot_type_1_crest_id_2": 0,
	                    "equip_crest_slot_type_1_crest_id_3": 0,
	                    "equip_crest_slot_type_2_crest_id_1": 0,
	                    "equip_crest_slot_type_2_crest_id_2": 0,
	                    "equip_crest_slot_type_3_crest_id_1": 0,
	                    "equip_crest_slot_type_3_crest_id_2": 0,
	                    "edit_skill_1_chara_id": 0,
	                    "edit_skill_2_chara_id": 0
	                }
	            ],
	            "helper_list": [],
	            "helper_detail_list": [],
	            "bonus_factor_list": [
	                {
	                    "factor_type": 12,
	                    "factor_value": 2
	                }
	            ],
	            "scoring_enemy_point_list": [],
	            "score_mission_success_list": [],
	            "clear_time": 36,
	            "is_best_clear_time": 0,
	            "converted_entity_list": []
	        },
	        "repeat_data": [],
	        "update_data_list": {
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------
