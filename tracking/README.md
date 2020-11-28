## Problem 1: Exact Inference Observation
+ Với mỗi position (p) trong legalPostion nếu noisyDistance là None có nghĩa là pacman đã ăn con ma và vị trí của con ma, cập nhật jail, nếu không thì cập nhật belief dựa trên trueDistance
## Problem 2: Exact Inference with Time Elapse
+ Với mỗi position (p) trong legalPostion trả về phân phối so với các vị trí kế nhiệm của bóng ma từ Trạng thái trò chơi đã cho. Cập nhật các khoảng cách trong các vị trí kế nhiệm trả vêf dựa vào beliefs
## Problem 3: Exact Inference Full Test
+ Với mỗi action lấy ra từ legal = [a for a in gameState.getLegalPacmanActions()], lấy tất cả successors từ action đó. Lặp lấy toàn bộ vị trí phân phối của ghost, cập nhật giá trị value[action] += 100/khoảng cách đó. Trả về mảng giá trị của các action
## Problem 4: Approximate Inference Observation
+ Hàm initializeUniformly: list of all possible position a ghost can take
+ Hàm getBeliefDistribution: duyệt từng particle trong self.particles, với mỗi giá trị beliefDistribution[particle] cộng thêm 1.0.
+ Hàm observe: if pacman ate the ghost then the particle position is jail position of the ghost, otherwise the belief is updated as per the trueDistance same as the exactInference class
## Problem 5: Approximate Inference with Time Elapse
+ Duyệt hết các phần tử trong self.numParticles, lấy ra tất cả vị trí của ghost, lấy mẫu một số vị trí cho particles
## Problem 6: Joint Particle Filter Observation
+ Hàm initializeParticles(self): liệt kê tất cả những vị trí hợp lệ, tráo ngẫu nhiên.
+ Hàm getBeliefDistribution: duyệt tất cả các particle trong self.particles cộng beliefDistribution[particle] thêm 1.0, trả về beliefDistribution
+ Hàm observeState: Nếu số lượng noisyDistance nhỏ hơn số lượng ma thì kết thúc. Ngược lại, duyệt các phần tử trong self.numParticles, gán ghostBelief = 1.0, với mỗi ghostAgent trong self.numGhosts, nếu noisyDistance là None đối với ghostAgent, thì ghost sẽ xuất hiện trong prison của nó, ngược lại cập nhật belief dựa trên trueDistance