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
"""This example gets all active labels.
"""

# Import appropriate modules from the client library.
from googleads import dfp


def main(client):
  # Initialize appropriate service.
  label_service = client.GetService('LabelService', version='v201608')
  query = 'WHERE isActive = :isActive'
  values = [
      {'key': 'isActive',
       'value': {
           'xsi_type': 'BooleanValue',
           'value': 'true'
       }},
  ]
  # Create a statement to select labels.
  statement = dfp.FilterStatement(query, values)

  # Retrieve a small amount of labels at a time, paging
  # through until all labels have been retrieved.
  while True:
    response = label_service.getLabelsByStatement(statement.ToStatement())
    if 'results' in response:
      for label in response['results']:
        # Print out some information for each label.
        print('Label with ID "%d" and name "%s" was found.\n' % (label['id'],
                                                                 label['name']))
      statement.offset += dfp.SUGGESTED_PAGE_LIMIT
    else:
      break

  print '\nNumber of results found: %s' % response['totalResultSetSize']


if __name__ == '__main__':
  # Initialize client object.
  dfp_client = dfp.DfpClient.LoadFromStorage()
  main(dfp_client)
