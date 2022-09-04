/party/update_party_name
==================================================

- Base address: production-api.dragalialost.com/2.19.0_20220714193707
- Method: POST
- Status code: 200

Request headers
----------------

.. code-block:: text

	Host: production-api.dragalialost.com

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

	Content-Type: application/x-msgpack

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