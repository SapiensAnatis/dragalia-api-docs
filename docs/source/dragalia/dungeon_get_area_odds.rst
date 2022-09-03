/dungeon/get_area_odds
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
	    "dungeon_key": "af7704da374abb78c65e1aa00217f0de45f77c18",
	    "area_idx": 1
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
	        "odds_info": {
	            "area_index": 1,
	            "reaction_obj_count": 1,
	            "drop_obj": [],
	            "enemy": [
	                {
	                    "param_id": 100010109,
	                    "is_pop": 1,
	                    "is_rare": 0,
	                    "piece": 0,
	                    "enemy_drop_list": [
	                        {
	                            "drop_list": [
	                                {
	                                    "type": 8,
	                                    "id": 101001001,
	                                    "quantity": 1,
	                                    "place": 0
	                                },
	                                {
	                                    "type": 4,
	                                    "id": 0,
	                                    "quantity": 40,
	                                    "place": 0
	                                },
	                                {
	                                    "type": 8,
	                                    "id": 202001001,
	                                    "quantity": 1,
	                                    "place": 0
	                                }
	                            ],
	                            "coin": 1,
	                            "mana": 1
	                        }
	                    ],
	                    "enemy_idx": 0
	                },
	                {
	                    "param_id": 100010101,
	                    "is_pop": 1,
	                    "is_rare": 0,
	                    "piece": 0,
	                    "enemy_drop_list": [
	                        {
	                            "drop_list": [],
	                            "coin": 0,
	                            "mana": 1
	                        }
	                    ],
	                    "enemy_idx": 1
	                },
	                {
	                    "param_id": 100010101,
	                    "is_pop": 1,
	                    "is_rare": 0,
	                    "piece": 0,
	                    "enemy_drop_list": [
	                        {
	                            "drop_list": [],
	                            "coin": 0,
	                            "mana": 1
	                        }
	                    ],
	                    "enemy_idx": 2
	                }
	            ],
	            "grade": []
	        },
	        "update_data_list": {
	            "functional_maintenance_list": []
	        }
	    }
	}

Notes
------