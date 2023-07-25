show dbs

use parkhs

show dbs

db.mycollection.insertOne({name:1})


show dbs

show collections

db.createCollection('cappedCollection',{capped:true, size:10000})

db.cappedCollection.insertOne({x:1})

db.cappedCollection.find()

for(i=0; i<1000; i++){
    db.cappedCollection.insertOne({x:i})
}

db.cappedCollection.find()