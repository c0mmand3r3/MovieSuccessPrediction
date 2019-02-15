import numpy as np;
from sklearn.linear_model import LinearRegression,SGDRegressor;
from sklearn.model_selection import train_test_split,cross_val_score;
import pandas as pd;
import csv;
import math;


#data extractor from csv file
data=pd.read_csv('training_data_set_filter.csv',keep_default_na=False);
X=data[list(data.columns)[-13:-1]];
Y=data['hitflop'];
input_x=X.values.astype(float);
output_y=np.reshape(Y.values,(-1,1)).astype(float);
model=LinearRegression();
x_train,x_test,y_train,y_test=train_test_split(input_x,output_y);
model.fit(x_train,y_train);


def returnActorId(name):
    data=csv.reader(open('BollywoodActorRanking.csv'))
    for row in data:
        if(row[1]==name):
            return row;
    return False;

#print(returnActorId('Govinda'));
def returnDirectorId(name):
    data = csv.reader(open('BollywoodDirectorRanking.csv'),delimiter=',')
    for row in data:
        if(row[1]==name):
            return row;
    return False;


def getActorsDirectorData(act_name,director_name):
    act_movie_count = 0;
    act_movie_ratingSum = 0;
    act_movie_normalizedMovieRank = 0;
    act_movie_googleHits = 0;
    act_movie_normalizedGoogleRank = 0;
    act_movie_normalizedRating = 0;
    count_val1 = 0;
    for id, hole_name in enumerate(act_name.split(',')):
        count_val1 = id + 1;
        row = returnActorId(hole_name.strip());
        if (type(row) is list):
            if (row[2] == 'NULL'):
                act_movie_count += 0;
            else:
                act_movie_count += float(row[2]);
            if (row[3] == 'NULL'):
                act_movie_ratingSum += 0;
            else:
                act_movie_ratingSum += float(row[3]);
            if (row[4] == 'NULL'):
                act_movie_normalizedMovieRank += 0;
            else:
                act_movie_normalizedMovieRank += float(row[4]);
            if (row[5] == 'NULL'):
                act_movie_googleHits += 0;
            else:
                act_movie_googleHits += float(row[5]);
            if (row[6] == 'NULL'):
                act_movie_normalizedGoogleRank += 0;
            else:
                act_movie_normalizedGoogleRank += float(row[6]);
            if (row[7] == 'NULL'):
                act_movie_normalizedRating += 0;
            else:
                act_movie_normalizedRating += float(row[7]);
        else:
            act_movie_count += 0;
            act_movie_ratingSum += 0;
            act_movie_normalizedMovieRank += 0;
            act_movie_googleHits += 0;
            act_movie_normalizedGoogleRank += 0;
            act_movie_normalizedRating += 0;
    dir_movie_count = 0;
    dir_movie_ratingSum = 0;
    dir_movie_normalizedMovieRank = 0;
    dir_movie_googleHits = 0;
    dir_movie_normalizedGoogleRank = 0;
    dir_movie_normalizedRating = 0;
    count_val2 = 0;
    for id, hole_name in enumerate(director_name.split(',')):
        count_val2 = id + 1;
        row = returnDirectorId(hole_name.strip());
        if (type(row) is list):
            if (row[2] == 'NULL'):
                dir_movie_count += 0;
            else:
                dir_movie_count += float(row[2]);
            if (row[3] == 'NULL'):
                dir_movie_ratingSum += 0;
            else:
                dir_movie_ratingSum += float(row[3]);
            if (row[4] == 'NULL'):
                dir_movie_normalizedMovieRank += 0;
            else:
                dir_movie_normalizedMovieRank += float(row[4]);
            if (row[5] == 'NULL'):
                dir_movie_googleHits += 0;
            else:
                dir_movie_googleHits += float(row[5]);
            if (row[6] == 'NULL'):
                dir_movie_normalizedGoogleRank += 0;
            else:
                dir_movie_normalizedGoogleRank += float(row[6]);
            if (row[7] == 'NULL'):
                dir_movie_normalizedRating += 0;
            else:
                dir_movie_normalizedRating += float(row[7]);
        else:
            dir_movie_count += 0;
            dir_movie_ratingSum += 0;
            dir_movie_normalizedMovieRank += 0;
            dir_movie_googleHits += 0;
            dir_movie_normalizedGoogleRank += 0;
            dir_movie_normalizedRating += 0;
    return [[act_movie_count/count_val1,act_movie_ratingSum/count_val1,act_movie_normalizedMovieRank/count_val1,act_movie_googleHits/count_val1,
            act_movie_normalizedGoogleRank/count_val1,act_movie_normalizedRating/count_val1,dir_movie_count/count_val2,
            dir_movie_ratingSum/count_val2,dir_movie_normalizedMovieRank/count_val2,dir_movie_googleHits/count_val2,
            dir_movie_normalizedGoogleRank/count_val2,dir_movie_normalizedRating/count_val2]];

decision={
    1:'Disaster',
    2:'Flop',
    3:'Below Average',
    4:'Average',
    5:'Semi Hit',
    6:'Hit',
    7:'Super Hit',
    8:'Blockbuster',
    9:'All-Time Blockbuster',
}

print("Movie Prediction System");
while(True):
    print('\n')
    mov_name=input("Name of the movie : ");
    actor_name=input("Actor & Actress (seperated by comma) : ");
    director_name=input("Directors (seperated by comma) : ");
    inp_x=getActorsDirectorData(actor_name.title(),director_name.title());
    prediction_value=model.predict(inp_x)
    value=math.ceil(prediction_value[0][0]);
    if(value<=1):
        value=1;
    elif(value>=9):
        value=9;
    print('Prediction : {0:20}'.format(decision[value]));

