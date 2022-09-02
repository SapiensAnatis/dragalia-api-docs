Dragalia Lost API documentation
===================================

This repository is meant to provide info about the API used by Dragalia Lost, i.e. typical requests and the responses that the server gives for them.

.. note::

   This project is under active development. It is not endorsed by Nintendo.


Redactions
------------------------
Some information has been redacted from requests and responses as it is potentially sensitive. Where this has been done, it will be replaced by an <identifier> in angle brackets. A list of redactions and the corresponding identifiers can be found below.

.. list-table:: Redactions
   :widths: 25 50
   :header-rows: 1

   * - Identifier
     - Description
   * - <id_token> 
     - Access token associated with the user account, retrieved from `core_v1_gateway_sdk_login`

Contents
------------------------

.. toctree::
   :maxdepth: 1
   :glob:
   :caption: Dragalia Lost endpoints
   
   dragalia/*

.. toctree::
   :maxdepth: 1
   :glob:
   :caption: Nintendo endpoints

   nintendo/*


.. toctree::
   :maxdepth: 1
   :caption: Contributing

   template.rst