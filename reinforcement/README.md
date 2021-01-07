# reinforcementlearning

# Q1: Value Iteration.
  Thay đổi giá trị theo số lần lăp. Với mỗi lần lặp:
  - States khả dujngv-> chỉnh sửa value tương ứng vs từng trạng thái 
  Hàm computeQValueFromValues(state, a): đưa ra Q(s,a): giá trị sau khi thực hiện action a\
# Q2: Bridge Crossing Analysis
  Thay đổi giá trị discount và noise
  - discount:hệ số discount
  - noise: xác suất di chuyển hướng không mong muốn ( tỉ lệ khám phá)
# Q3: Policies
  a, Đi đường dưới, đến vị trí +1: livingReward âm(-1)\
  b, Đi đường trên, đến vị trí +1: livingReward = 0,noise > 0, khi đó sẽ phải tránh vực\
  c, Đi đường dưới, đến vị trí +10:living reward cao hơn câu a nhưng vẫn âm, phù hợp để ưu tiên đến vị trí +10 (-0.5)
  d, Đi đường trên, đến vị trí +10:living reward cao hơn câu c nhưng vẫn âm (-0.1)
  e, Sống càng lâu càng tốt: livingReward rất cao (+100)
# Q4:Q-Learning
  Xây dựng hàm Q-learning:\
  V*(s): hàm getValue(state) = maxQ(s,a)|mọi a = hàm computeValueFromQValues(state)\
  Công thức cập nhật values xây dựng tại hàm update\
# Q5: Epsilon Greedy
  xây dựng hàm getAction\
  - lấy ramdom.random()(0->1)
  - Với tỉ lệ nhỏ hơn tỉ lệ khám phá (flipcoin(p) return True): thực hiện hành động khám phá, action random, nếu không thực hiện theo chính sách ban đầu
# Q6:Bridge Crossing Revisited

  
  
