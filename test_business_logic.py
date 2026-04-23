import pytest
from business_logic import calculate_gacha_probability

class TestGachaProbability:
    def test_base_probability(self):
        for pull in range(1, 74):
            prob = calculate_gacha_probability(pull)
            assert prob == 0.006, f"第{pull}抽概率错误"

    def test_soft_pity_start(self):
        prob = calculate_gacha_probability(74)
        assert prob == 0.066, "第74抽概率错误"

    def test_soft_pity_increase(self):
        expected_prob = 0.066
        for pull in range(74, 90):
            prob = calculate_gacha_probability(pull)
            assert prob == expected_prob, f"第{pull}抽概率错误"
            expected_prob += 0.06

    def test_hard_pity_guarantee(self):
        prob = calculate_gacha_probability(90)
        assert prob == 1.0, "第90抽概率错误"

    def test_invalid_pull_number(self):
        with pytest.raises(ValueError):
            calculate_gacha_probability(0)
        
        with pytest.raises(ValueError):
            calculate_gacha_probability(-1)

    def test_pull_over_90(self):
        prob = calculate_gacha_probability(91)
        assert prob == 0.006, "第91抽概率错误"