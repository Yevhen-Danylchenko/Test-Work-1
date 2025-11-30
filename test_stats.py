import pytest
from DataLoader import DataLoader

def test_cpa_calculation():
    # базові перевірки
    assert DataLoader.calculate_cpa(100, 10) == 10
    assert DataLoader.calculate_cpa(50, 5) == 10
    assert DataLoader.calculate_cpa(0, 0) is None
    assert DataLoader.calculate_cpa(100, 0) is None

def test_merge_rows():
    # імітація агрегації двох рядків
    spend1, conv1 = 100, 10
    spend2, conv2 = 50, 5

    total_spend = spend1 + spend2
    total_conv = conv1 + conv2
    cpa = DataLoader.calculate_cpa(total_spend, total_conv)

    assert total_spend == 150
    assert total_conv == 15
    assert cpa == 10