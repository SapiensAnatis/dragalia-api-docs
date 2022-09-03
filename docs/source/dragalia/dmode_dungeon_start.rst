/dmode_dungeon/start
============================================================

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
	    "chara_id": 10950503,
	    "start_floor_num": 1,
	    "servitor_id": 2,
	    "bring_edit_skill_chara_id_list": [
	        10840501,
	        10440301
	    ]
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
	        "dmode_dungeon_state": 2,
	        "dmode_ingame_data": {
	            "recovery_count": 1,
	            "recovery_time": 1662162807,
	            "unique_key": "66709573935_1662162924",
	            "start_floor_num": 1,
	            "target_floor_num": 60,
	            "dmode_level_group_id": 1,
	            "unit_data": {
	                "chara_id": 10950503,
	                "dmode_chara_level_group_id": 1,
	                "skill_1_level": 3,
	                "skill_2_level": 2,
	                "ability_1_level": 2,
	                "ability_2_level": 2,
	                "ability_3_level": 2,
	                "ex_ability_level": 5,
	                "ex_ability_2_level": 5,
	                "burst_attack_level": 2,
	                "combo_buildup_count": 0
	            },
	            "servitor_id": 2,
	            "dmode_servitor_passive_list": []
	        },
	        "update_data_list": {
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------