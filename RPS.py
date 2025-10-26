import random

def player(prev_play, opponent_history=[]):
    # Lưu lịch sử nước đi của đối thủ
    if prev_play != "":
        opponent_history.append(prev_play)

    # Chiến lược mặc định cho ván đầu tiên
    if not opponent_history:
        return "R"

    # Đếm tần suất xuất hiện của R, P, S trong lịch sử đối thủ
    counts = {"R": 0, "P": 0, "S": 0}
    for move in opponent_history:
        counts[move] += 1

    # Tìm nước đi mà đối thủ dùng nhiều nhất
    most_common = max(counts, key=counts.get)

    # Chọn nước phản công để thắng nước phổ biến nhất của đối thủ
    counter_moves = {"R": "P", "P": "S", "S": "R"}
    guess = counter_moves[most_common]

    # Phát hiện và phản ứng khi đối thủ thay đổi chiến thuật nhanh
    if len(opponent_history) >= 3:
        last3 = opponent_history[-3:]
        # Nếu đối thủ đang theo chu kỳ R→P→S hoặc P→S→R
        if last3 == ["R", "P", "S"] or last3 == ["P", "S", "R"] or last3 == ["S", "R", "P"]:
            # Dự đoán nước kế tiếp trong chu kỳ
            next_in_cycle = {"R": "P", "P": "S", "S": "R"}[opponent_history[-1]]
            # Phản công
            guess = counter_moves[next_in_cycle]

    return guess
