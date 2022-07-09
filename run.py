import math

# ギア比とスキッドポイント数の計算
def skid_point(chain_ring: int, cog: int):
    lcm = math.lcm(chain_ring, cog)
    num_skid_points = round(lcm // chain_ring, 2)
    gear = round(chain_ring / cog, 2)
    return gear, num_skid_points

# チェーンリングの歯の数の入力
try:
    chain_ring = int(input('チェーンリングの歯の数を入力してください。: '))
except ValueError:
    print('-----------------------')
    print('⚠️ 数値を入力してください。')
    print('-----------------------')
    try:
        chain_ring = int(input('チェーンリングの歯の数を入力してください。: '))
    except ValueError:
        print('-----------------------')
        print('⚠️ 数値を入力してください。言うこと聞かないので処理を中断します。')
        print('-----------------------')
        exit()

# コグの歯の数の入力
try:
    cog = int(input('コグの歯の数を入力してください。: '))
except ValueError:
    print('-----------------------')
    print('⚠️ 数値を入力してください。')
    print('-----------------------')
    try:
        cog = int(input('コグの歯の数を入力してください。: '))
    except ValueError:
        print('-----------------------')
        print('⚠️ 数値を入力してください。言うこと聞かないので処理を中断します。')
        print('-----------------------')
        exit()

# 出力
print('-----------------------')
print('ギア比:', skid_point(chain_ring, cog)[0])
print('スキッドポイント数:', skid_point(chain_ring, cog)[1])
print('-----------------------')
exit()
