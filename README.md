# python-AI-learning
Đại học Công nghệ - Đại học Quốc Gia Hà Nội - Trí Tuệ nhân tạo
## Bài 1 : DFS
* Define state: node, action, cost;
* Inital State
+ Stack: chứa các state
+ Visited_list: đánh dấu các nút đã thăm
+ cost: tổng chi phí đạt được goal state
* Ý tưởng:
- Push vào stack state ban đầu
- Duyệt vòng lặp với điều kiện stack khác rỗng
- Nếu đỉnh của stack được lấy ra và là goal state thì return actions
- Ngược lại, thêm tất cả các successors của đỉnh của state hiện tại vào stack
- Lặp lại cho đến khi đạt được goal state