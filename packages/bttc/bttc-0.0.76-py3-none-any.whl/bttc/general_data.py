# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Module to hold data used in general utility module `genral_utils`."""

import dataclasses


@dataclasses.dataclass
class ActivityRecord:
  """Dataclass to represent UI Activity. e.g.:
  'com.google.android.apps.youtube.music/.activities.MusicActivity'
  """

  full_activity_path: str

  @property
  def package(self) -> str:
    """The package part of activity.

    Take activity below for example:
    'com.google.android.apps.youtube.music/.activities.MusicActivity'

    The package of it will be:
    'com.google.android.apps.youtube.music'
    """
    return self.full_activity_path.split('/')[0]
