/shop/special_shop_purchase
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
	    "goods_id": 40261,
	    "payment_type": 2,
	    "quantity": 1,
	    "selected_unit": {
	        "entity_type": 1,
	        "entity_id": 10150106
	    }
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
	        "special_shop_purchase": [
	            {
	                "goods_id": 40261,
	                "last_buy_time": 1664542105,
	                "effect_start_time": 0,
	                "effect_end_time": 0,
	                "buy_count": 1
	            }
	        ],
	        "is_quest_bonus": 0,
	        "is_stone_bonus": 0,
	        "is_stamina_bonus": 0,
	        "stone_bonus": [],
	        "stamina_bonus": [],
	        "quest_bonus": [],
	        "update_data_list": {
	            "album_passive_notice": {
	                "is_update_chara": 1,
	                "is_update_dragon": 0
	            },
	            "shop_notice": {
	                "is_shop_notification": 1
	            },
	            "chara_list": [
	                {
	                    "chara_id": 10150106,
	                    "rarity": 5,
	                    "exp": 0,
	                    "level": 1,
	                    "additional_max_level": 0,
	                    "hp_plus_count": 0,
	                    "attack_plus_count": 0,
	                    "limit_break_count": 0,
	                    "is_new": 1,
	                    "gettime": 1664542105,
	                    "skill_1_level": 1,
	                    "skill_2_level": 0,
	                    "ability_1_level": 1,
	                    "ability_2_level": 0,
	                    "ability_3_level": 0,
	                    "burst_attack_level": 0,
	                    "combo_buildup_count": 0,
	                    "hp": 64,
	                    "attack": 42,
	                    "ex_ability_level": 1,
	                    "ex_ability_2_level": 1,
	                    "is_temporary": 0,
	                    "is_unlock_edit_skill": 0,
	                    "mana_circle_piece_id_list": [],
	                    "list_view_flag": 1
	                }
	            ],
	            "diamond_data": {
	                "paid_diamond": 0,
	                "free_diamond": 0
	            },
	            "unit_story_list": [
	                {
	                    "unit_story_id": 110059021,
	                    "is_read": 0
	                }
	            ],
	            "present_notice": {
	                "present_count": 1,
	                "present_limit_count": 1
	            },
	            "functional_maintenance_list": []
	        },
	        "entity_result": {
	            "converted_entity_list": [],
	            "new_get_entity_list": [
	                {
	                    "entity_type": 1,
	                    "entity_id": 10150106
	                }
	            ]
	        }
	    }
	}

Notes
------