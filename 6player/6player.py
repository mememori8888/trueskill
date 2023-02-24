#!/usr/bin/env python
# -*- coding: utf-8 -*-


from trueskill import TrueSkill
import mpmath
import pandas as pd

# 6player.ver


#csvから値を取得する。
filepath = r'/home/mamhidet/usr/Trueskill/input.csv'

#csvからデータ読み込み
df = pd.read_csv(filepath,header=None)
#output_header
output_header = ['raceid',
                 'payer1',
                 'payer2',
                 'payer3',
                 'payer4',
                 'payer5',
                 'payer6',
                 'payer1_mu',
                 'payer1_sigma',
                 'payer2_mu',
                 'payer2_sigma',
                 'payer3_mu',
                 'payer3_sigma',
                 'payer4_mu',
                 'payer4_sigma',
                 'payer5_mu',
                 'payer5_sigma',
                 'payer6_mu',
                 'payer6_sigma'
                 ]
#output.csvにつながるdf
output_df = pd.DataFrame(columns=output_header)
count = len(df)
#dfを1行ずつ読み込む(6行パターン)
player_list = df.loc[0,1:6].to_list()
for i in range(1,count,1):
    race_id:int = df.loc[i,0]
    player_skill_list:int = df.loc[i,1:6].to_list()
    player_rank_list:int = df.loc[i,7:12].to_list()


    # print(player_list)
    # print(player_skill_list)
    # print(player_rank_list)


    env = TrueSkill(backend='mpmath')

    if player_skill_list[0] == '':
        r1 = 'N/A'
    else: 
        r1  =  env . create_rating (float(player_skill_list[0])) 
    
    if player_skill_list[1] == '':
       r2 = 'N/A'
    else:
        r2  =  env . create_rating (float(player_skill_list[1]))
    
    if player_skill_list[2] == '':
       r3 = 'N/A'
    else:
        r3  =  env . create_rating (float(player_skill_list[2]))

    if player_skill_list[3] == '':
       r4 = 'N/A'
    else:
        r4  =  env . create_rating (float(player_skill_list[3]))

    if player_skill_list[4] == '':
       r5 = 'N/A'
    else:
        r5  =  env . create_rating (float(player_skill_list[4]))

    if player_skill_list[5] == '':
       r6 = 'N/A'
    else:
        r6  =  env . create_rating (float(player_skill_list[5]))

    # print(r6)
    # 新しい評価を計算する
    rating_groups  =  [( r1 ,),  ( r2 ,),  ( r3 ,),  ( r4 ,),  ( r5 ,),  ( r6 ,)]
    # print(rating_groups) 
    rated_rating_groups  =  env . rate ( rating_groups ,  ranks = player_rank_list) 
    # 新しい評価を保存します
    (r1 ,),  ( r2 ,) ,  ( r3 ,),  ( r4 ,),  ( r5 ,),  ( r6 ,) =  rated_rating_groups
    #output_df用のリストを作成する。
    output_list = []
    mu_sigma_list = [r1.mu,r1.sigma,r2.mu,r2.sigma,r3.mu,r3.sigma,r4.mu,r4.sigma,r5.mu,r5.sigma,r6.mu,r6.sigma]
    output_list.append(race_id)
    output_list.extend(player_skill_list)
    output_list.extend(mu_sigma_list)
    print(output_list)
    #dfに登録して、output.csvに書き込む
    param_df = pd.DataFrame([output_list],columns=output_header)
    output_df = pd.concat([output_df,param_df])

#csvに出力
output_df.to_csv('6_player_output.csv',index=False)
print(output_df)
    # print(rated_rating_groups)
    # print(r1.mu)




