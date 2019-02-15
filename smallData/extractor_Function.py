import pandas as pd;
import csv;

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
    print(dir_movie_count)
    print(act_movie_count)
    print(count_val1)
    return [[act_movie_count/count_val1,act_movie_ratingSum/count_val1,act_movie_normalizedMovieRank/count_val1,act_movie_googleHits/count_val1,
            act_movie_normalizedGoogleRank/count_val1,act_movie_normalizedRating/count_val1,dir_movie_count/count_val2,
            dir_movie_ratingSum/count_val2,dir_movie_normalizedMovieRank/count_val2,dir_movie_googleHits/count_val2,
            dir_movie_normalizedGoogleRank/count_val2,dir_movie_normalizedRating/count_val2]];
