
import turicreate as tc

ITEM_LIST = ["a", "b", "c", "d"]

sf = tc.SFrame({'user_id': ["0", "0", "0", "1", "1", "2", "2", "2"],
                'item_id': ["a", "b", "c", "a", "b", "b", "c", "d"],
                'rating': [1, 3, 2, 5, 4, 1, 4, 3]})

m = tc.recommender.create(sf, target='rating')

recs = m.recommend(users=['misko'])
print(recs)

preds = m.predict(tc.SFrame({'user_id': ["misko", "misko", "misko", "misko"], 'item_id': ITEM_LIST}))
for pred, item in zip(preds, ITEM_LIST):
    print(item, pred)

print("-" * 30)

# Now say I've liked product "a"

recs = m.recommend(users=['misko'],
                   new_observation_data=tc.SFrame({'user_id': ["misko"], 'item_id': ["a"], 'rating': [5]})
                   )
print(recs)


preds = m.predict(dataset=tc.SFrame({'user_id': ["misko", "misko", "misko", "misko"], 'item_id': ITEM_LIST}),
                  new_observation_data=tc.SFrame({'user_id': ["misko"], 'item_id': ["a"], 'rating': [5]}))
for pred, item in zip(preds, ITEM_LIST):
    print(item, pred)