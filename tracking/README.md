## Problem 1: Exact Inference Observation
+ Với mỗi position (p) trong legalPostion nếu noisyDistance là None có nghĩa là pacman đã ăn con ma và vị trí của con ma, cập nhật jail, nếu không thì cập nhật belief dựa trên trueDistance
## Problem 2: Exact Inference with Time Elapse
+ Với mỗi position (p) trong legalPostion trả về phân phối so với các vị trí kế nhiệm của bóng ma từ Trạng thái trò chơi đã cho. Cập nhật các khoảng cách trong các vị trí kế nhiệm trả vêf dựa vào beliefs