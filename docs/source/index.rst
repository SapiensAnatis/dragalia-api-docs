Dragalia Lost API documentation
===================================

This repository is meant to provide info about the API used by Dragalia Lost, i.e. typical requests and the responses that the server gives for them.

.. note::

   This project is under active development. It is not endorsed by Nintendo or Cygames.


Redactions
------------------------
Some information has been redacted from requests and responses as it is potentially sensitive. Where this has been done, it will be replaced by an <identifier> in angle brackets. Some of the more common redactions and what they stand for can be found below.

.. list-table::
   :widths: 25 50
   :header-rows: 1

   * - Identifier
     - Description
   * - <id_token> 
     - Access token associated with the user account, retrieved from :doc:`nintendo/core_v1_gateway_sdk_login`
   * - <device_id>
     - Unique device identifier, appears in the headers of most requests
   * - <device_account>
     - Device account ID, retrieved from :doc:`nintendo/core_v1_gateway_sdk_login`
   * - <device_analytics_id>
     - Unique device ID used for analytics tracking, retrieved from :doc:`nintendo/core_v1_gateway_sdk_login`
   * - <user_id>
     - Nintendo account ID, retrieved from :doc:`nintendo/core_v1_gateway_sdk_login`
   * - <city>
     - The user's precise location, retrieved from :doc:`/nintendo/bigdata_v1_analytics_events_config`

Contents
------------------------

.. toctree:: 
  :maxdepth: 1
  :glob:
  :caption: Resources

  info/*
  template.rst

.. toctree::
  :maxdepth: 1
  :glob:
  :caption: Nintendo endpoints

  nintendo/*

.. toctree::
  :maxdepth: 1
  :glob:
  :caption: Dragalia Lost endpoints
  
  dragalia/*

.. toctree:: 
  :maxdepth: 1
  :glob:
  :caption: Web view endpoints

  views/*

