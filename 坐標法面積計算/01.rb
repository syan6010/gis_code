require "matrix"
require "./spatialFun.rb"

# class Poly
#     def initialize point_set
#         @point_set = point_set
#     end

#     class << self
#         def area 
#             a_value = 0
#             @point_set.each do |point|
                
#             end 
#         end
#     end
# end



a = Point.new 175000, 2540000 
b = Point.new 175300, 2540050
c = Point.new 175050, 2540400 


matab =  Matrix[[c.n, b.n], [c.e, b.e]]
matbc =  Matrix[[b.n, a.n], [b.e, a.e]]
matcd =  Matrix[[a.n, c.n], [a.e, c.e]]

 
area = ((matab.det + matbc.det + matcd.det) * 0.5).abs

d = midpoint(2, 3, a, b)



# 依據地號界址檔及界址坐標檔，利用坐標法計算每一宗地之面積。宗地面積以平方公尺為單位，採四捨五入法計算至小數點以下第 2 位止
p area.round 2
p d
