import sys
import random
from code_feedback import Feedback
from pl_helpers import name, points
from pl_unit_test import PLTestCase


class Test(PLTestCase):

    # ---------------------------- package check ----------------------------
    @points(1)
    @name("Student imports numpy or torch")
    def test_import(self):
        ok = ("numpy" in sys.modules) or ("torch" in sys.modules)
        Feedback.set_score(int(ok))
        if not ok:
            Feedback.add_feedback("You must import either numpy or torch.")

    # ---------------------------- deterministic checks ---------------------
    @points(1)
    @name("male, 55 -> Reject")
    def test_rule1(self):
        self._check("male", 55, "Reject")

    @points(1)
    @name("female, 60 -> Reject")
    def test_rule2(self):
        self._check("female", 60, "Reject")

    @points(1)
    @name("male, 45 -> Accept")
    def test_rule3(self):
        self._check("male", 45, "Accept")

    @points(1)
    @name("female, 30 -> Need more info")
    def test_rule4(self):
        self._check("female", 30, "Need more info")

    # ---------------------------- hidden random checks ---------------------
    @points(1)
    @name("Hidden random cases")
    def test_random(self):
        import random

        cases = [
            ("male",   random.randint(51, 65), "Reject"),          # rule 1
            ("female", random.randint(55, 70), "Reject"),          # rule 2
            ("male",   random.randint(41, 50), "Accept"),          # rule 3
            ("female", random.randint(25, 40), "Need more info"),  # rule 4
            ("male",   random.choice([20, 70]),  "Reject"),        # edge-reject
            ("female", random.choice([22, 80]), "Reject")          # edge-reject
        ]

        passed = 0
        for g, a, expected in cases:
            if self.st.evaluate_claim(g, a) == expected:
                passed += 1

        # normalise to [0,1] for Feedback.set_score
        Feedback.set_score(passed / len(cases))

    # ---------------------------- helper -----------------------------------
    def _check(self, gender, age, expected):
        result = self.st.evaluate_claim(gender, age)
        Feedback.set_score(int(result == expected))
        if result != expected:
            Feedback.add_feedback(
                f"evaluate_claim({gender!r}, {age}) returned {result!r} "
                f"but expected {expected!r}"
            )
