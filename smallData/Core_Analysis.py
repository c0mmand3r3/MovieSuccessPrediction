import numpy as np;
from sklearn.linear_model import LinearRegression,SGDRegressor;
from sklearn.model_selection import train_test_split,cross_val_score;

import pandas as pd;
import csv;


#data extractor from csv file
bollywood_actor_data=pd.read_csv('BollywoodActorRanking.csv',keep_default_na=False);
bollywood_director_data=pd.read_csv('BollywoodDirectorRanking.csv',keep_default_na=False);
bollywood_movie_data=pd.read_csv('BollywoodMovieDetail.csv',keep_default_na=False);



#creating new csv file for data extraction
data_actor={
    'actor_id':list(bollywood_actor_data['actorId']),
    'actor_movieCount': list(bollywood_actor_data['movieCount']),
    'actor_ratingSum': list(bollywood_actor_data['ratingSum']),
    'actor_normalizedMovieRank': list(bollywood_actor_data['normalizedMovieRank']),
    'actor_googleHits': list(bollywood_actor_data['googleHits']),
    'actor_normalizedGoogleRank': list(bollywood_actor_data['normalizedGoogleRank']),
    'actor_normalizedRating': list(bollywood_actor_data['actorId']),
}

data_director={
    'director_id': list(bollywood_director_data['directorId']),
    'director_movieCount': list(bollywood_director_data['movieCount']),
    'director_ratingSum': list(bollywood_director_data['ratingSum']),
    'director_normalizedMovieRank': list(bollywood_director_data['normalizedMovieRank']),
    'director_googleHits': list(bollywood_director_data['googleHits']),
    'director_normalizedGoogleRank': list(bollywood_director_data['normalizedGoogleRank']),
    'director_normalizedRating': list(bollywood_director_data['normalizedRating']),
}

df_act=pd.DataFrame(data_actor);
df_dir=pd.DataFrame(data_director);

df_act.to_csv('act_filter_file.csv');
df_dir.to_csv('dir_filter_file.csv');


#processing the data for creating training and testing file
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


#getting data ready for actor and director


#for actors

act_mean_movie_count=[];
act_mean_movie_ratingSum = [];
act_mean_movie_normalizedMovieRank = [];
act_mean_movie_googleHits = [];
act_mean_movie_normalizedGoogleRank = [];
act_mean_movie_normalizedRating = [];

actor_curresponding_field=list(bollywood_movie_data['actors']);
for idd,string in enumerate(actor_curresponding_field):
    #print(idd);
    if(string=='N/A'):
        act_mean_movie_count.append(0);
        act_mean_movie_ratingSum.append(0);
        act_mean_movie_normalizedMovieRank.append(0);
        act_mean_movie_googleHits.append(0);
        act_mean_movie_normalizedGoogleRank.append(0);
        act_mean_movie_normalizedRating.append(0);
    else:
        act_movie_count=0;
        act_movie_ratingSum = 0;
        act_movie_normalizedMovieRank = 0;
        act_movie_googleHits = 0;
        act_movie_normalizedGoogleRank = 0;
        act_movie_normalizedRating = 0;
        count_val=0;
        for id,hole_name in enumerate(string.split('|')):
            count_val=id+1;
            #print(hole_name.strip(),'   ',id);
            row=returnActorId(hole_name.strip());
            if(type(row) is list):
                if(row[2]=='NULL'):
                    act_movie_count+=0;
                else:
                    act_movie_count+=float(row[2]);
                if(row[3]=='NULL'):
                    act_movie_ratingSum+=0;
                else:
                    act_movie_ratingSum+=float(row[3]);
                if(row[4]=='NULL'):
                    act_movie_normalizedMovieRank+=0;
                else:
                    act_movie_normalizedMovieRank+=float(row[4]);
                if(row[5]=='NULL'):
                    act_movie_googleHits+=0;
                else:
                    act_movie_googleHits+=float(row[5]);
                if(row[6]=='NULL'):
                    act_movie_normalizedGoogleRank+=0;
                else:
                    act_movie_normalizedGoogleRank+=float(row[6]);
                if(row[7]=='NULL'):
                    act_movie_normalizedRating+=0;
                else:
                    act_movie_normalizedRating+=float(row[7]);
            else:
                act_movie_count += 0;
                act_movie_ratingSum+=0;
                act_movie_normalizedMovieRank+=0;
                act_movie_googleHits+=0;
                act_movie_normalizedGoogleRank+=0;
                act_movie_normalizedRating+=0;
        act_mean_movie_count.append(act_movie_count/count_val);
        act_mean_movie_ratingSum.append(act_movie_ratingSum/count_val);
        act_mean_movie_normalizedMovieRank.append(act_movie_normalizedMovieRank/count_val);
        act_mean_movie_googleHits.append(act_movie_googleHits/count_val);
        act_mean_movie_normalizedGoogleRank.append(act_movie_normalizedGoogleRank/count_val);
        act_mean_movie_normalizedRating.append(act_movie_normalizedRating/count_val);


