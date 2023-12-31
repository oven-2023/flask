import configparser
import json
import os
import numpy as np
import pandas as pd
import csv
import random
import configparser
import logging
from random import sample
from flask import Flask, request, jsonify
from sklearn.metrics.pairwise import cosine_similarity
from model import User, Work, RatingWork
import sqlalchemy
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

# # database 설정
# config = configparser.ConfigParser()
# config.read('config.ini')
# database_url = config['database']['url']
#
# engine = sqlalchemy.create_engine(database_url)
#
# Session = sessionmaker(bind=engine)
# session = Session()

# config = configparser.ConfigParser()
# config.read('config.ini')
# database_url = config['database']['url']
#
# engine = sqlalchemy.create_engine(database_url)
#
# Session = sessionmaker(bind=engine)
# session = Session()
#
# logging.basicConfig(level='DEBUG')
# logging.debug('ready to get')
# with open('Rating.csv', 'w', newline='') as csvfile:
#     csv_writer = csv.writer(csvfile)
#     logging.debug('ready to write')
#     users = session.query(User).all()
#     # all_works = session.query(Work).all()
#
#     csv_writer.writerow(["user_id", "work_id", "rating"])
#
#     for user in users:
#         # random_works = sample(all_works, 4)
#         user_id_str = str(user.user_id)
#
#         rating_works = session.query(RatingWork).filter(RatingWork.user_id == user.user_id).all()
#
#         for rating_work in rating_works:
#             work_id_str = str(rating_work.work_id)
#             rating = str(rating_work.rating)
#             total_str = user_id_str + "," + work_id_str + "," + rating
#             csv_writer.writerow(total_str.split(','))
#
#         # for work in random_works:
#         #     work_id_str = str(work.work_id)
#         #     rating = str(random.randint(1, 3) + 2)
#         #     total_str = user_id_str + "," + work_id_str + "," + rating
#         #     csv_writer.writerow(total_str.split(','))
#
# with open('Movie.csv', 'w', newline='') as csvfile:
#     csv_writer = csv.writer(csvfile, delimiter='|')
#     logging.debug('ready to write movie')
#     works = session.query(Work).all()
#
#     csv_writer.writerow(["work_id", "sf", "action", "adult", "adventure", "animation", "comedy", "criminal",
#                              "documentary", "drama", "family", "fantasy", "horror", "music", "musical", "mystery",
#                              "performance", "romance", "thriller", "variety", "war", "western"])
#
#     for work in works:
#         row_data = [work.work_id, int.from_bytes(work.sf, byteorder='big'),int.from_bytes(work.action, byteorder='big'),
#                         int.from_bytes(work.adult, byteorder='big'), int.from_bytes(work.adventure, byteorder='big'),
#                         int.from_bytes(work.animation, byteorder='big'), int.from_bytes(work.comedy, byteorder='big'),
#                         int.from_bytes(work.criminal, byteorder='big'), int.from_bytes(work.documentary, byteorder='big'), int.from_bytes(work.drama, byteorder='big'),
#                         int.from_bytes(work.family, byteorder='big'), int.from_bytes(work.fantasy, byteorder='big'), int.from_bytes(work.horror, byteorder='big'),
#                         int.from_bytes(work.music, byteorder='big'), int.from_bytes(work.musical, byteorder='big'), int.from_bytes(work.mystery, byteorder='big'),
#                         int.from_bytes(work.performance, byteorder='big'), int.from_bytes(work.romance, byteorder='big'), int.from_bytes(work.thriller, byteorder='big'),
#                         int.from_bytes(work.variety, byteorder='big'), int.from_bytes(work.war, byteorder='big'), int.from_bytes(work.western, byteorder='big')]
#         csv_writer.writerow(row_data)
#
#
# rating_src = os.path.join(os.getcwd(), 'Rating.csv')
# logging.debug(os.getcwd())
# u_cols = ['user_id', 'work_id', 'rating']
# ratings = pd.read_csv(rating_src,
#                           sep=',',
#                           names=u_cols,
#                           encoding='latin-1')
#
# ratings['rating'] = pd.to_numeric(ratings['rating'], errors='coerce')
#
# ratings = ratings.set_index('user_id')
# ratings = ratings.drop('user_id', axis=0)
# ratings.head()
#
# movie_src = os.path.join(os.getcwd(), 'Movie.csv')
# i_cols = ['work_id',
#               'sf', 'action', 'adult', 'adventure', 'animation', 'comedy', 'criminal', 'documentary', 'drama',
#               'family ', 'fantasy',
#               'horror', 'music', 'musical', 'mystery', 'performance', 'romance', 'thriller', 'variety', 'war',
#               'western',
#               ]
# movies = pd.read_csv(movie_src,
#                          sep='|',
#                          names=i_cols,
#                          encoding='utf-8')
# movies = movies.set_index('work_id')
# movies = movies.drop('work_id', axis=0)  # index 중복되어 삭제
# movies.head()

