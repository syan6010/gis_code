require "matrix"

class Point
    attr_reader :e, :n
    def initialize e, n
        @e = e
        @n = n
    end
end

# 畢氏定理求距離
def distance a, b
    Math.sqrt (a.e - b.e) ** 2 + (a.n - b.n) ** 2
end

# 求中點
def midpoint m, n, a, b
    Point.new((m * b.e + n * a.e).to_f / (m + n), (m * b.n + n * a.n).to_f / (m + n))
end

# 求方位角

# 坐標法計算面積