#for director

dir_mean_movie_count=[];
dir_mean_movie_ratingSum = [];
dir_mean_movie_normalizedMovieRank = [];
dir_mean_movie_googleHits = [];
dir_mean_movie_normalizedGoogleRank = [];
dir_mean_movie_normalizedRating = [];

dir_curresponding_field=list(bollywood_movie_data['directors']);
for idd,string in enumerate(dir_curresponding_field):
    #print(idd);
    if(string=='N/A'):
        dir_mean_movie_count.append(0);
        dir_mean_movie_ratingSum.append(0);
        dir_mean_movie_normalizedMovieRank.append(0);
        dir_mean_movie_googleHits.append(0);
        dir_mean_movie_normalizedGoogleRank.append(0);
        dir_mean_movie_normalizedRating.append(0);
    else:
        dir_movie_count=0;
        dir_movie_ratingSum = 0;
        dir_movie_normalizedMovieRank = 0;
        dir_movie_googleHits = 0;
        dir_movie_normalizedGoogleRank = 0;
        dir_movie_normalizedRating = 0;
        count_val=0;
        for id,hole_name in enumerate(string.split('|')):
            count_val=id+1;
            #print(hole_name.strip(),'   ',id);
            row=returnDirectorId(hole_name.strip());
            if(type(row) is list):
                if(row[2]=='NULL'):
                    dir_movie_count+=0;
                else:
                    dir_movie_count+=float(row[2]);
                if(row[3]=='NULL'):
                    dir_movie_ratingSum+=0;
                else:
                    dir_movie_ratingSum+=float(row[3]);
                if(row[4]=='NULL'):
                    dir_movie_normalizedMovieRank+=0;
                else:
                    dir_movie_normalizedMovieRank+=float(row[4]);
                if(row[5]=='NULL'):
                    dir_movie_googleHits+=0;
                else:
                    dir_movie_googleHits+=float(row[5]);
                if(row[6]=='NULL'):
                    dir_movie_normalizedGoogleRank+=0;
                else:
                    dir_movie_normalizedGoogleRank+=float(row[6]);
                if(row[7]=='NULL'):
                    dir_movie_normalizedRating+=0;
                else:
                    dir_movie_normalizedRating+=float(row[7]);
            else:
                dir_movie_count += 0;
                dir_movie_ratingSum+=0;
                dir_movie_normalizedMovieRank+=0;
                dir_movie_googleHits+=0;
                dir_movie_normalizedGoogleRank+=0;
                dir_movie_normalizedRating+=0;
        dir_mean_movie_count.append(dir_movie_count/count_val);
        dir_mean_movie_ratingSum.append(dir_movie_ratingSum/count_val);
        dir_mean_movie_normalizedMovieRank.append(dir_movie_normalizedMovieRank/count_val);
        dir_mean_movie_googleHits.append(dir_movie_googleHits/count_val);
        dir_mean_movie_normalizedGoogleRank.append(dir_movie_normalizedGoogleRank/count_val);
        dir_mean_movie_normalizedRating.append(dir_movie_normalizedRating/count_val);

hitflop_movie=list(bollywood_movie_data['hitFlop']);


analysis_data={
    'act_movie_count':act_mean_movie_count,
    'act_movie_ratingSum':act_mean_movie_ratingSum,
    'act_movie_normalizedMovieRank':act_mean_movie_normalizedMovieRank,
    'act_mean_movie_googleHits':act_mean_movie_googleHits,
    'act_mean_movie_normalizedGoogleRank':act_mean_movie_normalizedGoogleRank,
    'act_mean_movie_normalizedRating':act_mean_movie_normalizedRating,
    'dir_movie_count': dir_mean_movie_count,
    'dir_movie_ratingSum': dir_mean_movie_ratingSum,
    'dir_movie_normalizedMovieRank': dir_mean_movie_normalizedMovieRank,
    'dir_mean_movie_googleHits': dir_mean_movie_googleHits,
    'dir_mean_movie_normalizedGoogleRank': dir_mean_movie_normalizedGoogleRank,
    'dir_mean_movie_normalizedRating': dir_mean_movie_normalizedRating,
    'hitflop':hitflop_movie,
}

df_filter_data_for_training=pd.DataFrame(analysis_data);
df_filter_data_for_training.to_csv('training_data_set_filter.csv');




