def calculate_gacha_probability(pull_num):
    if not isinstance(pull_num, int) or pull_num <= 0:
        raise ValueError("抽数必须是正整数")
    
    effective_pull = pull_num % 90
    if effective_pull == 0:
        effective_pull = 90
    
    if 1 <= effective_pull <= 73:
        return 0.006
    elif 74 <= effective_pull <= 89:
        return 0.006 + (effective_pull - 73) * 0.06
    elif effective_pull == 90:
        return 1.0
    else:
        raise ValueError("无效的抽数")