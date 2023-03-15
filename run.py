import math

class SkidPointCalculator:
    def __init__(self, chain_ring: int, cog: int):
        self.chain_ring = chain_ring
        self.cog = cog

    def calculate_lcm(self):
        return math.lcm(self.chain_ring, self.cog)

    def calculate_num_skid_points(self):
        return round(self.calculate_lcm() / self.chain_ring, 2)

    def calculate_gear_ratio(self):
        return round(self.chain_ring / self.cog, 2)

    def calculate_skid_point(self):
        return self.calculate_gear_ratio(), self.calculate_num_skid_points()

# チェーンリングの歯の数の入力
while True:
    try:
        chain_ring = int(input('チェーンリングの歯の数を入力してください。: '))
        break
    except ValueError:
        print('-----------------------')
        print('⚠️ 数値を入力してください。')
        print('-----------------------')

# コグの歯の数の入力
while True:
    try:
        cog = int(input('コグの歯の数を入力してください。: '))
        break
    except ValueError:
        print('-----------------------')
        print('⚠️ 数値を入力してください。')
        print('-----------------------')

calculator = SkidPointCalculator(chain_ring, cog)

# 出力
print('-----------------------')
print('ギア比:', calculator.calculate_gear_ratio())
print('スキッドポイント数:', calculator.calculate_num_skid_points())
print('-----------------------')