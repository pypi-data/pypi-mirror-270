# pylint: disable=C0103
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
Author: reharish, abi-sheak
Requirements: robotframework
"""

from robot.api import SuiteVisitor

class TestRepeater(SuiteVisitor):
    """
    TestRepeater is a Robot Framework Listener that repeats each test case in a suite a specified number of times.

    This listener is intended to be used as a listener plugin with Robot Framework.

    count (int): The number of times each test case should be repeated.

    Example:

    robot --listener TestRepeater:<count> <test-suite>

    robot --listener TestRepeater:2  example/example.robot

    """

    ROBOT_LISTENER_API_VERSION = 3

    def __init__(self, count):
        """
        Initialize TestRepeater with the given repetition count.

        count (int): The number of times each test case should be repeated.
        """
        self.count = int(count)

    def start_suite(self, suite, result):
        """
        Called when a suite starts.
        Creates a tests list as from the count.

        Repeats each test case in the suite.
        """
        testcases = []
        for iteration in range(1, self.count + 1):
            for test in suite.tests:
                copy = test.copy(name=f"{iteration} - {test.name}")
                testcases.append(copy)
        suite.tests = testcases

    def end_suite(self, suite, result):
        """
        Called when a suite ends.
        """
        pass

    def start_test(self, test, result):
        """
        Called when a test starts.
         """
        pass

    def end_test(self, test, result):
        """
        Called when a test ends.
        """
        pass

    def start_keyword(self, keyword, result):
        """
        Called when a keyword starts.
        """
        pass

    def end_keyword(self, keyword, result):
        """
        Called when a keyword ends.
        """
        pass
