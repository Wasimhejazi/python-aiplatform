# -*- coding: utf-8 -*-
# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for ImportIndex
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-aiplatform


# [START aiplatform_v1beta1_generated_IndexService_ImportIndex_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import aiplatform_v1beta1


async def sample_import_index():
    # Create a client
    client = aiplatform_v1beta1.IndexServiceAsyncClient()

    # Initialize request argument(s)
    config = aiplatform_v1beta1.ConnectorConfig()
    config.big_query_source_config.table_path = "table_path_value"
    config.big_query_source_config.datapoint_field_mapping.id_column = "id_column_value"
    config.big_query_source_config.datapoint_field_mapping.embedding_column = "embedding_column_value"

    request = aiplatform_v1beta1.ImportIndexRequest(
        name="name_value",
        config=config,
    )

    # Make the request
    operation = client.import_index(request=request)

    print("Waiting for operation to complete...")

    response = (await operation).result()

    # Handle the response
    print(response)

# [END aiplatform_v1beta1_generated_IndexService_ImportIndex_async]
