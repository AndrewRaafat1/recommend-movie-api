import requests
import json
import time
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
 #get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])
def get_movies_from_tastedive(movie):
    baseurl = "https://tastedive.com/api/similar"
    params= {}
    params['q'] = movie
    params['type'] = 'movies'
    params['limit']= 5
    params['k']='381982-Test-45QSVYT8'
    params["info"]="1"
    calling = requests.get(baseurl,params)
    return(calling.json())

def extract_movie_titles(movie):
    dic = get_movies_from_tastedive(movie)
    newlst = []
    for item in dic['Similar']['Results']:
        newlst.append(item['Name'])
    return newlst

def extract_movie_plot(movie):
  dic = get_movies_from_tastedive(movie)
  newlst = []
  for item in dic['Similar']['Results']:
    newlst.append(item['wTeaser'])
  return newlst

# def get_related_titles(movie):
#     newlst=[]
#     newlst.append((extract_movie_titles(get_movies_from_tastedive(movie))))
#     return newlst

#def get_related_plots(movie):
 # newlst=[]
  #newlst.append(extract_movie_plot(get_movies_from_tastedive(movie)))
  #return newlst

def get_movies_data(movie):
    baseurl="http://www.omdbapi.com/"
    params={}
    params["t"]=movie
    params["r"]="json"
    params['apikey']="2bcbf473"
    request = requests.get(baseurl,params)
    result=request.json()
    return result

def extract_movie_rating(movie):
    similar_movies= extract_movie_titles(movie)
    newlst=[]
    for movie in similar_movies:
      result=get_movies_data(movie)
      #for num in result["Ratings"]: 
      if (result["Ratings"][1]["Source"]) == "Rotten Tomatoes":
          newlst.append((int(result["Ratings"][1]["Value"][:-1])))
      else:
           newlst.append(0)
    return newlst


def title_polt_rating(movie):
  titles = extract_movie_titles(movie)
  ratings = extract_movie_rating(movie)
  plots = extract_movie_plot(movie)
  new_dic = {}
  x=0
  for title in titles:
    new_dic[title] = [plots[x],ratings[x]]
    x +=1
  return new_dic

def sorted_recommendations(movies):
  movies_list = movies.keys()
  return sorted(movies_list, key = lambda x:movies[x][1], reverse = True)
  
#def get_sorted_recommendations(movies):
#    ratings = {}
 #   listofmovies =get_related_titles(movies)
  #  for movie in listofmovies:
   #     ratings[movie]=(get_movie_rating(get_movie_data(movie)))*(-1)
        
    #sortedl = sorted(listofmovies, key =lambda movie:ratings[movie])
    #return (sortedl)
#print(get_sorted_recommendations("Sherlock Holmes"))    
#print(get_related_plots("Lion"))
#print(extract_movie_rating("Lion"))
#print(extract_movie_titles("Lion"))
#print(get_movies_data("The Light Between Oceans"))
#print(title_polt_rating("Lion"))
print(""" 
         _\|/_
         (o o)
 +----oOO-{_}-OOo----------------------+
 |                                     |
 |                                     |
 |             Welcome to my            |
 |         Movies recommendations      |
 |               programme             |
 |                                     |
 |                                     |
 +------------------------------------
""")
time.sleep(3)
movie = input("Enter a Movie name to get recommendations\n →		")
print("Loading...")
time.sleep(1.5)
print("10%")
time.sleep(1)
print("30%")
time.sleep(2)
print("50%")
time.sleep(1.5)
print("70%")
time.sleep(0.5)
print("100%")
time.sleep(1)
print("Done!")
time.sleep(0.5)
print("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
list_of_Sorted =sorted_recommendations(title_polt_rating(movie))
for i in range(5):
  time.sleep(1)
  print(str((i+1)) + ": " + list_of_Sorted[i])
  if (str(title_polt_rating(movie)[list_of_Sorted[i]][1])!="0"):
    print("Rating : " + str(title_polt_rating(movie)[list_of_Sorted[i]][1]) + " %")
  else:
    print("Rating : No Rating found on rotten tomatoes")
  time.sleep(1)
  print("▬▬ι═══════════════════════════════════════════ι▬▬\n")
number = input("Enter a Movie number to get more info\n →		")
print("\n↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓\n")
print(str(title_polt_rating(movie)[list_of_Sorted[int(number)-1]][0]))
time.sleep(10)









