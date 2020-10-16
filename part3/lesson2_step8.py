def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert substring in full_string, f"expected {full_string}, got {substring}"


test_substring("my name is", 'kill')
