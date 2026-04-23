import pytest
# pylint: disable=undefined-variable
from business_logic import calculate_gacha_probability
# pylint: enable=undefined-variable


class TestGachaProbability:
    def test_base_probability(self):
        """测试1-73抽的基础概率"""
        for pull in range(1, 74):
            prob = calculate_gacha_probability(pull)
            assert prob == pytest.approx(0.006), f"第{pull}抽概率错误"

    def test_soft_pity_start(self):
        """测试74抽的概率（6.6%）"""
        prob = calculate_gacha_probability(74)
        assert prob == pytest.approx(0.066), "第74抽概率错误"

    def test_soft_pity_increase(self):
        """测试74-89抽的递增概率"""
        expected_prob = 0.066
        for pull in range(74, 90):
            prob = calculate_gacha_probability(pull)
            assert prob == pytest.approx(expected_prob), f"第{pull}抽概率错误"
            expected_prob += 0.06

    def test_hard_pity_guarantee(self):
        """测试90抽必出（概率1.0）"""
        prob = calculate_gacha_probability(90)
        assert prob == pytest.approx(1.0), "第90抽概率错误"

    def test_invalid_pull_number(self):
        """测试0/负数抽数，应抛出错误"""
        with pytest.raises(ValueError):
            calculate_gacha_probability(0)

        with pytest.raises(ValueError):
            calculate_gacha_probability(-1)

    def test_pull_over_90(self):
        """测试超过90抽重置（91抽=1抽）"""
        prob = calculate_gacha_probability(91)
        assert prob == pytest.approx(0.006), "第91抽概率错误"