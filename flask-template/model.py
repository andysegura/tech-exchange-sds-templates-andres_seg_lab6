# Copyright 2021 Google LLC
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

def capital_check(answers):
    correct_answers = {
        'texas':'austin',
        'arizona':'phoenix',
        'colorado':'denver',
        'new mexico':'santa fe',
        'california':'sacramento',
        'georgia':'atlanta',
        'new york':'albany',
    }
    graded_answers = {}
    total = 0.0
    correct = 0
    for answer in answers:
        total += 1
        if correct_answers[answer] == answers[answer].lower():
            graded_answers[answer] = 'correct.'
            correct += 1
        else:
            graded_answers[answer] = 'wrong, correct answer is ' + correct_answers[answer]
    graded_answers['score'] = str(round((correct/total) * 100, 2))
    return graded_answers