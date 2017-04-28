#!/usr/bin/env python
#
# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""This example gets all content metadata key hierarchies.
"""

# Import appropriate modules from the client library.
from googleads import dfp


def main(client):
  # Initialize appropriate service.
  content_metadata_key_hierarchy_service = client.GetService(
      'ContentMetadataKeyHierarchyService', version='v201611')

  # Create a statement to select content metadata key hierarchies.
  statement = dfp.FilterStatement()

  # Retrieve a small amount of content metadata key hierarchies at a time,
  # paging through until all content metadata key hierarchies have been
  # retrieved.
  while True:
    response = (
        content_metadata_key_hierarchy_service
        .getContentMetadataKeyHierarchiesByStatement(
            statement.ToStatement()))
    if 'results' in response:
      for content_metadata_key_hierarchy in response['results']:
        # Print out some information for each content metadata key hierarchy.
        print('Content metadata key hierarchy with ID "%d" and name "%s" was '
              'found.\n' % (content_metadata_key_hierarchy['id'],
                            content_metadata_key_hierarchy['name']))
      statement.offset += dfp.SUGGESTED_PAGE_LIMIT
    else:
      break

  print '\nNumber of results found: %s' % response['totalResultSetSize']


if __name__ == '__main__':
  # Initialize client object.
  dfp_client = dfp.DfpClient.LoadFromStorage()
  main(dfp_client)