@app.route("/spring", methods=['GET'])
def spring():
    # database 설정
    config = configparser.ConfigParser()
    config.read('config.ini')
    database_url = config['database']['url']

    engine = sqlalchemy.create_engine(database_url)

    Session = sessionmaker(bind=engine)
    session = Session()

    logging.basicConfig(level='DEBUG')
    logging.debug('ready to get')
    with open('Rating.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        logging.debug('ready to write')
        users = session.query(User).all()
        # all_works = session.query(Work).all()

        csv_writer.writerow(["user_id", "work_id", "rating"])

        for user in users:
            # random_works = sample(all_works, 4)
            user_id_str = str(user.user_id)

            rating_works = session.query(RatingWork).filter(RatingWork.user_id == user.user_id).all()

            for rating_work in rating_works:
                work_id_str = str(rating_work.work_id)
                rating = str(rating_work.rating)
                total_str = user_id_str + "," + work_id_str + "," + rating
                csv_writer.writerow(total_str.split(','))

            # for work in random_works:
            #     work_id_str = str(work.work_id)
            #     rating = str(random.randint(1, 3) + 2)
            #     total_str = user_id_str + "," + work_id_str + "," + rating
            #     csv_writer.writerow(total_str.split(','))

    with open('Movie.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter='|')
        logging.debug('ready to write movie')
        works = session.query(Work).all()

        csv_writer.writerow(["work_id", "sf", "action", "adult", "adventure", "animation", "comedy", "criminal",
                             "documentary", "drama", "family", "fantasy", "horror", "music", "musical", "mystery",
                             "performance", "romance", "thriller", "variety", "war", "western"])

        for work in works:
            row_data = [work.work_id, int.from_bytes(work.sf, byteorder='big'),int.from_bytes(work.action, byteorder='big'),
                        int.from_bytes(work.adult, byteorder='big'), int.from_bytes(work.adventure, byteorder='big'),
                        int.from_bytes(work.animation, byteorder='big'), int.from_bytes(work.comedy, byteorder='big'),
                        int.from_bytes(work.criminal, byteorder='big'), int.from_bytes(work.documentary, byteorder='big'), int.from_bytes(work.drama, byteorder='big'),
                        int.from_bytes(work.family, byteorder='big'), int.from_bytes(work.fantasy, byteorder='big'), int.from_bytes(work.horror, byteorder='big'),
                        int.from_bytes(work.music, byteorder='big'), int.from_bytes(work.musical, byteorder='big'), int.from_bytes(work.mystery, byteorder='big'),
                        int.from_bytes(work.performance, byteorder='big'), int.from_bytes(work.romance, byteorder='big'), int.from_bytes(work.thriller, byteorder='big'),
                        int.from_bytes(work.variety, byteorder='big'), int.from_bytes(work.war, byteorder='big'), int.from_bytes(work.western, byteorder='big')]
            csv_writer.writerow(row_data)


    rating_src = os.path.join(os.getcwd(), 'Rating.csv')
    logging.debug(os.getcwd())
    u_cols = ['user_id', 'work_id', 'rating']
    ratings = pd.read_csv(rating_src,
                          sep=',',
                          names=u_cols,
                          encoding='latin-1')

    ratings['rating'] = pd.to_numeric(ratings['rating'], errors='coerce')

    ratings = ratings.set_index('user_id')
    ratings = ratings.drop('user_id', axis=0)
    ratings.head()

    movie_src = os.path.join(os.getcwd(), 'Movie.csv')
    i_cols = ['work_id',
              'sf', 'action', 'adult', 'adventure', 'animation', 'comedy', 'criminal', 'documentary', 'drama',
              'family ', 'fantasy',
              'horror', 'music', 'musical', 'mystery', 'performance', 'romance', 'thriller', 'variety', 'war',
              'western',
              ]
    movies = pd.read_csv(movie_src,
                         sep='|',
                         names=i_cols,
                         encoding='utf-8')
    movies = movies.set_index('work_id')
    movies = movies.drop('work_id', axis=0)  # index 중복되어 삭제
    movies.head()  # 상위 5개 행 출력

    ######### neightbor size를 정해서 예측치를 계산하는 함수 #########
    def CF_knn(user_id, work_id, neighbors_size=0):
        if int(work_id) in ratings_matrix.columns:  # 해당 영화가 존재하면
            # 주어진 사용자(user_id)와 다른 사용자의 유사도 추출
            sim_scores = user_similarity[user_id].copy()
            # 주어진 영화(movie_id)와 다른 사용자의 유사도 추출
            movie_ratings = ratings_matrix[work_id].copy()
            # 주어진 영화에 대해서 평가하지 않은 사용자를 가중 평균 계산에서 제외하기 위해 인덱스 추출
            none_rating_idx = movie_ratings[movie_ratings.isnull()].index
            # 주어진 영화를 평가하지 않은 사용자와의 유사도 제거
            movie_ratings = movie_ratings.dropna()
            # 주어진 영화를 평가하지 않은 사용자와의 유사도 제거
            sim_scores = sim_scores.drop(none_rating_idx)

            ### neighbors_size가 지정되지 않은 경우 ###
            if neighbors_size == 0:  # neighbor_size가 0이면 기존의 simple CF와 같음
                mean_rating = np.dot(sim_scores, movie_ratings) / sim_scores.sum()

            ### neighbors_size가 지정된 경우 ###
            else:
                if len(sim_scores) > 1:
                    # neighbor_size와 sim_score 중에 작은 걸 택해야 분리 가능
                    neighbors_size = min(neighbors_size, len(sim_scores))
                    sim_scores = np.array(sim_scores)
                    movie_ratings = np.array(movie_ratings)
                    user_idx = np.argsort(sim_scores)  # sim_scores 오름차순 인덱스
                    sim_scores = sim_scores[user_idx][-neighbors_size:]  # 정렬된 것을 뒤부터 뽑아냄
                    movie_ratings = movie_ratings[user_idx][-neighbors_size:]
                    mean_rating = np.dot(sim_scores, movie_ratings) / sim_scores.sum()
                else:
                    mean_rating = 3.0

        # train/test set의 분할에 따라 ratings_matrix에 해당 영화 없으면 기본값
        else:
            mean_rating = 3.0
        return mean_rating

    ratings_matrix = ratings.pivot_table(values='rating',
                                         index='user_id',
                                         columns='work_id')

    ### train set의 모든 가능한 사용자 pair의 코사인 유사도 계산 ###
    matrix_dummy = ratings_matrix.copy().fillna(0)
    user_similarity = cosine_similarity(matrix_dummy, matrix_dummy)
    user_similarity = pd.DataFrame(user_similarity,
                                   index=ratings_matrix.index,
                                   columns=ratings_matrix.index)

    def recom_movie_by_CF_knn(user_id, n_items, neighbors_size=30):
        user_movie = ratings_matrix.loc[user_id].copy()

        for movie in ratings_matrix.columns:
            if pd.notnull(user_movie.loc[movie]):  # 사용자가 해당 영화를 봤으면
                user_movie.loc[movie] = 0  # 추천 리스트에서 제외
            else:
                user_movie.loc[movie] = CF_knn(user_id, movie, neighbors_size)

        movie_sort = user_movie.sort_values(ascending=False)[:n_items]  # 내림차순
        recom_movies = movies.loc[movie_sort.index]  # 인덱스 반환
        return recom_movies

    
    # data_from_spring = request.data.decode('utf-8') # POST 요청에서 userId 추출
    data_from_spring = request.args.get('userId')
    userId = int(data_from_spring)

    recommendations = recom_movie_by_CF_knn(user_id=str(userId), n_items= 1, neighbors_size=20)
    index_array = recommendations.index.to_numpy()
    recom_data = json.dumps(index_array.tolist())
    logging.debug(recom_data)
    logging.debug(type(recom_data))
    data_list = json.loads(recom_data)
    logging.debug(type(data_list))

    return jsonify({"result":recom_data})


if __name__ == '__main__':
    app.run(debug=False,host="0.0.0.0",port=6000)