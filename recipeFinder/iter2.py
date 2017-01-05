from google.appengine.api import search

index = search.Index(name="product1earch1")

try:
    search_results = index.search("stories")
    for result in search_results:
        print(result.id)
except search.Error:
    print("ERROR!")
